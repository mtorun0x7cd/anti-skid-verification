<!--
SPDX-FileCopyrightText: 2026 Mert Torun
SPDX-License-Identifier: CC-BY-4.0
-->

# Version of record

This folder holds the paper "Ensuring Functional Equivalence in Retrofitted Anti-Skid Systems for European Public Transportation: A Hybrid Two-Layer Verification Methodology" by Mert Torun as it was deposited: a Working Paper in the series Kölner Beiträge zur technischen Informatik, volume 2/2026, published on Cologne Open Science, a publication server of TH Köln, on 2026-09-22.

| File | Work | Record | Bytes | SHA-256 | Licence | Relation to the sources |
| --- | --- | --- | --- | --- | --- | --- |
| `2026_02_Retrofitted_Anti-Skid_System.pdf` | Paper, document type Working Paper, Kölner Beiträge zur technischen Informatik 2/2026 | Cologne Open Science, document 1494, <https://doi.org/10.57684/COS-1494> | 1,565,058 | `bcf68b4b845c68ab48b43c1d91c855af7f8aac18f7a7a0846a43210ca66a3ebf` | CC BY-NC-ND 4.0, as the catalogue record states; the imprint on page 2 names the licence terms without a version. The measurement captures of Figs. 3 and 5 and Listing 1, which is adapted from the test fixture report, are third-party material, see [`NOTICE`](../NOTICE) | The version of record, byte-identical with the file the catalogue record serves. It cannot be rebuilt from this repository: [`paper/`](../paper/) holds the author's corrected manuscript, not the source of this file |

The deposited file is the editors' build of the version the author sent on 28 June 2026: the editors added the series cover (page 1), the imprint (page 2) and the running header and footer of the series with the page numbers (pages 3 to 10), and produced the file on 21 September 2026; the author's text is on pages 3 to 10. No later version of the paper went to the editors.

## Relation to the sources

The LaTeX sources of the version of 28 June 2026 are not available to this repository; the earliest sources of the paper that are, of 12 July 2026, already differ from the deposited text. [`paper/`](../paper/) therefore holds the author's corrected manuscript: its text is the text of pages 3 to 10 of this file, and where it differs, the difference is a correction listed in [`ERRATA.md`](../ERRATA.md); [`paper/README.md`](../paper/README.md) names each one. The deposited file stays as it is; after the tag `cos-1494`, the text of the paper changes only through `ERRATA.md`.

## Verifying the file

### Without an account

1. In a clone of this repository, check the file against [`SHA256SUMS`](SHA256SUMS):

   ```sh
   cd publication
   sha256sum -c SHA256SUMS          # on macOS: shasum -a 256 -c SHA256SUMS
   ```

2. Hash the file the catalogue record serves and compare the result with `SHA256SUMS`:

   ```sh
   curl -sSfL -o deposited.pdf https://cos.bibl.th-koeln.de/files/1494/2026_02_Retrofitted_Anti-Skid_System.pdf
   sha256sum deposited.pdf
   ```

3. The release `cos-1494` carries the file and `SHA256SUMS` as assets. The public REST API reports a digest for each asset. Written in hexadecimal without any algorithm prefix, as the command below prints it, the digest of the PDF must equal its line in `SHA256SUMS`:

   ```sh
   curl -sSf https://api.github.com/repos/mtorun0x7cd/anti-skid-verification/releases/tags/cos-1494 \
     | jq -r '.assets[] | "\(.digest | sub("^[^:]*:"; ""))  \(.name)"'
   ```

### With plain git

The record tag `cos-1494` carries the author's SSH signature. The public key is published at <https://api.github.com/users/mtorun0x7cd/ssh_signing_keys>; its fingerprint is `SHA256:h0XIy0K+hRkQ921LjtoKu/jSPvvlP0r4BiAMuyEPIrI`.

```sh
key=$(curl -sSf https://api.github.com/users/mtorun0x7cd/ssh_signing_keys | jq -r '.[0].key')
echo "$key" | ssh-keygen -lf -                    # shows the fingerprint above
echo "info@mtorun0x7cd.com $key" > allowed_signers
git -c gpg.ssh.allowedSignersFile=allowed_signers tag -v cos-1494
```

### With a GitHub account

```sh
gh release verify cos-1494 --repo mtorun0x7cd/anti-skid-verification
```

The deposited PDF is untagged, that is, it has no structure for assistive technology; its metadata declare PDF/A-1a, to which it does not conform (`ERRATA.md`, section 2). As the version of record it cannot change: corrections to the paper are listed in [`ERRATA.md`](../ERRATA.md).
