# Arithmetic Reciprocal Incidence Matches the Rigged Transpose but Is Not a Core for the Seam

For a finite labelled arithmetic distribution

\[
\nu_z^+=\sum_jw_je^{-za_j}\delta_{a_j},
\]

conjugate-reflected transport gives support at `-a_j` with conjugated
characters. Since the completed theta forcing is real and even,

\[
B_f^\times(\mathfrak J\nu_z^+)
=\overline{B_f^\times(\nu_z^+)}.
\]

This proves exact reciprocal-transpose compatibility separately on primitive,
square, and connected-tail packets, and the common-domain theorem passes it to
their completions.

However, every positive prime-power support is at least `log 2`. All arithmetic
currents annihilate every test function supported in `(0,log 2)`, while a seam
distribution there need not. Hence the arithmetic boundary span is not a core
for the continuum seam dual. Arithmetic matching cannot extend the adjoint
incidence by density.

The next gate is an independent reflected `H1` seam correspondence retaining
both endpoint value and flux traces.

Research packet:
`research/grothendieck/arithmetic-reciprocal-incidence-matches-the-rigged-transpose-but-is-not-a-core-for-the-seam.md`

Exact checker:
`research/grothendieck/checkers/check_arithmetic_transpose_match_and_seam_gap.py`

The checker passes 6/6 exact tests.
