# Execution-interface ontology pressure audit

Owner: `marici.Buzzard`

Disposition: no Lean ontology extension warranted.

## Scope

This audit compares the bounded execution interfaces introduced in:

- `AuditRecord.lean`;
- `BoundedModelCheckAudit.lean`;
- `SemanticFidelity.lean`;
- `SafetyLiveness.lean`;
- `BoundedLiveness.lean`;
- the shared `SourceAuthorized` predicate in `TemporalAuthority.lean`.

It asks whether the interfaces duplicate one another or should be collapsed
into a single execution-proof record.

## Result

The interfaces form distinct proof obligations:

1. `BoundedClaim.Universal` quantifies a predicate over every inhabitant of
   one already chosen type.
2. `CheckedDomain.Covers` proves that an explicit enumerator contains every
   inhabitant of that type.
3. `SemanticModelCheck.Faithful` equates model and source semantics pointwise.
4. `Eventually` asserts existence of some future goal state.
5. `CompletesBy` adds a logical-step upper bound.
6. `SourceAuthorized` states that a source-authority witness is present.

Only the following directed implications are certified:

- checked cases plus coverage imply universality on the declared type;
- model checking plus coverage plus fidelity transfers to source universality;
- bounded completion implies eventual completion.

Existing hostile fixtures refute the converses and cross-promotions:

- bounded certification need not be universal;
- old-type coverage need not cover an enlarged type;
- coverage and fidelity are independent;
- safety and semantic fidelity do not supply liveness;
- liveness supplies no finite deadline;
- completion evidence supplies no deadline authority.

## Consolidation decision

Do not introduce an umbrella `ExecutionCertificate` structure. Such a record
would make unrelated fields appear jointly standard, encourage callers to fill
unavailable premises with placeholders, and obscure which implication is
actually used.

Do not merge `BoundedClaim.domain` with `CheckedDomain.members`. The former is
an arbitrary set used by proposition-level certification; the latter is an
executable finite enumerator with a no-duplicates witness. Their bridge is
already explicit in `FiniteModelCheck.toBoundedClaim`.

Do not replace `DeadlineAuthorized` with a new authority primitive. It is a
typed wrapper around the existing shared `SourceAuthorized` predicate and
correctly preserves the distinction between evidence and permission.

## Smallest missing interfaces

No new common type is justified yet. Future source packets may motivate:

- relational rather than equality-based semantic refinement;
- initial-state and step/trace simulation witnesses;
- typed clock conversion with coherence laws;
- scheduler fairness or bounded-delay contracts.

Each should enter only after independent frozen instances exist and hostile
sector distinctions survive. Until then, failed attempts to state stronger
theorems are evidence of missing source data, not invitations to add fields.

## Verification boundary

This was a source and type-relationship audit. It changed no Lean declaration,
so no new build claim is made. The immediately preceding aggregate check was
`Build completed successfully (8735 jobs)` before this markdown-only audit.
No Git command or site build was run.
