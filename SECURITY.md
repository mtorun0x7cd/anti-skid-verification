# Security policy

## Scope

This repository holds the paper "Ensuring Functional Equivalence in Retrofitted Anti-Skid Systems for European Public Transportation: A Hybrid Two-Layer Verification Methodology" as deposited, the author's corrected manuscript of it, the LaTeX sources of the research report from which it derives, the slides of the talk on it, the traceability data of the diagnostic path and the scripts that check them. It runs no service and is not developed further; no version receives security updates. The hardware, the FPGA design and the firmware the works describe are not part of it.

## What to report privately

- A secret, a credential or personal data committed to this repository by mistake, in a file or in the history.
- Content that identifies a third party that the works keep anonymous, such as a mark, a designation or a production code on a board, in a file, an image or a PDF.
- A file that is not what this repository says it is, for example a PDF whose SHA-256 differs from `publication/SHA256SUMS`, or a deposited file that differs from the one the catalogue record serves.
- A weakness of the workflows under `.github/` that could let someone change what the repository publishes.

## How to report

Use GitHub's private vulnerability reporting (the tab Security, then Report a vulnerability), or write to [info@mtorun0x7cd.com](mailto:info@mtorun0x7cd.com), naming the file, the problem and how to see it.

## What is not a vulnerability

The isolation of the STM32 Diagnostics Board, the watchdog and the brown-out supervision are design features that the works describe; the report says what of them was tested and what was not, and recommends a cybersecurity assessment of the USB and SD-card interfaces before any deployment. The scripts in `tools/` are checks of this repository, not hardened software. An error in the text of the paper or the report is a correction, not a security report; see the README, section Corrections.

## What to expect

Reports are read. A reply or a fix is not guaranteed, because the repository is not maintained as software.
