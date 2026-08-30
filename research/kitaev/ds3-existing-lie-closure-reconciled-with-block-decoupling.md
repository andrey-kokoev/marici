# Reconcile the D(S3) Lie audit with pairwise block decoupling

Owner: `marici.Kitaev`

## Question

Does the existing two-flux Lie calculation already prove the pairwise
decoupling condition required for independent control of repeated simple
blocks?

## Claim boundary

Yes, inside the frozen endpoint coefficient model.

The admitted ideal controls are the Hermitian quadratures of all six gauge
actions together with the transposition- and three-cycle-flux projectors,
treated as independently switchable Hamiltonians. Their real anti-Hermitian
Lie closure has dimension 33. Its derived algebra has dimension

\[
28=4(2^2-1)+2(3^2-1),
\]

with block ranks

\[
(0,0,3,8,8,3,3,3).
\]

Because the derived algebra is the full direct sum

\[
\mathfrak{su}(2)^4\oplus\mathfrak{su}(3)^2,
\]

the repeated two- and three-dimensional blocks are not diagonally locked.
Thus the single-block and equal-size pair-decoupling tests are already passed
by the stronger exact derived-algebra certificate.

The full block-unitary algebra is not reached. The center has rank five rather
than eight, leaving three central phase covectors absent. One additional
endpoint quadrature separates the only remaining sector collision, between
`G` and `H`, for dephasing; three are required for arbitrary independent
central phases.

This does not prove that the ideal generators are physically executable.
Still untyped are source-local pulse Hamiltonians, independent sign and
amplitude control, time ordering, leakage, and fault bounds. Associative
endpoint availability alone supplies none of these constructor claims.

Evidence is the existing packet
`s3-two-flux-projective-lie-controllability.md`, checker source
`checkers/check_s3_two_flux_lie_control.py`, and stored exact result
`results/s3-two-flux-lie-control.json`. No checker was run in this audit.

## Disposition

Close repeated-block decoupling as an algebraic endpoint question.

Keep two distinct open gates:

1. lift the eight ideal Hamiltonian directions—six gauge quadrature families
   and two flux projectors—into an authorized source-local control theory;
2. decide whether the intended operation needs only projective conjugation,
   one extra sector-separating central direction, or all three missing central
   phase directions.

The first falsifier for the lift is any claimed implementation in which a
nominally independent generator cannot be signed, scaled, or pulsed without
also changing another endpoint block or leaving the protected module.
