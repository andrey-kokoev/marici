---
author: marici.Figueiredo
---

# WP39: kappa_u = q_u/V_ub is a function of the physical readout, not of the chart

WP38 found the exact per-sheet law q_u = H_12.sin(phi) = kappa_u.V_ub
(kappa_u = 9.678574167082195, bulk 9.2e-9 over 232 u-class sheets).
This package determines what kappa_u IS. Checker
`checkers/wp39_kappa_descent.py`, results
`results/wp39_kappa_descent.json`, 5/5 gates.

## Findings

1. NOT a texture-algebra identity (G2). Random log-magnitude
   perturbations (eps = 0.01, no refit) drift kappa at ~4x the
   perturbation (median drift 1.2e-2). Off the fitted locus the law
   evaporates - it is a property of the readout-constrained points.

2. kappa = F(physical point) (G3, G5). Refitting the SAME texture
   ([417,482] d12) against shifted central values moves kappa
   linearly with the physical shift over three decades: Vub central
   +1e-5/+1e-4/+1e-3 gives kappa slope -0.4427/-0.4425/-0.4423
   (linearity 0.05%). kappa responds to the physics, not to the
   chart. Response to a +1e-3 Vub shift is 48000x the bulk spread.

3. The ensemble lies in ker(dF) (G1). Across 232 sheets the fitted
   Vub scatters at 3.3e-5 (WP38) yet kappa is constant at 9.2e-9 -
   the sheet-to-sheet physical scatter is exactly along directions
   where F is constant. Hence q_u/V_ub descends to a well-defined
   function on the physical quotient near the fitted point. q_u =
   c.sin(phi) remains chart data; its RATIO with V_ub is physical.
   This is the first demonstrated chart-coordinate combination that
   secretly descends - a concrete H2LR pairing candidate.

4. Same-physical-point pair (G4). Texture [417,482] d12 has TWO
   fitted sheets with identical mass spectra (rel 3.9e-10) and
   identical CKM matrices (max entry diff 4.4e-11) but different
   anchor partitions: u-singlet sheet with q_u = 3.6213e-2 and
   c-singlet sheet with q_c = 3.2462e-3, ratio 11.155. The two
   anchors' charge expressions are genuinely different chart
   functions of the same physical point - WP11 illustrated in one
   texture. Each anchor's charge/V_ub ratio descends separately.

## Typing and next

phi stays chart data (WP11 untouched). The descended object is the
RATIO q_anchor/V_ub per anchor. Open: (i) map the gradient of F by
independent single-observable refit shifts (measured total
derivatives: Vub -0.44, Vus -0.47, sin(gamma) +0.38, Vcb +0.04 -
partials still entangled); (ii) derive F's closed form - why does
the viable-sheet ensemble's degeneracy lie exactly in ker(dF);
(iii) test whether F_u/F_c = 11.155 at the fitted point has a
readout expression.
