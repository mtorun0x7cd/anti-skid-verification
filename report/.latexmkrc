# Keep build artefacts out of the source tree (project convention).
$aux_dir = '.tmp.nosync/latex';
$out_dir = '.tmp.nosync/latex';
# The first pdflatex pass writes the aux file of each included chapter into the
# folder chapters/ of the aux directory; latexmk creates that folder only after
# the pass has failed on it. Creating it here keeps the first pass of a clean
# build free of that fatal error; make_path creates what is missing and deletes
# nothing.
use File::Path qw(make_path);
make_path("$aux_dir/chapters");
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

