---
author: marici.Figueiredo
---

# 3160 — Protected Tree Matching Does Not Bound Loop Erosion

## Result

For unequal protected pair masses and independent reciprocal vertices, the
Dirac norm-quartic contribution is

\[
-8(y^4+z^4)|n|^4.
\]

The product-preserving transformation \(y\mapsto ty\), \(z\mapsto z/t\)
changes this loop response. At fixed product,

\[
y^4+z^4\geq2(yz)^2,
\]

with equality only for balanced magnitudes. The packets \((1,1)\) and
\((2,1/2)\) have equal product but erosion sums two and \(257/16\).

## Consequence

Flip protection closes operator support but tree-product matching neither
identifies nor upper-bounds RG erosion. A source balance law or two calibrated
threshold widths is required. No numerical flavor selector follows.

## Durable verification

- Packet: research/flavor/flavor-protected-vertex-imbalance.md
- Checker: research/flavor/checkers/wp670_protected_vertex_imbalance.py
- Result: research/flavor/results/wp670_protected_vertex_imbalance.json
- Epistemic graph event: `ev-000000006511-731fbe33-a830-4adb-bd24-e285c3cebcd5`
