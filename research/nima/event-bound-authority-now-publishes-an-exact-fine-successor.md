# Event-bound authority now publishes an exact fine successor

## Delivered transition

The fixed two-history family now has an atomic authority-gated transition from its approximate common section to an exact fine state. This goes beyond resolving one admission query: the successor retains the authorized history and the appended fine inequality as its actual query contract.

Both A and B successors pass independent arithmetic replay. Six exact point answers verify, 28 invalid operations are rejected, and concurrent commit and revocation controls pass. The predecessor authority-aware query-resolution workload also passes unchanged.

## Joint semantic and authority gate

The owner supplies the original history before retirement through the existing process-local authority prototype. Its immutable vault record binds the retirement event, expected context/section digest and actual-history label.

The requested operation remains h<=1/2 followed by admission at (1,1). Before publishing a fine successor, the new service:

1. Checks the live handle and independently expected predecessor.
2. Verifies the distinguishing obstruction for that exact operation and point.
3. Resolves the archive reference against the retirement event and context.
4. Reconstructs the complete expected fine state from the AUTHORIZED history.
5. Checks the candidate's parent/event binding and exact successor equality.
6. Publishes a new head only after all checks succeed.

A candidate for the opposite history is rejected even when it is a mathematically valid fine-state certificate for that other branch.

The session lock protects the transition and receipts. The vault lock is held from authority resolution through publication, preventing revocation from racing between validation and commit. Two concurrent commits from one parent yield one successor and one stale-head refusal.

## Complete fine successor, not a selected old witness

The successor contains the fixed family's polygon halfspaces, 0<=h<=1, all supporting-envelope inequalities for the selected original history, every previously retained public frame, and the appended h<=1/2 row.

For A the history rows require h>=f(p,q). For B they require h<=g(p,q). Their identities are reconstructed from the original family, not inferred from the old section's returned source vector.

Candidate verification is exact reconstruction of this entire linear specification. It does not assume global nonemptiness or use a sampled point as a completeness certificate.

The old approximate section is removed from the session. Approximate lifting is disabled, and calling the old lift method fails with USE_EXACT_FINE_QUERY. The new descriptor explicitly advertises exact point admission and exact lifting, not approximate lifting or archival re-exposure. Further fine/public successor operations are currently unsupported rather than inherited accidentally from the approximate-state API.

## Exact subsequent queries

At a requested public point the service evaluates every public row and reduces the remaining fine inequalities to an exact interval for h.

- A violated public row certifies rejection outside the refined public domain.
- Incompatible lower and upper bounds certify an empty fine fiber.
- Otherwise the interval midpoint supplies an exact source lift through the owning affine inverse.

The separate verifier imports no session or vault. It reconstructs the expected complete fine state, checks the interval or violated-row certificate, and verifies positive answers directly against original atom caps, exact public moments, t1=51 and EVERY fine inequality.

At (1,1), refined A rejects and refined B admits. At the first original public vertex both admit, confirming that the A rejection is not a claim of whole-domain emptiness. A point outside the polygon is rejected for both.

The old selected approximate lift at (1,1) has h=1. It is rejected as a witness for the new h<=1/2 contract. Thus the update cannot silently keep answering under the old semantics.

## Failure and revocation behavior

Foreign and forged references, a fully formed opposite-history candidate, missing or altered fine evidence, stale parents, foreign events and false obstructions leave the old receipt and head unchanged.

A revoked reference cannot authorize a new commit. If identity was deliberately not retained, no fine successor can be published through this interface.

Revocation is PROSPECTIVE. Once a valid commit has published the exact fine state, later vault revocation does not erase that state or retrospectively revoke its query capability. The revocation/commit race permits only these two orders: revoke first and refuse without change, or commit first and retain the authorized fine successor. Retroactive revocation would require a different owning contract.

## Authority and accounting limits

The owner-history admission boundary is inherited from `authority_aware_upgrade.py`. This remains a trusted-process fixed-family prototype, not proof of truthful physical provenance, a serialized-token import protocol or an arbitrary projection-compiler migration.

The arithmetic replay is conditional on the fixture's owner-authorized A/B identity. It does not authenticate a JSON history label. Authority and atomicity are exercised by the live session workload; those facts cannot be reconstructed from an exported arithmetic packet alone.

Fine-state encodings are charged separately from the current authority vault encoding. The selected history label is now retained inside the fine state; it has not been forgotten. The fine heads retain zero old-section and zero replacement-section bytes because exact queries use the retained interval constraints rather than a replacement triangulation.

The workload's vault byte count includes its current control records. These serialized lengths are not a complete heap, historical archive or restart ledger. No storage-compression theorem is claimed.

## Reproduction

    python research/nima/checkers/check_authority_bound_fine_successor.py
    python research/nima/checkers/verify_authority_bound_fine_successor.py

Implementation: `research/nima/checkers/authority_bound_fine_successor.py`.

Artifacts: `research/nima/results/authority-bound-fine-successor*.json`.

Predecessor: `research/voevodsky/ambiguous-capability-upgrades-require-event-bound-history-authority.md`.
