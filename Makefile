# Retrofitted Anti-Skid Systems - deterministic build
#
# Targets:
#   make all      build the paper, the report, and the public talk deck
#   make paper    build the IEEE paper only
#   make report   build the research report only
#   make slides   build the talk deck + handout (the tracked, public slides)
#   make prep     build the local-only speaker materials (notes, cards, FAQ, prep)
#   make check    run ChkTeX on all sources
#   make clean    remove build artefacts
#
# Built PDFs are staged under .tmp.nosync/dist/ for release upload; they are
# not tracked and not written into docs/ (which holds only social-preview art).
#
# biber on the report is overridable for platforms where the TeX Live
# universal binary fails to self-extract (e.g. macOS):
#   make BIBER=/opt/homebrew/bin/biber

.PHONY: all paper report slides prep check clean

LATEXMK := latexmk
BIBER   ?= biber
LFLAGS  := -pdf -interaction=nonstopmode -file-line-error -synctex=0
SLIDEOUT := slides/.tmp.nosync/latex
DIST     := .tmp.nosync/dist

# Deterministic, reproducible output for a given source revision.
export SOURCE_DATE_EPOCH ?= $(shell git log -1 --pretty=%ct 2>/dev/null || echo 0)
export FORCE_SOURCE_DATE := 1

all: paper report slides

paper:
	cd paper && $(LATEXMK) $(LFLAGS) paper.tex
	mkdir -p $(DIST) && cp paper/.tmp.nosync/latex/paper.pdf $(DIST)/paper.pdf

report:
	cd report && $(LATEXMK) $(LFLAGS) -e '$$biber=q{$(BIBER) %O %S}' report.tex
	mkdir -p $(DIST) && cp report/.tmp.nosync/latex/report.pdf $(DIST)/report.pdf

# Public talk deck (tracked).
slides:
	cd slides && $(LATEXMK) $(LFLAGS) presentation.tex handout.tex
	mkdir -p $(DIST)
	cp $(SLIDEOUT)/presentation.pdf $(DIST)/presentation.pdf
	cp $(SLIDEOUT)/handout.pdf       $(DIST)/handout.pdf

# Local-only speaker materials (sources are not version-controlled).
prep:
	cd slides && $(LATEXMK) $(LFLAGS) presentation_with_notes.tex \
		speaker_notes_script.tex speaker_notes_cards.tex faq.tex preparation.tex
	mkdir -p $(DIST)
	cp $(SLIDEOUT)/presentation_with_notes.pdf $(DIST)/presentation_with_notes.pdf
	cp $(SLIDEOUT)/speaker_notes_script.pdf    $(DIST)/speaker_notes_script.pdf
	cp $(SLIDEOUT)/speaker_notes_cards.pdf     $(DIST)/speaker_notes_cards.pdf
	cp $(SLIDEOUT)/faq.pdf                     $(DIST)/FAQ_VIMS2026.pdf
	cp $(SLIDEOUT)/preparation.pdf             $(DIST)/Preparation_VIMS2026.pdf

check:
	find paper report slides -name '*.tex' -not -path '*/.tmp.nosync/*' \
		-exec chktex -q -l .chktexrc {} +

clean:
	-cd paper && $(LATEXMK) -C paper.tex
	-cd report && $(LATEXMK) -C report.tex
	-cd slides && $(LATEXMK) -C presentation.tex handout.tex
	rm -rf .tmp.nosync paper/.tmp.nosync report/.tmp.nosync slides/.tmp.nosync report/.tmp out archive
	find . -path ./.git -prune -o -type f \( \
		-name '*.aux' -o -name '*.log' -o -name '*.out' -o -name '*.toc' -o \
		-name '*.bbl' -o -name '*.blg' -o -name '*.fdb_latexmk' -o -name '*.fls' -o \
		-name '*.synctex.gz' -o -name '*.nav' -o -name '*.snm' -o -name '*.vrb' -o \
		-name '*.acn' -o -name '*.acr' -o -name '*.alg' -o -name '*.bcf' -o \
		-name '*.glg' -o -name '*.glo' -o -name '*.gls' -o -name '*.ist' -o \
		-name '*.lof' -o -name '*.lot' -o -name '*.run.xml' \
	\) -print -delete
