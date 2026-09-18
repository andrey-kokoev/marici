# Determinant line is a normalized Hopf module

Let relative operators compose by

$$
A\star B=A+B+AB,
\qquad
I+(A\star B)=(I+A)(I+B).
$$

The third-order determinant has multiplier

$$
\det_3(I+A\star B)
=e^{\alpha_3(A,B)}
\det_3(I+A)\det_3(I+B),
$$

where

$$
\alpha_3(A,B)
=r(A\star B)-r(A)-r(B),
\qquad
r(A)=-\operatorname{Tr}A+\frac12\operatorname{Tr}(A^2).
$$

Thus the bare `det_3` line is a projective one-dimensional module. The cocycle identity for `alpha_3` is exactly associativity coherence for that projective action.

Normalize by

$$
\Delta_3(A)=e^{-r(A)}\det_3(I+A).
$$

Then

$$
\Delta_3(A\star B)=\Delta_3(A)\Delta_3(B).
$$

Therefore `Delta_3` is a genuine character of the relative-operator groupoid on the determinant-unit locus. Pullback along any source-compatible assignment

$$
\kappa:Q_a\longmapsto A_a,
\qquad
A_{a+b}=A_a\star A_b
$$

makes the normalized determinant line a one-dimensional module over the translation Hopf algebra:

$$
Q_a\cdot z=\Delta_3(A_a)z.
$$

The module law follows directly from multiplicativity. Reciprocal transport is represented by the inverse character whenever

$$
A_{-a}=A_a^{\star-1}.
$$

## Exact remaining source condition

The Hopf-module theorem is unconditional after a compatible `kappa` is given. What remains open in the current source is construction of a source-graph-indexed assignment

$$
\kappa_G:Q_a\mapsto K_{G,a}
$$

whose first two trace coordinates equal the primitive and square endpoint currents and whose connected coordinate is the retained `det_3` tail.

Hence anomaly normalization is not a missing coherence: it is precisely the coboundary that strictifies the projective determinant module. The missing datum is the source realization `kappa_G`.

Status: normalized determinant Hopf-module theorem proved; source pullback remains open.
