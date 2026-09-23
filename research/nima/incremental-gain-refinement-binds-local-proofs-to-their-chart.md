# Incremental gain refinement binds local proofs to their chart

## Delivered integration

The balanced-gain adapter now supports archive-backed append-only updates with chart-sensitive block-proof reuse. Seven transitions independently match fresh compilation, and ten raw audit answers verify. Nine stale-chart, dependency, operation, policy and threshold mutations are rejected.

This extends the persistent difference interface's cache contract; it does not introduce another solver or weaken chart admission.

## Update contract

`GainHistory.refine_block(index, row)` appends a positive-gain row to a declared raw-atom block. `refine_public(row)` appends a gain row between currently public raw atoms to the exterior relation. Both operations require an archive-backed state.

The old snapshot remains unchanged. The new raw evidence remains retained even if the gain chart becomes unsupported. No earlier row is deleted to restore balance.

Every update reruns exact global chart admission. The implementation does not yet maintain the chart graph incrementally. A balanced chart uses the existing canonical convention: the minimum positive scale in each connected component is one.

## Cache dependency

A local closure proof is reusable only when all of these agree:

    source rule and binding, m,
    complete raw block and boundary,
    scales on every node of that block,
    complete normalized block.

The global normalized-state binding changes whenever raw history changes. That alone does not invalidate an unchanged mathematical block proof: local reuse is checked against the explicit dependencies above, and the resulting global certificate is bound to the new complete state.

Conversely, unchanged raw block evidence is not sufficient for reuse. Joining two gain components can reconcile their scales by rescaling a whole old component. Its normalized source caps and offsets then change, so its cached distances no longer address the new normalized problem.

All changed dependencies trigger block-closure recomputation. The composed interface is re-closed afterward. The independent verifier reconstructs both expected raw states, verifies both charts and normalized certificates, and checks every declared cache hit against those local dependencies.

## Decisive component-join control

Initially the two gain components have canonical scale patterns

    (1,2,1) and (1,3,1).

A chart-compatible row inside the first block leaves the second block's proof reusable, despite the changed global history binding.

A subsequent row joining the components imposes a relative scale of 1/2. Canonical normalization changes the first component to (2,4,2), while the second remains (1,3,1). Nodes 1,2,3 change scale. Both block closures must now be recomputed, including the first block whose raw evidence was untouched by this update.

A separate public-endpoint join exercises the same dependency issue for an exterior row: changed chart scales can invalidate local proofs even when no block receives new raw evidence.

## Unsupported charts versus contradictions

An appended incompatible gain cycle produces a verified UNBALANCED_CHART rejection. The state and complete raw evidence are retained, but the adapter refuses raw audit queries with `NotImplementedError` rather than returning a mathematical ambiguity or inconsistency status.

The workload includes two successive unsupported states with checked feasible raw zero witnesses. These are genuinely nonempty carriers that the chosen representation cannot normalize. Appending another row does not remove the offending gain cycle.

A different update preserves the chart but creates a cross-block negative cycle. Both local blocks remain consistent; their composed interface is inconsistent. Its original-row cycle expansion verifies, and raw threshold requests return INCONSISTENT. Further compatible evidence preserves that inconsistency.

Chart rejection and negative-cycle emptiness therefore remain separate branches with different proofs.

## Raw query and retention semantics

`GainHistory.audit(node, threshold)` uses the current checked scales and composed distance summary. Thresholds remain in raw atom coordinates. No previous normalized bound is reinterpreted under a new chart.

The producer compares these incremental answers with fresh raw-state compilation. The independent verifier derives the bounds from the current certified chart and summary, and rejects a mutation that scales the caller's raw threshold.

This gain-refinement adapter is archive-backed only. Public-only construction is refused; hidden-endpoint public updates and nonpositive gains are rejected. The earlier public-only difference-history interface remains available for its declared language. No new gain-update capability is inferred merely from possession of a coarse summary.

## Separate work accounts

Across seven updates:

- global chart admission runs seven times;
- five chart-admitted updates recompute seven local closures and reuse three;
- two unbalanced updates produce no normalized closure;
- interface closure reruns for each chart-admitted update;
- arithmetic verification replays the complete predecessor and successor proofs.

These are workload counts, excluding initialization and fresh comparison runs. They are not an incremental-verification or total runtime bound. Full raw evidence, charts, normalized rows, local proofs and saved snapshots remain retained information. No source values or conditioning budgets become cheaper merely because a proof is reusable.

## Reproduction

    python research/nima/checkers/check_incremental_gain_interfaces.py
    python research/nima/checkers/verify_incremental_gain_interfaces.py

Implementation: `research/nima/checkers/incremental_gain_interfaces.py`.

Artifacts: `research/nima/results/incremental-gain*`.

The difference-refinement and balanced-gain-adapter verifiers also pass unchanged. This is a separate research adapter, not a general LP fallback, observation-authentication service, archive-compression theorem or fresh upstream source-admission proof.
