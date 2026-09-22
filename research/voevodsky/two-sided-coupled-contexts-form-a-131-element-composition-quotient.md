# Two-sided coupled contexts form a 131-element composition quotient

## Independently frozen candidate

The source/evidence protocol supplies 638 concrete reachable states and sixteen action labels. Before computing contextual equivalence, define Q(w) as the partial transformation of those concrete states induced directly by the word w. This is an independent action observer built from the existing constructors; it is not asserted to be the earlier numerical assembled observer on source paths.

A context consists of a chosen admitted initial state, a left word, the tested word, and a right word. A failed prefix yields bottom. Successful evaluation observes the terminal typed source corner, received value and issued value. Interior event traces are not an output of this frozen contract.

The DPC prediction is that concrete action equality coincides with equality in all such contexts.

## Exact result

The owning source/evidence verifier passes freshly. Every concrete state has an exported-in-memory left reachability witness. Enumerating all finite words by their distinct partial transformations terminates with 1,267 values of Q.

The right-profile fixed point has 62 classes. For each word, its contextual signature records, for every reachable left state, either bottom or the resulting right-profile class. There are 131 distinct signatures. This characterizes all two-sided contexts: every left state is reachable, and right-profile equality tests all suffix observations.

The DPC is refuted by redundancy: Q retains distinctions that no declared two-sided context exposes.

## Explicit witness

Compare the one-event words source(2,0) and source(2,1). Both have the same admission domain. They change different retained marks in the concrete source state, but yield identical signatures across every reachable left context and every right suffix.

A concrete distinguishing source context is initial state 2 followed by acquire, source(3,0), deliver, issue(1). The two tested words then reach concrete states 7 and 11. Those states have different marks and identical continuation profiles. This establishes a real difference of Q values alongside equality of every contextual observation.

## Structural synthesis

The 131 contextual classes form a two-sided composition quotient of the 1,267-element concrete action monoid. The checker verifies 40,544 left/right generator congruence instances; stability under arbitrary word multiplication follows by induction.

The 62-state right-profile observer describes positions relative to future observations. The 131-element contextual quotient describes transformations of those positions, tested from all reachable histories. States and developments therefore yield different but related structures: a state representation and its observable action monoid.

Even two-sided context equivalence remains relative to the independently fixed observation map. Adding left contexts does not force all source distinctions to become visible. Retained marks irrelevant to this protocol remain invisible in both directions.

Logical reversal into an admitted opposite protocol is not established by this test. A monoid has a formal opposite; realizing that opposite with the declared constructors remains a separate obligation.

## Reproduction

    python research/voevodsky/checkers/check_two_sided_coupled_context.py

Artifacts:

- `results/two-sided-coupled-context-contract.json`
- `results/two-sided-coupled-context.json`
