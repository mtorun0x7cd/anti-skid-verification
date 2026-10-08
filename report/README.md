<!--
SPDX-FileCopyrightText: 2026 Mert Torun
SPDX-License-Identifier: CC-BY-4.0
-->

# report/

This folder holds the LaTeX sources of the research report "Ensuring Functional Equivalence and Compliance with Functional Safety Standards in Retrofitted Anti-Skid Systems for European Public Transportation: A Methodological Approach to Testing, Certification, and Risk Mitigation for Modernised Safety-Critical Electronics" by Mert Torun, TH Köln. It is the revised edition of October 2026 of the report submitted in August 2025 in the Master's programme Computer Science & Engineering (Technische Informatik). The revised edition is not yet deposited; its record, with a DOI, follows its deposit on ePublications, a publication server of TH Köln.

## Edition note

This is not the version that was assessed. The assessment refers to the report as submitted in August 2025; the revised edition has not been re-assessed. Page ii of the report, "About this edition", lists what changed, and these are the changes a reader of the assessed version needs to know:

- **The two defects of the diagnostic path, B4 and B5.** The submitted report recorded them as a freeze of the SD-card logging and a corrupted third byte in the SPI transmission, both open. This edition describes the causes found in the STM32 firmware of 2023 and the fix applied to that firmware after the submission; the cause of the freeze seen with the firmware of 2025 is not established (Section 5.3, Table 5.4). The rebuilt unit was observed operating as a whole in early 2026; the diagnostic path was not verified separately, and no log or capture of that run was archived.
- **The defects and how they were found.** Table 5.4 is new and lists six defects; the sixth, the swapped 7-segment displays (B6), is documented in the follow-on report and was in neither the submitted report nor the paper. How the defects B1 to B3 were found is corrected.
- **Prior work.** Results and measurement captures that come from prior work are credited to it, among them the oscilloscope captures of the watchdog and of the frequency sweep, taken by Mark Leyer on the Rev 0.0 prototype in 2023 (Figure 5.1, Figure C.1).
- **References.** Nine references of the submitted report could not be traced to a published work; four are replaced by works read for this edition and five are removed (the table on page ii).
- **Standards.** No compliance with EN 50716 is claimed, and the checklist of Chapter 7 marks what is not documented.
- **Front and back matter.** Appendix E of the submitted report (a sample "Prüfzertifikat" template) and its blank statutory declaration form are not part of this edition; a declaration of the author takes the place of the latter (page iii).
- **Photographs.** In the board photographs of Appendix A, a graphic logo and a board designation of third-party origin are masked, on one board together with the production code of the PCB manufacturer; the layout views, rendered anew from the design files, leave them out. None of these markings carries technical content.

Page ii also names the corrections that do not change a result: the real-time clock, the bill of materials, the schematic sheets and their captions, the design rules, the displays of the LED Board layout, the watchdog service path, the legacy processor and the authorship of the Rev 1.0 design.

## Overlap with the paper

The paper published as <https://doi.org/10.57684/COS-1494> derives from the version of this report submitted in August 2025, and where the two differ, the revised edition is the corrected one (page ii). This edition in turn takes over parts of the paper: its description of the causes of B4 and B5 in the firmware of 2023 and of their fix follows Section V-E of the paper (Section 5.3), and Figures 3.1 and 4.1 are derived from Figs. 1 and 4 of the paper, as the comments in `fig/system_overview.tex` and `fig/test_fixture.tex` state. The two works share:

- Figure 3.1 and Figure 4.1, adapted from Figs. 1 and 4 of the paper;
- Figure 5.2, which shows the mapping of the two layers to the V-model that Fig. 2 of the paper shows, in a drawing of its own: six boxes with a note on each, no box for the implementation and no colours (page 46 of this report, page 6 of the deposited paper);
- Figure 5.1 and Figure C.1, which reproduce the same measurement captures by Mark Leyer as Figs. 5 and 3 of the paper; they are third-party material in both;
- Tables 5.2, 5.4 and 5.5, which revise Tables I, II and III of the paper;
- the YAML test case of Appendix D.1, which, like Listing 1 of the paper, is adapted from Listing 3 of the test fixture report;
- single sentences and captions.

Measured on 2026-10-08 on the text of a build of the report and of pages 3 to 10 of the deposited paper, as pdftotext extracts it without its layout option, in Unicode form NFKC, with a word divided by a hyphen at a line end joined where the next line begins with a lower-case letter, then in lower case, and with a word taken as a run of the letters a to z and the digits, together with an apostrophe, straight or curly, and the letters that follow it: 379 of the 43,256 sequences of six words in the report also occur in the paper. They form 106 passages of at most 34 words: the acknowledgements, the title of the paper as the report cites it, entries of the bibliography, items of lists, captions and single sentences.

As the title page of the report states, passages that also appear in the paper remain under the paper's licence, CC BY-NC-ND 4.0; the sources of Figures 3.1 and 4.1 carry that licence ([`NOTICE`](../NOTICE), section 1). Figure 5.2, the report's own drawing, stays under CC BY 4.0 with the report.

## Contents

| Part | File | Subject |
| --- | --- | --- |
| Title page, page ii, page iii, abstracts, acknowledgements | `report.tex`, `meta/`, `abstract/`, `keywords/` | Title page with the licence; the edition note; the author's declaration; the abstract in English and, marked as translations, in German, French, Turkish and Spanish |
| Chapter 1 | `chapters/chapter1.tex` | Introduction: purpose, research questions, contributions and who did what, objectives and scope |
| Chapter 2 | `chapters/chapter2.tex` | Background: the prior work this report continues, verification strategies, rail retrofits, standards |
| Chapter 3 | `chapters/chapter3.tex` | System architecture: the four boards, the FPGA core, the STM32 Diagnostics Board, supervision and isolation |
| Chapter 4 | `chapters/chapter4.tex` | Testing methodology: the two layers, the requirement basis (Table 4.1), the verification artefacts |
| Chapter 5 | `chapters/chapter5.tex` | Results: test outcomes (Table 5.2), the state of the evidence (Table 5.3), the integration defects (Table 5.4), the causes of B4 and B5 and the fix applied (Section 5.3), the standards (Table 5.5), limitations |
| Chapter 6 | `chapters/chapter6.tex` | Conclusion, lessons learned, future work |
| Chapter 7 | `chapters/chapter7.tex` | Safety checklist for retrofits |
| Appendix A | `chapters/appendixA.tex`, `fig/photos/`, `fig/schematic/`, `fig/layout/` | Board photographs, schematic, layouts |
| Appendix B | `chapters/appendixB.tex` | Bill of materials and design rules |
| Appendix C | `chapters/appendixC.tex`, `fig/watchdog_capture.jpg` | Format of the fixture's test log; the watchdog capture of 2023 |
| Appendix D | `chapters/appendixD.tex` | A YAML test case of the fixture and a VHDL excerpt |
| References | `bib/references.bib` | The bibliography, read with Biber |
| Figures | `fig/system_overview.tex`, `fig/test_fixture.tex`, `fig/v_model_mapping.tex` | Figures 3.1, 4.1 and 5.2 as TikZ sources |
| Build | `report.xmpdata`, `.latexmkrc` | PDF/A-2b metadata; output directory and glossary rules of the build |

The VHDL sources, the STM32 firmware, the YAML test suites of the fixture and the design files are not published with the report; the README of this repository, section "What is public and what is not", says why.

## Building

With TeX Live (pdfLaTeX, Biber and latexmk with makeglossaries), from the root of the repository:

```sh
make report    # writes report/.tmp.nosync/latex/report.pdf
```

The build date is the time of the last commit that changed `report/`; outside a clone, set `SOURCE_DATE_EPOCH` by hand. The build is a PDF/A-2b file of 102 pages. On 2026-10-08, two builds with the same `SOURCE_DATE_EPOCH` gave the same bytes, and veraPDF found the build conformant to PDF/A-2b. The build is untagged, that is, it has no structure tree for assistive technology: PDF/A-2b does not require one, and pdfinfo reports `Tagged: no`. It declares its language, English, and carries bookmarks and page labels.

## Licence

The report is licensed under CC BY 4.0, as its title page states. Excluded is material credited to others in a caption or in the text, among it the adapted and reproduced figures, the board designs of Rev 0.0 and Rev 1.0, content taken from the legacy manual, the VHDL excerpt in Appendix D, the fixture test case and the TH Köln logo; [`NOTICE`](../NOTICE) lists these files. The list on the title page names the Rev 0.0 designs only; the Rev 1.0 designs, which Appendix A credits to Leyer, fall under the same exclusion of material credited to others. Passages that also appear in the paper remain under its licence, CC BY-NC-ND 4.0.
