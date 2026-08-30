# An SU(4) cubic invariant selects the carrier orientation but not the portal: WP787

## Question

Does the smallest parent with both a \(3+1\) fundamental and a nonzero cubic
invariant evade the WP786 mirror-completion obstruction?

## Exact parent direction

Take

\[
T=\operatorname{diag}(1,1,1,-3).
\]

It is traceless and gives the fundamental \(3+1\) weights directly. Its first
invariants are

\[
\operatorname{tr}T^2=12,\qquad
\operatorname{tr}T^3=-24,\qquad
\operatorname{tr}T^4=84.
\]

Unlike the SO(5) parent of WP744, the cubic invariant is nonzero and can
distinguish the two orientations.

## Minimal cubic vacuum

On \(\Phi=aT\), consider the bounded invariant potential

\[
V(\Phi)
=\frac{\kappa}{3}\operatorname{tr}\Phi^3
+\frac{\lambda}{4}
\left(\operatorname{tr}\Phi^2\right)^2,
\qquad \lambda>0.
\]

The nonzero stationary point is

\[
a_*=\frac{\kappa}{6\lambda},
\]

with

\[
V(a_*)=-\frac{\kappa^4}{108\lambda^3},
\qquad
V''(a_*)=\frac{4\kappa^2}{\lambda}.
\]

The complete normalized adjoint Hessian has eight positive modes with
eigenvalue \(2\kappa^2/(3\lambda)\), six Goldstone zeroes, and one positive
radial mode with eigenvalue \(\kappa^2/(3\lambda)\). Thus this is not merely a
ray minimum: it is locally stable modulo the expected
\(SU(4)/(SU(3)\mathbin{\times}U(1))\) orbit.

For fixed \(\kappa\), the cubic term chooses an orientation. But
\(\kappa\mapsto-\kappa\) defines the mirror source theory with the opposite
vacuum. The sign of the cubic coefficient therefore still needs independent
source authority.

## Portal descent exposes a new coefficient

The smallest linear adjoint spurion on a fundamental carrier gives

\[
g_n=\eta a_*,
\qquad
g_m=-3\eta a_*,
\qquad
g_n-g_m=\frac{2\eta\kappa}{3\lambda}.
\]

The parent vacuum and its Hessian are unchanged when \(\eta\) changes sign,
while the portal contrast reverses. Moreover,

\[
\kappa\longmapsto\rho\kappa,
\qquad
\eta\longmapsto\frac{\eta}{\rho}
\]

leaves the portal contrast invariant while changing the source scales. The
orientation constructor and the portal constructor have not yet been
parallelized.

## Classification

The SU(4) cubic potential is a genuine stable \(3+1\) carrier rigidifier and a
conditional orientation selector. It is not yet the required asymmetric
portal source:

- the sign of \(\kappa\) labels mirror source theories;
- the sign and magnitude of \(\eta\) are independent;
- the ratio \(\eta\kappa/\lambda\) has a continuous source fiber;
- the Hessian is a vacuum-basin result, not an RG basin;
- no finite threshold map or calibrated physical16 instrument is present.

The progressive successor must derive the cubic coefficient and portal vertex
from one quantized chiral operation. If they enter as unrelated invariants,
the construction only moves the tuning from \(g_n-g_m\) to
\(\eta\kappa/\lambda\).

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp787_su4_cubic_orientation_portal_fiber.py

Generated result:
research/flavor/results/wp787_su4_cubic_orientation_portal_fiber.json
