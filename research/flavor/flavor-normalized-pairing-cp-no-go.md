# Normalization and orthogonality do not select physical CP: WP1021

## Question

Does adding a nonconic positive normalization and exact portal orthogonality
repair the scale-free obstruction and force CP transmission?

## Admitted source constraints

Take the FDM-2 singlet vacuum (z=4/5+3i/5) and impose

\[
\|a\|^2=\|b\|^2=1,qquad a^Tb=0.
\]

These are genuine nonconic conditions: the WP1020 rescaling ray is removed.
They remain source equations only as declared assumptions; no physical
constructor for them is inferred.

## Exact hostile portal

Choose

\[
a=e_1,qquad b=e_2^T,qquad
Y_0=\operatorname{diag}(1,2,4).
\]

The portal is unit normalized, orthogonal, rank one, and complex. Its Gram is

\[
H_d=
\begin{pmatrix}
2&2z&0\\
2\bar z&4&0\\
0&0&16
\end{pmatrix}.
\]

Both up and down spectra are nondegenerate, but the third generation is
disconnected from the mixing block. Consequently the commutator has rank two
and

\[
\det[H_u,H_d]=0.
\]

Thus normalization repairs scale but not cyclic transmission.

## Contextual partition

The same unit-norm source equations admit both this CP-blind portal and an
exact normalized version of the WP90 CP-transmitting portal. Norm and
pairwise angle therefore do not separate the physical classes. The signed
Jarlskog instrument detects the partition but selects neither side.

All 1,210 fitted sheets have nonzero (J), so the hostile normalized portal
remains outside the fitted class.

## Smallest exact falsifier

The pair (a=e_1), (b=e_2^T) is the smallest falsifier: it satisfies both
norm constraints and exact orthogonality while producing only one mixing
edge. No phase can form a three-edge invariant cycle.

## Claim boundary

This closes normalization plus orthogonality, not every nonconic source law.
It does not deny that a stronger source object could enforce cyclic
three-generation incidence and a positive oriented-volume margin. It assigns
no implicit time or causal interpretation.

## Disposition

Do not treat a positive pairing or fixed portal norm as a physical CP
selector. The next candidate must derive three-generation cyclic incidence
and exclude both disconnected support and cubic cancellation, with a
weak-basis-invariant positive margin and physical calibration.

Verification: uv run --with sympy python
research/flavor/checkers/wp1021_normalized_pairing_cp_no_go.py.
