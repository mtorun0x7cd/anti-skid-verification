<!--
SPDX-FileCopyrightText: 2026 Mert Torun
SPDX-License-Identifier: CC-BY-4.0
-->

# paper/

This folder holds the author's corrected manuscript of the paper, not the source of the deposited file. The version of record is [`publication/2026_02_Retrofitted_Anti-Skid_System.pdf`](../publication/2026_02_Retrofitted_Anti-Skid_System.pdf), the editors' build of the version the author sent on 28 June 2026; the LaTeX sources of that version are not available to this repository.

## Relation to the deposited text

The text of `paper.tex` is the text of pages 3 to 10 of the deposited file. Where it differs, the difference is the correction of an error that [`ERRATA.md`](../ERRATA.md) lists; there are no other differences. The manuscript was reconciled with the deposited text in October 2026: changes made to it after 28 June 2026 that do not make the correction an entry of `ERRATA.md` states were taken back, among them the author's degree on the author line. The other errors that `ERRATA.md` lists stand in `paper.tex` as they were deposited.

| Place in the deposited file | Deposited text | Text in `paper.tex` | Erratum |
| --- | --- | --- | --- |
| p. 3, Section I, first sentence | "comply with increasingly stringent safety standards [1], [2]" | "comply with increasingly stringent safety standards [2]" | [P-E003](../ERRATA.md#p-e003) |
| p. 4, Section II-C | "achieved certification against EN 15595 [18] through HIL testing" | "achieved certification against EN 15595 [18]" | [P-E013](../ERRATA.md#p-e013) |
| p. 4, Section II-D | "EN 50716 [22] (software/HDL modification)" | "EN 50716 [22] (software modification)" | [P-E015](../ERRATA.md#p-e015) |
| p. 8, Table III | "SW/HDL modification" | "SW modification" | [P-E015](../ERRATA.md#p-e015) |
| p. 4, Section III-A | "(adapted from the OpenCores t48_core)" | "(the OpenCores t48_core, integrated unmodified)" | [P-E018](../ERRATA.md#p-e018) |
| p. 6, Section IV-B 1) | "the NVRAM_ble signal (active-low chip enable) was erroneously held at logic high in the inherited Rev 0.0 design, effectively disabling the non-volatile memory entirely [11]" | "the NVRAM_ble signal (the active-low byte-low-enable) was erroneously held at logic high in the inherited Rev 0.0 design, preventing correct access to the non-volatile memory [11]" | [P-E031](../ERRATA.md#p-e031) |
| p. 7, Section IV-C | "the main 64-pin system connector" | "the main 48-pin DIN 41612 (type F) system connector" | [P-E034](../ERRATA.md#p-e034) |
| p. 7, Section V-A 1) | "(NVRAM_ble was erroneously held high, disabling the chip [11])" | "(NVRAM_ble, the byte-low-enable, was erroneously held high [11])" | [P-E031](../ERRATA.md#p-e031) |
| p. 8, Table II, row B1 | "NVRAM chip enable (NVRAM_ble) held high" | "NVRAM byte-low-enable (NVRAM_ble) held high" | [P-E031](../ERRATA.md#p-e031) |
| p. 8, Section V-B | "the NVRAM chip-enable error (B1)" | "the NVRAM byte-low-enable error (B1)" | [P-E031](../ERRATA.md#p-e031) |

Reference [1] keeps its number after its citation in the first sentence was withdrawn, because it is still cited on pages 4 and 9 and the reference list is the deposited one; `paper.tex` keeps the number with a `\nocite`. A build of `paper.tex` has eight pages: the series cover, the imprint and the running header and footer of the deposited file are the editors'. Compared word by word with pages 3 to 10 of the deposited file on 2026-10-05, a build differed only in the corrections above, in line, column and page breaks, and in the order in which a text extractor reads equations, figures and the listing; the citation numbers and the reference list were the same.

After the tag `cos-1494`, the text of the paper changes only through `ERRATA.md`: each later change to the manuscript names the identifier of its erratum (`P-E001` to `P-E049`) in its commit message.

## Contents

| Path | Content | Licence |
| --- | --- | --- |
| `paper.tex` | The manuscript, IEEEtran journal format | CC BY-NC-ND 4.0, the licence of the paper; Listing 1, adapted from Listing 3 of reference [28] ([P-E037](../ERRATA.md#p-e037)), is third-party material, marked as an SPDX snippet; see [`NOTICE`](../NOTICE) |
| `references.bib` | Its 29 references, as the deposited reference list prints them | CC BY-NC-ND 4.0 |
| `fig/watchdog_reaction.png`, `fig/comp_upsweep.png`, `fig/comp_downsweep.png` | Figs. 3 and 5: oscilloscope captures by Mark Leyer of 2023, reproduced from reference [10] ([P-E029](../ERRATA.md#p-e029)) | Third-party material, not licensed by this repository; see [`NOTICE`](../NOTICE) |
| `IEEEtran.cls`, `IEEEtran.bst` | The IEEEtran class (version 1.8b) and bibliography style (version 1.14), unedited | LPPL 1.3c |
| `.latexmkrc` | Output directory of the build | MIT |

## Building

With TeX Live (pdfLaTeX, BibTeX and latexmk), from the root of the repository:

```sh
make paper    # writes paper/.tmp.nosync/latex/paper.pdf
```

The build date is the time of the last commit that changed `paper/`; outside a clone, set `SOURCE_DATE_EPOCH` by hand.
