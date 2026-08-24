---
author: marici.Figueiredo
---

# 1995 - The Valley-Binding Mechanism: the Pi-8 Arc Closed at Constraint Level (WP46)

WP20 (1937) reduced the pi/8 question to one exact open residual: why do
the chi2 minima of the nine-link textures select magnitude sets whose
a1/(D_u D_d) = |J|/sin(window)? Since sin(phi) = |J| D_u D_d / a1 is an
identity at every point (re-verified: G4, max rel err 3.8e-9 over all 1210
viable minima), the phase spectrum IS the a1 spectrum, so the residual is:
what pins the valley phases? WP46 answers it at the constraint level with
the stored WP20 audit data plus absorbed (magnitude-refit) chi2 profiles.
Checker checkers/wp46_valley_binding.py, results
results/wp46_valley_binding.json, 5/5 gates.

## The valley-binding dictionary (G1, G3)

Re-clustering all 1210 minima at 0.02 deg resolution (the exact fiber
phases are delta-peaks; WP20's 0.15 deg bins merged neighbors) gives 23
dense sub-valleys. Every one is bound by exactly ONE physical observable,
uniform across every orbit that realizes it (G3: 23/23 shared):

  bound by gamma:    68.02, 68.01, 68.00, 46.86, 68.05   (n = 75+58+19+115+12)
  bound by beta:     23.86, 23.89, 22.82, 22.87, 21.67, 23.67 (n = 48+34+32+26+33+13)
  bound by |Vcd|:    89.73, 89.69, 68.92, 89.51, 69.72, 68.53 (n = 64+32+84+43+29+12)
  bound by |Vtd|:    46.94 (n = 127)
  bound by |Vts|:    89.61, 89.20 (n = 25+33)
  bound by |Vus|:    44.03 (n = 12)
  bound by ys/yud:   42.83 (orbit 0, n = 30), 69.22 (orbit 2, n = 12)

The WP20 46.8/46.95 "two-face" bin resolves at fine resolution into two
distinct sub-valleys: 46.86 (gamma-bound, the orbit-4 exact fiber phase)
and 46.94 (|Vtd|-bound). Every multi-orbit sub-valley carries its binding
observable in ALL of its orbits - the active constraint is physical data,
identical across presentations, which is exactly why different orbits
minimize at the same phase. The sharing mechanism WP20 observed ("the
extra valleys are the same valleys") is thereby explained: one constraint
equation, one root, many charts.

## The active constraint after absorption (G2)

LM magnitude re-fits at phi shifted by +-1,2,4 deg on the 8 largest
valleys: the binding observable contributes the largest share of the chi2
growth (top shares 0.35..0.61). The raw chart-facing sensitivity (which
CKM element the chart's loop edge feeds: Vcd, Vtd, Vts vary by orbit) and
the absorbed landscape constraint differ informatively: after the fit
re-absorbs what it can, gamma is the dominant active constraint in every
CKM valley outside the beta band (with alpha = 180 - beta - gamma its
dependent shadow at 0.23..0.27 share). beta pins the beta band (share
0.61). So at landscape level the valley spectrum is the root set of a
small system of scalar physical-data equations:

  gamma(phi; refit) = gamma_measured     (the 46-89 deg valleys)
  beta(phi; refit)  = beta_measured      (the 21-24 deg valleys)
  ys/yud(phi; refit) = measured ratio    (42.83 and 69.22)

## The two mass-bound valleys (G5)

Orbit 0's 42.83 valley and orbit 2's 69.22 valley are bound by the MASS
ratio ys/yud (uniformity 1.0 in both), not by any CKM readout. Neither is
CKM-inherited (min distance to any CKM angle or combination: 2.34 deg and
1.24 deg) and neither sits on the pi/8 lattice (2.17 deg and 1.72 deg
off). They are the only valleys whose active constraint lives in the mass
sector - and the constraint is the SAME ratio in both, one more instance
of the sharing mechanism.

## The closure chain (WP20 residual closed)

1. A viable minimum must fit the 17 observables; the active (least
   re-absorbable) constraint at each minimum is a single physical datum -
   gamma, beta, a CKM modulus, or ys/yud (G1, G2).
2. The valley phase is the root of that datum's fit equation; the datum
   and the equation class are orbit-independent, so the root is shared
   across orbits (G3) - discreteness and cross-orbit sharing explained.
3. The a1 spectrum follows identically: a1 = |J| D_u D_d / sin(phi_valley)
   (G4) - this answers WP20's question: the minima select those magnitude
   sets because the fit equation forces phi, and the identity forces a1.
4. The pi/8 proximity is not an attractor: it factors as (CKM-readout
   binding) x (the measured CKM angles' own lattice proximity, WP14b T4),
   and the two mass-bound valleys are not even CKM-inherited yet still
   off-lattice. Nowhere does the lattice itself select anything.

What remains genuinely open is only the question WP14b relocated to the
physical point itself: why the MEASURED CKM angles sit near pi/8
multiples. That is not a question about sparse presentations and is out
of the texture map's reach by its own typing (WP45): it belongs to the UV
or to a cross-sector parent-object statement about constant values.

## Honesty notes

- G2 top shares are 0.35..0.61, not 1.0: the fits are collective; the
  binding observable is the dominant active constraint, not the sole one.
- Raw sensitivities are computed at fixed magnitudes (WP20 convention);
  the absorbed profiles (G2) are the landscape statement.
- Fringe records (sub-clusters n < 10) are reported, not gated.

Artifacts: checkers/wp46_valley_binding.py, results/wp46_valley_binding.json.
Depends on: WP14b (1911), WP19 (1936), WP20 (1937), WP45 (1988).
