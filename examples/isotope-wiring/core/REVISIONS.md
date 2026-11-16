# Immutable revisions and revision-bound ground rewrites

## Scope and implementation

`revisions.mjs` adds a synchronous, in-memory revision store, atomic ground-record
rewrites, retained-before-image undo, revision-path composition, branch-head
compare-and-swap, and dependency-complete bundle replay. It does not alter the
visual application, autosave, browser persistence, or the legacy compiler.

This layer is a ground rewrite calculus with explicit occurrence matches, not a
pattern matcher. The subsequent [typed-rule layer](RULES.md) constructs both
pushout squares and compiles them into these ground operations. A successful
ground incidence check alone is not proof of DPO gluing conditions.

## 1. Three identities that must not be collapsed

| Identity | Bound data | Equality means |
|---|---|---|
| State ID | Full normalized schema, sets, maps, model labels, supplied context, metadata | Same retained construction state, including context/metadata |
| Revision ID | State ID, exact parent revisions, operation event, engine-source digest | Same revision record and ancestry boundary |
| Operation/receipt ID | Full versioned operation or replay receipt | Same declared edit and replay evidence |

IDs are domain-separated SHA-256 digests of canonical JSON. Objects and reports
are frozen; inputs are copied. Array ordering in context and metadata remains
meaningful. Kernel record sets/schema presentations use the kernel's normalized
order. Hash equality is not graph-isomorphism evidence, source authentication,
edit authority, or physical truth.

The source digest binds the revision module and its local transitive machinery:
finite diagrams, attributed diagrams, model predicates, schemas, and typed rules. Node's runtime
and cryptographic implementation are execution dependencies, not separately
content-hashed artifacts. Bundles require the exact current source digest;
cross-engine migration is deliberately not automatic.

A state may appear at several revisions. This is necessary for branches,
alternative edit orders, undo, and no-op events. A seed with identical state and
engine is deterministic; no timestamp or random ID is inserted merely to force
uniqueness. Branch heads are separate mutable pointers.

## 2. Exact operations and atomicity

Create a store with `createRevisionStore()`, then:

```
const seed = store.seed(object, context, metadata)
const operation = store.preparePatch(seed.id, {
  remove: [{ sort: 'pair', id: 'existing-pair' }],
  add: [{ sort, id, label, incidence }],
  replace: [{ sort, id, label, incidence }],
  contextAfter: completeReplacementContext,
  metadataAfter: completeReplacementMetadata,
  provenance: optionalDeclaredDerivation,
})
const { revision, receipt } = store.applyPatch(seed.id, operation)
```

The example shows the request fields; omit unused fields. An added or replaced
record supplies its complete model label and all outgoing schema incidences.
`preparePatch` retains exact before-images for every deletion/replacement and for
context/metadata changes. A match is an explicit `(sort,id)` with that before-image,
not a search by label, count, or coordinates. The complete input state and exact
input revision are additional read preconditions.

Optional provenance is immutable operation data, not construction metadata or a
verified claim. Typed rules retain their definitions and matches there; the
separate rule-history audit checks that these declarations explain the ground
operation. It participates in operation/revision identity, but not state identity.

The same occurrence may not appear in multiple edit lists. Removing and adding
one ID must be expressed as a replacement rather than two overlapping actions.
Unknown fields, unknown sorts, missing matches, and existing added IDs are refused.

`applyPatch(currentRevision, operation)` requires both the exact input revision
and its state ID. Matching construction state at another revision is insufficient.
It validates the operation's digest and regenerates its canonical request and
before-images from the frozen input before executing it.

All deletions, additions, and replacements are applied to a private candidate.
Every remaining outgoing incidence must refer to a remaining record. A
`dangling-reference` error lists the offending arrow, source record, target sort,
and absent target. All schema equations and attribute domains are then checked
by the existing kernel. Only a fully checked candidate is committed.

An atomic edit can delete an edge, add a replacement, and explicitly redirect
all affected pair references. It may not delete the edge alone and rely on an
implicit cascade. Unreferenced support is not garbage-collected automatically.

Model validity is not an admission condition for the structural rewrite. A typed
candidate with duplicate occupancy or wrong counts is retained and can receive
refuted predicate results. A schema-invalid candidate cannot be committed.

### Full-state metadata semantics

Omitted `contextAfter` or `metadataAfter` means preserve that whole component.
Supplying either field means replace it completely. Thus `{metadataAfter:{}}`
actually removes prior metadata; it does not inherit undeclared fields from a
base definition. Nested field-patch syntax is not supplied in this milestone.

Metadata may include a retained legacy source, but such a field remains an origin
record, not an automatically regenerated current legacy definition. Re-exporting
a modified construction through the old app's format remains a separate adapter
obligation.

## 3. Undo and the path category

`undo(currentRevision, receiptId)` only accepts a receipt whose output is exactly
the current revision. It restores the entire before-state, including context and
metadata, but produces a new revision with the current revision as parent.
Undoing that restore event can restore its own before-state. No event is erased.

For a successful edit `r0 -> r1`, undo produces `r1 -> r2` with equal state IDs
for r0 and r2, but distinct revision IDs. This is a roundtrip under the state
projection, not an inverse in the revision-history category.

`makePath(source, receiptIds)` checks every revision boundary. Its empty list is
the identity path. `composePaths(after,before)` concatenates checked paths when
the intermediate revision agrees exactly. Identity and associativity follow from
list concatenation; the tests also execute these laws.

An explicitly applied no-op is a new provenance event, not the empty path. Two
independent edit orders can produce the same state ID with different revisions
and paths. The implementation does not quotient them merely on endpoint-state
equality. A transport/comparison calculus for edits is still required before
claiming reusable independence or higher coherence witnesses.

## 4. Branches, verification, and conservative invalidation

`setHead(name, expected, next)` uses compare-and-swap on a known revision.
`applyAtHead(name, operation)` checks the active revision, applies the operation,
and advances the head. These operations are synchronous within one store; this
is not a distributed or cross-process locking protocol.

Applying an operation explicitly to an old known revision is allowed as branch
creation. Applying that stale operation to a newer active head is refused. A
failure does not move the head or append partial state/history.

`verifyAt(revisionId)` runs the model checker and binds its report to the exact
revision, full state, and engine digest. Every edit invalidates all prior reports
for its new revision. Reports remain accessible under their original revisions;
none is relabelled as current. Even undo to an equal state does not inherit a
report automatically. The later [selective verification layer](SELECTIVE.md)
adds `verifyAt(target,{reuseFrom:source})`, which explicitly constructs a new
report by comparing exact declared predicate reads and current prerequisites.
`verificationById` retains historical baseline reports; export still omits them.

## 5. Export and replay, not implicit persistence

`exportBundle()` returns a JSON payload containing all seeds, ordered replay
receipts with full operations, branch heads, and the engine digest. The bundle
retains dependencies for undo and both branches. The caller must actually save
it to obtain disk durability; this module does not write files.

`importRevisionBundle(bundle)` constructs a fresh store. It:

1. checks the envelope and exact engine digest;
2. reconstructs and checks each seed's canonical diagram and attributes;
3. replays every operation against its declared revision;
4. compares complete generated receipts with supplied receipts;
5. resolves all branch heads and rejects noncanonical/duplicate history.

Corrupt states, recomputed-but-false receipt claims, missing dependencies, and
engine mismatches are refused. Failed imports do not mutate any existing store.
Verification reports are deliberately omitted from exported bundles and must be
recomputed after replay. History validation is not digital signature verification
or an authority check.

## 6. Executed checks and residuals

```
node --test tests/isotope-wiring-revisions.test.mjs
```

Fifteen tests cover immutable identity, exact/stale boundaries, forged before-images,
overlapping edits, atomic dangling refusals, coordinated deletion, explicit edge
reference replacement, independent edit orders, schema refusal, metadata deletion,
undo/redo state recovery, conservative verification invalidation, branch CAS,
path laws, exact bundle replay, and corrupt/missing/duplicate dependency refusal.

The combined structural, adapter, model, and revision suites have 51 passing
tests. The three separate legacy-engine TODO failures remain unresolved; adding
this core does not patch the old editor.

[RULES.md](RULES.md) now supplies reusable monic rules, explicit preserved-context
match transport, checked DPO applications, and bounded independence witnesses.
[OVERLAPS.md](OVERLAPS.md) checks supplied overlapping peaks and joining routes;
[SELECTIVE.md](SELECTIVE.md) adds process-local read-projection verification reuse.
[CENSUS.md](CENSUS.md) enumerates bounded fixed-pattern overlaps, and
[VERIFICATION-BUNDLES.md](VERIFICATION-BUNDLES.md) replays verification dependency
closures across processes. Global confluence, version migration, and automatic
durable storage remain open. Resource quotas and untrusted-bundle sandboxing
are not implemented. Browser integration remains deferred.
