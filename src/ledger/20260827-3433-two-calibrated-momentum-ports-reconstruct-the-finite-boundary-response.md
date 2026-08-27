---
author: marici.Figueiredo
---

# 3433 — Two Calibrated Momentum Ports Reconstruct the Finite Boundary Response

## Claim

The complete quadratic boundary dependence of the WP769 transfer function is
carried by

\[
s=r_0+r_L,
\qquad
t=r_0r_L.
\]

After subtracting the calibrated bulk inverse response at fixed (m=\ell=1),

\[
Y(p)=p^2\cosh\mu\,s
+\frac{p^4\sinh\mu}{\mu}\,t,
\qquad
\mu=\sqrt{1+p^2}.
\]

One momentum leaves an affine fiber. The two spacelike ports (p=1,2) form a
matrix with strictly positive determinant and reconstruct (s,t) exactly.
They determine the unordered endpoint pair, which is the faithful coordinate
for the symmetric transfer response, without identifying labelled endpoint
ontology.

## Classification

This is a jointly faithful, experimentally typed relational readout on the
quadratic boundary packet. It is not a source selector. Physical realization
still requires the actual flavor production and decay channels to implement
the two calibrated ports with a nonsingular uncertainty-completed Jacobian.
The source must separately fix (m\ell), gauge normalization, and the RG
trajectory before descent to `physical16`.

## Durable verification

- Packet: research/flavor/flavor-two-momentum-boundary-response-tomography.md
- Checker:
  research/flavor/checkers/wp770_two_momentum_boundary_response_tomography.py
- Generated result:
  research/flavor/results/wp770_two_momentum_boundary_response_tomography.json
- Exact checker outcome: 10/10 PASS.
- Sequence authority: seqclaim-e6890615d74862ca2a00e83e.
- Epistemic-graph admission:
  ev-000000007342-acd741a0-cab6-4808-b261-cf591301f9c8.
