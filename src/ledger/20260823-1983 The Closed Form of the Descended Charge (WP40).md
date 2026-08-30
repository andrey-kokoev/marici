---
author: marici.Figueiredo
---

# 1983 — The Closed Form of the Descended Charge (WP40)

WP39 showed that kappa_u = q_u/V_ub is a function of the physical point, not of
the chart. WP40 determines that function. The answer is a monomial in physical
data only:

  q_u = C * y_t^2 * |V_cb| * sin(gamma_CKM),   C = 0.9993729706

verified across all 232 u-anchor sheets of the fitted ensemble with bulk maximum
deviation 2.3e-11 (one outlier sheet at ~1e-7, the known 394_348_d02 case).

Physical reading: the u-anchor sheet's weak charge q_u = H_12 * sin(phi) is y_t^2
times the height of the CKM unitarity triangle (|V_cb| sin gamma = |V_ub| sin beta
= 2*Area/base). A pure chart quantity (WP11: phi is chart data) equals, on the
fitted locus, a monomial built entirely from weak-basis invariants.

## How it was found

The gradient of F = kappa_u in the 10-dimensional physical coordinate space
(6 Yukawas + Vus, Vcb, Vub, gamma) was measured by refitting the reference sheet
([417,482] d12 u-anchor) against 17 single-observable shifted targets (+1e-3
relative) and solving the 10-parameter response problem (17 equations, rank 10,
lstsq residual 6.3e-5). The measured gradient:

  y_t: +2.0010   Vcb: +0.9978   Vub: -0.9993   gamma: +0.4790

Everything else below 1e-3. The gamma exponent 0.4790 equals gamma*cot(gamma) =
0.4799 at the fitted angle, i.e. kappa_u is proportional to sin(gamma), not to a
power of gamma. The forward test of the closed-form gradient through the measured
17x17 response matrix gives residual 7.7e-4; deleting the gamma term degrades it
400-fold (0.317).

## Falsified candidates (stay falsified)

- y_t^2 * |Vtd| / Vus: ensemble max deviation 3.6e-4 (G5).
- y_t^2*|Vtd|*sin(alpha)/|Vcd|, y_t^2*sqrt(J/(Vcb^2*y_b^2)), and two
  sin(beta)/sin(gamma) variants: excluded earlier by refit tracking at 1-2%.
- Ensemble-only log-log regression cannot discriminate (collinearity, residual
  7.6e-13 with smeared exponents); the refit-response method is the decisive tool.

## Texture independence

C is constant at 4.6e-10 (theta-half-split) while the block-mixing angle spans
0.0388-0.0531 rad; corr(C, theta) = -0.058. C is not a function of the texture
mixing angle.

## Open item

C = 1 - 6.27e-4, universal. Identical under all four normalization variants
(eigenvalue vs observable y_t^2, observable vs Wolfenstein-barred gamma), so it is
not a gamma-convention artifact. Small residual exponents after the monomial
(y_t +0.001, Vcb -0.002, Vub +0.001 in the gradient) suggest a smooth subleading
correction, unidentified. Also open: the c-anchor and t-anchor analogs, and the
readout expression of F_u/F_c = 11.155 at the same-point pair.

## Typing

WP11 stands: phi and q_u are chart data. What WP39/WP40 establish is that on the
fitted locus the chart combination q_u/V_ub (WP39), equivalently q_u itself as a
function of physical data (this entry), descends to the physical quotient. The
closed form makes the H2LR pairing candidate concrete:

  <K_flavor, O_flavor> : (edge data, loop holonomy) -> y_t^2 |V_cb| sin(gamma)

with the left side evaluated in any fitted u-anchor chart.

Certificate: checkers/wp40_charge_closed_form.py -> results/wp40_charge_closed_form.json (5/5 gates).
