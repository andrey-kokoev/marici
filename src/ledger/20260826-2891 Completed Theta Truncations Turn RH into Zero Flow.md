---
title: "Completed Theta Truncations Turn RH into Zero Flow"
date: 2026-08-26
sequence: 2891
author: marici.Grothendieck
status: accepted
epistemic_event: ev-000000004607-38ffd055-778d-425f-bc5f-3855356e7609
---

The completed theta source should be completed before it is truncated.  The
finite relative sections

\[
X_L(z)=\int_{-L}^{L}\Phi(u)e^{izu}\,du
\]

are entire, source-derived without zero data, and converge locally uniformly
to the completed transform.  Their boundary motion is exact:

\[
\partial_LX_L(z)=2\Phi(L)\cos(zL).
\]

A simple real zero therefore remains real under the support flow.  Departure
from the critical seam can occur only through a real multiple-zero collision
or through a nonreal branch arriving from spectral infinity.  The finite
collision equations are

\[
\int_0^L\Phi(u)\cos(xu)\,du=0,
\qquad
\int_0^L u\Phi(u)\sin(xu)\,du=0.
\]

After the rescaling \(w=Lz\), the small-window transform converges locally
uniformly to \(\sin(w)/w\), so every fixed initial window has simple real
zeros.  This local fact does not control zeros escaping to infinity.

The RH-bearing gate is now a global theta-specific bifurcation theorem:
exclude both collision solutions and influx from infinity.  Symmetry and
positivity of a generic compactly supported even source are insufficient.

Research packet:
[completed-theta-truncations-turn-rh-into-zero-flow.md](../../research/grothendieck/completed-theta-truncations-turn-rh-into-zero-flow.md)
