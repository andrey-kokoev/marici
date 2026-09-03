# Grade parity, not grade exchange, eliminates reciprocal mixing

## Question

Which involutive symmetry on the reciprocal Pauli return forces the cross-grade \(X\) channel to vanish?

## Two involutions

For

\[
K=aI+xX+zZ,
\]

consider grade parity \(Z\) and grade exchange \(X\).

Conjugation by grade parity gives

\[
ZKZ=aI-xX+zZ.
\]

Therefore

\[
ZKZ=K
\quad\Longleftrightarrow\quad
x=0.
\]

This is exactly the condition that primitive and square grades reduce \(K\).

Conjugation by grade exchange gives

\[
XKX=aI+xX-zZ.
\]

Therefore

\[
XKX=K
\quad\Longleftrightarrow\quad
z=0.
\]

Grade exchange equalizes the two diagonal loads but preserves the cross-grade \(X\) route.

## Combined symmetry

If both involutions are physical symmetries, then

\[
x=z=0,
\qquad
K=aI.
\]

The return becomes scalar on the strict two-grade plane. Strict confinement then reduces to

\[
0\le a<1.
\]

## Why the names matter

An operator that exchanges primitive and square basis vectors is not the same as one that assigns them opposite parity. Confusing these actions reverses the confinement conclusion: exchange permits mixing, while parity forbids it.

Neither matrix is automatically a physical symmetry. The source must provide a map from the primitive-square grading to the declared physical route space and show that the complete return intertwines the chosen involution. The source grade operator \(N=\operatorname{diag}(1,2)\) defines the parity

\[
(-1)^N=\operatorname{diag}(-1,1),
\]

which differs from \(Z\) only by an irrelevant overall sign for conjugation. Thus grade parity is source-native on the arithmetic plane, but its preservation by the physical return remains a separate theorem.

## Verification

`research/aspect/checkers/check_pauli_involution_constraints.py` verifies that grade parity flips only \(X\), grade exchange flips only \(Z\), and both invariances leave only the scalar channel using exact rational matrices.

## Disposition

A source theorem that the physical return commutes with \((-1)^N\) would eliminate reciprocal cross-grade mixing. Exchange symmetry or reciprocity alone cannot. The next test is whether parity preservation can follow from a weaker selection rule on route amplitudes rather than from the unavailable full return.
