# Verified checkpoints reuse local arithmetic without trusting cache claims

## Delivered gate

The difference and balanced-gain refinement lanes now share a verifier-owned checkpoint service. It reuses already checked local arithmetic, not merely already generated closure certificates.

Across eight plans and 22 transitions, checkpoint verification agrees with full replay. Successor verification performs 15 local arithmetic checks and reuses 25 checked results, versus 40 local checks for full successor replay. Twenty targeted attacks and 22 stale-handle replays are rejected.

## Checkpoint authority

`VerifierSession.bootstrap(language, expected_state, proof)` fully verifies an archive-backed initial state and issues an opaque, process-local handle. The expected state comes from the owning caller, not from the candidate packet as its own authority.

A checkpoint retains immutable encodings of the complete expected state, proof, checked result and local arithmetic results. Those encodings bind the source, full history, retention policy, boundaries, chart and proof identities.

`advance(handle, expected_before, expected_operation, candidate)` accepts only the current handle of that session. It reconstructs the expected successor through the existing append-operation verifier. A foreign handle, stale handle, mismatched predecessor or altered expected operation cannot select a different trusted history.

There is no checkpoint import API. A serialized digest or a candidate's assertion that a proof was previously checked is not authority to skip arithmetic. Forks and process restarts require a new full bootstrap. The service is a trusted in-process verifier, not a security boundary against code that can modify its memory or replace its functions.

## Local reuse rule

Each cached local result is bound to:

- the local verification-rule epoch and constraint language;
- source binding, atom count and retention policy;
- complete raw block, including its boundary and ordered evidence;
- the actual normalized nodes and edges presented to the arithmetic checker;
- every local chart scale for gain states;
- the exact local proof digest.

A hit requires both the dependency digest and proof digest to match the verifier's own previous checkpoint entry. A miss runs the existing exact path, triangle-completeness and source-edge checks. Cached distance matrices are stored as immutable rational encodings; a checked local negative cycle is represented by a bound empty result and is reusable under the same rule.

Global gain-chart admission still runs before normalized block reuse. A component join can therefore invalidate a cached block even if its raw evidence and old proof bytes have not changed.

## What still gets checked

The initial state is fully replayed. For every successor, the service checks:

- expected state and operation bindings;
- structural ownership and boundary constraints;
- gain-chart equations and normalization, or the unbalanced-cycle rejection;
- local dependencies and proof identities;
- changed local arithmetic;
- the complete composed interface proof;
- the public summary or the expanded original-edge negative cycle;
- the producer's reuse and recomputation declarations.

The predecessor arithmetic is not replayed: the session already owns its checked checkpoint. The old global proof is not reused as the new interface proof.

The existing full verifiers gained internal callback hooks to support this substitution. Their default entrypoints still run full replay. The comparison uses that full-replay path and the same established arithmetic kernel; it is not a claim of a second independently implemented solver.

## Atomic advancement and mutation controls

New checkpoints are published only after arithmetic and transition-envelope checks both succeed. A failed candidate cannot advance or poison the head. Session calls are serialized, so two concurrent updates using one handle produce one accepted successor and one stale-handle refusal.

Inputs are copied into immutable encodings. Mutating the caller's initial state, proof or returned receipt after bootstrap does not alter the trusted checkpoint. The tests exercise this isolation explicitly.

Targeted controls cover foreign handles, wrong predecessors, changed source bindings, altered boundaries and policy, modified reused proofs, false cache-hit declarations, corrupted interface proofs, stale chart proofs, changed scales and invalid negative-cycle expansions. A public-only checkpoint cannot acquire fine-update authority through this API.

## Work and storage accounts

For this workload:

| Account | Count |
|---|---:|
| Bootstrap local checks | 16 |
| Successor local checks | 15 |
| Successor local cache hits | 25 |
| Full successor replay local checks | 40 |
| Fresh successor interface checks | 18 |
| Fresh gain chart/rejection checks | 7 |
| Maximum encoded checkpoint size | 7,777 bytes |
| Successor local-proof bytes hashed | 22,532 bytes |

Four successors require no interface check: two have a checked local contradiction, and two have unsupported gain charts. Local negative-cycle reuse is tested explicitly, rather than inferred from consistent-matrix reuse.

These are kernel-call counts, not wall-clock or arithmetic-operation bounds. Proof hashing, full packet parsing, state copying, chart reconstruction, interface work and checkpoint storage remain charged. The local-proof hash-byte count does not include all envelope hashing or serialization. Encoded checkpoint size is the service's JSON representation size, not Python heap usage.

The service retains only its current head; externally saved histories and experiment packets are separate retained information. No evidence compression, cross-process attestation or upstream observation authentication is claimed.

## Reproduction

    python research/nima/checkers/check_checkpoint_verifier.py

Implementation: `research/nima/checkers/checkpoint_verifier.py`.

Results: `research/nima/results/checkpoint-verification.json`.

Bound input/source hashes and per-step work accounts: `research/nima/results/checkpoint-verification-trace.json`.

The modular difference, balanced-gain adapter, incremental difference and incremental gain verifier suites all pass with full replay unchanged as their default behavior.
