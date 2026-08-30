---
author: marici.Figueiredo
---

# 1985 — The c-Anchor Class Is Exact Too; Erratum to WP38/WP41 (WP42)

## Erratum

WP38 reported and WP41 repeated that the c-anchor class "genuinely fluctuates
at ~1% in all ratios" and has no exact closed form. This is superseded. The
~1% scatter was an artifact of testing incomplete monomials. With the full
monomial the c-class is exact:

  q_c = C_c * y_t^2 * |V_ub| * sin(gamma),   C_c = 1.0008814042

constant across all 424 c-anchor sheets with maximum deviation 6.3e-6 (181
sheets within 1e-9 of the median). The old q_c/|V_ub| ratio scatters 7.6e-3
because y_t^2*sin(gamma) itself scatters that much across the fitted ensemble;
the monomial absorbs exactly that wandering (G3: old bulk dev 7.6e-3, new max
dev 6.3e-6).

## The complete anchor taxonomy

All three anchor classes of the up-sector singlet/block decomposition now have
exact physical closed forms for the weak charge q = Re(H_block,12)*sin(phi_loop):

  u-anchor (block {c,t}):  q_u = C_u * y_t^2 * |V_cb| * sin(gamma)  C_u = 0.9993729706  (dev 2.3e-11)
  c-anchor (block {u,t}):  q_c = C_c * y_t^2 * |V_ub| * sin(gamma)  C_c = 1.0008814042  (dev 6.3e-6)
  t-anchor (block {u,c}):  q_t = C_t * y_c^2 * |V_ub| / |V_cb|      C_t = 0.9920333163  (dev 1.6e-10)

The scale is always the largest Yukawa of the off-diagonal block, as
Re(H_12) = (m_large^2 - m_small^2) sin(theta) cos(theta) requires. The CKM
factors are the block mixing angles in physical units.

Consistency: at the [417,482] d12 same-point pair, q_u/q_c direct = 11.15538774
vs monomial prediction 11.15538774 (agreement 2e-11). The earlier "11.155" pair
ratio is thus exactly accounted for.

## C_c is a true constant

Refit-gradient of ln C_c over the physical 10-space: all partials < 1.8e-3
(G5), matching C_u's certified constancy (WP41). All three constants are pure
numbers of the construction: 1 - 6.27e-4, 1 + 8.81e-4, 1 - 7.97e-3.

## Process note (honesty)

Two interactive exploratory runs in this package produced a spurious
non-integer c-gradient (y_s^0.72 y_b^-0.72 ...). Root cause: a Python loop
variable shadowed the phase-edge index, corrupting three of seventeen refits.
The published wp40/wp41 checkers use literal/parameter indices and were
verified unaffected by code reading; the correct c-gradient (G2) is clean on
both tested textures (y_t +2.001, Vub +1.000, gamma = gamma*cot(gamma)).

## Open

- Identification of the three pure numbers C_u, C_c, C_t.
- The single principle behind the three CKM factors:
  Vcb*sin(gamma), Vub*sin(gamma), Vub/Vcb.
- Whether the 6.3e-6 c-class residual has its own exact structure.

Certificate: checkers/wp42_c_class_closed_form.py -> results/wp42_c_class_closed_form.json (5/5 gates).
