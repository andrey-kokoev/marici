# Incomparable analytical proof branches resolve by primitive-evidence merge

## Result

The two-branch DPC is **corroborated on this finite composition test**:

| Evidence | Frozen private middle task |
| --- | --- |
| Common projection272 ancestor | UNRESOLVED |
| A: improved theta masses/moments only | UNRESOLVED |
| B: improved signed pairing only | UNRESOLVED |
| Verified primitive-evidence merge | CERTIFIED_INFEASIBLE |

Both arrival orders give the same final evidence digest and decision. No common commit or acknowledgement is required by the stipulated independent local-decision policy.

This is retrospective composition of existing analytical certificates, not a blinded numerical discovery. The two proofs improve different coordinates of the same fixed analytical object; no statistical independence of their errors is assumed.

## Frozen task and fork

The detector, source family, raw observations and order-16 prior are the unchanged private middle-threshold task. The common ancestor supplies projection272 bounds for C, H, L, both theta masses X and both moments mu.

Branch A substitutes the certified theta-Taylor mass and moment intervals but keeps the old C interval. Branch B substitutes the certified signed fixed-hat C interval but keeps the old mass and moment intervals. H and L remain identical throughout.

Both branches refine their ancestor, but neither refines the other: A is strictly tighter on the theta coordinates and B is strictly tighter on C. They are incomparable as primitive-evidence packages, even if their projected scalar gain intervals happen to be nested.

The contract and input hashes were written before constructing the branch results. The first implementation attempt hit Python's integer-string serialization limit; only that limit was removed. A subsequent attempt was rejected because a referenced analytical artifact changed during execution. The successful run passed all frozen-hash checks. Neither failure led to a change in the task, branches or merge rule.

## Why the merge decides

The merge intersects matching primitive intervals and then recomputes

    E = 2 X_A X_B (C+H(mu_A-L))(C+H(mu_B-L)).

Positivity and monotonicity justify its exact rational endpoint bounds. Both owning proofs concern the same deployed detector and fixed analytical quantities, so the actual quantities satisfy both packages. Their joint use does not require independently attainable endpoint combinations.

The resulting gain upper bound lies below the task's feasibility threshold. The exact source-task replay certifies that even the necessary source cost exceeds the unchanged budget.

A useful negative control merely intersects the two branches' scalar gain intervals. That remains **UNRESOLVED**. The decision therefore genuinely uses retained primitive information lost in the separate scalar projections; it is not a version-label or arrival-order trick.

An empty primitive intersection is handled as EVIDENCE_CONSISTENCY_FAILURE. It is not converted into source-task infeasibility. The empty-intersection control uses synthetic conflicting boxes to test rejection; it does not claim two sound analytical proofs can contradict one another about the same fixed quantity.

## Local admission and arrival order

Each branch frame binds the exact task, common parent, owning evidence hash, primitive bounds, claimed task status and necessary cost. The receiver verifies the frame against the declared branch and independently replays the source-task implication. Modified task, parent, status and cost fields are rejected even after recomputing the envelope digest.

In each stipulated reliable-message schedule, one branch arrives at logical time two and the other at four. The first leaves the task unresolved; the second permits the merged certificate by deadline five. Reversing arrival order changes neither the final primitive package nor the answer.

Duplicates and late ancestor evidence cannot discard retained constraints: merging them again leaves the accepted joint package unchanged. There is no arbitrary total ordering of branch labels.

This is closed admission over two named branches, not a general proof checker for arbitrary submitted analysis. Hash binding is not authentication and does not itself establish analytical truth.

## Timing and scope

The 30-second budget covers finite local branch construction, validation and task replay using analytical certificates already available initially. The successful run took approximately 0.15 seconds. It does not include generating the theta or signed-pairing certificates.

Message times and atomic validation events are stipulated logical assumptions, not measured physical delivery guarantees. Host computation time is not silently translated into those logical times. The result is therefore a finite conditional availability test, not a claim about network consensus, irreversible simultaneous action or arbitrary deadlines.

The analytical validity of the supplied primitive bounds remains supported by the owning theta and signed-pairing proofs. Our checks establish their task-specific composition and the exact decision implications.

## Reproduction

    python research/nima/checkers/check_incomparable_proof_branch_merge.py
    python research/nima/checkers/verify_incomparable_proof_branch_merge.py

Artifacts:

- `research/nima/results/incomparable-proof-branch-contract.json`
- `research/nima/results/incomparable-proof-branch-merge.json`
- `research/nima/results/incomparable-proof-branch-verification.json`

The independent replay reconstructs both branches from their owning artifacts, checks incomparability and the primitive intersection, recomputes every gain and task result, and checks both arrival schedules. It passes.

## What this corroborates

Complementary, correctly anchored analytical certificates can resolve a task that neither projected branch certificate resolves alone. Confluence comes from retaining and intersecting the actual primitive constraints—not from declaring one branch newer, trusting a verdict, or imposing a common commit.

This does not revive the failed fixed-method midpoint DPC. It concerns a different frozen task and a different evidence contract, and those ledger entries remain distinct.
