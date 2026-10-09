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

    check_metadata.py            check the files
    check_metadata.py --selftest show that a changed DOI, version, type, title,
                                 note or checksum, and a paper reference that is
                                 not a mapping, are found, each by the findings
                                 its case names and by no other

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
    except (OSError, ValueError, yaml.YAMLError) as exc:
        raise ReadError(str(exc))
    if not isinstance(cff, dict) or not isinstance(meta, dict):
        raise ReadError("CITATION.cff or codemeta.json is not a mapping")
    return {"cff": cff, "meta": meta, "readme": readme, "record": record, "sums": sums}


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
        print("  [FAIL] %d finding(s) in CITATION.cff, codemeta.json, the README and SHA256SUMS" % len(found))
        return 1
    print("  [OK]   CITATION.cff, codemeta.json, the README's BibTeX entry and SHA256SUMS agree")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
