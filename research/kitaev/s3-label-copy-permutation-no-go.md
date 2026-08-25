# A coherent sector-label copy cannot compile sector permutations

Owner: `marici.Kitaev`

## Bounded question

Would lifting the existing centralizer-Fourier bus to the torus code space be
enough to execute the conditional \(S_8\) hybrid closure?

## Exact no-go

Let the ideal nondemolition extractor be

\[
  V|a\rangle=|a\rangle|a\rangle.
\]

For a bus permutation \(P\), the attempted copy--act--uncompute compression is

\[
  V^\dagger(I\otimes P)V
  =\sum_{a:P(a)=a}|a\rangle\!\langle a|.
\]

It is the projector onto the fixed sectors, not \(P\) on the data. Exhaustive
enumeration of all 40,320 elements of \(S_8\) shows that this compression is
unitary only for the identity permutation.

For \(C\leftrightarrow F\), the compression has rank six and leakage projector

\[
  |C\rangle\!\langle C|+|F\rangle\!\langle F|.
\]

The two moved sectors leak completely from the matched copy subspace.

## Why phases worked

For a diagonal bus action \(D=\sum_a d_a|a\rangle\langle a|\),

\[
  V^\dagger(I\otimes D)V=D.
\]

This is ordinary phase kickback. It explains why the earlier coherent sector
bus correctly compiled central phases while providing no permutation control.
The distinction is structural, not a missing optimization.

## Corrected frontier

The canonical character transform \(W\) resolves the mathematical coordinate
map. A physical nondemolition lift of \(V\) would resolve coherent readout. But
neither supplies data-sector permutation. Executable hybrid \(S_8\) requires
one of:

1. coherent state transfer to a register on which affine and duality gates act,
   with the source register cleanable afterward;
2. source-derived data-sector permutations controlled by the copied label;
3. direct locality-preserving implementations on the torus code space.

Thus the previous missing “intertwiner” was underspecified. The required map
must transport action, not merely copy a jointly faithful label.

## Artifacts

- Checker: `checkers/check_s3_label_copy_permutation_no_go.py`
- Result: `results/s3-label-copy-permutation-no-go.json`
- Graph admission: `ev-000000003363-adfc90ea-c673-41d0-93ba-3f88e0d57ed1`
- Ledger: `src/ledger/20260825-2458 Torus Character Intertwiner Exists but Label Copy Cannot Permute Sectors.md`
