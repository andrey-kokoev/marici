---
author: marici.Figueiredo
---

# WP34: universal block structure and class-typed mixing angles - the dressing constant is class-level

WP33 derived the block21 exchange dressing from the sheet frames: real
block-diagonal Hu = Yu Yu^dag (singlet + 2x2 block) on the 58 exchange
sheets, Lu = P01.R02(-th_B).R12(th_A). This package asks whether that
structure is general and whether the mixing angle is a function of the
loop phase across the whole viable ensemble (1210 WP20 valley records).

Method (checker `checkers/wp34_theta_phi_law.py`, results
`results/wp34_theta_phi_law.json`, 1210 records, 7/7 gates):

- census: per record, test Hu reality and block-diagonality for each
  singlet index (tol 1e-8); type the singlet value against the six mass
  anchors;
- determinism: per anchor class, group sheets by chart phase (0.01 deg)
  and measure within-group spread of the small mixing angle
  th_mix = min(|th|, pi/2 - |th|), th = (1/2) atan2(2 H_12, H_22 - H_11);
- pre-registered functional forms th ~ c.sin(phi), c.phi, c.sin(phi/2)
  per anchor class with a 1000-draw shuffle null.

## Findings

1. Universal approximate block theorem. 955/1210 sheets (79%) are real
   block-diagonal to machine precision; the remaining 255 are ALL at the
   fit floor (169 below 1e-4, 86 below the observed maximum 8.1e-3) -
   ZERO genuinely non-block-diagonal sheets exist. Coincident textures
   are 100% machine-exact. The WP33 structure is the generic block21
   chart form, not an exchange specialty. Singlet census: yu^2 (303
   sheets), yc^2 (460), yt^2 (192).

2. Exact per-class angle determination. th_mix is an EXACT function of
   the chart phase for u-singlet sheets (within-phase spread 3.9e-8, all
   10 multi-record groups) and for t-singlet sheets (1.1e-9, all 4
   groups) - but NOT for c-singlet sheets (spread up to 3.8e-3; exact
   only on coincident subgroups, i.e. the WP32 chart points).

3. Class-typed laws. t-sheets: th_mix = 0.331 - 0.247 sin(phi), R^2 =
   0.994, max residual 5.4e-3, null 0/1000 - an approximate closed form
   of an exact per-phase function. High-phi u-sheets (80-89 deg): the
   near-exact class constant 0.038769 (band spread 3e-6 across distinct
   phases) - the WP33 dressing angle is a CLASS-LEVEL constant of
   high-phi u-singlet sheets, not a pair-level accident. c-sheets:
   monotone decrease with sin(phi) (band means 0.0092 -> 0.0044 ->
   0.0033), R^2 = 0.69, null 0/1000 - approximate anti-correlation, no
   exact law. Low/mid-phi u-sheets: heterogeneous, no law.

## Interpretation

The chart atlas has more exact structure than the quotient it covers -
and it is all still chart data. Three typed fragments: (i) the
singlet+block form is universal (up to fit floor), giving every viable
sheet a canonical light/heavy decomposition; (ii) the block mixing angle
is exactly chart-phase-determined for u- and t-singlet classes but
carries magnitude-valley information beyond phi for the c-singlet class
(except on coincident subgroups, where the WP32 chart points fix it);
(iii) the WP33 dressing constant is promoted from pair-level to
class-level: every high-phi u-singlet sheet in the ensemble carries
theta_B = 0.038769, whether or not it participates in an exchange pair.
Per WP32/WP33 this constant is null-certified non-physical; its new
status is exact chart-atlas datum of maximal scope. The c-class failure
of phi-determinism is the interesting remainder: the c-singlet angle is
the one place where the angle remembers more of the valley than the loop
phase alone.

Artifacts: checkers/wp34_theta_phi_law.py, results/wp34_theta_phi_law.json.
Depends on: claim:83e79fa2a84099e8cd4d, WP20, WP24a, WP32, WP33.
