# Changelog

All notable changes to this repository are listed here. The format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/). The first entry is the record tag `cos-1494`; from 1.1.0 on, the versions follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) and cover the code, the data and the documentation. The text of the paper changes only through [`ERRATA.md`](ERRATA.md).

This repository was recreated with a new history on 2026-10-05; the earlier release, v1.0.3 of 2026-08-01, was not the version of record and is withdrawn. It carried the research report in its state before the revision.

## [1.1.0] - 2026-10-05

### Added

- `README.md`: the two works, the abstract of the paper with four translations and the abstract of the report in five languages, the publication, the version of record, a summary of the work, the contents, the traceability data, what is public and what is not, how to reproduce the documents, the limitations, the corrections, the citation and the licences.
- `slides/`: the sources of the deck and the handout of the talk on the paper at the VIMS-Workshop 2026 on 22 May 2026, revised in October 2026 so that they agree with the revised edition of the report and with `ERRATA.md`; each revised frame says what changed. The deck as presented is not archived.
- `verification/`: the traceability data of the diagnostic path, reconstructed in 2026 from Chapter 5 of the report: eight requirements and nine tests or checks with their status and the evidence each status rests on, a JSON Schema, a generated CSV view, an empty template and a data dictionary. No test has the status PASS.
- `tools/check_traceability.py`, which checks the traceability data and refuses PASS without archived primary evidence; `tools/check_metadata.py` and `tools/check_links.py`, which check the citation metadata and the links; and the targets `slides`, `traceability` and `metadata` of the `Makefile`.
- The workflows, the correction form, `SECURITY.md`, `CONTRIBUTING.md`, `FUNDING.yml`, the opt-in pre-commit hook in `.githooks/`, which scans staged changes with `gitleaks git --staged`, the configurations of gitleaks and markdownlint, and the social card.

### Changed

- `CITATION.cff` and `codemeta.json` carry the version 1.1.0; their description names the slides and the traceability data, and `codemeta.json` names Python and the shell among the languages and Python with PyYAML and jsonschema among the requirements.
- `NOTICE` and `REUSE.toml` give the licences of the files added; `report/README.md` gives the measured overlap of the text of the report with the deposited paper.

### Fixed

Statements in files that the record tag `cos-1494` holds, corrected here; the tag keeps them as they were:

- `CITATION.cff`: the reference to the research report carries the English abstract of its revised edition; at the tag the reference has no abstract.

## [cos-1494] - 2026-10-05

### Added

- `publication/2026_02_Retrofitted_Anti-Skid_System.pdf`, the deposited paper, a Working Paper in the series Kölner Beiträge zur technischen Informatik 2/2026, byte-identical with the file behind <https://doi.org/10.57684/COS-1494>: 1,565,058 bytes, SHA-256 `bcf68b4b845c68ab48b43c1d91c855af7f8aac18f7a7a0846a43210ca66a3ebf`; with `SHA256SUMS` and a `README.md` on how to verify it.
- `paper/`, the author's corrected manuscript of the paper, not the source of the deposited file: its text is the deposited text except where it applies the corrections of P-E003, P-E013, P-E015, P-E018, P-E031 and P-E034. The sources carry the licence of the paper, CC BY-NC-ND 4.0.
- `report/`, the LaTeX sources of the research report in its revised edition of October 2026, which build a PDF/A-2b file of 102 pages; the report is licensed under CC BY 4.0, as its title page states.
- `ERRATA.md`: 49 entries on the errors of the paper, the properties of its record and of the deposited file, and the web addresses of the paper that no longer work or have moved.
- `CITATION.cff`, `codemeta.json`, `NOTICE`, `REUSE.toml`, the licence texts, the `Makefile` and the configuration files.

[1.1.0]: https://github.com/mtorun0x7cd/anti-skid-verification/compare/cos-1494...v1.1.0
[cos-1494]: https://github.com/mtorun0x7cd/anti-skid-verification/releases/tag/cos-1494
