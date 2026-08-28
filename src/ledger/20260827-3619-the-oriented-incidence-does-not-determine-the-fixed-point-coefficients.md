---
id: marici-ledger-20260827-3619
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP821
---

# The Oriented Incidence Does Not Determine the Fixed-Point Coefficients

The coupled flow

\[
\beta_x=2x^2(-b+cx-dy),
\qquad
\beta_y=2y(ay-fx)
\]

has a positive nonzero solution

\[
x_*=\frac{ab}{ac-df},
\qquad
y_*=\frac{bf}{ac-df}
\]

when \(ac-df>0\). The exact packet
\((a,b,c,d,f)=(1,1,3,1,1)\) gives
\((x_*,y_*)=(1/2,1/2)\) with local infrared stability exponents
\(1/2\) and \(2\). Combined with WP820's selected unit charge contrast, it
conditionally fixes a positive portal magnitude \(e_*=1/\sqrt2\).

WP820's incidence does not determine the loop coefficients. The same charge
packet with coefficients \((1,1,1,1,1)\) has no finite fixed point, while a
threshold shift to \((1,1,4,1,1)\) moves it to \((1/3,1/3)\). The known WP805
chiral fixed point supplies common-action algebra but lies outside
perturbative control and erases orientation in squared coupling coordinates.

## Evidence

- Packet: research/flavor/flavor-same-incidence-gauge-yukawa-fixed-point-interface.md
- Checker: research/flavor/checkers/wp821_same_incidence_gauge_yukawa_fixed_point_interface.py
- Generated result: research/flavor/results/wp821_same_incidence_gauge_yukawa_fixed_point_interface.json
- Exact result: 22 of 22 checks passed.
- Ledger-sequence claim: seqclaim-34d5998dbf802a7cfa575fbd, value 3619.
- Graph admission: ev-000000007767-33b1a777-f2e0-421c-a3c8-cd5f7622cc87.

## Claim boundary

The toy coefficient packet is a conditional algebraic construction, not a
derived flavor theory. A complete matter-spectrum constructor, global basin,
threshold-stable fixed point, physical16 descent, and calibrated detector
remain open.
