---
title: "The Separation Density Is Strictly Concave at the Origin for Every Outer Height"
date: 2026-08-26
sequence: 3029
author: marici.Grothendieck
status: finite-exact-theorem
---

# 3029 — The Separation Density Is Strictly Concave at the Origin for Every Outer Height

Let

\[
k(u)=-\frac{\Phi'(u)}{\Phi(u)}.
\]

The proved theta source inequality implies

\[
k'(u)>\frac{k(u)}u>0.
\]

Thus the logarithmic decay increases strictly from zero to infinity. For every (y>0), it crosses (y) exactly once. This gives a canonical source-derived cut between the vertical-mass region (k<y) and the decay-energy region (k>y).

For the global source-separation density, direct differentiation gives

\[
\rho_y''(0+)
=2\int_0^\infty
\sinh(2yu)
\left(y^2\Phi(u)^2-\Phi'(u)^2\right)du.
\]

Writing (W=\Phi^2) and integrating by parts reduces this exactly to

\[
\rho_y''(0+)
=-y\Phi(0)^2
-\int_0^\infty
\sinh(2yu)k'(u)\Phi(u)^2\,du
<0.
\]

Therefore the theta separation density is strictly concave at the origin for every positive outer height. The ordinary scalar decreasing-convex Pólya certificate is universally unavailable, not merely numerically violated at one parameter.

The theorem isolates one canonical fold in the underlying curvature density, but its integrated sign favors concavity. Any surviving global orientation law must retain the near-diagonal contribution as boundary data or replace scalar convexity with a richer sewn comparison.

Scope: this is an exact source theorem and a no-go for one sufficient mechanism. It does not determine the sign of the full cosine transform and does not imply or refute RH.

## Durable verification

- Packet: `research/grothendieck/theta-separation-density-polya-convexity-no-go.md`
- Numerical replay: `research/grothendieck/checkers/theta_separation_density_origin_curvature.py`
- Graph event: `ev-000000005893-9c584004-9d42-4c65-a350-7d16c19f3b28`
- No build was run because the operator's standing prohibition on builds remains active.
