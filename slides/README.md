<!--
SPDX-FileCopyrightText: 2026 Mert Torun
SPDX-License-Identifier: CC-BY-4.0
-->

# slides/

This folder holds the LaTeX sources of the deck and the handout of the talk on the paper at the VIMS-Workshop 2026 of the research focus Vernetzte intelligente Infrastrukturen und mobile Systeme (VIMS), TH Köln, on 2026-05-22, as page 2 of the deposited paper records it. They are sources only; no PDF of the slides is part of this repository.

## Which state this is

The deck as presented on 2026-05-22 is not archived. The earliest preserved sources of the deck and the handout date from 2026-07-12; the sources here are those, revised in October 2026, after the presentation, so that they agree with the revised edition of the research report and with [`ERRATA.md`](../ERRATA.md). Each frame of the deck that differs from the sources of July 2026 says at its foot what changed; the handout says so under its title. The main changes:

- The title, the venue and the publication are named in full: the paper's title with its subtitle, the workshop with its research focus and date, and the paper as a Working Paper in Kölner Beiträge zur technischen Informatik 2/2026, published under <https://doi.org/10.57684/COS-1494>. The author's degree and the name of the supervisor are no longer printed.
- The defects follow Table 5.4 of the report: six instead of five, each with how it was found, and B4 and B5 with the status the report gives them: a fix of the firmware of 2023 was applied, the diagnostic path was not verified separately, and no log was archived; for the freeze seen with the firmware of 2025 no fix is documented, and whether the VHDL transmitter was changed is not documented.
- The evidence is described as the report describes it in Section 5.1.3: simulation and the fixture runs indicate equivalence of the fault handling, the only measurement against the original board shows a deviation of the sweep, and the evidence does not demonstrate equivalence. The frames "three converging lines" and "frequency-sweep equivalence" are replaced.
- Prior work is credited: the board design and the measurement captures of M. Leyer (2023), the test fixture and its test case of A. Dolata, D. Ostermann and F. Schiffelers (2023), the redesign of S. Ayoub (2014).
- Statements that the report does not support are taken out: the deployment across several operators, the firmware size, the isolation of the solder defects by boundary scan, the memory masked by a cache, and the statement that the defects are a proof of the method.

## Contents

| File | Content |
| --- | --- |
| `presentation.tex` | The deck (Beamer, 16:9); it inputs the two files below |
| `deck_preamble.tex` | Packages, theme, title data and the macro that marks a revised frame |
| `deck_frames.tex` | The 15 frames |
| `handout.tex` | A one-page A4 synopsis, independent of the deck |
| `.latexmkrc` | Output directory of the build |

The frame on the frequency sweep includes the two captures in [`../paper/fig/`](../paper/fig/).

## Building

With TeX Live (pdfLaTeX and latexmk), from the root of the repository:

```sh
make slides    # writes slides/.tmp.nosync/latex/presentation.pdf and handout.pdf
```

## Licence

The deck and the handout are licensed under CC BY 4.0. Not covered is the material of third parties: the two captures of the frequency sweep by M. Leyer, which the deck includes from `paper/fig/`, and the YAML test case on the Layer 2 frame, adapted from the test fixture report and marked as an SPDX snippet; see [`NOTICE`](../NOTICE). Two parts of `deck_frames.tex` come from the paper and keep its licence, CC BY-NC-ND 4.0, marked as SPDX snippets: the research question on the frame "The question", quoted from page 3 of the deposited paper, and the drawing of the V-model on the frame "Two layers on the V-model", after Fig. 2 of the paper.
