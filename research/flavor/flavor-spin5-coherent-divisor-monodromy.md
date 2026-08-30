# The Coherent Yukawa Divisor Has Trivial Projector Monodromy and a Central Amplitude Lift

## Bipartite factorization

Reorder Completion B into the two eight-component sets

\[
\mathcal A=(S_4,X_4),
\qquad
\mathcal B=(V_5,n_0,n_1,n_2).
\]

The WP887 mass matrix has the exact form

\[
\mathcal M_B=
\begin{pmatrix}0&K\\K^T&0\end{pmatrix}.
\]

On the WP888 vacuum slice,

\[
\det K=-9253764\,
y_1^2y_2^2y_3y_6(y_1y_5-y_2y_4).
\]

Thus the square in \(\det\mathcal M_B=(\det K)^2\) is caused by bipartite
doubling, not by two independent coherent zeros.

## Generic coherent point

At

\[
(y_1,y_2,y_3,y_4,y_5,y_6)
=\left(2,3,5,7,\frac{21}{2},13\right),
\]

the coherent coordinate

\[
t=y_1y_5-y_2y_4
\]

vanishes while all coordinate factors remain nonzero. Exact calculation gives

\[
\operatorname{rank}K=7,
\qquad
\dim\ker K=\dim\ker K^T=1.
\]

If \(r\) and \(l\) span the right and left kernels, the \(y_5\) derivative
has nonzero transverse pairing

\[
l^T(\partial_{y_5}K)r=-\frac{39}{5}.
\]

The zero is therefore simple and transverse.

## Local two-state cell

After nonsingular changes of basis, the only vanishing sector is locally

\[
\mathcal M_{\rm eff}(t)=
\begin{pmatrix}0&ct\\ct&0\end{pmatrix},
\qquad c\ne0.
\]

Its signed eigenvalues are (+ct) and (-ct), with constant projectors

\[
P_\pm=\frac12
\begin{pmatrix}1&\pm1\\\pm1&1\end{pmatrix}.
\]

Analytic continuation around (t=0) returns each signed eigenbranch and each
projector to itself. There is no branch exchange and no branch-dependent
comparison frame.

For a Takagi frame describing nonnegative physical masses, absorbing the
phase of \(t\) uses a half-phase. A loop \(t\mapsto e^{2\pi i}t\) returns that
frame with the common central sign (-1). This sign disappears from
projectors and all quadratic mass readouts. Detecting it requires a coherent
reference path and therefore defines a new relational amplitude experiment.

## Architectural consequence

Aspect's alternative is decided on the generic coherent stratum:

- the two signed branches share one transported projector comparison frame;
- the physical architecture is additive at this cell;
- the recursive branch-by-branch adapter count is not forced;
- a single central lift remains only at the amplitude-frame level.

Coordinate-divisor intersections and higher-corank points are separate
strata and may have richer monodromy. This packet does not extrapolate the
generic result across those intersections.

## Selector consequence

Neither the trivial projector monodromy nor the central amplitude sign selects
the cycle coordinate (ho), the Yukawa magnitudes, or a mass ratio. The
coherent divisor is a physical rank-loss boundary, not an attractor or source
selection law.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp889_spin5_coherent_divisor_monodromy.py
~~~
