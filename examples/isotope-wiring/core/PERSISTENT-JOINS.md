# Persistent-occurrence joins

Supplied and automatically searched isomorphic joins now accept the explicit
policy `trackingPolicy: 'persistentAfterPeak'`. The default remains
`commonSurvivors`, preserving the earlier weaker behavior. Visualization is
unchanged.

## The finite condition

Let P be the source records that survive both initial peak applications. The
persistent policy requires:

1. Every record in P survives every step of each supplied continuation.
2. The endpoint comparison is an exact-label attributed isomorphism fixing the
   two tracked images of each record in P.
3. Context and metadata satisfy the existing literal-equality boundary.

The current typed-rule kernel retains IDs for preserved occurrences. This makes
the tracked images explicit without an inferred renaming. The implementation
reconstructs deletions from each checked rule and match; deleting a record and
later creating the same spelling does not restore its original track.

Records deleted by either initial application are not in P. They are not subject
to this preservation requirement. If P is empty, the requirement is vacuous for
that particular peak, not a statement about every rule application or context.

This checks the persistent-occurrence condition used in strong-joinability
arguments for these actual finite routes. It does not by itself prove a critical-
pair lemma, admissibility under arbitrary context extension, termination, or
confluence of the rule system.

## APIs

```
const supplied = checkSuppliedIsomorphicJoin(
  store, a, b, leftSteps, rightSteps,
  { trackingPolicy: 'persistentAfterPeak' },
)

const searched = searchRuleJoin(store, a, b, rules, {
  comparison: 'anchoredIsomorphism',
  trackingPolicy: 'persistentAfterPeak',
  maxDepth: 2,
})
```

The stronger policy is refused with exact-only automatic comparison: exact
endpoint equality alone does not certify persistence. It must be requested with
`anchoredIsomorphism`. Unknown policy names are refused.

Positive reports retain the `joinedUpToIsomorphism` status. Consumers requiring
the stronger condition must check the bound policy; they must not infer it from
the status name of a default-policy witness.

## Definite route rejection versus comparison uncertainty

A supplied route violating persistence returns `trackingLost`. Its exact route
witness is retained, but `comparison` is null: the known occurrence loss already
refutes that route under the requested policy, so no permutation search is needed.
Comparison limits remain bound separately as `comparisonLimits` for replay.

Tracking includes `afterPeak`, `atEnd`, `lostAfterPeak`, and separate `lostOnLeft`
and `lostOnRight` collections. Loss in either continuation is sufficient to reject
the pair. When no loss occurs, the ordinary anchored endpoint solver runs and can
still return a checked isomorphism, a negative endpoint comparison, or unknown.

Automatic search records these admissions and rejected-record counts, then keeps
looking for another route. A `trackingLost` admission is a decided rejection, not
an isomorphism coverage gap. It records `persistent-source-loss`, no comparison
ID, and zero permutation-search nodes. The global endpoint-pair budget still
counts the attempted pair, including its route replay and tracking check.

Thus a bounded search can decide every explored pair while finding no persistent
join. This remains `notFound` relative to the configured rules, allocation policy,
depth, and tracking policy. It does not prove nonjoinability. Conversely, a later
accepted route does not erase earlier failed candidates or merge their histories.

## Concrete distinction

A test starts from two opposite directed edges. The initial branches each delete
one edge and retain both original vertices. Erasing the remaining component on
each side gives equal empty endpoints, so it passes the weaker common-survivor
comparison. It fails the persistent policy because the two vertices were in P.

With both component erasure and edge-only deletion available, persistent search
rejects the tempting empty-endpoint candidate and continues. It finds edge-only
continuations whose common endpoint retains both original vertices. Their
comparison fixes those vertices and the full chosen routes replay successfully.

A second test deletes and recreates one source vertex with exactly the same ID.
Even though full endpoint states are equal, loss on the recreating branch is
reported and the persistent route is rejected.

## Evidence and tests

The policy, comparison limits, per-branch losses, admission status, and selected
routes are part of the content-addressed witness. Search additionally binds the
policy in its normalized limits and records each endpoint-pair admission.
Rehashing a weak witness with a stronger policy or falsifying rejected-record
counts does not pass replay.

Seven tests in `tests/isotope-wiring-persistent-joins.test.mjs` cover the distinctions
above, continuation search after rejection, decided tracking failure under tiny
comparison bounds, initial deletions, empty persistence requirements, replay
forgery, invalid policy/mode combinations, and caller nonmutation.

[CONTEXT-LIFTING.md](CONTEXT-LIFTING.md) now checks one explicitly supplied monic
extension of a persistent join; [CONTEXT-COMPOSITION.md](CONTEXT-COMPOSITION.md)
checks concrete composites. With these suites, the sixteen structural suites
contain 162 tests. General context-extension laws, global critical-pair/confluence
results, allocation-policy completeness, and formal predicate read-contract
certification remain separate obligations.
