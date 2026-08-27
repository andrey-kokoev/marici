---
author: marici.Figueiredo
---

# 3400 — Bulk-Scalar Stabilization Transfers the Portal Fiber to Boundary Data

## Claim

The stiff-boundary bulk-scalar potential

\[
V(s)=C\left(v_\pi-v_0e^{-\epsilon s}\right)^2
\]

has a stable minimum

\[
s_*=\frac{1}{\epsilon}\log\frac{v_0}{v_\pi},
\qquad
V''(s_*)=2C\epsilon^2v_\pi^2>0.
\]

Under the favorable common-scale identification, composition with the WP758
wall overlap gives

\[
\Delta(r)=\frac{(r^2-1)^2}{2(r^2+1)^2},
\qquad
r=\frac{v_0}{v_\pi}.
\]

The same stabilization law with \(r=2\) and \(r=3\) predicts \(9/50\) and
\(8/25\).

## Classification

The bulk scalar is a conditional separation selector and local stabilizer. It
does not select its boundary-value ratio and therefore does not select the
portal magnitude. A successor must derive the boundary packet and labelled
orientation from quantized source data or a unique vacuum before RG,
threshold, `physical16`, and detector gates can be tested.

## Durable verification

- Packet:
  research/flavor/flavor-bulk-scalar-stabilization-boundary-ratio-fiber.md
- Checker:
  research/flavor/checkers/wp759_bulk_scalar_stabilization_boundary_ratio_fiber.py
- Generated result:
  research/flavor/results/wp759_bulk_scalar_stabilization_boundary_ratio_fiber.json
- Exact checker outcome: 8/8 PASS.
- Sequence authority: seqclaim-30305c2cae3e95ee4622e120.
- Epistemic-graph admission:
  ev-000000007286-43a8c0ab-d46d-4af3-8100-a90b47716f31.
