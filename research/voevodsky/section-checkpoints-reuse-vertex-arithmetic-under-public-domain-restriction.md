# Section checkpoints reuse vertex arithmetic under public-domain restriction

## Delivered adapter and explicit limits

A process-local section verifier now follows Nima's verifier-owned checkpoint pattern for the fixed owning square-section contract. It is a separate adapter, NOT a new language accepted by Nima's service and NOT an integrated migration issuer. It does not issue archive capabilities, optimize public queries or claim a generic triangulation verifier.

The previously independently verified square section supplies the test proof. Bootstrap checks the complete fixed source/evidence contract and every selected source vertex. Expected state is supplied separately from candidate packets. The adapter has no checkpoint import API; each session starts by full replay.

## What is reusable

A checked vertex result is keyed by rule epoch, fixed source contract, capability policy, complete fine rows, public vertex and actual source lift. A changed lift cannot reuse its predecessor's arithmetic. The trusted cache contains only entries admitted in the session. Inputs and retained state/proof are serialized snapshots; mutating caller state, proof or receipts cannot change the checkpoint.

Public refinement does not alter these source/fine obligations: the section remains valid on its original domain. Thus successful public restriction reuses all four checked vertex results.

## What must still be checked

Every transition checks the current opaque handle, independently expected predecessor and append operation, exact expected successor, frame dimension and rational syntax, capability policy, full fixed triangulation and shared vertex array, and fine evidence rows. A failed transition does not publish a new head. Calls are lock-serialized; concurrency itself is not exercised in this workload.

The coverage certificate is deliberately simple and complete: the original two triangles cover the square, so restricting their union by any appended public halfspaces covers the restricted domain. Their shared-face equality is inherited from the shared vertex array. No new clipped triangulation or geometric vertex enumeration is needed. The fresh cover counter denotes one execution of this fixed topology/schema obligation, not a general-purpose coverage algorithm or an LP count.

The same argument handles an empty restricted domain without trusting a candidate's emptiness claim. Lift requests check the exact accumulated public frames before interpolation. No separate feasibility claim is issued for the restricted domain.

## Capability boundary

A selected section authorizes returning its admitted source lift at an allowed public point. It does not authorize fine re-exposure: archive requests always fail in this adapter. Hidden fine refinements and archive-bit escalation are rejected. This is application policy in a trusted process, not confidentiality of retained section data or a boundary against code that can modify verifier memory.

## Results and accounting

Three public transitions include a cut crossing both cells, a second restriction, and an impossible restriction. Checkpoint and full replay use the same exact arithmetic kernel:

- bootstrap: four local arithmetic checks;
- successors: zero new local checks and twelve verifier-owned hits;
- full successor replay: twelve local checks;
- fresh fixed-cover checks: one per successor;
- twenty-seven refused invalid operations.

Controls include altered vertex lifts, missing coverage cells, false predecessors, foreign/stale handles, nonpublic operations, capability escalation, excluded/empty-domain lifts and attempted archive requests. Initial caller/receipt/proof mutation isolation is also exercised. The independent original section verifier was freshly rerun after the adapter workload.

The artifact separately reports live state encoding, full section encoding, checkpoint encoding, archive bytes (zero), local hash bytes and arithmetic/check counters. Checkpoint size includes its retained state and proof, so these byte categories overlap; they must NOT simply be summed as disjoint resident allocations. There is no migration-proof byte charge because this adapter does not perform migration verification. Serialized size is not Python heap size, and call counts are not elapsed time or bit complexity.

## Next integration boundary

This establishes the local reuse rule for public restriction. A real end-to-end retirement service must still connect migration-verifier authority to bootstrap and explicitly manage answer-only, lift and archive policies across the owning APIs. A section checkpoint must not substitute its fixed contract for an independently expected arbitrary migration. The current adapter makes that remaining boundary explicit rather than claiming the entire lifecycle is delivered.

## Reproduction

    python research/voevodsky/checkers/check_section_checkpoint.py
    python research/voevodsky/checkers/verify_polyhedral_common_section.py

Implementation: `checkers/section_checkpoint.py`.

Artifact: `results/section-checkpoint.json`.
