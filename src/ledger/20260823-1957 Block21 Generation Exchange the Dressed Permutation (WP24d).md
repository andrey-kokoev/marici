---
author: marici.Figueiredo
---
# 1957 - Block21 Generation Exchange: the Dressed Permutation

- Date: 2026-08-23
- Author: marici.Figueiredo
- Status: theorem-form statement, certified at stated precisions (164/164 same-point block21 pairs)
- Supersedes: extends 1955-1956 (WP24c/WP24b) from permutation-u diagonal textures to the 4-edge-u block21 class

## Scope

1955-1956 established that every permutation-u diagonal-class texture over
the best-fit point carries a 2-fold readout fiber whose deck involution is
light-generation exchange 1<->2, with Yu_2 = P01 Yu_1 P01 exact. WP24d tests
the block21 class (4-edge u-sectors), where the u zero-pattern cannot
support a bare permutation. Result: the exchange survives, but the
weak-basis map is a rotation-dressed permutation, not a bare one.

## The dressed-permutation exchange (29 cross-cluster (0,4) pairs)

For every same-physical-point block21 pair with d-phase-edge pattern (0,4)
(29/29 textures):

1. **Same physical point:** physical16 agreement <= 1.2e-8.
2. **u-side conjugation exact:** Hu_2 = Lu Hu_1 Lu^dagger with
   Lu = Uu_2 Uu_1^dagger (eigh-phase-free), max defect 1.0e-9.
3. **Lu is a universal dressed permutation:** |Lu - P01|_max = 0.038757 for
   every pair, and the Lu entries agree across all 29 pairs to spread
   2.4e-4. The dressing is a small rotation: |Lu_02|, |Lu_21| ~= 0.0094,
   |Lu_12|, |Lu_20| ~= 0.0388, |Lu_22| ~= 0.9992 (cos of the same angle).
   The dressing angle 0.038757 rad is physical-point data; an identity probe
   against elementary best-fit combinations (|Vcb|, |Vts|, |Vub|, |Vtd|,
   mass ratios and square roots) finds no clean match (closest: |Vts|,
   off by 2.3e-3). Recorded as unidentified, not as a CKM element.
4. **u-magnitude census:** only 4 value-set pairs across the 29 textures;
   the exchange redistributes magnitudes through the 2x2 block with exact
   product identities - Hu_00 = yc^2 (sheet 1) or yu^2 (sheet 2), and the
   2x2-block determinant factor bc = yu*yt (sheet 1) or yc*yt (sheet 2).
   Generation exchange is exact at the level of these products.
5. **d-side at fit precision:** |Hd_2| = |Lu Hd_1 Lu^dagger| holds to
   3.5e-6 and the D' spanning-tree phase solve closes to 4.0e-6 (both
   fit-precision level, not the 1.2e-12 of the diagonal class; the stored
   block21 minima are less converged). Given the Hd identity,
   Yd_2 = D' Lu Yd_1 W with W unitary follows algebraically exactly as in
   1956; the raw W-unitarity number (~13.7) is meaningless without yd^-2
   conditioning (4e9 amplification of the 3.5e-6 Hd defect) and is not
   claimed as evidence either way.

## The 135 within-cluster coincident pairs are the same mechanism

The remaining 135 same-point block21 sheet pairs (Delta-phi census
{0.0:32, 0.01:26, 0.03:22, 0.08:55} degrees) were candidates for being
near-duplicate minima rather than genuine sheets. The signature census
rules this out: 135/135 are exchange-like -

- the u-magnitude multisets of the two sheets differ in every case
  (log-magnitude redistribution up to max-diff >= 2.5, not refit noise);
- every Lu is far closer to P01 than to the identity
  (|Lu - P01| in [0.041, 0.44], median 0.053; |Lu - I| >= 1.0).

The dressing angle is pair-dependent for coincident pairs (unlike the
universal 0.0388 of the (0,4) class), and the near-zero Delta-phi reflects
near-equal chart loop phases of the two exchange sheets within one cluster,
not duplication. Sheet multiplicity per texture is therefore genuine fiber
multiplicity everywhere; coincident sheets do not inflate single-cluster
counts with artifacts.

## Combined statement (with 1955, 1956)

Over the best-fit point, every multi-minimum texture examined carries a
readout fiber of cardinality >= 2 whose deck involution is light-generation
exchange 1<->2: 72 permutation-u diagonal textures (bare P01, machine
precision) and 164 block21 same-point pairs (rotation-dressed P01, exact on
the u-side, fit precision on the d-side). The deck group acts by
weak-basis transformations, so the sheets are one physical flavor point in
two charts; the loop phase remains chart data (1956), and the dressed
rotation is the block21 avatar of the same exchange.

## Durable verification

- Checkers: research/flavor/checkers/wp24d_block21_exchange.py,
  research/flavor/checkers/wp24d_coincident_signature.py
- Results: research/flavor/results/wp24d_block21_exchange.json,
  research/flavor/results/wp24d_coincident_signature.json
- Sequence claim: seqclaim-0cd32c7091791d780fe6f576 (value 1957)

## Disclosure

MCP route: the loader binding remains unavailable (pre-existing session
fault, disclosed since WP21). The stdio disclosure client initially failed
today with proxy preflight refusal workspace_artifact_missing: the pinned
ledger-domain build d040aefe went stale when the mcp-surfaces workspace was
re-materialized to 68c9e7e7. The client now resolves the child entrypoint
from the workspace artifact manifest at call time; no build was run and no
mcp-surfaces state was mutated. Run-manifest discipline debt from WP23a/d
remains open for closeout disclosure.
