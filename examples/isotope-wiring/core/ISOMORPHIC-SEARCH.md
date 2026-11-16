# Automatic search with anchored endpoint isomorphisms

`searchRuleJoin` now has an opt-in comparison mode combining
[bounded route search](JOIN-SEARCH.md) with [supplied isomorphic joins](ISOMORPHIC-JOINS.md).
The default remains exact full-state equality. Visualization is unchanged.

## API and result contract

```
const result = searchRuleJoin(store, planA, planB, continuationRules, {
  comparison: 'anchoredIsomorphism',
  maxDepth: 2,
  maxNodes: 128,
  maxComparisons: 128,
  isomorphismOptions: { maxSearchNodes: 10000, maxRecords: 24 },
})
verifyJoinSearch(store, JSON.parse(JSON.stringify(result.report)))
```

`comparison` accepts only `exact` and `anchoredIsomorphism`. In exact mode a
positive report has status `joined` and an ordinary supplied-join witness.
In anchored mode it has status `joinedUpToIsomorphism` and a supplied-isomorphic-join
witness, even when the selected endpoints also happen to be exactly equal.
Callers must not treat these two witness formats as interchangeable.

The existing `notFound` status and coverage field remain separate. Neither mode
establishes nonjoinability or confluence. Fresh allocation still uses the same
single deterministic policy; isomorphic comparison does not enumerate allocations.

## Comparisons follow routes, not just states

The initial endpoints are compared first. Each newly discovered route node is
then compared against previously discovered nodes on the opposite branch, in
insertion order. Each pair is checked by replaying its full supplied programs
through `checkSuppliedIsomorphicJoin`. The returned endpoint revisions must match
the explored nodes exactly.

This derives the anchors from the actual common source occurrences surviving
both routes. Callers cannot replace those anchors with an unanchored comparison.
The scope remains the supplied comparator's scope: exact labels and incidence,
literal context/metadata agreement, and the explicitly chosen tracking policy.
[PERSISTENT-JOINS.md](PERSISTENT-JOINS.md) adds `trackingPolicy: 'persistentAfterPeak'`
to require every common post-peak occurrence to survive both continuations.
The default `commonSurvivors` policy does not impose that stronger requirement.

Opposite nodes are not deduplicated by state or graph isomorphism. Identical full
states may carry different source-occurrence histories, particularly after a
record is deleted and recreated. The comparator records lost tracking rather
than inferring identity from an ID's spelling. Search still makes no shortest-path
or optimization claim.

## Explicit comparison budgets

`maxComparisons` defaults to 128 and accepts values from 1 through 4,096. It applies
to anchored mode only and counts every endpoint-pair check, including the initial
pair and cheap cardinality or identity checks. When another required pair would
exceed it, exploration stops with `coverage: 'partial'` and a `maxComparisons`
cutoff. Merely reaching the cap is not a cutoff if no further pair is needed.

Each pair also has the supplied comparator's traversal and record bounds.
An `unknown` result records an `isomorphism` cutoff and exploration can continue.
A comparator `notCompared` result likewise records a comparison gap, rather than
a negative answer. A persistent-policy `trackingLost` admission instead skips the
comparator: it is a decided route rejection, not an unknown comparison. The trace
records its admission and lost-record count, and search continues. Match-search and global route-node limits remain independently active.
All limit options are validated before traversal, including at depth zero.

Thus `exhaustedDepthBound` in anchored mode requires completion of the bounded
route trees and decisions for all their cross-branch pairs. It is still relative
to the declared rule list, depth, exact-label fragment, and allocation policy.
A later positive witness may coexist with earlier unresolved comparisons; it
reports `stoppedAtJoin`, retains the cutoff evidence, and makes no exhaustive
coverage claim.

Repeated supplied-route replay can be expensive. The limits bound enumeration
counts, not memory usage, label/history size, or wall-clock execution. There is
no general resource sandbox.

## Evidence and replay

Reports bind the comparison mode, normalized budgets, per-pair witness/comparison
identities, endpoint revision IDs, decisions, solver node counts, and cutoff
reasons. `verifyJoinSearch` reruns the same mode and compares the complete report.
Rehashing a changed mode, false comparison result, or erased cutoff does not pass.

A positive bundle contains the original source history and chosen routes. It can
be replayed and audited with `verifyRuleHistory`, and the chosen isomorphic witness
can be checked separately with `verifyIsomorphicJoin`. The caller's history,
heads, and existing model reports are unchanged. No model verification is inherited
by a compared or newly constructed endpoint.

## Executed boundaries and remaining work

Seven tests in `tests/isotope-wiring-isomorphic-search.test.mjs` cover fresh-name
joins missed by default exact comparison, source-swap refusal followed by valid
residual continuations, per-comparison unknowns, global comparison exhaustion,
positive joins after unresolved comparisons, forged claims, and option validation.

With the [persistent-join](PERSISTENT-JOINS.md) and
[context-lifting](CONTEXT-LIFTING.md) and [context-composition](CONTEXT-COMPOSITION.md)
suites, the sixteen structural suites contain 162 tests. Concrete monic extensions can now be checked. General context-extension
laws, global confluence, allocation-policy completeness, and formal predicate
read-contract certification remain open.
