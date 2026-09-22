# Incremental observer refinement requires retained lift provenance

## Frozen finite construction

Use the freshly rebound and independently replayed four-state primitive-evidence family P,A,B,AB. First minimize its bound output behavior with only merge A enabled. Then enable merge B and recompute the continuation quotient.

The old partition is {P,A}, {B}, {AB}; the new partition is {P}, {A}, {B}, {AB}. States B and AB are retained in the full comparison carrier as possible initial evidence; starting from P with only A enabled reaches just P and A, both in the same old class.

The refined-to-old projection is explicit and commutes with the old merge-A transition. Thus structural refinement preserves every old behavior.

## Live-state obstruction

The old state identifies P with A. After enabling B, their successors have different outputs:

    P merge B = B  -> UNRESOLVED
    A merge B = AB -> CERTIFIED_INFEASIBLE.

A function receiving only the old compressed state cannot recover both possible actual refined states. Choosing a representative supplies an arbitrary section, not a faithful lift of the live state. This is an exact information obstruction, independent of computation time.

## Constructive lift with retained provenance

From a known P ancestor and a complete journal of accepted proof frames, replay reconstructs the primitive state. Each frame must match the declared bound frame and pass its envelope digest. The owning branch verifier is freshly run before this test, so its primitive evidence and implication checks back the recognized frame set.

The checker verifies the empty journal and one through eight copies of A. Duplicate A frames leave the evidence unchanged. Replay recovers P from the empty journal and A from every nonempty tested journal, then applies B correctly. A modified status is rejected even after recomputing the envelope digest.

For this split, a faithfully maintained accepted-A flag plus access to its validated bound evidence can carry the needed distinction; an entire unbounded journal is not a demonstrated necessity. The test implements journal replay because its provenance is explicit.

## Completeness boundary

Removing A from the journal makes it indistinguishable from a legitimately empty journal when only the old compressed state remains. Envelope integrity does not establish journal completeness. The successful lift assumes a known ancestor and faithful retention of accepted evidence. It does not supply an authenticated storage or crash-recovery protocol.

## DPC disposition

The constructive observer refinement exists and its projection preserves old transitions. The lift of a live state succeeds with distinguishing retained provenance. An unconditional live upgrade from the old minimal observer state is refuted.

Consequently preservation of transformation potential across enlargement of the continuation language requires a recoverable lift to future refined states. Minimality for today's continuations can erase exactly the distinction tomorrow's extension needs.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/check_incremental_continuation_refinement.py

Artifact: `results/continuation-quotient/incremental-continuation-refinement.json`.
