# Keep build artefacts out of the source tree (project convention).
$aux_dir = '.tmp.nosync/latex';
$out_dir = '.tmp.nosync/latex';
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

