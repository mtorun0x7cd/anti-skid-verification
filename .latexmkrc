# SPDX-FileCopyrightText: 2026 Mert Torun
# SPDX-License-Identifier: MIT
#
# latexmk settings for a run in the root of the repository. The folders
# paper/, report/ and slides/ carry their own .latexmkrc, which the Makefile uses.

$aux_dir = '';
$out_dir = '';
$biber = 'biber %O %S';
add_cus_dep('glo', 'gls', 0, 'run_makeglossaries');
add_cus_dep('acn', 'acr', 0, 'run_makeglossaries');
sub run_makeglossaries {
    my $base = $_[0];
    $base =~ s|^.*/||;
    my $dir = $out_dir;
    if ($dir eq '') { $dir = '.'; }
    if ( $silent ) {
        system "makeglossaries -q -d '$dir' '$base'";
    } else {
        system "makeglossaries -d '$dir' '$base'";
    };
}

$hash_calc_ignore_pattern{'xml'} = '^';

