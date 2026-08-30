---
author: marici.Figueiredo
---

# 1984 — The t-Anchor Closed Form and the Two Universal Constants (WP41)

WP40 gave the u-anchor charge law. WP41 extends the refit-gradient method to the
t-anchor class and settles the nature of the u-class normalization.

## Result 1: the t-anchor closed form

The 10-dimensional refit-gradient of ln q_t on the reference t-sheet is

  y_c: +2.0010   Vub: +0.9863   Vcb: -0.9865   (all others < 3e-3)

and therefore

  q_t = C_t * y_c^2 * (|V_ub| / |V_cb|),   C_t = 0.9920333163

verified ensemble-wide over all 192 t-anchor sheets with bulk maximum deviation
1.6e-10. Rival forms fail the forward response test at 28x residual or worse
(yc^2*Vub/Vcb*sin(gamma): 28x; yc^2*Vus*Vcb: 65x; yt^2*Vub/Vcb: 177x).

## The emerging pattern

With q = Re(H_block,12) * sin(phi_loop) (WP37) and H the up-sector Yukawa
metric, each anchor class has

  q_anchor = C_anchor * (largest Yukawa in the 2x2 block)^2 * (CKM factor)

  u-anchor (block {c,t}):  y_t^2 * |V_cb| * sin(gamma)   C_u = 0.9993729706
  t-anchor (block {u,c}):  y_c^2 * |V_ub| / |V_cb|       C_t = 0.9920333163

The block's largest Yukawa sets the scale, exactly as
Re(H_12) = (m_large^2 - m_small^2) sin(theta) cos(theta) suggests; the CKM
factors are then the measured block-mixing angles in physical units, up to the
constants C. The c-anchor class has NO exact form of this type (genuine ~1%
texture fluctuation, correlating with the block splitting Delta, WP37/38).

## Result 2: C_u is a true constant, not a physical function

The refit-gradient of ln C_u over the 10-dim physical space has every partial
below 1.5e-3 (residual 1.3e-4). Combined with C_u's constancy at 2.3e-11 across
the ensemble, C_u = 1 - 6.27e-4 is a pure number of the construction/fitting
convention, not a disguised function of the physical point. Same conclusion
expected for C_t = 1 - 7.97e-3 (not separately gradient-tested here).

## Open items

- Identification of the pure numbers C_u and C_t ((Vub/Vcb)^2 = 8.07e-3 is near
  but 1.2% off 1 - C_t; lambda^2/81 is near but 0.27% off 1 - C_u).
- Why the c-anchor class alone carries an order-1% texture fluctuation, and its
  exact dependence on the block splitting.
- The readout expression of F_u/F_c = 11.155 at the same-point pair.
- A single principle producing both CKM factors (Vcb*sin(gamma) vs Vub/Vcb).

Certificate: checkers/wp41_t_class_and_C_constant.py -> results/wp41_t_class_and_C_constant.json (4/4 gates).
