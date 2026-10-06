#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Mert Torun
# SPDX-License-Identifier: MIT
"""Check the links of this repository to doi.org, nbn-resolving.org and itself.

Only these hosts and paths are requested: the DOI and URN resolvers, which carry
the citable addresses of the paper, and this repository's own pages on
github.com. Other hosts are not requested, because publishers and many other
sites answer scripts with 403, and a check that fails for that reason says
nothing about the link. The web addresses printed in the paper are not checked
here either: the deposited paper cannot change, and ERRATA.md lists those that
moved.

The URLs are taken from the Markdown files outside fenced code blocks, from
CITATION.cff and from codemeta.json; the LaTeX sources of the paper, the report
and the slides are not read. The workflow runs this check on push and by hand,
never as a required check.

    check_links.py          request every URL in scope
    check_links.py --list   name the URLs in scope and request nothing

Any other argument is refused with a usage line before a file is read or a URL
is requested.

Exit status: 0 every link answered with a success or a redirect; 1 a link
answered with an HTTP error, and every request received an HTTP response; 2 the
arguments were not understood, a file could not be read, no URL in scope was
found (a check over nothing is not a pass), or a request received no HTTP
response at all, because name resolution, the connection or the transfer
failed or timed out, so that its link was not checked. 2 beats 1: when no
request received a response, nothing could be checked, and when only some
did, the links that answered with an error are still listed.
"""

import http.client
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = re.compile(r"https?://[^\s<>()\"'`\]\[|]+")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
OWN = ("/mtorun0x7cd/anti-skid-verification",)
SKIP = {".git", ".tmp.nosync"}
AGENT = "anti-skid-verification link check"
USAGE = "usage: check_links.py [--list]"


def in_scope(url):
    host_path = url.split("://", 1)[1]
    host, _, path = host_path.partition("/")
    path = "/" + path.split("#", 1)[0]
    if host in ("doi.org", "nbn-resolving.org"):
        return True
    if host != "github.com":
        return False
    return any(path == base or path.startswith(base + "/") for base in OWN)


def urls_of(path):
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".md":
        kept, fenced = [], False
        for line in text.splitlines():
            if FENCE.match(line):
                fenced = not fenced
                continue
            if not fenced:
                kept.append(line)
        text = "\n".join(kept)
    return [match.group(0).rstrip(".,;:") for match in URL.finditer(text)]


def collect():
    files = sorted(p for p in ROOT.rglob("*.md") if not SKIP.intersection(p.relative_to(ROOT).parts))
    files += [ROOT / "CITATION.cff", ROOT / "codemeta.json"]
    found = {}
    for path in files:
        if path.is_file():
            for url in urls_of(path):
                if in_scope(url):
                    found.setdefault(url, path.relative_to(ROOT).as_posix())
    return found


def request(url):
    """Return the HTTP status and the address reached, or, when no HTTP response
    came back at all, the reason as a string."""
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url.split("#", 1)[0], method=method, headers={"User-Agent": AGENT})
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.status, response.geturl()
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in (403, 405, 501):
                continue
            return exc.code, url
        except (urllib.error.URLError, http.client.HTTPException, TimeoutError, OSError, ValueError) as exc:
            return str(exc), url
    return "no answer", url


def main(argv):
    if argv[1:] not in ([], ["--list"]):
        print(USAGE, file=sys.stderr)
        return 2
    try:
        found = collect()
    except (OSError, UnicodeDecodeError) as exc:
        print("ERROR %s; nothing was checked" % exc, file=sys.stderr)
        return 2
    if not found:
        print("ERROR no URL in scope was found; nothing was checked")
        return 2
    if argv[1:] == ["--list"]:
        for url, source in sorted(found.items()):
            print("%s  (%s)" % (url, source))
        return 0
    failed = unanswered = 0
    for url, source in sorted(found.items()):
        status, final = request(url)
        if not isinstance(status, int):
            unanswered += 1
            print("NO RESPONSE %s (%s): %s" % (url, source, status))
            continue
        good = 200 <= status < 400
        failed += not good
        print("%s %s (%s): %s%s" % ("PASS" if good else "FAIL", url, source, status,
                                    "" if final == url.split("#", 1)[0] else ", reached " + final))
    if unanswered == len(found):
        print("ERROR no request received an HTTP response (name resolution, connection or timeout); "
              "nothing could be checked")
        return 2
    if unanswered:
        print("ERROR %d of %d request(s) received no HTTP response, so their links were not checked; "
              "%d link(s) answered with an error" % (unanswered, len(found), failed))
        return 2
    print("%s: %d of %d link(s) failed" % ("FAIL" if failed else "OK", failed, len(found)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
