# Bounded automatic matching in a fixed host

`matching.mjs` enumerates monic, exact-label-preserving natural transformations
from a checked rule's left-hand pattern to the attributed object at an exact
revision. It complements the overlap census in [CENSUS.md](CENSUS.md): that census
constructs jointly covered hosts; this matcher searches an existing fixed host.
Visualization and website behavior remain unchanged.

## APIs

```
const census = enumerateRuleMatches(store, revisionId, rule, {
  maxSearchNodes: 10000,
  maxMatches: 256,
  maxPatternRecords: 24,
  maxHostRecords: 128,
})
verifyRuleMatchCensus(store, JSON.parse(JSON.stringify(census)))

const found = census.matches.find(m => m.applicability === 'applicable')
if (found) {
  const { plan } = materializeRuleMatch(store, revisionId, rule, found.components)
  const result = applyRewrite(store, revisionId, plan)
}
```

Enumeration and materialization do not commit edits or move branch heads. An
enumerated entry contains explicit match components, its allocation, a serialized
plan specification when applicable, and any localized dangling refusal. To obtain
a checked plan owned by a store, materialize the match again there. A serialized
plan-shaped object is not an admitted plan.

## Coverage and applicability

For every pattern record, the search chooses an unused host record of the same
sort with exactly equal canonical label data. It checks naturality whenever the
images on both ends of an incidence have been assigned. Thus each completed
assignment is a sortwise injection satisfying all schema arrows. The existing
attributed-morphism constructor checks the result again.

If traversal completes, every such assignment has been considered. This is the
coverage argument, supported by bounded independent counting oracles; it is not
a proof-assistant certificate. Matches related by a pattern automorphism remain
distinct. Parallel host occurrences remain distinct even when their labels and
endpoints agree. No coordinate-frame transport or attribute-variable unification
is inferred.

A structural match is not necessarily an applicable rewrite. The existing
planner checks the complement and both pushout squares:

- `applicable`: the planner admits the rewrite at this exact revision;
- `dangling`: deletion would leave external incidence pointing at a deleted
  record. The match remains in the census, with no admitted plan.

Only the expected dangling refusal is classified this way; unexpected engine
errors abort. There are no implicit model guards or negative application
conditions. In particular, finding and applying an isotope pair-removal match can
leave a structurally valid object that fails the inventory predicate.

Rediscovering a match after an edit does not prove preservation of an earlier
occurrence. Use `transportMatch` from [RULES.md](RULES.md) when a checked
factorization through the retained context is required.

## Bounds and interpretation of failure

The defaults are shown above. Hard accepted maxima are 1,000,000 search nodes,
4,096 matches, 128 pattern records, and 4,096 host records. Oversized objects are
refused. Reaching a node or match cap yields `partial` and an `exhaustedBy` reason.
Both applicable and dangling matches count toward the match cap.

An empty complete census establishes absence of matches only for this fixed
pattern/host/exact-label fragment. An empty partial census establishes no such
absence. Complete matching with only dangling results establishes no applicable
rewrite of this rule here, not absence of future applications after another edit.

Search nodes count partial assignments, including those rejected by the partial
naturality check. Enumeration has deterministic schema/record order, with no
resumable cursor. These limits are not a general memory, label-size, history-size,
or execution sandbox. No performance or asymptotic improvement is claimed.

## Fresh names and revision boundaries

For each structural match, materialization chooses one deterministic fresh-name
allocation for the records created by the rule. Names depend on the rule,
explicit match components, sort, and right-side record. Collisions with existing
host names or earlier allocations are resolved deterministically; even names of
records about to be deleted are excluded.

This policy is **not** an enumeration of all possible allocations. It suffices to
check structural applicability, but exact-state join search must account for its
name policy: alternative allocations can change exact endpoint equality. Callers
requiring chosen names can use the ordinary `planRewrite` API with the explicit
match and their own checked allocation.

Plans remain tied to their original revision. A metadata-only edit may leave the
same match components available but still requires a new plan. Equal ground
effects from different matches retain distinct provenance and revision IDs.

## Replay and integration

A match census binds its rule, source revision and full state, limits, search
status, entries, allocation policy, and engine source digest. Replay reruns the
search and compares the complete result. Rehashing false completeness, incidence,
or state-binding claims does not suffice. The source construction history must
be available, for example via an ordinary revision bundle; the census does not
embed that history itself.

The matcher can discover residual matches for a selected continuation rule on
each side of a supplied peak. Those explicit steps can then be passed to
`checkSuppliedJoin`. [JOIN-SEARCH.md](JOIN-SEARCH.md) now adds bounded multi-step search over a
supplied rule list. It reports match-search cutoffs and retains the exact-state
limitations of the deterministic fresh-name policy.

## Executed boundaries

Twelve tests in `tests/isotope-wiring-matching.test.mjs` cover:

- Injection counts for isolated-vertex patterns and hosts of sizes zero through
  three, without quotienting pattern automorphisms.
- Independent edge/loop occurrence counts on all 16 two-vertex simple directed
  graphs, plus parallel-edge occurrences.
- Exact labels, dangling deletions, honest bounds, empty-pattern creation,
  deterministic fresh allocations, stale revisions, and forged census claims.
- Automatic discovery of the imported O16 pair-removal occurrence; its application
  still fails the unchanged target inventory rather than inheriting verification.
- Automatic residual-match discovery for an explicitly selected joining route.

With the later join-search, isomorphic-join/search, persistent-join, and
[context-lifting](CONTEXT-LIFTING.md) and [context-composition](CONTEXT-COMPOSITION.md)
suites, the sixteen structural suites contain 162 tests. General criticality/context-extension laws, global confluence, and
formal read-contract certification remain open.
