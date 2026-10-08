#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Mert Torun
# SPDX-License-Identifier: MIT
"""Check the traceability data of the diagnostic path, and write its CSV view.

verification/test_traceability.yaml holds requirements of the diagnostic path,
the tests or checks of each, their status and the evidence each status rests on.
This check holds the file to these rules:

  1. it is valid against verification/traceability.schema.json (JSON Schema
     2020-12);
  2. a test whose status is PASS names at least one archived piece of primary
     evidence (a log, a capture, a measurement or a test protocol); text of the
     report alone never supports PASS;
  3. the layer of a test agrees with the prefix of its identifier (L1- or L2-),
     and requirement and test identifiers are unique;
  4. a test has the status NOT-DOCUMENTED exactly when its method is
     not-tested, and such a test has the date null: no test is documented;
  5. every label the file cites (a requirement's source, an evidence entry of
     the report) is a \\label in the LaTeX sources of report/, and every other
     evidence source is a key of report/bib/references.bib;
  6. every defect it names (B1 to B6) is a row of Table 5.4 of the report;
  7. verification/traceability.csv equals the CSV this script generates from
     the YAML file, byte for byte, including its constant column record_status.

    check_traceability.py              check the file and the CSV
    check_traceability.py --write-csv  write verification/traceability.csv, if
                                       the file holds the schema
    check_traceability.py --selftest   show that each rule refuses a case it is
                                       written for, with the finding the case
                                       names and no other, among them B4 marked
                                       PASS on the report's text alone

Any other argument, and any argument after one of the two options, is refused
with a usage line before a file is read or written.

Exit status: 0 the file holds (with --write-csv: the CSV was written; with
--selftest: every case was refused as named), 1 a rule fails (with --write-csv:
the schema; nothing is written; with --selftest: a case was not refused as
named), 2 the arguments were not understood, a file could not be read or
written, or PyYAML or jsonschema 4.0 or later is missing.
Needs PyYAML and jsonschema 4.0 or later.
"""

import copy
import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "verification" / "test_traceability.yaml"
SCHEMA = ROOT / "verification" / "traceability.schema.json"
CSV_PATH = ROOT / "verification" / "traceability.csv"
REPORT = ROOT / "report"
BIB = REPORT / "bib" / "references.bib"

USAGE = "usage: check_traceability.py [--write-csv | --selftest]"
PRIMARY = {"log", "capture", "measurement", "test-protocol"}
COLUMNS = ["requirement_id", "requirement", "requirement_source", "test_id", "layer", "method", "item_tested",
           "date", "status", "defect", "evidence", "note", "record_status"]


class ReadError(Exception):
    """A file could not be read or parsed, or a package the check needs is missing."""


def load_yaml(path):
    try:
        import yaml
    except ImportError:
        raise ReadError("PyYAML is not installed")
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
        raise ReadError("%s: %s" % (path.name, exc))
    if not isinstance(data, dict):
        raise ReadError("%s is not a mapping" % path.name)
    return data


def load_schema():
    try:
        return json.loads(SCHEMA.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ReadError("%s: %s" % (SCHEMA.name, exc))


def report_labels():
    labels = set()
    try:
        for tex in REPORT.rglob("*.tex"):
            labels.update(re.findall(r"\\label\{([^}]+)\}", tex.read_text(encoding="utf-8")))
    except (OSError, UnicodeDecodeError) as exc:
        raise ReadError("report sources: %s" % exc)
    if not labels:
        raise ReadError("no \\label found in report/; nothing to check against")
    return labels


def bib_keys():
    try:
        text = BIB.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise ReadError("%s: %s" % (BIB.name, exc))
    keys = set(re.findall(r"^@\w+\{([^,\s]+),", text, re.M))
    if not keys:
        raise ReadError("no entry found in %s" % BIB.name)
    return keys


def defect_rows():
    """The defect identifiers of Table 5.4 (label tab:bug_taxonomy) of the report."""
    path = REPORT / "chapters" / "chapter5.tex"
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise ReadError("%s: %s" % (path.name, exc))
    match = re.search(r"\\label\{tab:bug_taxonomy\}(.*?)\\end\{tabular\}", text, re.S)
    if not match:
        raise ReadError("Table 5.4 (tab:bug_taxonomy) not found in chapter5.tex")
    rows = set(re.findall(r"^\s*(B[1-9])\s*&", match.group(1), re.M))
    if not rows:
        raise ReadError("Table 5.4 has no defect rows")
    return rows


def schema_findings(data, schema):
    try:
        import jsonschema
    except ImportError:
        raise ReadError("jsonschema is not installed")
    # A release older than 4.0 has no validator for JSON Schema 2020-12; without this
    # test the run would end in an AttributeError with exit status 1, a finding's code.
    validator_class = getattr(jsonschema, "Draft202012Validator", None)
    if validator_class is None:
        raise ReadError("jsonschema 4.0 or later is needed")
    validator = validator_class(schema)
    return ["schema: %s at %s" % (error.message, "/".join(str(p) for p in error.absolute_path) or "(root)")
            for error in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))]


def evidence_text(item):
    where = item.get("locator", "")
    if item.get("source") == "report":
        ref = "report %s (%s)" % (where, item.get("label", ""))
    else:
        ref = "%s %s" % (item.get("source", ""), where)
    flags = [item.get("kind", ""), "archived" if item.get("archived") else "not archived",
             "public" if item.get("public") else "not public"]
    return "%s [%s]" % (ref, ", ".join(flags))


def rows(data):
    out = []
    for req in data.get("requirements", []):
        source = req.get("source", {})
        for test in req.get("tests", []):
            out.append({
                "requirement_id": req.get("id", ""),
                "requirement": " ".join(str(req.get("statement", "")).split()),
                "requirement_source": "report %s (%s)" % (source.get("locator", ""), source.get("label", "")),
                "test_id": test.get("id", ""),
                "layer": "L%s" % test.get("layer", ""),
                "method": test.get("method", ""),
                "item_tested": test.get("item", ""),
                "date": test.get("date") or "",
                "status": test.get("status", ""),
                "defect": test.get("defect") or "",
                "evidence": "; ".join(evidence_text(e) for e in test.get("evidence", [])),
                "note": " ".join(str(test.get("note", "")).split()),
                "record_status": " ".join(str(data.get("record_status", "")).split()),
            })
    return out


def render_csv(data):
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    for row in rows(data):
        writer.writerow(row)
    return buffer.getvalue()


def rule_findings(data, labels, keys, defects, csv_text):
    found = []
    seen_req, seen_test = set(), set()
    for req in data.get("requirements", []):
        rid = req.get("id")
        if rid in seen_req:
            found.append("requirement %s stands twice" % rid)
        seen_req.add(rid)
        label = (req.get("source") or {}).get("label")
        if label not in labels:
            found.append("%s: its source label %r is no \\label in report/" % (rid, label))
        for test in req.get("tests", []):
            tid = test.get("id", "")
            if tid in seen_test:
                found.append("test %s stands twice" % tid)
            seen_test.add(tid)
            prefix = re.match(r"L([12])-", tid)
            if not prefix or int(prefix.group(1)) != test.get("layer"):
                found.append("%s: the identifier does not carry its layer %r" % (tid, test.get("layer")))
            not_documented = test.get("status") == "NOT-DOCUMENTED"
            if not_documented != (test.get("method") == "not-tested"):
                found.append("%s: the status NOT-DOCUMENTED goes with the method not-tested and no other, "
                             "here status %s with method %s" % (tid, test.get("status"), test.get("method")))
            if not_documented and test.get("date") is not None:
                found.append("%s: a test that is not documented has the date null, here %r" % (tid, test.get("date")))
            evidence = test.get("evidence") or []
            if test.get("status") == "PASS" and not any(
                    e.get("kind") in PRIMARY and e.get("archived") is True for e in evidence):
                found.append("%s: PASS names no archived primary evidence (log, capture, measurement or test "
                             "protocol); report text alone does not support PASS" % tid)
            for item in evidence:
                if item.get("source") == "report":
                    if item.get("label") not in labels:
                        found.append("%s: evidence label %r is no \\label in report/" % (tid, item.get("label")))
                elif item.get("source") not in keys:
                    found.append("%s: evidence source %r is no key of report/bib/references.bib"
                                 % (tid, item.get("source")))
            defect = test.get("defect")
            if defect is not None and defect not in defects:
                found.append("%s: defect %s is no row of Table 5.4 of the report" % (tid, defect))
    if csv_text != render_csv(data):
        found.append("verification/traceability.csv differs from the CSV generated from the YAML file; "
                     "run tools/check_traceability.py --write-csv")
    return found


def check(data, schema, labels, keys, defects, csv_text):
    found = schema_findings(data, schema)
    if found:
        return found
    return rule_findings(data, labels, keys, defects, csv_text)


def context():
    return load_schema(), report_labels(), bib_keys(), defect_rows()


def read_csv():
    try:
        return CSV_PATH.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise ReadError("%s: %s" % (CSV_PATH.name, exc))


def find_test(data, test_id):
    for req in data["requirements"]:
        for test in req["tests"]:
            if test["id"] == test_id:
                return test
    raise ReadError("the self-test needs test %s in the data" % test_id)


def selftest():
    data = load_yaml(DATA)
    schema, labels, keys, defects = context()
    csv_text = render_csv(data)
    if check(data, schema, labels, keys, defects, csv_text):
        print("  [FAIL] selftest: the data of this repository do not hold, so no mutation can be judged")
        return 1

    def b4_pass_on_report_text(d):
        test = find_test(d, "L2-DP-06")
        test["status"] = "PASS"
        return d

    def pass_on_unarchived_capture(d):
        test = find_test(d, "L1-DP-09")
        test["status"] = "PASS"
        test["evidence"].append({"source": "savchuk2025", "locator": "p. 22", "kind": "capture",
                                 "archived": False, "public": False})
        return d

    def wrong_layer(d):
        find_test(d, "L1-DP-02")["layer"] = 2
        return d

    def not_documented_with_a_method(d):
        find_test(d, "L2-DP-07")["method"] = "operation"
        return d

    def not_tested_with_a_result(d):
        find_test(d, "L1-DP-09")["method"] = "not-tested"
        return d

    def not_documented_with_a_date(d):
        find_test(d, "L1-DP-01")["date"] = "2023"
        return d

    def unknown_status(d):
        find_test(d, "L2-DP-04")["status"] = "RESOLVED"
        return d

    def unknown_label(d):
        find_test(d, "L1-DP-03")["evidence"][0]["label"] = "sec:no_such_section"
        return d

    def unknown_source(d):
        find_test(d, "L1-DP-03")["evidence"][1]["source"] = "unknown2025"
        return d

    def unknown_defect(d):
        find_test(d, "L2-DP-05")["defect"] = "B9"
        return d

    def no_record_status(d):
        del d["record_status"]
        return d

    def duplicate_test(d):
        d["requirements"][0]["tests"].append(copy.deepcopy(d["requirements"][0]["tests"][0]))
        return d

    # Each case names the finding it has to produce; the case holds only if that
    # finding is its one and only finding, so that a mutation refused by another
    # rule, or not at all, is a failure of the self-test.
    cases = [
        ("B4 marked PASS on the report's text alone", b4_pass_on_report_text, None,
         "L2-DP-06: PASS names no archived primary evidence"),
        ("PASS on a capture that is not archived", pass_on_unarchived_capture, None,
         "L1-DP-09: PASS names no archived primary evidence"),
        ("an L1 identifier on a test of layer 2", wrong_layer, None,
         "L1-DP-02: the identifier does not carry its layer 2"),
        ("NOT-DOCUMENTED with a method other than not-tested", not_documented_with_a_method, None,
         "L2-DP-07: the status NOT-DOCUMENTED goes with the method not-tested and no other"),
        ("the method not-tested on a test with a result", not_tested_with_a_result, None,
         "L1-DP-09: the status NOT-DOCUMENTED goes with the method not-tested and no other"),
        ("a date on a test that is not documented", not_documented_with_a_date, None,
         "L1-DP-01: a test that is not documented has the date null"),
        ("a status outside the vocabulary", unknown_status, None,
         "schema: 'RESOLVED' is not one of "),
        ("an evidence label that the report does not define", unknown_label, None,
         "L1-DP-03: evidence label 'sec:no_such_section' is no \\label in report/"),
        ("an evidence source that the bibliography does not hold", unknown_source, None,
         "L1-DP-03: evidence source 'unknown2025' is no key of report/bib/references.bib"),
        ("a defect that Table 5.4 does not list", unknown_defect, None,
         "L2-DP-05: defect B9 is no row of Table 5.4 of the report"),
        ("a file without its record_status", no_record_status, None,
         "schema: 'record_status' is a required property"),
        ("a test identifier used twice", duplicate_test, None,
         "test L1-DP-01 stands twice"),
        ("a CSV view that differs from the data", None, csv_text.replace("OPEN", "PASS", 1),
         "verification/traceability.csv differs from the CSV generated from the YAML file"),
    ]
    failures = 0
    for name, mutate, other_csv, expected in cases:
        mutated = mutate(copy.deepcopy(data)) if mutate else data
        # The CSV is regenerated from the mutated data, so that only the rule the
        # case is written for can refuse it; the last case alters the CSV alone.
        found = check(mutated, schema, labels, keys, defects,
                      other_csv if other_csv is not None else render_csv(mutated))
        ok = len(found) == 1 and expected in found[0]
        failures += not ok
        print("  [%s] %s: %s" % ("ok" if ok else "FAIL", name, "; ".join(found) if found else "not found"))
        if not ok:
            print("         expected only: %s" % expected)
    if failures:
        print("  [FAIL] selftest: %d of %d case(s) not refused as their case names" % (failures, len(cases)))
        return 1
    print("  [OK]   selftest: all %d cases refused, each by the finding it names" % len(cases))
    return 0


def main(argv):
    if argv[1:] not in ([], ["--write-csv"], ["--selftest"]):
        print(USAGE, file=sys.stderr)
        return 2
    try:
        if argv[1:] == ["--selftest"]:
            return selftest()
        data = load_yaml(DATA)
        if argv[1:] == ["--write-csv"]:
            # The CSV is rendered only from data that hold the schema; malformed data
            # would otherwise end the rendering in a traceback with exit status 1.
            found = schema_findings(data, load_schema())
            if not found:
                try:
                    CSV_PATH.write_text(render_csv(data), encoding="utf-8")
                except OSError as exc:
                    print("  [ERR]  %s could not be written: %s" % (CSV_PATH.name, exc), file=sys.stderr)
                    return 2
                print("  [OK]   wrote %s" % CSV_PATH.relative_to(ROOT))
                return 0
        else:
            schema, labels, keys, defects = context()
            found = check(data, schema, labels, keys, defects, read_csv())
    except ReadError as exc:
        print("  [ERR]  %s; nothing was checked" % exc, file=sys.stderr)
        return 2
    for line in found:
        print("  [FAIL] %s" % line)
    if found:
        print("  [FAIL] %d finding(s) in the traceability data" % len(found))
        return 1
    tests = sum(len(r["tests"]) for r in data["requirements"])
    print("  [OK]   %d requirement(s) and %d test(s) hold the schema and the rules; the CSV is current"
          % (len(data["requirements"]), tests))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
