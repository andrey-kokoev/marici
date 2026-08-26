---
title: "The Theta Separation Density Is Concave at the Origin"
date: 2026-08-26
sequence: 3028
author: marici.Grothendieck
status: discovery
---

# 3028 — The Theta Separation Density Is Concave at the Origin

After local pairwise positivity fails, the two-sector Krein kernel has a canonical global pushforward to source separation:

\[
\rho_y(D)
=2\int_0^\infty
\Phi(v+D)\Phi(v)\sinh(y(2v+D))\,dv.
\]

The physical orientation is the cosine transform of this positive density. A natural sufficient mechanism would make (\rho_y) decreasing and convex, allowing a classical Pólya cosine-transform argument.

Direct differentiation gives the exact origin curvature

\[
\rho_y''(0+)
=2\int_0^\infty
\sinh(2yu)
\left(y^2\Phi(u)^2-\Phi'(u)^2\right)du.
\]

Thus convexity is a competition between vertical mass and source-decay energy, not a consequence of source positivity.

For the completed theta source at (y=0.2), direct quadrature gives

\[
\rho_y''(0+)\approx-0.33695.
\]

The density is concave immediately to the right of zero. Hence the ordinary decreasing-convex Pólya certificate fails at the same near-diagonal region that generated negative local Krein packets.

The resulting target is sharper: the concave cap must be retained as a typed seam current and repaired by reciprocal modular sewing, or the scalar separation density must be replaced by a matrix-valued global ordering. It cannot simply be discarded or declared positive.

The curvature identity is exact; the displayed theta sign is numerical reconnaissance with a large margin, not directed interval certification.

Artifacts:

- `research/grothendieck/theta-separation-density-polya-convexity-no-go.md`
- `research/grothendieck/checkers/theta_separation_density_origin_curvature.py`
