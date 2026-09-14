# Erratum: base dlog regularity does not determine the v_alg parity

The exact identity

\[
\nabla(v_{\rm alg}\bmod e_6)=d\log(E^4-X_1^2X_2^2)
\]

and the fact that this divisor is disjoint from generic \(E=0\) prove only that the **diagonal connection** of the algebraic quotient line has zero residue at the total-energy cusp.

The desired parity \(b\), however, is an **off-diagonal extension residue** from the elliptic quotient into that algebraic line. A regular diagonal block does not force the off-diagonal block to vanish.

A two-dimensional counterexample is

\[
A(E)dE=
\begin{pmatrix}
d\log(c+E^2)&\lambda\,dE/E\\
0&0
\end{pmatrix},
\qquad c\ne0.
\]

The diagonal divisor is a unit at \(E=0\), and its diagonal residue is zero, but

\[
\operatorname{Res}_{E=0}A=
\begin{pmatrix}0&\lambda\\0&0\end{pmatrix}
\]

has arbitrary off-diagonal extension class.

There was also a category mismatch in interpreting the base divisor as the desired dual cycle. The divisor

\[
E^4-X_1^2X_2^2=0
\]

lies in the kinematic base and controls transport of the algebraic line. The functional \(v_{\rm alg}^\vee\) is an integral Betti functional in the fiber. Identifying base winding with fiber intersection is precisely the missing Betti--de Rham/specialization map.

Therefore the claim

\[
b=0
\]

does not follow. The previous packet establishes only diagonal regularity and is superseded as a parity argument.

The same caution applies to the proposed odd \(e_6\) bit: the paired-node/component-difference geometry supplies a compelling primitive Betti candidate, but the source itself records that the integral normalization of the rational \(e_6\) line has not been fixed. Until that comparison is proved, \(a=1\) remains conditional rather than established.

Correct current status:

- global double-conic degeneration: established;
- four width-two conductor marks and compound-\(D_4\) geometry: established;
- Bunch--Davies relative orientation of the paired infinity nodes: established;
- integral map to the ordered \((e_6,v_{\rm alg})\) Betti plane: not established;
- numerical pair \((a,b)\): all four remain logically open.

Certificate:

- `research/voevodsky/checkers/diagonal_regular_does_not_kill_extension_residue.py`;
- `research/voevodsky/results/diagonal_regular_extension_counterexample.json`.
