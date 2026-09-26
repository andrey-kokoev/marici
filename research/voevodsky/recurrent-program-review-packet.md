# Review packet: finite mixed recurrent interaction-net programme

Review status: prepared, not independently reviewed or formally certified. No reviewer is assigned by this document. Graph admission records coordination, not mathematical truth.

## Entry points and reproduction

Read `mixed-recurrent-program-theorem.md`, then `reachable-concurrency-confluence.md` and `schedule-observation-contract.md`. Supported client surface: `checkers/program_runtime.py` (observe/advance); input normalization: `program_inputs.py`; estimates: `program_preflight.py`. Raw net classes are experimental internals.

Run `python research/voevodsky/checkers/check_recurrent_program_closure.py` with assertions enabled. Latest recorded closure contains19 passing fresh subprocess suites in `results/recurrent-program-closure.json`, with local Python hashes. It does not identify all environment dependencies or hash Markdown claims. Mutation sensitivity is separately reproducible with `check_closure_mutations.py` and is not silently included in the19-suite count.

## Claim-to-evidence map

| Claim | Written argument | Implementation / executable evidence | Remaining review question |
|---|---|---|---|
| Linear local replacement | cut-interface proofs and signature audit | retained_membership.replace; check_combined_signature.py, check_strict_return_interfaces.py | Does immutable boundary substitution reproduce every production mutation, including internal auxiliary links? |
| Query DONE includes full retained copy and erasure | query-acknowledgment-subsumes-single-copy-completion.md | acknowledged_membership.py; gate projection and completion tests | Check the NIL provenance argument for every QR/QS terminal case. |
| Strict add/union completion | strict-mixed-program-theorem.md | strict_set_program.py; strict mixed tests | Check complete-input suffix premise and terminal splice distinctness. |
| Conditional branch cleanup | conditional-insertion-completion-contract.md | conditional_insertion.py; conditional/successor tests | Verify both acknowledgments are consumed, and rejected budget is fully erased. |
| Runtime bounded recurrence | fuel-scanner-phase-theorem.md | fuel_scanner.py, triple_cursor.py; scanner tests | Validate fuel-first semantics, preparation ownership and recurrence restoring the invariant. |
| Five-instruction composition | mixed-recurrent-program-theorem.md | scanning_set_program.py; mixed corpus | Prove placeholder compilation produces exactly the intended interfaces for arbitrary finite lists. |
| Schedule independence | reachable-concurrency-confluence.md | check_local_diamonds.py; check_concurrency_invariant.py | Independently check exhaustive phase classification and quotient equivariance, not just sampled diamonds. |
| Public observation timing | schedule-observation-contract.md | observe methods; all-schedule and prefix tests | Ensure pending/false/exhaustion are distinct, roots fixed, ACK only at completion. |
| Logical resource envelope | runtime-resource-envelope.md; constructor-resource-accounting.md | preflight; resource/constructor/admission tests | Review monotonic bounds and their exclusion of input materialization/heap costs. |

All executable checks are bounded or template-level. Many share the production reducer: agreement is not an independent semantics implementation. Local fresh-name bijections fix roots but are not a general cyclic-graph isomorphism engine.

## Minimal independently checkable kernel

Separate four layers; do not put the whole compiler into the trusted core:

1. A finite graph value: agent IDs with kind/port declarations; a fixed-point-free involution on all ports; distinguished passive public roots. Validate full port coverage and inverse wiring. No forest assumption.
2. A replacement certificate: two distinct live principal-paired agents, fresh typed agents, and a matching over exposed old slots plus fresh ports. Every slot occurs exactly once. Include a name-allocation witness; do not infer freshness from absence alone when imported serial state is possible.
3. A pure replacement evaluator: compute outside peers from the original graph, remove the selected agents/incident edges, insert fresh declarations and reconnect the certificate using that snapshot. Reject malformed certificates without modifying the input. Preserve all unaffected wires and roots. Compare against the current imperative replace only on its admitted domain.
4. Typed rule certificates: identify the unique rule and certify its template and freshness against the57-case table. Matching ports correctly does not prove the denotation of that rule; phase/operation proofs sit above this layer.

Small-kernel properties to check independently: totality on admitted certificates, output well-formedness, frame preservation, root preservation when roots are not selected, and equivariance under injective renaming. Nonsplice disjoint certificates should commute under allocation-slot bijections. General splice composition needs representability conditions, not just slot conservation.

The current imperative replace mutates before its final audit and may leave a partial state after an invalid certificate; the proposed pure evaluator would be an independent reference, not a retroactive guarantee of transactional runtime mutation. Do not silently broaden the theorem to malformed or imported graphs.

## Scope boundary

Finite literal union, fixed conditional insertion alternatives and the particular fuel-bounded scanner are supported. Arbitrary branch bodies, unrestricted loops, runtime multi-input sharing, concurrent host mutation, persisted allocator recovery and memory/time sandboxing are not. No encoding of Nima's superform problem has been established.

## Next concrete review-enabling artifact

Implement the pure immutable replacement evaluator and differential-check it against captured production certificates. Test both valid cyclic boundary contexts and malformed certificates with unchanged input snapshots. This directly addresses the smallest shared trust bottleneck; another schedule sample would not. Keep it separate from the production mutator until its specification and differences are reviewed.
