---
author: marici.Figueiredo
---

# 1936 — The π/8 Accounting: Branch Cut, Exact Fiber in the Valley Set, and a Recorded Residual (WP19)

Date: 2026-08-23
Author: marici.Figueiredo
Status: established as stated; one unresolved observation recorded in §5
Supersedes: nothing. Completes the flavor brief's WP4 at the level of
the paper's ensemble claim. Consistent with 1911 (WP14b inheritance),
1929/1934 (WP16–WP18 fiber structure).

## 1. Question

Account for the fitted ensemble's loop-phase clustering near multiples
of π/8 (the brief's fourth work package), keeping the three claims
separate:

1. phase values empirically cluster near π/8 multiples;
2. a Yukawa-triangle angle equals a CKM angle at leading order;
3. a UV symmetry dynamically selects the simple phase.

All exact-fit solves below are `physical10`-fiber solves over the fit
point p*. Per the fiber-claim policy they certify finite ambiguity,
never uniqueness; every converged root's sheet membership is certified
by its `physical16` image against the two quotient sheets over p*.

## 2. Branch cut (exact)

The two cos δ sheets over p* (WP18) are not both viable against the
paper's 17-observable fit:

- small-δ sheet (cos δ > 0): χ² = 3.3628, below the 3σ/7-dof cut 20.28;
- large-δ sheet (cos δ < 0): χ² = 651.19, top pulls γ +16.3σ,
  |Vtd| +14.0σ, β −10.3σ, α −9.1σ.

The ensemble of viable textures lives entirely on the cos δ > 0 sheet.
The two-sheetedness of the measured ten-coordinate projection (1934) is
therefore resolved by data with overwhelming margin: the second sheet
never entered the paper's fit, and no ensemble property may be
attributed to it.

## 3. The exact fiber is contained in the scan's valley set (certified)

A dense multi-start completion of the viable-sheet exact fiber at p*
(class-phase anchors + 100 uniform phase anchors × 40 restarts per
orbit; residual < 1e-7; physical16 branch gate) was run for every orbit
whose WP15b dominant classes (χ²_min < 4) were not already matched to
the sampled atlas at 1°. Result: in every orbit, each exact viable
pinned phase has a dominant scan class within 1° — usually within
0.01°:

| orbit | exact pinned phases (deg) | matching scan classes (deg) |
|-------|---------------------------|-----------------------------|
| 0     | 42.831, 69.723            | 42.83, 69.72                |
| 4     | 46.861, 89.717            | 46.86, 89.73                |
| 5     | 21.671, 22.821            | 21.67, 22.82                |
| 7     | 89.717                    | 89.69, 89.73                |
| 10    | 22.866, 23.890            | 22.87, 23.89                |
| 11    | 89.733                    | 89.69, 89.73                |
| 13    | 89.717                    | 89.69, 89.73                |
| 14    | 22.821                    | 22.82                       |
| 15    | 89.717                    | 89.69, 89.73                |
| 16    | 68.922, 89.513            | 68.92, 89.51                |
| 17    | 89.733                    | 89.69, 89.73                |

(orbits 2, 6, 9 needed no completion: all their dominant classes matched
the sampled atlas phases in the first pass). The exact fit the paper
implicitly solves is therefore a subset of the scan's viable minima,
and the ensemble's phase content includes the exact fiber's phases.

## 4. The scan's extra valleys, and a falsified intermediate hypothesis

The intermediate hypothesis "every dominant class phase is a small
perturbation of its own orbit's exact pinned phase" is **falsified**:
34 class records sit 20–66° from their orbit's viable pinned set.
These are not defects and not bookkeeping mismatches (orbit indexing
verified aligned between WP15b and WP18; identical χ² floor 3.36 at
both valley types). They are additional, distinct viable χ² minima in
the same charts — other physical quotient points inside the 3σ data
ellipsoid.

Two structural facts about them:

- **Sibling orbits share the valley multiset.** Orbits 7, 11, 13, 15,
  17 present the same valley phases {23.67, 46.86/46.94, 89.69/89.73};
  orbit 4 presents the same set plus its own exact valley at 46.861.
- **The exact p* valley occupies different members of the shared set in
  different charts**: p* sits at folded phase 46.861 in orbit 4's chart
  and at 89.717 in orbit 7's chart. This is WP11's chart-dependence of
  the loop phase operating *inside the fit ensemble* — the same
  physical point carries different chart phases in sibling
  presentations, while the ensemble of physical minima is chart
  independent.

## 5. The accounting, and its boundary

Established at the level of the paper's claim:

- Every dominant class phase in the 134-class ensemble lies within
  2.22° of a window center {22.5°, 45°, 67.5°, 90°}; claim 1 of WP4 is
  reproduced exactly as an empirical statement.
- For the exact-fiber (p*) valleys the mechanism is now exact:
  (i) the measured CKM angles at p* (α = 89.224°, β = 22.801°,
  γ = 67.976°) lie within ~1° of 4π/8, π/8, 3π/8;
  (ii) WP14b inheritance (ledger 1911) pins the chart loop phase to the
  CKM-angle data, J² = ρ² sin²φ per chart;
  (iii) the window binning (half-width 11.25°) absorbs the rest.
  Class multiplicities are scan-basin weights, not physics.
- No lattice attractor and no UV quantization law is needed or
  indicated. Claim 3 of WP4 finds no support anywhere in the ensemble
  structure: nothing selects the simple phase beyond the measured CKM
  angles themselves.

**Recorded residual (unresolved observation).** The extra valleys of §4
also hug the window centers within ~2°, and inheritance at p* does not
explain their tightness: each extra valley is a different physical
point on a different sheet of the chart map, with its own ρ, and
arcsin(J/ρ) on those sheets has no established reason to land near a
π/8 multiple. Candidate mechanisms: per-valley inheritance with
sheet-specific ρ; χ²-floor selection of φ through next-to-leading
observable dependence. Deciding between them requires per-valley
`physical16` data that WP15b did not store. This is recorded, not
smoothed over: the "accounting" of the clustering is complete for the
exact fiber and empirical for the extra valleys.

## 6. Consequence for the sector question

WP4 is hereby closed at the level of the paper's evidence. The π/8
clustering is the measured near-π/8-ness of the CKM angles transported
into chart phase coordinates by inheritance, plus binning — not an
independent quantization phenomenon. This removes the last candidate
"conspicuous coincidence" that could have been promoted to a UV law,
and it leaves the sector assessment where WP11–WP18 put it: the
flavor carrier is the physical quotient with its invariant readout;
sparse textures are charts; the loop phase is chart data.

## 7. Artifacts

- `research/flavor/checkers/wp19_pi8_accounting.py`
- `research/flavor/checkers/wp19b_valley_coverage.py`
- `research/flavor/results/wp19_pi8_accounting.json`
- `research/flavor/results/wp19b_valley_coverage.json`

Reproduce:

```bash
cd research/flavor
./.venv/Scripts/python checkers/wp19_pi8_accounting.py   # slow: dense LM solves
./.venv/Scripts/python checkers/wp19b_valley_coverage.py # fast: stored artifacts only
```
