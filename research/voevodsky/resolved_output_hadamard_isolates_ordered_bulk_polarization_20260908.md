# Resolved-output Hadamard decomposition isolates the ordered bulk polarization

Date: 2026-09-08

## Construction

Retain the source-typed derivative-tail and output-wall ports before applying
the codiagonal.  The canonical unitary Hadamard transform sends their amplitudes
`(Bf,Mf)` to

\[
2^{-1/2}((B+M)f,(B-M)f).
\]

Consequently the resolved positive form has the exact decomposition

\[
G_{\rm res}=I+B^*B+M^2I
=I+\frac12G_++\frac12G_-,
\qquad
G_\pm=(B\pm M)^*(B\pm M).
\]

The codiagonalized history form satisfies

\[
G_{\rm hist}-G_{\rm res}
=\frac12(G_+-G_-)
=M(B+B^*).
\]

Thus the previously isolated cross operator is precisely the oriented norm
imbalance between the codiagonal and anti-codiagonal resolved outputs.

## Consequence

No block-triangular repair is needed to compare the two forms algebraically:
they are the even sum and oriented difference of two canonical resolved output
energies.  This also explains why summed positive energy cannot recover the
missing polarization: summing erases `G_+-G_-`.

The anti-codiagonal port cannot be discarded merely because the separate
external boundary trace cancels.  The endpoint cancellation theorem concerns
typed external flux; `G_-` here retains the complementary bulk output needed to
measure the ordered wall-tail cross term.

## Remaining authority gate

The identity does not prove that the completed theta/Pauli comparison realizes
`G_+` and `G_-` blockwise.  The next source theorem can now be stated more
narrowly: prove that the common rapid, wall-reduced core carries the Hadamard
resolved outputs and that the Pauli `X/Y` blocks intertwine their oriented norm
difference, with radical descent and cutoff naturality.

## Evidence

- `check_marici_rh_resolved_output_hadamard_decomposition_20260908.py`
- `marici_rh_resolved_output_hadamard_decomposition_certificate_20260908.json`
