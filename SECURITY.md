# Security Policy

## Status

This repository holds the source and compiled deliverables of an **active
research publication** — an IEEE-format paper, an M.Sc. research report, and the
accompanying presentation. It is not a deployed software system: it builds LaTeX
documents and carries no runtime, no network service, and no executable
application.

## Scope

The repository contains documents (LaTeX, BibTeX/BibLaTeX), a machine-readable
requirements-to-test traceability matrix (`verification/test_traceability.yaml`),
and the build tooling that produces the PDFs. There is no production code, no
credentials, and no network-facing component. The hardware and firmware
described in the paper (VHDL, STM32 firmware, the Python test fixture) are not
distributed here; the adapted OpenCores `t48` core referenced in the work is
GPL-2.0 and is likewise not included.

## Reporting

To report a factual error, a broken build, or any other substantive issue worth
recording, contact info@mtorun0x7cd.com. As an actively maintained research
repository, corrections that affect the published record are handled through the
normal camera-ready / erratum process.
