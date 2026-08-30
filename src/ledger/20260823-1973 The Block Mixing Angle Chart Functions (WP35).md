---
author: marici.Figueiredo
---

# WP35: the block mixing angle chart functions - reciprocal law for u-sheets, per-class law for c-sheets

WP34 established that the block mixing angle th_mix of the real
block-diagonal Hu is exactly chart-phase determined for u-singlet sheets
(spread 3.9e-8 cross-class) and t-singlet sheets (1.1e-9), but not for
c-singlet sheets (3.8e-3 cross-class at fixed phase). WP33 had noted a
high-phase 'dressing class constant' 0.038769. This package extracts and
types the exact chart functions th(phi) and certifies what the c-singlet
angle is data OF.

Method (checker `checkers/wp35_angle_functions.py`, results
`results/wp35_angle_functions.json`, 1210 WP20 valley records, 5/5
gates):

- per-anchor angle tables: group sheets by chart phase (0.01 deg),
  record mean th_mix, within-group spread, and the number of DISTINCT
  texture classes agreeing on each value;
- closed-form hunt over 12 pre-registered forms (sin/cos/tan in phi and
  phi/2, linear, and the reciprocal family a/sin^n, cot, cot(phi/2)),
  two-parameter least squares, 1000-draw shuffle null;
- c-class typing: within-class raw spread vs within-class linear-in-phi
  fit residuals vs cross-class spread at fixed phase.

## Findings

1. The u-class splits into two exact branches. UNMIXED sheets: th = 0
   exactly (fully diagonal Hu) - 6 phase groups (phi ~ 42.83, 44.03,
   68.02, 68.53, 69.22, 69.72 deg), 82 texture classes. MIXED sheets:
   7 phase groups (46.94-46.99, 68.01, 89.20, 89.61, 89.62 deg), 232
   texture classes.

2. The mixed u-branch obeys a reciprocal law:

       th_u(phi) = 0.038899 / sin(phi) - 0.000134

   max residual 3.3e-6 across all 7 mixed groups (fit floor), null rate
   0/1000. Equivalently sin(th).sin(phi) is constant at 0.0387566 within
   5.8e-6 for the phi > 60 deg groups. The WP33 'dressing class
   constant' 0.038769 was the sin(phi) ~ 1 limit of this law - not a
   high-phase special value but the law's normalization. The two
   branches coexist at nearby phases (68.01 mixed vs 68.02 unmixed), so
   mixing is a discrete texture property, with the phase setting the
   angle only on the mixed branch.

3. The t-class angle is exactly phase-determined (1.1e-9 cross-class)
   but carries NO exact closed form among the 12 registered candidates
   (best a/sin(phi)+b at max residual 2.9e-4, null 0.029). The 4-group
   table (th = 0.23779939, 0.22696892, 0.09574592, 0.08926943 at phi =
   22.82, 23.89, 68.92, 89.73 deg) is recorded as the empirical law.

4. The c-class angle is PER-CLASS phase data. Its within-class raw
   spread (6.1e-5) is fully accounted by a smooth slope ~ -1e-4/deg
   acting on the fit phi jitter of +-0.15 deg (linear-in-phi residuals
   <= 2.0e-5 = record noise), while across classes at FIXED phi the
   angle varies by 3.8e-3. So the c-angle is the one singlet class whose
   mixing carries magnitude-valley information beyond the loop phase;
   the u/t angles are pure phase data (u with a discrete mixed/unmixed
   branch bit).

## Typing

- u: 'phase law' with a discrete branch bit - unmixed (th = 0 exactly)
  vs mixed (reciprocal law in sin(phi), cross-class exact at 3.3e-6).
- t: 'empirical phase law' - phase-determined, no exact closed form.
- c: 'per-class phase law' - smooth in phi within class, class-dependent
  normalization across classes.

All quantities remain chart-atlas data of the sparse texture
presentation (WP11: the loop phase is a chart invariant, not presently a
physical invariant). No physical-invariant claim is made; the laws
constrain how the chart atlas is fibered, not the physical quotient.

## Verification

`./.venv/Scripts/python checkers/wp35_angle_functions.py` reproduces
`results/wp35_angle_functions.json` (5/5 gates: G1 u cross-class
exactness, G2 t cross-class exactness, G3 u mixed reciprocal law with
null, G4 t has no exact form, G5 c per-class phase law).
