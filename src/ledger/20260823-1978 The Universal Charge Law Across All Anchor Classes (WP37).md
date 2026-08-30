---
author: marici.Figueiredo
---

# WP37: the universal charge law - H_12.sin(phi) = q_anchor for every viable mixed sheet

WP36 derived the J-routing mechanism on the 303 u-class sheets. This
package extends the census and the law to all 955 viable block-diagonal
sheets (all anchors u/t/c, all orientations). Checker
`checkers/wp37_universal_charge.py`, results
`results/wp37_universal_charge.json`, 5/5 gates.

## Universal structure (exact, machine floor)

1. Phase-sector census (G1): EVERY viable block-diagonal sheet has its
   phase edge in the DOWN sector (955/955). Hu is real ensemble-wide;
   the loop phase lives only in Hd.

2. Universal J-routing (G2): zeroing the Hu block off-diagonal
   c = H_12 kills J on every mixed sheet (848 sheets: u 232, t 192,
   c 424; residual J0/J < 2.5e-15) and leaves J exactly on every
   unmixed sheet (107: u 71, c 36; J0/J = 1 to machine precision).
   The up-sector 2x2 block mixing is the unique J valve.

3. Exact commutator identity (G3, max err 2.1e-34) and first-harmonic
   Im(Hd) with magnitude-only factorization (G4) hold for all anchors.

## The charge law (G5)

Per-sheet theorem of WP36: J.Du.Dd = c.sin(phi).M(mags). Ensemble
readout shows the magnitude factor collapses to a class constant:

    q_anchor = H_12 . sin(phi)

    q_u = 3.621318e-02   within-class rel 2.9e-05   (EXACT, 232 sheets)
    q_t = 1.125347e-06   within-class rel 1.7e-08   (EXACT, 192 sheets)
    q_c = 3.245237e-03   within-class rel 1.0e-02   (APPROXIMATE, 424)

The c-class charge carries a genuine ~1% texture-level fluctuation,
partially correlated with the block splitting Delta = H_22 - H_11
(corr 0.73); a linear Delta correction still leaves 0.87% residual.
No exact refinement found - typed honestly as approximate.

## What this explains about WP35

WP35's three-way theta typing is the q-law masked by Delta behavior:
- u: theta_u(phi) = q_u/(Delta.sin phi) with Delta class-constant at
  the fitted level -> the observed reciprocal law.
- t: q_t is exactly constant (1.7e-8) but Delta = H_22-H_11 is the
  tiny fitted yc^2-yu^2 difference and drifts 3-10% across phase
  groups -> the reciprocal law was real but hidden in WP35.
- c: q_c approximate at 1% -> per-class theta behavior.

Charge ratios: q_u/q_c = 11.15, q_c/q_t = 2885. Open: identify
q_anchor as an explicit magnitude monomial and test the near-coincidence
q_u/V_cb ~ q_c/V_ub ~ 0.87.

## Typing

WP11 stands: phi remains chart data; nothing here claims descent to
the physical quotient. The charge law is a chart-space statement about
the scan ensemble's readout constraint, exact for u/t and approximate
at ~1% for c.
