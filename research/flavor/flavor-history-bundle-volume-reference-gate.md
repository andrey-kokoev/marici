# History-bundle volume-reference gate: WP1088

## Question

Does the conditional Wilson history bundle supply WP1081's volume reference
\(\rho\)?

## Determinant weight

For distinct Wilson eigenvalues
\(\lambda=(\lambda_1,\lambda_2,\lambda_3)\), the history determinant

\[
D(x)=\det[x,Ux,U^2x]
\]

has ray-phase weight \(+3\):

\[
D(\zeta x)=\zeta^3D(x).
\]

The checker uses \(\lambda=(2,3,5)\) and \(x=(1,1,1)\), giving \(D=6\).

The canonical coordinate volume form has ray-phase weight \(0\). Therefore

\[
\frac{D(\zeta x)}{1}=\zeta^3\frac{D(x)}{1}
\]

still does not descend to the projective ray.

## Bundle audit

WP1087's bundle

\[
Vx=\frac{1}{\sqrt3}(x,Ux,U^2x)
\]

supplies the three history grades, the determinant amplitude \(D\), and a
comparison node. It does not supply an independent section \(\rho\) of weight
\(-3\), a source transformation law, or a source coorientation.

## Classification

Conditional reference no-go. Even if the Wilson flag, cyclic ray, and history
bundle are eventually sourced, signed production requires a further source
volume/coorientation reference \(\rho\). Neither \(D\), the canonical unit
volume form, nor the history bundle itself may be promoted to \(\rho\).

Checker: `research/flavor/checkers/wp1088_history_bundle_volume_reference_gate.py`

Result: `results/wp1088_history_bundle_volume_reference_gate.json`
