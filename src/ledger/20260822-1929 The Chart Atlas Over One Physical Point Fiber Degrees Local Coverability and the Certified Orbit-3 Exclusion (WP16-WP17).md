---
author: marici.Figueiredo
---

# 1929 — The Chart Atlas Over One Physical Point: Fiber Degrees, Local Coverability, and the Certified Orbit-3 Exclusion (WP16/WP17)

## Question

After WP11-WP13 established that the loop phase is chart data and WP15
reproduced the paper's ensembles, two structural questions about the
sparse-texture atlas remained:

1. (WP16) What does the chart map's fiber over ONE physical flavor point
   look like — how many chart classes reach it, with how many
   preimages, and does the atlas cover a neighborhood of it?
2. (WP17) Is the WP15 nonviability of orbit 3 (the one nonviable orbit
   not explained by the WP13 structural J == 0 classes) a fitting
   artifact, or a certified exclusion — the chart's attainable image
   genuinely missing the physical region?

## Method

The physical coordinate.  physical10 = (6 quark singular values,
|Vus|, |Vub|, |Vcb|, signed Jarlskog J).  Dimension count
36 - 27 + 1 = 10 says this is generically a COMPLETE coordinate on the
physical quotient {(Yu,Yd)}/U(3)^3: two parameter sets with the same
physical10 are the same physical point.  Every fiber statement below is
therefore a statement about physical points, not about the 10-observable
subset being incomplete — closing the refinement Benincasa asked for
after WP6.

The point.  p* = exact physical10 image of the global-best WP15b fit
(orbit 15, member (281,395), chi2 = 3.3628 vs the 20.28 cut).

WP16a/b.  Exact inverse solves: for each of the 36 S3^3-orbit halves,
randomized Levenberg-Marquardt on the 10-residual system (10 chart
parameters), accepting roots at max relative residual < 1e-7, clustered
at 1e-4.  100 starts/rep in the atlas pass, 1500 in the stabilization
pass, 2000 on the seed member.  Checkers `wp16a_fiber_degree.py`,
`wp16b_atlas_fiber.py`, `wp16b_fiber_stability.py`.

WP16c.  Numerical Jacobian (central differences) of the chart map at
every distinct root found: full rank (10) at a preimage implies, by the
inverse function theorem, that the chart covers an open patch of the
physical quotient around p*.  Checker `wp16c_local_coverability.py`.

WP17.  Two independent methods.  (i) Empirical: the same exact inverse
solve for both sector halves of orbit 3, 2000 starts each, with
overflow-robust residuals.  Checker `wp17_orbit3_exclusion.py`.
(ii) Certified: WP10's closed symbolic criterion — a Hermitian Gram
matrix H = (diag A,B,C; off-diagonal squares p,q,r) admits a
zero-diagonal square root iff A B > p and
C(AB - p) >= rA + qB + 2 sqrt(p q r), with the convexity/minimum proof
in `wp10_orbit3_gram_criterion.py` — evaluated at 60-digit precision on
the exact Gram data of p*: H = V Dd V^dagger for the Yu-monomial half,
H = V^dagger Du V for the swapped half, each under all 6 row labelings.
Checker `wp17b_gram_criterion_at_pstar.py`.

## Results

WP16b (stabilized).  21 of 36 orbit halves carry an exact preimage of
p*; 67 distinct preimages at 1500-start density; per-chart degrees 1-7.
Degrees are rigorous lower bounds — orbit 0 grew 4 -> 7 between 100 and
1500 starts, so exact degrees need polynomial homotopy certification
(not installed).  The WP16a pilot's "degree 1" on the seed member was a
sampling undercount: the orbit-15 canonical representative (85,234)
verifiably carries TWO exact preimages with DIFFERENT loop phases,
phi = -pi/2 and phi = -0.901817, both with sane hierarchical
magnitudes, residuals < 1e-9.  Same complete physical invariant data,
different loop phase — the strongest falsifier form: the loop phase
varies along the fiber over one physical point.

WP16c.  Every preimage root found (44 in the main pass + 2 in the
supplemental orbit-15-swapped rerun) has chart-map Jacobian rank 10.
21/21 covering chart classes have at least one full-rank preimage:
every covering chart is a local diffeomorphism onto a neighborhood of
p*, and the atlas covers an open neighborhood of the physical point.

WP17.  Certified: at p* the realizability criterion FAILS for all 6 row
labelings in both sector halves — minimum relative gaps 3.07 (down
side, H = V Dd V^dagger) and 442.7 (up side, H = V^dagger Du V).
Empirical: 0 exact preimages in 2000 starts per half (best relative
residuals 0.56 and 0.99).  The WP15 failure channel (|Vub| stuck at
4.6e-5 vs 3.76e-3, beta at 0.28 deg vs 22.6 deg) is a genuine boundary
of the chart's attainable image, not a fitting artifact.

## Interpretation

Candidate A (the sparse texture groupoid) is a genuine multi-chart
atlas for Candidate B (the physical U(3)^3 quotient) LOCALLY around the
physical point: 21/36 chart classes reach it, every reaching chart is
regular there, and the charts overlap on open patches.  The fibers are
nontrivial — up to 7 preimages per chart found, including distinct loop
phases within one chart class — which is the fiber-level mechanism
behind the WP11-WP13 verdict: the loop holonomy is an internal lens
coordinate, not physical readout.  The admission criterion for flavor
as a fourth Marici sector remains unmet: no component of the loop
data descends to the quotient.  What survives is a precise statement
of the atlas/quotient relation itself.

## Limits

- Fiber degrees are lower bounds (LM sampling); certification needs
  homotopy continuation.
- Coverability is local: shown for a neighborhood of p* only.  The 15
  non-covering orbit halves at p* may cover elsewhere.
- The WP17 certification excludes the exact point p* (and WP10 already
  excluded the full 3-sigma box); it does not parameterize the orbit-3
  image boundary away from the physical region.

## Artifacts

- `research/flavor/checkers/wp16a_fiber_degree.py`,
  `wp16b_atlas_fiber.py`, `wp16b_fiber_stability.py`,
  `wp16c_local_coverability.py`, `wp17_orbit3_exclusion.py`,
  `wp17b_gram_criterion_at_pstar.py`
- `research/flavor/results/wp16a_fiber_degree_pilot.json`,
  `wp16b_atlas_fiber.json`, `wp16b_fiber_stability.json`,
  `wp16c_local_coverability.json`, `wp17_orbit3_exclusion.json`,
  `wp17b_gram_criterion_at_pstar.json`
