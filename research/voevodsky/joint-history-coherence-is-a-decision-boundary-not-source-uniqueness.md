# Joint-history coherence is a decision boundary, not source uniqueness

## Conjecture and test contract

A deadline-local observer can select a guaranteed sound action precisely when its nonempty joint source-history evidence fiber has a common allowed action. This is a finite information-theoretic statement with unrestricted computation and an explicit finite action set, not a claim about efficient reconstruction or distributed execution.

For each actual run there is one generating source/history. Alternative worlds represent uncertainty about that run, not multiple independent generating sources. Allowed actions are stipulated by the fixture task.

The common-action criterion itself follows from definitions: an action is sound for the transcript exactly when it is allowed in every world producing that transcript. The falsification targets are shortcuts that discard correlations, fabricate joint histories, or use evidence unavailable at the deadline.

## Exact adversarial fixtures

1. **Lost correlation.** Admitted source/history worlds give readings (0,0) and (1,1). Both allow only `hold`. Source reconstruction is nonunique but the decision is sufficient. Replacing the joint set by the Cartesian product adds (0,1) and (1,0); an ambient action table assigns those `switch`. The relaxed model now has no common action. This is false pessimism, not an actual obstruction.

2. **Invented coherence.** Take A's 0 record from the first history and B's 1 record from the second. Each value passes marginal admission, but no admitted history produces their pair. The naive ambient rule returns `switch`; the correct joint admission test rejects the packet. An empty fiber must not certify an action by vacuous universal quantification. This adversarial packet is intentionally not a valid single-source run.

3. **Unavailable evidence.** Two admitted worlds have readings (0,0) and (0,1), requiring `hold` and `switch` respectively. A must act at time 1; B's record reaches A at time 2. Global joint readings distinguish the worlds, but A's deadline transcript is identical in both. Exhausting the two deterministic actions proves that neither is guaranteed sound. Once the message arrives, the local fiber is a singleton and the correct action is available.

The third fixture assumes a stipulated reliable delivery time; it does not derive a physical latency bound. A periodic clock without an additional information channel cannot distinguish the identical transcripts.

## Result and limitations

All three shortcut claims fail on exact finite fixtures. Nonunique sources can permit a common action; compatible marginals need not form an admitted history; global decision sufficiency need not be deadline-local sufficiency.

No source-uniqueness requirement or physical tact quantum follows. The remaining substantial gates are faithful construction of joint-history fibers, source lineage, efficient representation, real delivery bounds, and execution constraints when multiple actors must act together. These fixtures do not integrate the existing theta or adelic pipelines and do not claim to validate them.

## Reproduction

    python research/voevodsky/checkers/check_joint_history_decision_boundary.py

Artifact: `results/joint-history-decision-boundary.json`.
