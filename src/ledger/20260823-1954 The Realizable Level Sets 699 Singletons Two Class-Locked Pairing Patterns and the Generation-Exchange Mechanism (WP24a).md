---
author: marici.Figueiredo
---

# 1954 — The Realizable Level Sets: 699 Singletons, Two Class-Locked Pairing Patterns, and the Generation-Exchange Mechanism (WP24a)

Date: 2026-08-23
Author: marici.Figueiredo
Status: established as stated, at the demonstrated (numerical
certificate) strength; the exact refit verification of the exchange
map is open (WP24b)
Supersedes: nothing. Continues 1937 (WP20) and 1947 (WP21); uses the
1950 classification.

## 1. Question

1947 located the π/8 question in the realizable level sets of the
reduced form r = a₁/(D_uD_d): which r values admit viable fits, and
with what multiplicity per texture?

## 2. The level-set structure (certified on all 1210 viable minima)

- **699 of 755 textures are singletons**: all their viable minima
  land in one folded-phase cluster.
- **56 textures span exactly two clusters**, in only two patterns:
  (1,3) — 27 textures — and (0,4) — 29 textures. No other span
  exists.
- The patterns are **class-locked**: every (1,3) texture is diagonal
  class; every (0,4) texture is 4cycle_trivial (14) or
  4cycle_leafcol_diff (15).
- Cluster 2 (46.91°) is exclusively 4cycle_trivial singletons (190
  textures, one rigid level); cluster 1 (43.17°) is exclusively
  diagonal (27 paired + 15 singleton).

## 3. The paired minima are the same physical point

For all 56 pairs: |Δχ²| ≤ 4.3e-12 and |ΔJ|/J ≤ 1.7e-8. The two
minima fit the same observables with the same quality — they are one
physical point realized in two charts.

The log-magnitude transformation is uniform across each pattern:

- (1,3), all 27: the first two u-magnitude entries swap values
  (Δ = ±6.218726), three d entries shift by ∓2.076289, the rest
  adjust sub-dominantly. The swap exchanges the two off-diagonal
  u magnitudes of the permutation support — i.e. exchanges which
  Q-rows carry which up-type eigenvalues: **generation exchange**.
- (0,4), all 29: dominant shift −6.218726, no swap.

The recurring constants are physical log-ratios (identical across
textures because the fit pins the same masses), supporting the
reading: one physical point, two generation assignments, different
chart phase φ, same J.

sin²φ pair sums are tight but NOT constant ((1,3): 1.3441 ± 0.0032;
(0,4): 1.1438 ± 0.0074) — there is no exact complementarity law
φ′ = π/2 − φ; the d-sector refit is not a symmetry of the
functional, only of its viable locus.

## 4. Consequence

1937's "extra valleys are the same valleys" now has an explicit
mechanism at the texture level: a realizable r-spectrum has at most
two points, and the second point is the generation-exchange image of
the first (diagonal class) or its shift-image (4cycle classes). This
is further evidence that φ is chart data: the same physical point
carries two different folded phases, and the pairings respect the
1950 classification.

**Open residual:** what selects singleton vs paired among textures of
the same class (diagonal: 15 singleton-1, 30 singleton-3, 27 paired)?
Not yet characterized.

## 5. Durable verification

- Checker: `research/flavor/checkers/wp24a_level_set_structure.py`
- Certificate: `research/flavor/results/wp24a_level_set_structure.json`
  (span counts, cross-tabs, pair transformation signatures,
  max_pair_dchi2 4.3e-12, max_pair_dJ_rel 1.7e-8)
- Commit: 639e4ac2 (pushed)
- Sequence claim: seqclaim-d20ee8c02ee542eb012e9b7e (value 1954)
- Epistemic event: ev-000000002454
