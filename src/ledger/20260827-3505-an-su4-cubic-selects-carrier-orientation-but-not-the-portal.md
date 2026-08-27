---
author: marici.Figueiredo
---

# 3505 — An SU(4) Cubic Selects Carrier Orientation but Not the Portal

## Claim

The \(SU(4)\) generator

\[
T=\operatorname{diag}(1,1,1,-3)
\]

provides a \(3+1\) fundamental and has
\(\operatorname{tr}T^3=-24\). On the adjoint ray, the minimal
cubic-plus-quartic potential has

\[
a_*=\frac{\kappa}{6\lambda},
\qquad
V_*=-\frac{\kappa^4}{108\lambda^3}.
\]

The complete adjoint Hessian contains eight positive modes, six Goldstone
zeroes, and one positive radial mode. Fixed nonzero \(\kappa\) therefore
selects and locally stabilizes a carrier orientation.

The smallest linear portal spurion instead gives

\[
g_n-g_m=\frac{2\eta\kappa}{3\lambda}.
\]

Changing \(\eta\)'s sign reverses the portal without changing the selected
vacuum, and a continuous \((\kappa,\eta)\) scaling fiber remains.

## Classification

The cubic parent is a conditional orientation selector and stable carrier
rigidifier. It does not select the portal sign or magnitude. The cubic
coefficient and portal vertex must descend from one quantized source
operation; otherwise the tuning has only moved to
\(\eta\kappa/\lambda\).

## Durable verification

- Packet:
  research/flavor/flavor-su4-cubic-orientation-portal-fiber.md
- Checker:
  research/flavor/checkers/wp787_su4_cubic_orientation_portal_fiber.py
- Generated result:
  research/flavor/results/wp787_su4_cubic_orientation_portal_fiber.json
- Exact checker outcome: 14/14 PASS.
- Sequence authority: seqclaim-0b36d763a8253af06ac23eb7.
- Epistemic-graph admission:
  ev-000000007510-155151ad-1155-4192-9a80-478cced2be1f.
