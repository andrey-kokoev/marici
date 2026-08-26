# Cutoff-Dependent Whitening Cannot Repair a Covariant Frame Bound

For the quotient lower-frame bound

\[
\beta(H,R)=\inf_{Rx\ne0}\frac{\|Hx\|}{\|Rx\|},
\]

any invertible source reparameterization (A) transported covariantly through
both maps leaves the bound exactly unchanged:

\[
\beta(HA,RA)=\beta(H,R).
\]

This follows by the substitution (y=Ax). It remains true even when (A)
depends on the cutoff. A coordinate change cannot repair collapsing
transversality when every typed operator is transported.

Take

\[
H_\varepsilon=\operatorname{diag}(1,\varepsilon),
\qquad R=I,
\qquad
A_\varepsilon=\operatorname{diag}(1,\varepsilon^{-1}).
\]

Then (H_\varepsilon A_\varepsilon=I), which looks perfectly conditioned.
But the covariantly transported residual is

\[
RA_\varepsilon=\operatorname{diag}(1,\varepsilon^{-1}),
\]

and the quotient lower-frame bound remains (\varepsilon). Comparing the
whitened seam to the untransported residual manufactures a false repair by
changing the source state typing.

Likewise, whitening a Gram matrix while leaving currents, conjugations, seam
rows, or endpoint probes fixed is not a coordinate change. It is a new
topology or a broken naturality square.

Target norm changes can alter the numerical bound. They preserve uniform
positivity only when the old and new norms are uniformly equivalent across
cutoffs. If the equivalence constants diverge, the renorming merely moves the
completion obstruction into the interface.

The compiler must therefore record a complete typed transport tuple

\[
(Q_N,R_N,H_N,\|\cdot\|_{Z_N},\|\cdot\|_{Y_N})
\longmapsto
(Q'_N,R'_N,H'_N,\|\cdot\|'_{Z_N},\|\cdot\|'_{Y_N})
\]

and verify covariance plus cutoff-uniform norm equivalence. A reported
condition number without this tuple has no invariant authority.

## Falsifiers

- Only the seam matrix is whitened.
- The residual or Gram metric is left in the old coordinates.
- A cutoff-dependent target norm has divergent equivalence constants.
- The smallest singular value improves only in an untransported Euclidean
  chart.
- A preconditioner is treated as a source constructor without authority.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
9/10. Covariant reparameterization, one-sided whitening, norm equivalence, and
topology change were frozen.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The lower-frame bound proved exactly invariant under arbitrary
invertible covariant source changes. Every apparent whitening repair therefore
either fails to transport a typed map or changes target norms nonuniformly.
