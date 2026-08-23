---
author: marici.Figueiredo
---
# 1960 - Raw-Phase Trench Landscapes: the Five L Levels Are Per-Class Properties, Not Universal Attractors

- Date: 2026-08-23
- Author: marici.Figueiredo
- Status: main question answered (per-class, not universal); sheet taxonomy established; two v2 artifacts diagnosed and repaired
- Supersedes: nothing. Continues 1959 (WP25a center selection), 1937 (WP20 phase spectrum)

## 1. Question and method correction

WP25a reduced the five cluster centers to five level sets L_c of
a1/(DuDd). WP25b asks: does EVERY texture's fixed-phase chi2 landscape
trench at all five levels (universal attractors; fit quality then
selects viability), or does each texture trench only at its own
level(s)?

Method correction with standalone value. The landscape must be swept
in the RAW phase phi in [-180, 180] deg, not the folded phase in
[0, 90]. The 17-observable fit target contains SIGNED unitarity-triangle
angles, so chi2(phi) != chi2(-phi) in general, and viable trenches
exist outside the first quadrant (cluster-1 stored raw phases are
-42.83 and +110.28 deg, folding to 42.83 and 69.72). A v2 folded-domain
sweep reproduced gates only for textures whose raw phase already lies
in [0, 90] and misdiagnosed cluster 1 and the oddball as bottomless;
the v3 raw-domain sweep (361-point periodic grid, 0.2 deg refinement,
boundary seams treated periodically) recovers every stored WP20
minimum as a landscape bottom.

Fit protocol per grid point: mass-only LM pre-fit then full
17-observable LM, seeded by the texture's own stored WP20 minimum
magnitudes plus one fresh hierarchy-aware start. Validation gate:
each stored minimum refit at its own raw phase must reproduce
chi2 < stored + 0.5. Gates pass 15/16; the single failure is one of
three stored points of 270_369_d00 (refit 23.67 vs stored 3.36), a
localized LM seed instability - the texture's trench itself is
reproduced from its other seeds and its landscape is trustworthy.

## 2. Main answer: per-class trenches

Eleven representative textures (two per cluster 0-4 plus the oddball).
Universality census (bottom within 0.75 deg of center, chi2 < 4):

| center | L level    | textures trenching                          |
|--------|-----------|---------------------------------------------|
| 23.151 | ~8.1e-5   | 267_302_d02, 267_309_d02 (cluster 0 only)   |
| 43.173 | ~4.64e-5  | 266_335_d00 (cluster 1 only)                |
| 46.907 | ~4.36e-5  | 270_348_d02, 270_369_d00 (cluster 2 only)   |
| 68.388 | ~3.42e-5  | 266_303_d00, 266_311_d01, 266_349_d00 (2)   |
| 89.572 | ~3.18e-5  | 267_271_d00, 267_279_d01 (cluster 4 only)   |

Away from its own level(s) every texture's chi2 rises to 1e2-1e4 at
the other centers. No texture trenches at more than two levels; none
at all five. The five L levels are therefore NOT universal attractors
of the per-texture landscape: they are an ensemble property of the
viable chart classes. Combined with 1959, center selection =
L-level-set selection = a per-class property, and the census of
levels reflects which classes are viable, not a shared valley
geometry.

## 3. Sheet taxonomy

Viable bottoms come in four patterns:

1. CP-sign pairs at one L level. 267_302_d02: raw +-23.80 deg, same
   J = 3.1715e-5, L = +-7.859e-5. Cluster-3 pair 266_303_d00,
   266_311_d01: raw +-68.00, L = +-3.4281e-5.
2. Two distinct L levels in one texture (cluster 1). 266_335_d00:
   sheets at raw -42.80 (|L| = 4.679e-5 = the cluster-1 level) and raw
   +110.20 (|L| = 3.390e-5); 266_349_d00: raw -44.00 (4.576e-5) and
   +111.40 (3.417e-5). The second sheet's |L| matches the CLUSTER-3
   level (3.42e-5) - cluster-1 textures realize both L1 and L3, which
   is why center 3 has three trenching textures.
3. Single sheets whose CP mirror is not viable: 267_309_d02 (mirror
   chi2 = 1.27e4), cluster-2 pair (mirrors 1.2e3, 2.9e3), cluster-4
   pair (mirror 9.0e3), oddball (mirror 1.1e4), cluster-1 mirrors
   (1.9e3, 2.4e3). Mirror chi2 values were computed on the grid, so
   the asymmetry is genuine landscape structure, not detector loss.
4. Branch-merged single bottom at 90 deg (cluster 4): raw +90.20,
   sin(phi) = 0.99999, L = |J| = 3.1798e-5 to 1e-9 - the two arcsin
   branches coalesce, one sheet remains.

## 4. The oddball sits at the cluster-0 level

311_273_u01 trenches at raw -24.00 deg (fold 24.00, dev 0.85 from
center 0), |L| = 7.841e-5, chi2 = 3.52. Its level matches the
cluster-0 trenches (7.859e-5, same ~3 percent below the
center-implied 8.08e-5) with mildly elevated chi2. The 6-edge-u
exceptional texture is a near-L0 texture outside the rigid part of
cluster 0, not a sixth level.

Level deviations: every trench sits 0.1-1.4 deg off its cluster
center with |L| a few percent below the center-implied value,
consistent with 1959's arcsin amplification of the 2e-4 |J| spread.
Trench bottoms reproduce the WP20 stored minima to <= 0.1 deg after
refinement.

## 5. v2 artifacts resolved

- Folded-domain failure (section 1): diagnosed as a domain bug, not
  fit weakness; fixed by the raw-domain sweep.
- Apparent twin identity: in v2 the 267_271_d00 and 267_279_d01
  curves coincided to displayed precision. In v3 their curves differ
  at 360/361 grid points (max diff 2.9e3) while their viable minima
  coincide to printed precision (raw 90.20, chi2 3.364, J and L equal
  to 6 digits). The v2 coincidence was a common fit-failure artifact.
  The pair shares its physical point but not its off-shell landscape:
  no texture-level identity.

## 6. Consequence for the program

The L spectrum is not an attractor structure that every texture
feels; it is a classification of viable chart classes, each class
trenching at one level (or, for cluster-1 diagonal textures, two).
Together with 1959 this closes the "universal quantization" reading
of the phase clustering from the landscape side: the discreteness is
a census of which classes are viable and at which level each trenches.
The remaining open object is the magnitude-valley mechanism that
selects the viable (class, level) pairs themselves.

## 7. Artifacts

- Checker: research/flavor/checkers/wp25b_trench_landscape.py (v3;
  docstring discloses the v1 fit-strength failure and the v2
  folded-domain bug, both overwritten).
- Results: research/flavor/results/wp25b_trench_landscape.json
  (361-point raw-phase curves, gates, bottoms with J and L).
- Seeds: fixed (seed=7); gates validated against
  results/wp20_valley_audit.json stored minima (15/16 pass, one
  localized seed instability disclosed in section 1).
