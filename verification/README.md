<!--
SPDX-FileCopyrightText: 2026 Mert Torun
SPDX-License-Identifier: CC-BY-4.0
-->

# verification/

This folder holds the traceability data of the diagnostic path of the retrofitted test-diagnosis module: for each requirement, the tests or checks made of it, their status and the evidence each status rests on. The data were reconstructed in 2026 from Chapters 3 and 5 of the research report: the requirements from the design description of Sections 3.2 and 3.3 and from Section 5.3, the statuses from what these sections and Tables 5.3 and 5.4 say of the tests; formal traceability matrices were not produced during the project (report, Section 4.5). They cover the diagnostic path only and are not a certification artefact. The same statement stands at the head of the YAML file and in every row of the CSV view, column `record_status`, because both files travel without this README.

The diagnostic path is the SPI link from the FPGA logger through the optocouplers to the STM32 diagnostics board, and the logging of the frames on the SD card and over USB. The fault handling of the safety-related core is not covered here; Tables 4.1, 5.2 and 5.3 of the report describe it.

## Files

| File | Content | Licence |
| --- | --- | --- |
| `test_traceability.yaml` | The data: 8 requirements and 9 tests | CC BY 4.0 |
| `traceability.csv` | A flat view of the data, one row per test, generated from the YAML file | CC BY 4.0 |
| `traceability.schema.json` | The schema of the YAML file (JSON Schema 2020-12) | MIT |
| `template.yaml` | An empty skeleton of the format for another project | MIT |

[`tools/check_traceability.py`](../tools/check_traceability.py) checks the data and writes the CSV view.

## The data at a glance

| Test | Requirement | Layer | Status | Defect |
| --- | --- | --- | --- | --- |
| L1-DP-01 | REQ-DP-01: the FPGA logger of 2023 sends 32-bit frames | L1 | NOT-DOCUMENTED | |
| L1-DP-02 | REQ-DP-02: the logger of 2025 sends the error vector as three bytes | L1 | OPEN | B5 |
| L1-DP-03 | REQ-DP-03: error codes reach the STM32 over the isolated link | L1 | OBSERVED | |
| L2-DP-04 | REQ-DP-04: the STM32 receives each 32-bit frame completely | L2 | FIX-APPLIED-NOT-VERIFIED | B5 |
| L2-DP-05 | REQ-DP-05: frames are written to the SD card without loss, firmware of 2025 | L2 | OPEN | B4 |
| L2-DP-06 | REQ-DP-05: the same, firmware of 2023 after the fix | L2 | FIX-APPLIED-NOT-VERIFIED | B4 |
| L2-DP-07 | REQ-DP-06: the log files can be retrieved over USB | L2 | NOT-DOCUMENTED | |
| L1-DP-08 | REQ-DP-07: faults on the isolated side do not feed back | L1 | NOT-DOCUMENTED | |
| L1-DP-09 | REQ-DP-08: the SPI signals cross the optocouplers in time | L1 | OBSERVED | |

No test has the status PASS: no log, capture or measurement of the diagnostic path is archived.

## Data dictionary

### File level

| Field | Meaning |
| --- | --- |
| `schema_version` | Version of the format, 1 |
| `title` | Title of the data |
| `record_status` | What the data are, where they come from and what they are not |
| `applies_to` | The work the data belong to: the research report in its revised edition |
| `as_of` | Date of the data, YYYY-MM-DD |
| `scope` | What the data cover, and what they do not |
| `requirement_source` | Where the requirements come from |
| `requirements` | The list of requirements |

### Requirement

| Field | Meaning |
| --- | --- |
| `id` | `REQ-DP-nn`: requirement nn of the diagnostic path |
| `statement` | The requirement, restated from the design intent the report describes; no requirement list exists for the module (report, Section 4.5) |
| `source` | Where the report describes it: `label` is the LaTeX label in `report/`, `locator` the section, table or equation |
| `tests` | The tests or checks of the requirement |

### Test

| Field | Meaning |
| --- | --- |
| `id` | `L1-DP-nn` or `L2-DP-nn`: test nn, with its layer in the prefix |
| `layer` | 1, component and interface tests; 2, system-level tests (report, Chapter 4) |
| `method` | `simulation`, `link-test`, `oscilloscope`, `jtag`, `fixture`, `operation`, `inspection`, `firmware-analysis`, or `not-tested` where no test is documented |
| `item` | What was tested: a design, the Rev 0.0 prototype or the rebuilt unit, with its firmware |
| `date` | When, as far as the sources say; `null` where no test is documented |
| `status` | One value of the vocabulary below |
| `defect` | The defect of Table 5.4 of the report that the test concerns, or `null` |
| `evidence` | What the status rests on, at least one entry |
| `note` | What the sources say about the test, in the words of the report where it gives them |

### Evidence

| Field | Meaning |
| --- | --- |
| `source` | `report` for the research report, otherwise the key of the work in `report/bib/references.bib` |
| `label` | For the report, the LaTeX label of the place cited |
| `locator` | Section, table or page |
| `kind` | `report-text`, `project-report`, `source-code`, or one of the primary kinds `log`, `capture`, `measurement`, `test-protocol` |
| `archived` | Whether the evidence is kept |
| `public` | Whether it is published; the project reports and the design sources are not |

## Status vocabulary

| Status | Meaning | The report's words |
| --- | --- | --- |
| `PASS` | Tested and passed, with at least one archived piece of primary evidence (log, capture, measurement, test protocol) named | "Pass" (Table 5.2) |
| `OBSERVED` | A result reported in a source, without an archived primary record | "Observed" (Table 5.2) |
| `FIX-APPLIED-NOT-VERIFIED` | A fix was applied; the item was not verified separately afterwards | "fix applied; diagnostic path not verified separately" (Table 5.4) |
| `OPEN` | A defect was found, and no fix or change is documented | "no fix documented", "change not documented" (Table 5.4) |
| `NOT-DOCUMENTED` | No test of the item is documented | "Not documented" (Table 5.2) |

The text of the report alone never supports `PASS`; the check refuses such a row.

## Checking the data

With Python 3, PyYAML and jsonschema 4.0 or later, from the root of the repository:

```sh
python3 tools/check_traceability.py              # the schema, the rules and the CSV view
python3 tools/check_traceability.py --selftest   # each rule refuses the case it is written for
python3 tools/check_traceability.py --write-csv  # regenerate traceability.csv after a change
```

The check holds the YAML file to the schema; requires archived primary evidence for `PASS`; requires the prefix of each test identifier to match its layer and every identifier to be unique; requires every label it cites to be a label in `report/`, every other source a key of the report's bibliography, and every defect a row of Table 5.4; and requires the CSV view to equal its regeneration. Its self-test applies each rule to a mutated copy that the rule has to refuse, among them B4 marked `PASS` on the report's text alone. CI runs both on every push.

## Reuse

[`template.yaml`](template.yaml) is the format without data. A filled-in copy for another retrofit is checked against [`traceability.schema.json`](traceability.schema.json); the rules of the check that refer to `report/` name this repository's report and have to be adapted. The data are licensed under CC BY 4.0, the schema, the template and the check under the MIT License.
