# Bounded endpoint isomorphisms and supplied joins

`isomorphic-joins.mjs` adds explicit endpoint comparisons to the existing
[typed rules](RULES.md) and [supplied joining routes](OVERLAPS.md). It does not
change the default exact-state semantics of [automatic join search](JOIN-SEARCH.md).
[ISOMORPHIC-SEARCH.md](ISOMORPHIC-SEARCH.md) now adds an opt-in anchored search mode.
Visualization and website behavior remain unchanged.

## 1. Compare two revision objects with explicit boundaries

```
const comparison = compareRevisionStates(store, leftRevision, rightRevision, {
  maxSearchNodes: 10000,
  maxRecords: 24,
  anchors: { vertex: { retainedLeft: 'retainedRight' } },
})
verifyStateComparison(store, JSON.parse(JSON.stringify(comparison)))
```

The two diagrams must have exactly the same schema presentation. Context and
metadata must be literally equal; their strings are not interpreted as references
and are not retargeted by the comparison. This is an incidence/label isomorphism
with those other fields held fixed, not a certificate that every contextual or
provenance assertion is equivariant under renaming.

At each sort, the solver searches bijections preserving exact canonical label
data and every schema incidence map. Anchors are required images of selected
records, not hints. They must name existing records and be injective. Each
successful forward map is reconstructed by the attributed-morphism checker, and
its inverse is checked by the existing kernel. Both maps appear in the report.

Possible statuses are:

- `isomorphic`: a checked forward map and inverse satisfy the anchors;
- `notIsomorphic`: sort cardinalities differ, or the finite bijection search was
  exhausted under these exact labels, incidences, and anchors;
- `unknown`: the record or traversal bound prevented that decision;
- `notCompared`: context or metadata differ, so the chosen comparison contract
  does not compare these states.

A negative result is about these endpoints and anchors, not all possible
continuations of a rewrite peak. An unanchored isomorphism may exist when an
anchored comparison is negative.

## 2. Search bounds and straightforward checks

The default search bounds are 10,000 visited assignment nodes and 24 records per
endpoint. The maximum accepted bounds are 1,000,000 nodes and 128 records. Equal
sort cardinalities are checked before permutation search, so a cardinality
obstruction can be reported without searching a large object.

An exact object equality with identity-compatible anchors is handled by checking
the identity directly, with zero permutation-search nodes. This shortcut also
works above the permutation record bound. Otherwise an oversized object yields
`unknown`, not a false negative. The bounds are not a general execution, label-size,
or memory sandbox.

There is no canonical labelling algorithm or symmetry quotient here. The search
uses deterministic schema/record order, restricts images by exact labels and
anchors, enforces injectivity, and checks naturality on partial assignments.

## 3. Supplied routes with surviving source occurrences fixed

```
const result = checkSuppliedIsomorphicJoin(
  store, planA, planB, leftSteps, rightSteps,
  { maxStepsPerBranch: 16, maxSearchNodes: 10000, maxRecords: 24 },
)
verifyIsomorphicJoin(store, JSON.parse(JSON.stringify(result.witness)))
```

Both programs are first executed by `checkSuppliedJoin` in an isolated store. Its
ordinary exact-state witness is retained as `routes`, even if its status is
`notJoined`. The new layer then tracks original source occurrences through every
application and fixes every source occurrence that survives both entire routes.
Fresh records may be renamed. No existing history or branch head is changed.

Under the default `commonSurvivors` tracking policy, the resulting status is
`joinedUpToIsomorphism`, `notJoined`, or `unknown`. The optional
[persistent policy](PERSISTENT-JOINS.md) also returns `trackingLost` when a
required source occurrence is lost; its comparison is then null.
A positive witness includes the original routes, terminal revision and state
bindings, the explicit comparison maps, and tracking data. The returned bundle
contains both chosen derivation histories. Isomorphic endpoints generally still
have different state IDs, and their revision histories are never identified.

For example, two rules create otherwise identical directed edges with fresh IDs
`fresh-A` and `fresh-B`. Their exact endpoints differ. The isomorphic comparison
fixes the two original vertices and maps only the fresh edges to each other.

Conversely, after opposite deletions in a two-vertex directed cycle, the remaining
single-edge graphs are isomorphic if the original vertices may be exchanged.
The supplied-join comparison refuses that exchange because those vertices survive
both routes. This is not just equality of counts or an arbitrary graph quotient.

## 4. Tracking is historical, not a spelling test

The kernel's retained-ID convention lets the comparison follow original records
by removing each application's actually deleted occurrences from the tracked set.
It never adds recreated IDs back to that set. Each rule declaration is checked;
the replayed match determines which concrete occurrences were deleted.

Tracking records three collections:

- `afterPeak`: source occurrences surviving both initial applications;
- `atEnd`: source occurrences surviving both complete routes;
- `lostAfterPeak`: members of the first collection missing from the second;
- `lostOnLeft` and `lostOnRight`: the losses localized to each continuation.

A test deletes a vertex and later recreates an identical record using the same
ID. The endpoints are even exactly equal, but the source vertex remains lost from
tracking on that route. The witness records this loss instead of presenting the
new occurrence as the old one.

A positive default-policy isomorphic endpoint comparison is **not automatically
strong joinability**. [PERSISTENT-JOINS.md](PERSISTENT-JOINS.md) now provides an
explicit policy checking preservation of every common post-peak occurrence. In particular, lost persistent occurrences are not repaired by an
isomorphism. Even when no tracking is lost, this implementation does not promote
the example to a general critical-pair or context-extension theorem.

## 5. Replay and evidence boundary

Comparison and joining reports bind the engine digest and are content-addressed.
Replay reconstructs the programs and comparisons, including the source tracking,
and compares the complete results. Rehashing a false forward/inverse map,
unknown-to-negative promotion, or missing-tracking claim does not pass replay.
Missing source history is refused; a returned joining bundle supplies it.

These checks neither transport existing model reports nor prove every predicate
invariant under renaming. The O16 test explicitly renames one pair occurrence,
checks the incidence isomorphism on its 100-record diagram, and then performs a
fresh model verification. No report was inherited by the renamed state.

The semantics of opaque identifier strings inside labels, context, metadata, or
external evidence still require their owning interpretation. This layer performs
no hidden rewriting of those values and authenticates no physical claim.

## 6. Executed boundaries and next step

Eleven tests in `tests/isotope-wiring-isomorphic-joins.test.mjs` cover parallel
incidence, changed labels/incidence, limits, context/metadata boundaries, anchored
fresh-name joins, forbidden source swaps, deletion/recreation tracking, forged
claims, isotope occurrence renaming, and missing source histories. All 256 ordered
pairs of two-vertex simple directed graphs are compared against an independent
oracle using the two possible vertex permutations.

With the later [isomorphic-search](ISOMORPHIC-SEARCH.md),
[persistent-join](PERSISTENT-JOINS.md), and [context-lifting](CONTEXT-LIFTING.md)
and [context-composition](CONTEXT-COMPOSITION.md) suites, the sixteen structural
suites contain 162 tests. Concrete monic context
extensions can now be checked; general criticality/context-extension laws,
global confluence, and formal predicate read-contract certification remain open.
