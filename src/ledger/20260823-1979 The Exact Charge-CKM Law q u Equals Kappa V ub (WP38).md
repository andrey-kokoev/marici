---
author: marici.Figueiredo
---

# WP38: the charge is CKM-composite - q_u = kappa_u * V_ub exactly per sheet

WP37 established q_anchor = H_12.sin(phi) as a class constant (exact
for u/t, ~1% approximate for c). This package asks whether the
constants are CKM-composite. Checker `checkers/wp38_charge_ckm.py`,
results `results/wp38_charge_ckm.json`, 5/5 gates.

## The exact u-class law (G1, G2)

Across all 232 viable mixed u-class sheets:

    q_u = H_12.sin(phi) = kappa_u * V_ub,
    kappa_u = 9.678574167082195

231/232 sheets sit within 9.2e-9 of the median kappa; exactly one
outlier at 3.4e-6 (class 394_348_d02). The deviation does not
correlate with chi2 (corr 0.14; chi2 is nearly constant 3.36-3.90),
so fit noise is excluded: this is an exact per-sheet identity of the
fitted ensemble, 17x sharper than WP37's class constancy (2.9e-5).
The WP37 picture 'q_u class-constant' was the shadow of the sharper
law 'q_u tracks V_ub per sheet'.

## t- and c-class status (G3, G4)

- t-class: q_t = 1.125347e-6 constant at 8.4e-9; every CKM element is
  equally constant within the class, so CKM tracking is unresolvable -
  the const law stands as the best description.
- c-class: every candidate ratio (const, q/Vub, q/Vcb, q/Vtd) scatters
  at ~1% with >38% of sheets beyond 1e-4 - genuinely approximate, no
  hidden exact bulk law. WP37's typing confirmed.

## Negative results (G5 + survey)

- The WP36 magnitude factor M in J.Du.Dd = c.sin(phi).M is NOT an
  edge-magnitude monomial: log-log regression over 232 u-class sheets
  returns all exponents ~0 (< 5e-4), consistent with M ~ Du.Dd.
- kappa_u is dimensionally yukawa^2 in scan units, but 9.68 > y_t^2 =
  0.935, so no pure Yukawa monomial can express it. A bounded
  exponent search over Yukawa/CKM factors produced only
  multiple-comparison-grade hits (best: yt^-1.Vus^-1.5 at 8.4e-6) -
  recorded as numerology, not identification. The structural
  derivation of kappa_u is OPEN; the natural route is the LO
  expression of V_ub for u-anchor textures (Vub_LO vs H_12.sin(phi)).

## Typing

All statements are chart-space laws of the fitted nine-link ensemble;
WP11 stands (phi is chart data). But the u-class law now ties chart
data (H_12.sin phi) to a PHYSICAL observable (V_ub) by an exact
constant - the first exact chart-to-readout bridge found in this
program. If kappa_u proves derivable from the texture LO structure,
this becomes a candidate H2LR pairing component.
