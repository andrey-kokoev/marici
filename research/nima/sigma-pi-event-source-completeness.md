# A source-derived comparison basis for binary E/Pi schedules

## Question

Can the already specified binary SP -> PSS rewrite supply its own resolution-order comparisons, instead of importing arbitrary semantic witnesses?

Active obligation: route/coherencer compatibility. Scope: one finite innermost-first word in S,P, with Bool-indexed sums/products, full residual labels, all intermediate presentations and reversible value maps. The target is comparisons of normalization schedules from this source word, not every equivalence of arbitrary atomic or dependent types.

Conjecture: the rewrite schedules are exactly linear extensions of a source-derived event poset. Independent-event swaps then generate every schedule comparison, and the independent-event cubes provide a contractible geometric coherence space. Rivals are missing dependency constraints, distinct residual events silently identified by their unlabelled word, and higher fillers inferred solely from pairwise squares.

## Claim boundary: the construction

A sum occurrence receives its original position s. A product occurrence receives its original position p. On rewriting a labelled S followed by P, retain P and replace S by two residuals labelled L,R. These labels indicate syntactic slots, not Bool values. The actual local value codec remains

((a,x),(b,y)) <-> (a,(b,(x,y))).

For a source sum s with m products to its right, events are indexed by those products: the kth such product crosses residuals labelled by binary L/R strings of length k, counting k from zero. The source therefore determines 2^m-1 events for that sum.

There are two dependency schemas:

1. Residual creation: a non-root crossing requires the crossing that created its residual at the preceding product.
2. Product order: each product crosses sums from right to left, and residuals of a sum from right to left.

All constraints refer to original labels and residual addresses. They are computed before schedule enumeration. Each product's events form a chain; creation dependencies go from an earlier product to a later one. This also proves acyclicity.

## Written arbitrary-word argument

### Termination and exact event count

Let a be the number of S in the normal signature. Equivalently, a is the sum over source S occurrences of 2 raised to the number of following P occurrences. Every SP -> PSS step preserves a and the number of P, while increasing the current number of S by one. The natural-number rank

a - current_S_count

strictly decreases. It is nonnegative because every current S contributes at least one to a. A terminal word has all P followed by all S, so every complete normalization uses exactly a-source_S_count events. This is a source-derived finite bound for each finite word, not a uniform global cutoff.

### Enabled events and ideals

Every actual rewrite executes one of the declared events. Its creating parent has executed; the same product has crossed every sum/residual to its right. Executed events therefore form an order ideal.

Conversely, take an event whose predecessors have executed. Its parent has created its S residual, which has not yet been split by this event or any descendant. Earlier products are to the left of that residual. Later products remain to the right of the product in question. The same-product chain has removed every intervening S residual. Thus this S and P are adjacent and the event is an actual redex.

Two simultaneously enabled events occupy disjoint SP redexes. Their labelled replacements commute. Hence each ideal determines one labelled state independently of its linear extension. The state also recovers the executed events: an event's residual address has been split exactly when the state contains strict descendant residuals of that address. Thus the source rewrite DAG is the ideal DAG, with labels retained.

### Completeness of independent swaps

Take two linear extensions. Locate the first event required by the target order in the current order. Every preceding unfixed event is incomparable with it: a predecessor would contradict target minimality, and a successor could not precede it in the current extension. Swap it left across those independent events. Repeat on the suffix.

This constructs a finite comparison retaining every intermediate complete schedule. The only comparison schema used is exchange of adjacent independent events. It proves schedule-order completeness for this source poset; it does not identify the two raw schedule records.

### Higher coherence from maximal-event deletion

A k-cell consists of an ideal J and k independent events enabled at J. Its vertices are the 2^k ideals obtained by executing subsets of those events. Include all such cells and all faces, obtaining the finite cubical complex K(P).

Choose a maximal event e. The e=0 subcomplex is K(P without e). Every cell with e fixed to 1 has all predecessors of e fixed to 1; its variable events are incomparable with e. The prism obtained by allowing e to vary is therefore also a declared cell. Sliding this coordinate to zero defines a deformation retraction onto K(P without e), fixed on that subcomplex. Repeating maximal-event deletion contracts K(P) to its empty ideal.

This is a written contraction proof for the geometric cubical realization. It supplies higher homotopies for schedule paths using the independent-event cube schema, while the labelled schedules and their comparison certificates remain separate retained records. It is not yet an Agda formalization of the cubical complex or its realization.

### Value compatibility

The local map is a natural invertible rearrangement. Applied in disjoint word contexts, these rearrangements commute. Thus independent-event cubes transport whole values consistently. The executable check additionally compares the actual lifted value maps on two labelled sample source values at every state edge and cube. Those samples are regressions; the universal value statement uses the naturality argument.

## Disposition and executable evidence

The checker exhausts every reachable labelled state and every independently generated ideal for all 127 primitive words of length at most six:

* 1,681 states and 2,660 edges;
* 5,857 cubical cells;
* 2,865 verified contraction prisms over 645 maximal-deletion stages;
* independent cubes through dimension four;
* 375 constructed schedule comparisons retaining 2,921 adjacent swaps.

Complete schedules are counted exactly by dynamic programming on each exhaustive DAG; the largest count is 127,952,289. These schedules were not individually enumerated. Schedule comparison runs use deterministic and sampled linear extensions; the general connectivity claim rests on the written adjacent-swap argument.

Hostiles pass by exposing the intended defect: deleting a creation dependency admits an impossible event; exchanging dependent events is refused; deleting higher cubes breaks the supplied contraction certificate; distinct schedules remain distinct recorded data.

This is the first concrete source-derived comparison basis in this branch. It covers resolution-order coherence for the fixed binary grammar. Arbitrary dependent indices, independent primitive source loops, cross-source presentation equivalences and the intended full package-level universal operator remain outside this theorem. The original three paired constructors embed into these words, but intermediate words need not be paired.

## Reproduction

```
python research/nima/checkers/check_sigma_pi_event_source.py
```

Executed through `marici-structured-command`, exit 0. Dependency-free.

* Construction: `research/nima/checkers/sigma_pi_event_source.py`.
* Check: `research/nima/checkers/check_sigma_pi_event_source.py`.
* Result, labelled poset examples and a full comparison route: `research/nima/results/sigma-pi-event-source.json`.

The arbitrary-word proofs above are written mathematics supported by exhaustive bounded regressions. No new proof-assistant certificate is claimed.
