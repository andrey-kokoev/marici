# Directed dual-number recursion closes the complex Schur arc enclosures

For the complex continuation slab, evaluate the reduced matrix and its
`L`-derivative together as Arb complex balls `(M,M')`. All quadrature formulas
are analytic between support thresholds, so differentiation may be performed
under the finite integrals.

For a block

\[
M=\begin{pmatrix}F&b\\c^T&d\end{pmatrix},
\qquad S=d-c^TF^{-1}b,
\]

put `y=F^{-1}b` and `x=F^{-T}c`. Then

\[
S'=d'-c'^Ty-x^Tb'+x^TF'y.
\]

This formula requires two interval linear solves but does not differentiate an
inverse explicitly.

For recursive symmetric LDL elimination, if

\[
T_{new}=T_{22}-T_{21}T_{12}/p,
\qquad p=T_{11},
\]

propagate

\[
T_{new}'=T_{22}'-
\frac{T_{21}'T_{12}+T_{21}T_{12}'}p+
\frac{T_{21}T_{12}p'}{p^2}.
\]

The reverse mode ordering found in the scout keeps all 18 strong pivots away
from zero and avoids the artificial pivot windings of ascending order.

On each of the 64 ellipse arcs, an enclosure at its midpoint gives

\[
|p(z)|\ge |p(z_j)|-\sup_{arc}|p'|\,|z-z_j|,
\]

and similarly for the scalar robust Schur complement. The current budgets
allow four times the observed secant derivative for every strong pivot and
1.2 times the observed derivative for the scalar robust Schur complement.
Thus a dual-number Arb pass over 64 arcs is sufficient; no dense determinant
enclosure is needed.
