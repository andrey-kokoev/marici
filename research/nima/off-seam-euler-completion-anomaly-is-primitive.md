# The off-seam Euler completion anomaly is primitive

## Sector-local threshold

Write the logarithm of a local Euler factor as

\[
-\log(1-p^{-s})=\sum_{k\ge1}\frac{p^{-ks}}{k}.
\]

Fix a compact set \(K\) inside the right open sector \(\operatorname{Re}s>1/2\). There is a number \(\delta>0\) such that

\[
\operatorname{Re}s\ge\frac12+\delta
\]

throughout \(K\).

For every \(k\ge2\),

\[
\sum_p\sup_{s\in K}\left|\frac{p^{-ks}}{k}\right|
\le
\frac1k\sum_p p^{-k(1/2+\delta)}
<\infty.
\]

The inequality is strict because \(k(1/2+\delta)>1\). Therefore every grade \(k\ge2\), and their combined sum, converges normally on compact subsets of the right open sector.

## Consequence

The prime-square current is singular at the seam but is not an off-seam completion obstruction. Inside the open right sector it belongs to the normally convergent Euler tail.

Only the primitive grade \(k=1\) fails this elementary convergence test in the critical-strip portion \(1/2<\operatorname{Re}s\le1\). Thus the finite-to-completed Euler anomaly in that sector is localized to:

- the primitive-prime current;
- its endpoint and archimedean coupling;
- the reciprocal comparison needed to join the opposite sector.

The left open sector has the reciprocal statement after applying \(s\mapsto1-s\).

## Relation to the seam filtration

There is no contradiction with the three-grade seam filtration:

- on the seam, \(k=1\) is distributional;
- on the seam, \(k=2\) is Hilbert-type but not trace-class;
- on the seam, \(k\ge3\) is trace-class;
- strictly off the seam, the \(k=2\) current gains enough decay to join the normally convergent tail.

The required regularization order is therefore location-sensitive. Order three is the first source-compatible seam regularization, while order two already suffices on compact subsets of either open sector after reciprocal typing.

## Completion-stability theorem template

Let \(T_X(s)\) be the normally convergent contribution of all grades \(k\ge2\), and let \(P_X(s)\) be the primitive current. A source-level zero-exclusion theorem on the right sector would follow from:

1. local uniform convergence of \(T_X\);
2. a source-derived completed primitive connection \(P(s)\);
3. local uniform convergence of the normalized primitive sections reconstructed from \(P_X\) to the section reconstructed from \(P\);
4. one retained nonzero basepoint normalization;
5. compatibility with endpoint and archimedean currents.

Hurwitz then prevents zero-free finite sections from acquiring an isolated zero in the open sector.

## Exact frontier

The hard analytic bound should target the primitive completed graph, not the already normally convergent square and higher grades. A bound on the entire undifferentiated Euler packet obscures this localization and risks asking the convergent channels to compensate for the sole divergent one.

The finite falsifier is correspondingly narrow: after subtracting the exact \(k\ge2\) normal limit and the declared endpoint and archimedean currents, any residual not supported in the primitive channel disproves the typed decomposition.

