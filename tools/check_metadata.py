#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Mert Torun
# SPDX-License-Identifier: MIT
"""Check that CITATION.cff, codemeta.json, the README and SHA256SUMS agree.

The four describe one repository and one paper in different formats, and
nothing but this check keeps them in step. It compares, between CITATION.cff
and codemeta.json: the name of the repository, its version, its licence and
repository address, the author with ORCID iD and affiliation, and the paper's
DOI, title, date of publication, language and licence. It checks two forms that
the CodeMeta 3.0 context needs and that JSON-LD expansion would otherwise lose
without a warning: the paper is typed schema:ScholarlyArticle and its language
is given as schema:inLanguage, and each software requirement is a node of type
SoftwareApplication with a name. The preferred citation of CITATION.cff must be
typed report: the publisher types the paper a Working Paper, for which CFF 1.2.0
has no type. It parses the @article entry in the README's
bibtex block and compares its author, title, journal, number, year, ISSN, DOI
and address with the preferred citation of CITATION.cff, and requires its note
to name the document type Working Paper. Last, the SHA-256 of the deposited
file in publication/SHA256SUMS must stand in README.md and publication/README.md.
A part of CITATION.cff or codemeta.json that these comparisons read but that
lacks the form they need (a list of persons, a mapping) is a finding, too.
The index of ERRATA.md is held against its entries: every entry under the
heading Errata has exactly one row, whose location (the entry's Location up to
its first comma), class and status are those of the entry, no row names an
entry that does not exist, and the sentence before the table counts the
entries per class as they are. A section without an entry is a finding, not a
pass.

    check_metadata.py            check the files
    check_metadata.py --selftest show that a changed DOI, version, type, title,
                                 note or checksum, a paper reference that is
                                 not a mapping, and an errata index row whose
                                 class differs from its entry, are found, each
                                 by the findings its case names and by no other

Any other argument, and any argument after --selftest, is refused with a usage
line before a file is read.

Exit status: 0 they agree (with --selftest: every case was found as named), 1 a
value differs or lacks its form (with --selftest: a case was not found as
named), 2 the arguments were not understood, a file could not be read or PyYAML
is missing.
Needs PyYAML.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPDX = "https://spdx.org/licenses/"
ARTICLE_TYPE = "schema:ScholarlyArticle"
LANGUAGE = "schema:inLanguage"
REQUIREMENT_TYPE = "SoftwareApplication"
DEPOSIT = "2026_02_Retrofitted_Anti-Skid_System.pdf"
USAGE = "usage: check_metadata.py [--selftest]"


class ReadError(Exception):
    """A file could not be read or parsed."""


def load(root):
    try:
        import yaml
    except ImportError:
        raise ReadError("PyYAML is not installed")
    try:
        cff = yaml.safe_load((root / "CITATION.cff").read_text(encoding="utf-8"))
        meta = json.loads((root / "codemeta.json").read_text(encoding="utf-8"))
        readme = (root / "README.md").read_text(encoding="utf-8")
        record = (root / "publication" / "README.md").read_text(encoding="utf-8")
        sums = (root / "publication" / "SHA256SUMS").read_text(encoding="utf-8")
        errata = (root / "ERRATA.md").read_text(encoding="utf-8")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        raise ReadError(str(exc))
    if not isinstance(cff, dict) or not isinstance(meta, dict):
        raise ReadError("CITATION.cff or codemeta.json is not a mapping")
    return {"cff": cff, "meta": meta, "readme": readme, "record": record, "sums": sums, "errata": errata}


def bibtex_entry(readme):
    """The fields of the one @article entry in a bibtex block of the README."""
    blocks = re.findall(r"```bibtex\n(.*?)```", readme, re.S)
    entries = [b for b in blocks if "@article{" in b]
    if len(entries) != 1:
        raise ReadError("the README holds %d @article entries in bibtex blocks, not one" % len(entries))
    body = entries[0]
    if body.count("{") != body.count("}"):
        raise ReadError("the braces of the BibTeX entry are not balanced")
    fields = {}
    for match in re.finditer(r"^\s*([a-z]+)\s*=\s*\{(.*)\},?\s*$", body, re.M):
        fields[match.group(1)] = match.group(2)
    return fields


def unbrace(text):
    return re.sub(r"[{}]", "", text)


def errata_index_findings(text):
    """The differences between the index under '## Errata' and the entries below it."""
    section = re.search(r"^## Errata\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not section:
        return ["ERRATA.md has no section Errata"]
    body = section.group(1)
    first = re.search(r"^### ", body, re.M)
    head = body[:first.start()] if first else body
    found, entries = [], []
    for match in re.finditer(r"^### (\S+)\n(.*?)(?=^### |\Z)", body, re.S | re.M):
        fields = dict(re.findall(r"^- \*\*(Location|Class|Status):\*\* (.*)$", match.group(2), re.M))
        missing = [name for name in ("Location", "Class", "Status") if name not in fields]
        if missing:
            found.append("ERRATA.md %s has no %s field" % (match.group(1), " or ".join(missing)))
            continue
        location = fields["Location"].split(",")[0].strip()
        if location.endswith("."):
            location = location[:-1]
        entries.append((match.group(1), location, fields["Class"].strip(), fields["Status"].strip()))
    if not entries and not found:
        return ["ERRATA.md has no entry under Errata, so its index was not compared"]
    rows = {}
    for line in head.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells[0] in ("Entry", "---"):
            continue
        link = re.fullmatch(r"\[([^\]]+)\]\(#([^)]+)\)", cells[0])
        if len(cells) != 4 or not link:
            found.append("ERRATA.md index: a row that is not entry, location, class and status: %r" % line)
            continue
        if link.group(2) != link.group(1).lower():
            found.append("ERRATA.md index: %s links to #%s, not to its anchor" % (link.group(1), link.group(2)))
        rows.setdefault(link.group(1), []).append(cells[1:])
    for ident, location, kind, status in entries:
        got = rows.pop(ident, [])
        if len(got) != 1:
            found.append("ERRATA.md index: %s has %d row(s), not one" % (ident, len(got)))
            continue
        for what, want, have in zip(("location", "class", "status"), (location, kind, status), got[0]):
            if want != have:
                found.append("ERRATA.md index: the %s of %s is %r, the entry says %r" % (what, ident, have, want))
    for ident in rows:
        found.append("ERRATA.md index: a row for %s, which has no entry" % ident)
    counted = re.search(r"^The (\d+) entries by class: (.+)\.$", head, re.M)
    if not counted:
        found.append("ERRATA.md index: no sentence 'The N entries by class: ...' before the table")
    else:
        claimed, actual = {}, {}
        for item in counted.group(2).split("; "):
            pair = re.fullmatch(r'(\d+) "([^"]+)"', item)
            if not pair:
                found.append("ERRATA.md index: %r in the count sentence is not a number and a class" % item)
                continue
            claimed[pair.group(2)] = int(pair.group(1))
        for _, _, kind, _ in entries:
            actual[kind] = actual.get(kind, 0) + 1
        if int(counted.group(1)) != len(entries) or claimed != actual:
            found.append("ERRATA.md index: the sentence counts %s entries, %r; the entries are %d, %r"
                         % (counted.group(1), claimed, len(entries), actual))
    return found


def form_findings(cff, meta):
    """The parts that compare() reads, where they lack the form it needs.

    Without this test such a file would end the run in an AttributeError or a
    KeyError with exit status 1, a finding's code, and without saying what is wrong.
    """
    found = []
    for what, value in (("CITATION.cff authors", cff.get("authors")),
                        ("codemeta.json author", meta.get("author"))):
        if not (isinstance(value, list) and value and all(isinstance(item, dict) for item in value)):
            found.append("%s is not a list of persons" % what)
    for what, value in (("CITATION.cff preferred-citation", cff.get("preferred-citation")),
                        ("codemeta.json referencePublication", meta.get("referencePublication"))):
        if not isinstance(value, dict):
            found.append("%s is not a mapping" % what)
    people = meta.get("author")
    if isinstance(people, list) and people and isinstance(people[0], dict):
        if not isinstance(people[0].get("affiliation", {}), dict):
            found.append("codemeta.json author affiliation is not a mapping")
    return found


def compare(files):
    cff, meta, readme = files["cff"], files["meta"], files["readme"]
    found = form_findings(cff, meta)
    if found:
        return found
    found.extend(errata_index_findings(files["errata"]))

    def same(what, a, b):
        if a != b:
            found.append("%s: %r against %r" % (what, a, b))

    pc = cff.get("preferred-citation") or {}
    ref = meta.get("referencePublication") or {}
    same("repository name (CFF title, codemeta name)", cff.get("title"), meta.get("name"))
    same("version", str(cff.get("version")), str(meta.get("version")))
    licences = meta.get("license") if isinstance(meta.get("license"), list) else [meta.get("license")]
    if SPDX + str(cff.get("license")) not in licences:
        found.append("licence: CFF %r is not among codemeta %r" % (cff.get("license"), licences))
    same("repository", cff.get("repository-code"), meta.get("codeRepository"))
    authors = cff.get("authors") or [{}]
    people = meta.get("author") or [{}]
    same("author family name", authors[0].get("family-names"), people[0].get("familyName"))
    same("author given name", authors[0].get("given-names"), people[0].get("givenName"))
    same("author ORCID iD", authors[0].get("orcid"), people[0].get("@id"))
    same("affiliation", authors[0].get("affiliation"), (people[0].get("affiliation") or {}).get("name"))
    same("type of the paper in codemeta.json", ref.get("@type"), ARTICLE_TYPE)
    same("type of the preferred citation", pc.get("type"), "report")
    languages = pc.get("languages")
    first = languages[0] if isinstance(languages, list) and languages else languages
    same("language of the paper (CFF languages, codemeta %s)" % LANGUAGE, first, ref.get(LANGUAGE))
    if "inLanguage" in ref:
        found.append("codemeta.json gives the language of the paper as inLanguage, a term the CodeMeta 3.0 "
                     "context does not define, so expansion drops it; write %s" % LANGUAGE)
    requirements = meta.get("softwareRequirements")
    if not isinstance(requirements, list) or not requirements:
        found.append("codemeta.json lists no softwareRequirements")
    else:
        for item in requirements:
            if not (isinstance(item, dict) and item.get("@type") == REQUIREMENT_TYPE
                    and isinstance(item.get("name"), str) and item.get("name").strip()):
                found.append("softwareRequirements: %r is not a %s node with a name" % (item, REQUIREMENT_TYPE))
    same("DOI address", "https://doi.org/" + str(pc.get("doi")), ref.get("@id"))
    same("CFF url of the paper", pc.get("url"), ref.get("@id"))
    same("title of the paper", pc.get("title"), ref.get("name"))
    same("publication date", str(pc.get("date-published")), ref.get("datePublished"))
    same("licence of the paper", SPDX + str(pc.get("license")), ref.get("license"))
    if "Working Paper" not in str(pc.get("notes", "")):
        found.append("the preferred citation of CITATION.cff does not name the document type Working Paper")
    sums = files["sums"].split()
    if len(sums) != 2 or sums[1] != DEPOSIT or not re.fullmatch(r"[0-9a-f]{64}", sums[0]):
        found.append("publication/SHA256SUMS does not hold one line for %s" % DEPOSIT)
    else:
        for name in ("readme", "record"):
            if sums[0] not in files[name]:
                found.append("the SHA-256 of SHA256SUMS does not stand in %s"
                             % ("README.md" if name == "readme" else "publication/README.md"))
    try:
        bib = bibtex_entry(readme)
    except ReadError as exc:
        found.append(str(exc))
        return found
    family, given = authors[0].get("family-names"), authors[0].get("given-names")
    same("BibTeX author", bib.get("author"), "%s, %s" % (family, given))
    same("BibTeX title", unbrace(bib.get("title", "")), pc.get("title"))
    same("BibTeX journal", unbrace(bib.get("journal", "")), pc.get("journal"))
    same("BibTeX number", bib.get("number"), str(pc.get("issue")))
    same("BibTeX year", bib.get("year"), str(pc.get("year")))
    same("BibTeX issn", bib.get("issn"), str(pc.get("issn")))
    same("BibTeX doi", bib.get("doi"), str(pc.get("doi")))
    same("BibTeX url", bib.get("url"), pc.get("url"))
    if "Working Paper" not in bib.get("note", ""):
        found.append("the BibTeX entry's note does not name the document type Working Paper")
    return found


def selftest():
    files = load(ROOT)
    if compare(files):
        print("  [FAIL] selftest: the files of this repository do not agree, so no mutation can be judged")
        return 1

    def mutated(key, value):
        return dict(files, **{key: value})

    meta, cff = files["meta"], files["cff"]
    ref = meta["referencePublication"]
    # Each case names the findings it has to produce, in their order, and the case
    # holds only if these are all its findings: a mutation that is refused for
    # another reason, or not at all, is a failure of the self-test.
    cases = [
        ("a changed DOI in codemeta.json",
         mutated("meta", dict(meta, referencePublication=dict(ref, **{"@id": ref["@id"] + "0"}))),
         ("DOI address: ", "CFF url of the paper: ")),
        ("a changed version in CITATION.cff", mutated("cff", dict(cff, version="9.9.9")),
         ("version: '9.9.9' against ",)),
        ("an article type in CITATION.cff",
         mutated("cff", dict(cff, **{"preferred-citation": dict(cff["preferred-citation"], type="article")})),
         ("type of the preferred citation: 'article' against 'report'",)),
        ("a bare ScholarlyArticle type in codemeta.json",
         mutated("meta", dict(meta, referencePublication=dict(ref, **{"@type": "ScholarlyArticle"}))),
         ("type of the paper in codemeta.json: 'ScholarlyArticle' against ",)),
        ("a changed title in the BibTeX entry",
         mutated("readme", files["readme"].replace("title   = {Ensuring", "title   = {Ensurring", 1)),
         ("BibTeX title: 'Ensurring ",)),
        ("a BibTeX note without Working Paper",
         mutated("readme", files["readme"].replace("note    = {Working Paper", "note    = {Paper", 1)),
         ("the BibTeX entry's note does not name the document type Working Paper",)),
        ("a changed checksum in SHA256SUMS",
         mutated("sums", ("0" * 64) + "  " + DEPOSIT + "\n"),
         ("the SHA-256 of SHA256SUMS does not stand in README.md",
          "the SHA-256 of SHA256SUMS does not stand in publication/README.md")),
        ("a second BibTeX entry", mutated("readme", files["readme"] + "\n```bibtex\n@article{x,\n}\n```\n"),
         ("the README holds 2 @article entries in bibtex blocks, not one",)),
        ("a paper reference in codemeta.json that is not a mapping",
         mutated("meta", dict(meta, referencePublication=[ref])),
         ("codemeta.json referencePublication is not a mapping",)),
        ("an errata index row whose class differs from its entry",
         mutated("errata", re.sub(r"^(\| \[P-E001\]\(#p-e001\) \| [^|]+ \| )[^|]+( \|)",
                                  r"\1typographical\2", files["errata"], count=1, flags=re.M)),
         ("ERRATA.md index: the class of P-E001 is 'typographical', the entry says ",)),
    ]
    failures = 0
    for name, case, expected in cases:
        found = compare(case)
        ok = len(found) == len(expected) and all(want in got for want, got in zip(expected, found))
        failures += not ok
        print("  [%s] %s: %s" % ("ok" if ok else "FAIL", name, "; ".join(found) if found else "not found"))
        if not ok:
            print("         expected: %s" % "; ".join(expected))
    if failures:
        print("  [FAIL] selftest: %d of %d mutation(s) not found as their case names" % (failures, len(cases)))
        return 1
    print("  [OK]   selftest: %d mutations found, each by the findings its case names" % len(cases))
    return 0


def main(argv):
    if argv[1:] not in ([], ["--selftest"]):
        print(USAGE, file=sys.stderr)
        return 2
    try:
        if argv[1:] == ["--selftest"]:
            return selftest()
        files = load(ROOT)
    except ReadError as exc:
        print("  [ERR]  %s; nothing was compared" % exc, file=sys.stderr)
        return 2
    found = compare(files)
    for line in found:
        print("  [DIFF] %s" % line)
    if found:
        print("  [FAIL] %d finding(s) in CITATION.cff, codemeta.json, the README, SHA256SUMS and the errata index"
              % len(found))
        return 1
    print("  [OK]   CITATION.cff, codemeta.json, the README's BibTeX entry and SHA256SUMS agree, and so do the errata"
          " index and its entries")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
