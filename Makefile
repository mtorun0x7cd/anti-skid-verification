# SPDX-FileCopyrightText: 2026 Mert Torun
# SPDX-License-Identifier: MIT
#
# Build and check the paper, the research report and the slides.
#
#   make paper            typeset paper/paper.tex into paper/.tmp.nosync/latex/paper.pdf
#   make report           typeset report/report.tex into report/.tmp.nosync/latex/report.pdf
#   make slides           typeset the deck and the handout into slides/.tmp.nosync/latex/
#   make check            run ChkTeX over the LaTeX sources; any warning fails
#   make verify-deposit   check publication/ against SHA256SUMS
#
# Each document is built with SOURCE_DATE_EPOCH set to the time of the last
# commit that changed its folder, so that two builds of one commit give the
# same bytes. Outside a clone, set SOURCE_DATE_EPOCH by hand; it then applies to
# every document. Each folder's .latexmkrc writes the output into its own
# .tmp.nosync/latex/, which git ignores. No target deletes anything.

SHELL       := /bin/bash
.SHELLFLAGS := -euo pipefail -c

LATEXMK ?= latexmk
BIBER   ?= biber
LFLAGS  := -pdf -interaction=nonstopmode -file-line-error -synctex=0

export FORCE_SOURCE_DATE := 1

# The commit time of folder $(1), unless SOURCE_DATE_EPOCH is set.
epoch = $(or $(SOURCE_DATE_EPOCH),$(shell git log -1 --format=%ct -- $(1) 2>/dev/null),$(error SOURCE_DATE_EPOCH is not set and git gives no commit time for $(1)/))

.PHONY: all paper report slides check verify-deposit

all: paper report slides

paper:
	cd paper && SOURCE_DATE_EPOCH=$(call epoch,paper) $(LATEXMK) $(LFLAGS) paper.tex

report:
	cd report && SOURCE_DATE_EPOCH=$(call epoch,report) $(LATEXMK) $(LFLAGS) -e '$$biber=q{$(BIBER) %O %S}' report.tex

# The deck includes the sweep captures of paper/fig/, so their commits count too.
slides:
	cd slides && SOURCE_DATE_EPOCH=$(call epoch,slides paper/fig) $(LATEXMK) $(LFLAGS) presentation.tex handout.tex

check:
	find paper report slides -name '*.tex' -not -path '*/.tmp.nosync/*' -exec chktex -q -I0 -l .chktexrc {} +

verify-deposit:
	cd publication && if command -v sha256sum >/dev/null; then sha256sum -c SHA256SUMS; \
		else shasum -a 256 -c SHA256SUMS; fi
