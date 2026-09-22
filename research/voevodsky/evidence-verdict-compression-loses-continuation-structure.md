# Evidence verdict compression loses continuation structure

## Exact conditional result

Using the four archived primitive boxes P, A, B, AB from Nima's incomparable-branch test, reconstruct the gain bounds and replay every status with the exact source-task engine. Continuations are merge with the archived A or B package. No new analytical intervals are fabricated.

P and A have identical current status UNRESOLVED. Apply the same B continuation:

    P meet B = B   -> UNRESOLVED
    A meet B = AB  -> CERTIFIED_INFEASIBLE.

Thus compression to the current verdict is not a continuation congruence on these evidence states.

## Minimal continuation distinction in the closed family

For each state, record the statuses after the empty continuation, A, and B:

| State | empty | A | B |
| --- | --- | --- | --- |
| P | unresolved | unresolved | unresolved |
| A | unresolved | unresolved | infeasible |
| B | unresolved | infeasible | unresolved |
| AB | infeasible | infeasible | infeasible |

All four signatures differ. Any deterministic state compression preserving all these continuation outputs must distinguish all four states. This is a four-state lower bound in this closed family, not a universal bit bound or a sufficiency claim for arbitrary new evidence.

## Scalar gain projection is a different question

The four exact scalar gain intervals are distinct. Consequently this test supplies no equal-scalar-image witness against existence of some induced continuation operation on these four images.

The specified scalar intersection operation does fail to commute with primitive merge followed by gain recomputation. Its result remains unresolved where the primitive merge resolves. This is an obstruction to that particular merge implementation, not proof that every possible scalar-state implementation fails.

## Admission failure retained

Fresh execution of Nima's independent replay fails its frozen input-hash gate: `signed-pairing-task-refinement.json` differs from the recorded contract. The original contract and artifacts were not rewritten.

The new checker verifies the archived contract/report binding, reconstructs exact gains and task results from its recorded primitive boxes, and records the changed owning-evidence digest. The mathematical continuation counterexample is therefore conditional on admission of those archived boxes. Fresh source-backed corroboration remains blocked until the owning evidence lineage is reconciled or the expected artifact is restored.

## Reproduction

    python research/voevodsky/checkers/check_evidence_compression_continuation.py

Artifact: `results/evidence-compression-continuation.json`.
