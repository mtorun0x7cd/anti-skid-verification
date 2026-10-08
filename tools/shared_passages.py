#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Mert Torun
# SPDX-License-Identifier: MIT
"""List the passages that the research report shares with the paper.

report/README.md gives the overlap of the report with the deposited paper, and
this tool makes that measurement. It reads the text of a build of the report and
of pages 3 to 10 of the deposited paper as pdftotext extracts it without its
layout option, page by page; brings it into Unicode form NFKC; joins a word
divided by a hyphen at a line end where the next line begins with a lower-case
letter; then sets it in lower case; and takes as a word a run of the letters a
to z and the digits, together with an apostrophe, straight or curly, and the
letters that follow it. A sequence of six words of the report is shared when
the same six words occur in that order in the paper. Shared sequences that
overlap form one passage.

It writes OUTPUT, a Markdown file that lists every passage with the page of the
report on which it begins, as the page labels of the build name it and as PDF
page, its length in words and its wording, and the totals. The passages are text
of the paper, and the file says in its header that they remain under the licence
of the paper, CC BY-NC-ND 4.0.

    shared_passages.py REPORT_PDF PAPER_PDF OUTPUT

From the root of the repository, after make report:

    python3 tools/shared_passages.py report/.tmp.nosync/latex/report.pdf \\
        publication/2026_02_Retrofitted_Anti-Skid_System.pdf report/SHARED_PASSAGES.md

An option, a missing or a fourth argument, and an OUTPUT that is one of the two
PDF files are refused with a usage line before a file is read. Nothing is written
but OUTPUT, and OUTPUT only once both PDF files have been read; the same two
files give the same OUTPUT byte for byte, whatever their paths.

Exit status: 0 the list was written, 2 the arguments were not understood,
pdftotext could not read a PDF file, the paper has fewer than 10 pages, or OUTPUT
could not be written.
Needs pdftotext (Poppler) and the Python standard library.
"""

import hashlib
import os
import re
import subprocess
import sys
import unicodedata
import zlib

USAGE = "usage: shared_passages.py REPORT_PDF PAPER_PDF OUTPUT"
LENGTH = 6
PAPER_PAGES = (3, 10)
WORD = re.compile(r"[a-z0-9]+(?:['\u2019][a-z]+)?")
DIVIDED = re.compile(r"(?<=[^\W\d_])-\n(?=[^\W\d_])")
COMMAND = ("python3 tools/shared_passages.py report/.tmp.nosync/latex/report.pdf "
           "publication/2026_02_Retrofitted_Anti-Skid_System.pdf report/SHARED_PASSAGES.md")
MARKDOWN = re.compile(r"([\\`*_\[\]<>~&$|])")


class ReadError(Exception):
    """A PDF file could not be read."""


def pdf_text(path, pages=None):
    """The text of each page of a PDF file, as pdftotext extracts it without -layout."""
    command = ["pdftotext", "-enc", "UTF-8"]
    if pages:
        command += ["-f", str(pages[0]), "-l", str(pages[1])]
    try:
        run = subprocess.run(command + [path, "-"], capture_output=True)
    except OSError as exc:
        raise ReadError("pdftotext could not be started: %s" % exc)
    if run.returncode != 0:
        raise ReadError("pdftotext could not read %s: %s"
                        % (path, run.stderr.decode("utf-8", "replace").strip()))
    text = run.stdout.decode("utf-8")
    # pdftotext ends every page with a form feed
    return text[:-1].split("\f") if text.endswith("\f") else text.split("\f")


def join_divided(text):
    """Join a word divided by a hyphen at a line end where the next line begins
    with a lower-case letter."""
    return DIVIDED.sub(lambda m: "" if text[m.end()].islower() else m.group(0), text)


def words(pages):
    """(word, page index, start, end, page text) of every word: the text in NFKC
    with divided words joined, the word found in its lower case, its place given
    in that text."""
    out = []
    for number, page in enumerate(pages):
        text = join_divided(unicodedata.normalize("NFKC", page))
        lower, source = [], []
        for index, char in enumerate(text):
            for low in char.lower():
                lower.append(low)
                source.append(index)
        lower = "".join(lower)
        for match in WORD.finditer(lower):
            out.append((match.group(0), number, source[match.start()], source[match.end() - 1] + 1, text))
    return out


def passages(report, paper):
    """The number of sequences of the report, the positions of the shared ones,
    and the passages as (first word, last word) index pairs."""
    tokens = [w[0] for w in report]
    shared_set = set(tuple(paper[i:i + LENGTH]) for i in range(len(paper) - LENGTH + 1))
    total = max(len(tokens) - LENGTH + 1, 0)
    shared = [i for i in range(total) if tuple(tokens[i:i + LENGTH]) in shared_set]
    spans = []
    for i in shared:
        if spans and i <= spans[-1][1]:
            spans[-1][1] = i + LENGTH - 1
        else:
            spans.append([i, i + LENGTH - 1])
    return total, shared, spans


def wording(report, first, last):
    """The text of a passage as the page gives it, its white space collapsed."""
    parts = []
    for _word, page, start, end, text in report[first:last + 1]:
        if parts and parts[-1][0] == page:
            parts[-1][2] = end
        else:
            parts.append([page, start, end, text])
    return " ".join(" ".join(text[start:end].split()) for page, start, end, text in parts)


# Page labels: the catalog's /PageLabels number tree, read with the standard
# library from the plain objects of the file and from its object streams.
OBJECT = re.compile(rb"(?<![0-9])(\d+)\s+\d+\s+obj\b")


def pdf_objects(data):
    """Object number -> source of the object, for the objects of the file and
    for those packed into its object streams."""
    heads = list(OBJECT.finditer(data))
    objects = {}
    for k, head in enumerate(heads):
        end = heads[k + 1].start() if k + 1 < len(heads) else len(data)
        objects[int(head.group(1))] = data[head.end():end]
    for body in list(objects.values()):
        dictionary, found, rest = body.partition(b"stream")
        if not found or not re.search(rb"/Type\s*/ObjStm\b", dictionary):
            continue
        count = re.search(rb"/N\s+(\d+)", dictionary)
        first = re.search(rb"/First\s+(\d+)", dictionary)
        if not (count and first and re.search(rb"/Filter\s*/FlateDecode\b", dictionary)):
            continue
        try:
            raw = zlib.decompressobj().decompress(rest.lstrip(b"\r\n"))
        except zlib.error:
            continue
        offset = int(first.group(1))
        header = raw[:offset].split()[:2 * int(count.group(1))]
        pairs = [(int(header[i]), int(header[i + 1])) for i in range(0, len(header) - 1, 2)]
        for i, (number, start) in enumerate(pairs):
            stop = pairs[i + 1][1] if i + 1 < len(pairs) else len(raw) - offset
            objects.setdefault(number, raw[offset + start:offset + stop])
    return objects


def numeral(value, style):
    """A page number in the style of a /PageLabels range: D, R, r, A, a or none."""
    if style in (b"D", None):
        return str(value) if style else ""
    if style in (b"R", b"r"):
        out = ""
        for amount, letters in ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                                (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")):
            while value >= amount:
                out += letters
                value -= amount
        return out if style == b"R" else out.lower()
    letter = chr(ord("A") + (value - 1) % 26) * ((value - 1) // 26 + 1)
    return letter if style == b"A" else letter.lower()


def page_labels(data, count):
    """The label of each page, or None where the file does not give them all."""
    objects = pdf_objects(data)
    roots = re.findall(rb"/Root\s+(\d+)\s+\d+\s+R", data)
    catalog = objects.get(int(roots[-1])) if roots else None
    if catalog is None:
        return None
    tree = re.search(rb"/PageLabels\s*(?:(\d+)\s+\d+\s+R|<<)", catalog)
    if not tree:
        return None
    tree = objects.get(int(tree.group(1)), b"") if tree.group(1) else catalog[tree.start():]
    nums = re.search(rb"/Nums\s*\[(.*?)\]", tree, re.S)
    if not nums:
        return None
    ranges = []
    for match in re.finditer(rb"(\d+)\s*(<<.*?>>|\d+\s+\d+\s+R)", nums.group(1), re.S):
        entry = match.group(2)
        if entry.endswith(b"R"):
            entry = objects.get(int(entry.split()[0]), b"")
        if re.search(rb"/P\b", entry):
            return None          # a prefix is not read here; the PDF pages stand alone
        style = re.search(rb"/S\s*/([DRrAa])\b", entry)
        start = re.search(rb"/St\s+(\d+)", entry)
        ranges.append((int(match.group(1)), style.group(1) if style else None,
                       int(start.group(1)) if start else 1))
    ranges.sort(key=lambda r: r[0])
    if not ranges or ranges[0][0] != 0:
        return None
    labels = []
    for page in range(count):
        first, style, start = [r for r in ranges if r[0] <= page][-1]
        labels.append(numeral(start + page - first, style))
    return labels


def render(report_pages, report_digest, paper_digest, labels, report, paper, result):
    """The Markdown text of the list; it holds no path and no date."""
    total, shared, spans = result
    longest = max((last - first + 1 for first, last in spans), default=0)
    lines = [
        "<!--",
        "SPDX-FileCopyrightText: 2025-2026 Mert Torun",
        "SPDX-License-Identifier: CC-BY-NC-ND-4.0",
        "-->",
        "",
        "# Passages shared by the report and the paper",
        "",
        "This file is generated by [`tools/shared_passages.py`](../tools/shared_passages.py); do not edit it by hand. "
        "From the root of the repository, after `make report`, this command writes it anew:",
        "",
        "```sh",
        COMMAND,
        "```",
        "",
        "This version was generated from a build of the report of %d pages, SHA-256 `%s`, and from pages %d to %d "
        "of the deposited paper, SHA-256 `%s`. [`README.md`](README.md#overlap-with-the-paper) describes the "
        "measurement." % (report_pages, report_digest, PAPER_PAGES[0], PAPER_PAGES[1], paper_digest),
        "",
        "The passages below are text of the paper that the report also contains. As the title page of the report "
        "states, they remain under the licence of the paper, CC BY-NC-ND 4.0.",
        "",
        "## Totals",
        "",
        "- Words: {:,} in the report, {:,} on pages {} to {} of the paper".format(
            len(report), len(paper), PAPER_PAGES[0], PAPER_PAGES[1]),
        "- Sequences of six words in the report: {:,}".format(total),
        "- Of these, sequences that also occur in the paper: {:,}".format(len(shared)),
        "- Passages they form: {:,}, the longest of {:,} words".format(len(spans), longest),
        "",
        "## Passages",
        "",
        "Each passage gives the page of the report on which it begins, as printed and as PDF page, its length in "
        "words and its wording, as the text of the build gives it.",
        "",
    ]
    for number, (first, last) in enumerate(spans, start=1):
        page = report[first][1]
        where = "PDF p. %d" % (page + 1)
        if labels and labels[page]:
            where = "p. %s (%s)" % (labels[page], where)
        text = MARKDOWN.sub(r"\\\1", wording(report, first, last))
        lines.append('{}. {}, {:,} words: "{}"'.format(number, where, last - first + 1, text))
    return "\n".join(lines) + "\n"


def main(argv):
    args = argv[1:]
    if len(args) != 3 or any(a.startswith("-") for a in args):
        print(USAGE, file=sys.stderr)
        return 2
    report_path, paper_path, output = args
    if os.path.realpath(output) in (os.path.realpath(report_path), os.path.realpath(paper_path)):
        print("%s\nOUTPUT must not be one of the two PDF files" % USAGE, file=sys.stderr)
        return 2
    try:
        with open(report_path, "rb") as handle:
            report_data = handle.read()
        with open(paper_path, "rb") as handle:
            paper_data = handle.read()
        report_pages = pdf_text(report_path)
        paper_pages = pdf_text(paper_path, PAPER_PAGES)
    except (OSError, UnicodeDecodeError, ReadError) as exc:
        print("  [ERR]  %s; nothing was written" % exc, file=sys.stderr)
        return 2
    if len(paper_pages) != PAPER_PAGES[1] - PAPER_PAGES[0] + 1:
        print("  [ERR]  %s gives %d of the pages %d to %d; nothing was written"
              % (paper_path, len(paper_pages), PAPER_PAGES[0], PAPER_PAGES[1]), file=sys.stderr)
        return 2
    report = words(report_pages)
    paper = [w[0] for w in words(paper_pages)]
    result = passages(report, paper)
    try:
        labels = page_labels(report_data, len(report_pages))
    except (ValueError, IndexError, KeyError):
        labels = None            # the list then gives the PDF pages alone
    text = render(len(report_pages), hashlib.sha256(report_data).hexdigest(),
                  hashlib.sha256(paper_data).hexdigest(), labels, report, paper, result)
    try:
        with open(output, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
    except OSError as exc:
        print("  [ERR]  %s could not be written: %s" % (output, exc), file=sys.stderr)
        return 2
    total, shared, spans = result
    longest = max((last - first + 1 for first, last in spans), default=0)
    print("  [OK]   wrote {}: {:,} of the {:,} sequences of six words in the report also occur in the paper, "
          "in {:,} passages of at most {:,} words".format(output, len(shared), total, len(spans), longest))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
