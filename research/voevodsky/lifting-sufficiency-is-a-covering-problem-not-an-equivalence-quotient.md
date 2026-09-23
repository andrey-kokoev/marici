# Lifting sufficiency is a covering problem, not an equivalence quotient

## Frozen contracts and state model

Fix a finite family of source histories, a public observer, and deterministic exact interfaces. A migration maps each history to a persistent state. Subsequent answers may use that state and shared family code, not an uncharged external history oracle. Count history-dependent state cardinality separately from shared programs, certificate archives, migration verification and transcript storage.

Compare three contracts:

1. exact public answers and public-only refinements;
2. the same plus an old-compatible fine witness for any admitted public point;
3. the same plus re-exposure of the exact fine possibility relation.

The point is semantic sufficiency, not literal reuse of an old history-bound proof packet. If independently replayable original-history evidence must accompany future outputs, that extra context must also be counted or independently supplied under a different storage contract.

## Common-lift grouping criterion

Suppose histories in a group G share public image Q and have fibers W_E(y). A common pointwise lifting function exists exactly when

    intersection_(E in G) W_E(y) is nonempty for every y in Q,

subject to the required effective/regular selection condition. Necessity follows because identical persistent states and identical requests produce one answer, which must be valid for every history in the group. Sufficiency follows by retaining or computing a common selection. Nonemptiness alone does not generally give a computable or continuous selection; the owning finite singleton-image construction below supplies explicit rational selections.

Crucially, pairwise ability to share a lifting function is NOT an equivalence relation. It need not be transitive. Nor does pairwise compatibility generally guarantee groupwise compatibility in higher-dimensional fibers. State minimization is therefore a partition/covering problem over jointly compatible groups, not simply quotienting histories by pairwise overlap.

## Owning m=3 example

Take the common public moments of (50,51,52). Its full source fiber is parameterized by

    x(h)=(50-h/128, 51+129h/128, 52-h).

The parameter direction has zero total and zero weighted moment. For 0<=h<=3 every point obeys the owning atom caps. Define five histories by the fixed moment equalities and the additional h intervals

    [0,1], [1,2], [2,3], [0,3], [1/2,5/2].

These are legitimate rational linear source constraints: h=52-x_2. The moment equalities determine the remaining coordinates uniquely at each h. Each history therefore denotes exactly its specified segment, not just the displayed sample lifts.

All five public images are the same singleton. Public-only refinement either retains that point or makes the state empty. One state plus the accumulated public refinement status is enough to represent all histories under the first contract; none of the original history identity is needed for their public mathematical answers.

## Sharp state counts

### Public answers: one initial state

All histories have the same complete public semantics. A shared state achieves the lower bound of one state for a nonempty family.

### Valid lifting: two initial states

The intervals [0,1] and [2,3] are disjoint, so these histories cannot share a lifting state. At least two states are required.

Two suffice: use h=1 for histories [0,1], [1,2], [0,3], [1/2,5/2], and h=3 for [2,3]. The source formula computes a valid fine witness from the state bit. A public refinement excluding the common point suppresses lifting; a retaining refinement preserves validity.

The checker exhausts all nonempty groups, classifies those with nonempty interval intersection, and computes a minimum compatible partition. It independently runs the greedy interval-stabbing construction, also returning two groups.

### Fine re-exposure: five initial states

All five fine intervals differ. Possible or forced rational thresholds on h distinguish each pair. Re-exposing the exact fine relation therefore requires five distinct states, achieved by storing its family index.

Thus the sharp initial history-dependent counts are 1,2,5 states, or 0,1,3 fixed-width bits. These exclude shared family code and later public evidence, which have the same semantics for every member and must still be retained or summarized separately. They are not total storage measurements for the production interface.

## Nontransitive shareability

The first and second histories share the witness h=1. The second and third share h=2. The first and third share no witness. Treating 'can share a valid lift' as an equivalence and taking its transitive closure would incorrectly merge all three.

This is a substantive correction to the earlier equivalence-map language: relational outputs require common acceptable outputs, not identical answer functions before a selector has been fixed. Fixing a particular deterministic selector induces an equivalence of its outputs, but optimizing over selectors is a different problem.

## Interval-family theorem

For any finite family of nonempty closed bounded intervals on one common public fiber, minimum valid-lift state count equals minimum points stabbing all intervals. Grouping histories by a selected common point and selecting a point from every compatible group establish both directions.

It also equals the maximum number of pairwise disjoint intervals. Greedily choose the least right endpoint of remaining intervals and discard all intervals containing it. Each later chosen interval starts strictly after the preceding chosen endpoint, giving disjoint witness intervals. Any stabbing set must hit those separately, while the greedy points hit every interval. This proves optimality, including touching endpoints.

For higher-dimensional fine fibers the correct object is groupwise intersection, not just pairwise disjointness. No analogous universal easy minimization theorem is claimed here.

## Disposition

The lane now has a lower-bound/achievability separation for the three retirement contracts on an owning source. Public summaries, lifting state and fine archives can require genuinely different history information. The next structural question is how the compatible-group problem changes for nontrivial public domains and required continuous or efficiently certified common selections—not another benchmark of packet serialization.

## Reproduction

    python research/voevodsky/checkers/check_minimal_continuation_state.py

Artifact: `results/minimal-continuation-state.json`.

This is an exact mathematical checker and exhaustive finite state-count control, not an independent migration verifier or a fresh analytical-admission replay.
