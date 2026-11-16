# Bounded multi-step join search

`join-search.mjs` builds on [MATCHING.md](MATCHING.md) and
[OVERLAPS.md](OVERLAPS.md). This document describes the default exact comparison;
[ISOMORPHIC-SEARCH.md](ISOMORPHIC-SEARCH.md) adds an opt-in anchored comparison mode.
Given two checked plans at the same exact revision, it
searches their branch continuations using a supplied ordered list of typed rules.
The visualization and website remain disconnected.

## API

```
const result = searchRuleJoin(store, planA, planB, continuationRules, {
  maxDepth: 2,
  maxNodes: 128,
  matchOptions: { maxSearchNodes: 10000, maxMatches: 256 },
})
verifyJoinSearch(store, JSON.parse(JSON.stringify(result.report)))

if (result.report.status === 'joined') {
  verifyJoinWitness(store, result.report.witness)
  // result.bundle contains the source history and the checked chosen routes.
}
```

The same ordered rule list is used on both branches. An empty list is permitted;
duplicate rules are refused. There are at most 16 continuation rules, a maximum
depth of eight continuations per branch, and at most 1,024 discovered route nodes.
The defaults are depth two and 128 nodes. Depth zero checks just the two immediate
peak endpoints. The initial two applications are additional to the continuation
depth and account for the first two route nodes.

All matcher limits are validated even when no matching is needed. Matching retains
its own pattern/host sizes, search-node and result caps. Global route-node limits
do not constitute a general execution, history-size, or memory sandbox.

## Exploration and retained history

The search first executes the initial peak in an isolated store. It then explores
the two route trees breadth-first, beginning with the left and right endpoints.
At each node it enumerates matches in rule-list order and applies only admitted
plans. Each new endpoint is compared against endpoints already reached from the
other branch using complete canonical state data, including context and metadata.

The state index chooses a representative opposite endpoint to exhibit a join;
it does **not** remove equal-state nodes from the exploration queue. Different
histories remain different routes. Identity-rule cycles therefore consume route
nodes and depth, rather than silently becoming identity history paths. No shortest
join or optimal search-order claim is made.

On finding an equal endpoint, the implementation reconstructs the selected
continuations through `checkSuppliedJoin` at the original source. A positive result
is accepted only when that independent replay produces `joined`. The returned
revision bundle contains those chosen routes, not every discarded exploration
branch. Search replay reconstructs the exploration when its counters and coverage
claims need checking.

Neither search nor replay commits edits, moves heads, or alters verification
reports in the caller's store.

## Result meanings

In the default exact mode, `status` is `joined` or `notFound`. The opt-in anchored
mode instead reports `joinedUpToIsomorphism` on success. `coverage` describes why
exploration stopped:

- `stoppedAtJoin`: a replayed joining route was found; other possibilities need
  not have been examined.
- `exhaustedDepthBound`: the finite route trees through the declared continuation
  depth were explored without a matcher or global node cutoff, under the fixed
  rule list and allocation policy.
- `partial`: at least one matching search, pattern/host object bound, or global
  route-node cap prevented that bounded coverage.

A matcher cutoff is retained even if another explored route later supplies a
positive join. Positive replay remains valid; the cutoff only prevents a claim
of exhaustive search. A complete match census containing only dangling matches
contributes no applicable successors, whereas an object-bound refusal contributes
a coverage gap rather than a mathematical negative result.

**No `notFound` result proves nonjoinability.** Greater depth, another rule,
a different allocation, or a comparison up to isomorphism may change the result.
Even depth exhaustion is relative to this precise search configuration, not an
unqualified critical-pair or confluence statement.

## Allocation policy is a real restriction

Successor plans use the matcher's `match-local-fresh.v1` deterministic allocation.
The search does not enumerate the infinitely many possible fresh ID choices.
Those names participate in exact full-state comparison.

A test makes this limitation explicit. The immediate branches retain differently
named single edges. A replacement rule removes its matched edge and creates an
otherwise identical edge. The default names depend on the match, so one step per
branch leaves different fresh IDs and the search reports `notFound`. Supplying a
common fresh edge name on both branches instead produces a checked exact-state
join at the same depth.

Thus even a fully explored bounded search under this policy can miss a join at
that depth when arbitrary allocations are allowed. [ISOMORPHIC-JOINS.md](ISOMORPHIC-JOINS.md) now compares supplied endpoints with
explicit maps fixing surviving source occurrences. [ISOMORPHIC-SEARCH.md](ISOMORPHIC-SEARCH.md)
now integrates that comparison as an optional search mode with separate budgets.
Exact equality remains the default; allocation normalization is still separate.

## Evidence and replay

The report binds the source peak, ordered rule declarations, normalized limits,
allocation policy, counts, per-matcher census identities, explicit cutoff reasons,
engine digest, and any successful supplied-join witness. It includes a content ID.

`verifyJoinSearch` reconstructs the initial plans in a fresh store and reruns the
search. Rehashing forged statuses, cutoff claims, or exploration counts does not
pass exact comparison. The caller must provide the source history, either already
in a store or through a revision bundle. A successful returned bundle also
contains enough source history for this replay. Failed searches return no new
revision bundle and no purported nonjoinability certificate.

These are implementation-level checked witnesses, not signatures, formal proof
terms, model-validity preservation, or physical evidence. Existing engine-version
and typed-rule provenance boundaries remain unchanged.

## Executed boundaries

Eleven tests in `tests/isotope-wiring-join-search.test.mjs` cover:

- One- and two-step joins, one-sided continuations, and zero-continuation equality.
- Depth/rule-list restrictions, matcher/object caps, global node caps, and cycles.
- Positive joins despite partial exploration of other matches.
- Chosen-route history audits and replay from the returned bundle.
- The fresh-allocation counterexample above, forged claims, invalid inputs,
  missing source history, and caller-store nonmutation.

The later isomorphic-join/search, persistent-join, and
[context-lifting](CONTEXT-LIFTING.md) and [context-composition](CONTEXT-COMPOSITION.md)
suites bring the sixteen structural suites to 162 tests. Remaining work includes allocation semantics, general criticality
and context-extension laws, global confluence, and mechanically certified
predicate read contracts. No visualization work is included.
