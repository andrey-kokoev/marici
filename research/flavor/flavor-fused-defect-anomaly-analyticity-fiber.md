# Fused-defect anomaly and analyticity fiber: WP1110

## Question

What anomaly and analyticity constraints must the twenty-three WP1109
fused-defect fields satisfy before values can be constructed?

## Exact constraints

The boundary exponents must realize the full seven-channel vector

\[
\left(\frac12,\frac14,0,2,2,-\frac14,0\right),
\]

not merely its mod-\(\mathbb Z^7\) residue
\((1/2,1/4,0,0,0,3/4,0)\). The parent gauge-gravity completion has coefficient
\(-3\), but the local Green–Schwarz split remains required. The contact
counterterm is a separate rank-one direction: the full contact/interaction
space has rank \(8\), while the interaction quotient has rank \(7\).

The remaining constraints are:

- integer clock law \(B/A=6n^2\) with a selected sign \(\sigma\);
- independent \(\rho\) of weight \(-3\), explicitly not \(1/D\);
- a \(6\times6\) branch-to-physical16 kernel;
- event reweighting from \((6,8,1,4,2,2)/23\) to \((1/4)^6\);
- gain \(3/2\);
- physical16 quotient descent and normalization.

These are necessary conditions, not constructed values.

## Classification

Conditional gate. WP1110 converts the WP1109 field fiber into an exact
constraint fiber while leaving source-authorized values open.

Checker: `research/flavor/checkers/wp1110_fused_defect_anomaly_analyticity_fiber.py`

Result: `results/wp1110_fused_defect_anomaly_analyticity_fiber.json`
