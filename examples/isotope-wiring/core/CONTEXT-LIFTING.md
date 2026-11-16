# Checked extension of one persistent join into a supplied context

`context-lifting.mjs` lifts a [persistent-occurrence join](PERSISTENT-JOINS.md)
through one explicitly supplied monic attributed embedding of its source into a
larger diagram. This is a replayable certificate for that concrete extension,
not a universal context-extension or confluence theorem. Visualization is unchanged.

## API

```
const result = liftPersistentJoin(
  baseStore, persistentWitness,
  extensionStore, extensionRevision, sourceEmbedding,
  { allocations: { left: leftAllocations, right: rightAllocations } },
)
verifyContextLift(baseStore, extensionStore, result.certificate)
```

The base witness must replay successfully, have status `joinedUpToIsomorphism`,
and explicitly declare `trackingPolicy: 'persistentAfterPeak'`. A default-policy
witness is not silently upgraded, even when its particular tracks happen to survive.

The embedding must be a checked monic attributed morphism from the base peak's
exact source object to the object at `extensionRevision`. Source and target IDs
need not agree. Labels and every incidence map must agree along the embedding.
The larger construction may have its own context and metadata; these are not
inferred from or equated with the smaller construction's interpretation.

Neither caller store is changed. The result contains `certificate`, `baseBundle`,
and `extensionBundle`; each bundle includes the relevant source history and the
replayed chosen routes. Branch heads are not advanced automatically.

## Per-step construction

For each base application, in each branch:

1. Reconstruct its rule, match, checked plan, and application witness at the exact
   smaller revision.
2. Compose its match with the current source embedding to obtain a match in the
   larger object.
3. Plan and apply the same typed rule in an isolated larger store. The existing
   two-pushout checker still enforces the dangling and fresh-allocation conditions.
4. Construct the next embedding: retained records follow the old embedding, and
   created records follow their corresponding right-hand-rule allocations.
5. Check that the new embedding is monic and that both the retained-context and
   rule-comatch squares commute.

This updated embedding is used for the next match. A later rule referencing a
fresh base record is transported to its actual larger counterpart, not matched by
spelling. The certificate retains every larger application and intermediate
embedding, so those boundaries are replayed rather than merely described.

## Fresh allocation

By default, each larger application uses the base application's fresh names.
Additional context may already occupy those names; such collisions are refused.
They are never silently repaired.

An allocation override is an array for either branch, with exactly one entry per
application, including the initial peak application. A null slot selects the base
allocation. Otherwise the slot is an ordinary allocation object keyed by sort and
right-hand-rule record. Omitted branch arrays use all base allocations. The
certificate stores the complete normalized allocation programs.

One test adds an unrelated context edge named `fresh-A`, colliding with a base
creation. Explicit overrides create `extended-A` and `extended-B` instead. The
extended comparison maps those two created edges to each other and fixes the
unrelated context edge. A subsequent deletion follows the updated embedding and
deletes `extended-A`, not the context occurrence with the base spelling.

## Extending the endpoint comparison

The original endpoint isomorphism and the two final embeddings determine a map
on the embedded smaller endpoint. Every original larger-source occurrence outside
the initial embedding image is fixed. These outside records are an occurrence
collection, not necessarily a closed subdiagram: an outside edge can point into
the embedded source.

The combined assignment must cover the entire larger left endpoint, be an
attributed morphism, and have a checked inverse. The comparison square must commute:

\[
H\circ i_{\mathrm{left}} = i_{\mathrm{right}}\circ h,
\]

where h is the base comparison and H is the extended comparison. No permutation
search or inference from equal cardinalities is used for H.

The lift independently tracks larger-source occurrences through both routes.
Every common post-peak occurrence must survive both continuations and be fixed by
H. Every outside occurrence must also survive. The larger endpoints' context and
metadata must remain literally equal. No interpretation or retargeting of opaque
identifier strings in those fields is performed.

## Refusal and evidence boundaries

A strong base join does not make every initial match applicable in every larger
host. Added incidence can point at a record that an initial rule would delete.
The larger planner then refuses with its ordinary dangling-condition diagnostic.
That is a refusal of this supplied extension, not a nonjoinability theorem.

Allocation failures, nonmonic embeddings, mismatched source histories, and failed
commuting squares are also refusals. Even failure after the left branch has
already replayed changes only isolated scratch stores; no partial result is
published into either caller store.

Certificates bind both the checked base witness and the larger source boundary,
embedding, normalized allocation programs, larger route witnesses, intermediate
embeddings, outside records, persistent records, and explicit endpoint comparison
maps. Replay reconstructs all of this. Rehashing false maps or context-coverage
claims does not validate them. Engine-source changes require fresh same-engine
recomputation; no migration is inferred.

This mechanism certifies the supplied finite construction, not all context
embeddings, all critical overlaps, model validity, physical claims, or the truth
of unrelated historical provenance declarations. New model verification remains
an explicit operation. Execution and history-size sandboxing are not implemented.

## Executed checks

Eight tests in `tests/isotope-wiring-context-lifting.test.mjs` cover renamed source
IDs, context attached to retained vertices, per-step transport after allocation
overrides, fresh-name collisions, initial dangling obstructions, nonmonic/weak
inputs, forged certificates, missing dependencies, and failure without caller
mutation. Returned histories are replayed and their typed-rule applications audited.

[CONTEXT-COMPOSITION.md](CONTEXT-COMPOSITION.md) now checks concrete compositions
of these lifts, including every step triangle and the endpoint comparison square.
With that suite, the sixteen structural suites contain 162 tests. Universal
context/coherence laws, critical-pair/confluence theorems, allocation-policy
completeness, and formal predicate read-contract certification remain open.
