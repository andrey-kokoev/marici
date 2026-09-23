# Allocation checkpoints now declare their continuation capabilities

## Delivered boundary

A wrapper around the owning moment-column checkpoint now distinguishes three contracts:

1. Replay the already checked current allocation.
2. Answer a new query or refine the public history using fresh source/pricing verification.
3. Restore an actual fine history through a separately admitted authority.

Detaching the source backend preserves the first capability and refuses the other two. It does not promote the retained columns to a complete interface.

Seven refusal controls pass. A separate source-aware verifier replays both a feasible allocation and an infeasible local allocation, verifies a changed-objective query, and checks the six-exposure obstruction. The owning active-cap moment-master regression also passes.

## Admission and retained allocation

Bootstrap delegates to Grothendieck's full moment-master verifier and exact compaction verifier. A public-frame advance likewise requires the expected predecessor and frame, complete source/pricing proof and valid compaction.

The wrapper retains an immutable allocation capsule containing the complete expected state, compacted source columns and weights, checked status, source-rule identifier, original proof digest and reconstructed allocation. It does not accept imported serialized checkpoint claims.

Allocation replay recomputes per-block mass, weighted raw endpoints and globally weighted moments. For an OPTIMUM checkpoint it also reconstructs the glued raw source, verifies shared endpoint agreement, checks retained frames and computes the objective. This describes the current certified allocation; it does not claim identity with every hidden coordinate of the pre-compaction witness or with an actual observed source.

For an INCONSISTENT checkpoint, replay returns local convex allocations only. No global source lift, feasible public allocation or attained objective is supplied. Those Phase-I mixtures need not glue or satisfy the requested history.

## Detachment is an explicit capability transition

Detachment removes the wrapper's backend verifier session, backend handle and local pricing caches, and issues a fresh live handle. The capsule remains unchanged.

The test replaces the source verification, pricing verification, source-graph construction and source-admission entrypoints with traps. Saved allocation replay still succeeds. Attempts to submit a new query or public refinement fail before any trapped entrypoint can run, even when the supplied query proof was valid while the backend was attached.

The positive control changes the objective and runs full source/pricing verification before detachment. It does not answer by optimizing over the saved column dictionary and does not overwrite the original saved allocation.

Old handles, serialized cache claims and caller mutations of returned receipts cannot enable detached capabilities. There is no in-place backend reattachment; a caller needing a new source-aware session must obtain a fresh checked bootstrap.

Detachment here means LOGICAL BACKEND ACCESS IS DISABLED. The source rule is fixed mathematical code and the expected state still names its intervals, chart and observer. This is not cryptographic deletion, proof that the source cannot be reconstructed, or a claim that external source code and archives vanished.

## Five saved columns do not supply complete support access

The workload freshly verifies the six uniquely exposed points from the owning four-atom block. For each point it checks original source admission, the network support certificate, objective pullback and the signed increment objective.

Every increment coefficient is nonzero and chooses one endpoint of its interval. Each point is therefore the unique maximizer of its exposing functional on the increment box. Since that point satisfies the original caps, it remains the unique maximizer on the capped source subset.

Any convex mixture of admitted source columns attaining such a unique maximum must use only that maximizing source point. Six distinct unique maximizers therefore cannot all be represented by any fixed dictionary of five source columns.

For the explicit dictionary consisting of the first five exposed points, the sixth objective has

    retained-dictionary support = 19,
    verified full-source support = 20.

This is a bare-block completeness obstruction, not a claim that every restricted domain needs six columns, or that five columns cannot preserve a chosen allocation. It is also not a lower bound for affine section formulas or other interface representations.

## History authority remains separate

The wrapper refuses fine restoration from saved columns, an archive-shaped list of candidate histories, or a self-declared owner. Its source columns are mathematical witnesses, not actual-history selectors.

The event-bound restoration adapters in the parallel lanes solve a different problem: an owning authority identifies the original fine history and a verifier checks its refined successor. This allocation wrapper does not install that authority protocol or infer an event association from a pricing checkpoint.

Thus detached replay is not archival re-exposure, and source/pricing access is not original-history provenance.

## Verification and costs

`verify_allocation_continuation_checkpoint.py` imports no continuation-session implementation. It uses the owning arithmetic verifier to replay the full source proofs, compaction, reconstructed allocations, changed-objective query and six exposure certificates.

That offline replay deliberately HAS source access. It does not grant source access to the detached live session. The live refusal behavior and absence of source calls are separately tested in process.

Receipts charge the allocation capsule and attached checkpoint payload separately; the latter becomes zero after detachment. While attached, the two serialized objects duplicate some state and columns. Their byte counts are not distinct information-theoretic quantities or a complete Python heap ledger.

Saved complete transcripts, comparison runs and shared source code remain separately retained and charged. No bound on future regeneration, cumulative work or rational coefficient growth follows from the five-column allocation bound.

## Reproduction

    python research/nima/checkers/check_allocation_continuation_checkpoint.py
    python research/nima/checkers/verify_allocation_continuation_checkpoint.py

Implementation: `research/nima/checkers/allocation_continuation_checkpoint.py`.

Artifacts: `research/nima/results/allocation-continuation-checkpoint*.json`.

Owning allocation contract: `research/grothendieck/bounded-moment-column-checkpoints-preserve-allocations-not-whole-interfaces.md`.

Parallel authority contract: `research/voevodsky/archive-authority-now-publishes-an-actual-fine-refined-successor.md`.
