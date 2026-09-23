# Owning migrations now bootstrap point-witness checkpoints

## Delivered connection

`migration_checkpoint.Session` now gates process-local retirement authority on the existing independent owning projection verifier. Bootstrap snapshots the independently supplied fine plan and candidate migration packet, fully verifies the migration, and only then publishes a session handle. Invalid bootstrap leaves the session uninitialized.

This connects real owning migrations to checkpoint authority without pretending that the separate square-section artifact proves a section for their different fine histories. The supported cached object here is an independently checked POINT witness, not a section over the whole public domain. The square-section adapter remains separate.

## Lifecycle

Bootstrap can select answer-only, fine-lift, archive-only or combined lift/archive policies. Public successor operations are reconstructed from the expected predecessor and caller-supplied public row. A candidate's complete successor descriptor and objective must match, and its LP answer certificate is checked by the existing independent arithmetic verifier before publication.

New heads invalidate old handles. There is no checkpoint import or candidate-asserted cache hit API. Private fields are not a hostile-process security boundary. Serialized state/context snapshots isolate mutable caller inputs and returned receipts; cached witnesses are immutable tuples and callers receive copies.

Archive capability reconstructs the original fine plan with translated public refinements via the existing retirement implementation. Lift capability alone does not expose that method. The current lift context still contains the fine plan, so this is an operation-policy distinction, not information hiding.

## Safe point reuse

The first fine-lift request invokes the existing producer and then checks atom caps, original fine evidence, and exact projection to the requested public point. That immutable witness is cached within the session's unchanged source/fine context.

A public refinement does not invalidate those local facts. It CAN invalidate the point's eligibility. Every request checks all current runtime/public frames BEFORE looking up a cached witness. Thus a locally valid cached witness is refused after its public point has been excluded. A stale handle is refused before any lookup.

No cache entry survives into another migration or process: the session bootstraps once. Hence its unchanged fine/source binding is implicit in ownership of the cache, not supplied by an untrusted cache digest.

## Tests

Two real owning migrations pass two successor transitions each. For each lift-enabled session:

- one full migration verification;
- two fresh successor answer checks;
- one independent fine-witness check;
- two point-witness cache hits;
- a later exclusion of that same cached point, correctly refused.

Twenty-two targeted refusals cover invalid migration, capability escalation, stale query statement, hidden refinement, foreign/stale handle, wrong objective, archive denial, excluded cached point and absent lift capability for answer-only/archive-only states. Separate archive-only sessions reconstruct their original fine plan exactly. Caller and returned-witness mutation isolation is exercised. Successful successor answer certificates are also freshly replayed outside the session.

These counts are not section-local arithmetic reuse counts. They count a distinct witness cache and do not include all producer-side validation work. The predecessor migration is not rerun for each public successor; its authority comes from session-owned state.

## Accounting and remaining gap

Receipts separate live descriptor, lift context, archive and cached witness encodings. This is not a full Python heap or checkpoint-footprint account: fixed verifier code, handle/lock overhead, migration packets required externally for restart, and temporary candidate packets are not included. Migration evidence is verified at bootstrap but not retained as an importable attestation.

The domain-wide section attachment remains unimplemented. Its certificate must bind the SAME expected fine history and public domain as the verified migration; merely pointing at a previously checked section from another fixture is unsound. Integrating that attachment, or adding this language to Nima's checkpoint backend, is a further explicit step.

## Reproduction

    uv run --with sympy python research/voevodsky/checkers/check_migration_checkpoint.py

Implementation: `checkers/migration_checkpoint.py`.

Artifact: `results/migration-checkpoint.json`.
