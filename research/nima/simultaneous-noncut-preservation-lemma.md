# Simultaneous non-cut criterion for hereditary star connectivity

## Lemma

Let `R` be a finite pure facet collection such that, for every face `Q` occurring in `R`, the flip graph

\[
G_R(Q)=\{F\in R:Q\subseteq F\}
\]

is connected. Let `F` be a facet of `R`. Suppose that for every face `Q subseteq F`, either

1. `G_R(Q)` has one vertex, or
2. `F` is not a cut vertex of `G_R(Q)`.

Then every face-star of `R\{F}` is connected.

## Proof

Take any face `Q` occurring in `R\{F}`. If `Q` is not contained in `F`, deleting `F` changes no vertex of `G_R(Q)`, so its graph remains connected.

If `Q subseteq F`, then `Q` occurs in another retained facet, so `G_R(Q)` has at least two vertices. By hypothesis, `F` is not a cut vertex. Therefore

\[
G_{R\setminus\{F\}}(Q)=G_R(Q)-F
\]

is connected.

These cases exhaust all retained faces, proving hereditary star connectivity after deletion.

## Corollary

If at every deletion stage one selects a facet that is simultaneously non-cut in every face-star containing it, then:

1. every suffix has connected face-stars;
2. every deleted facet is coadmissible relative to its suffix;
3. reversing the deletion sequence is a shelling.

The second implication follows from the link-connectivity argument: for every retained `G`, connectivity of the star of `F intersection G` supplies a first retained flip and hence a shared ridge containing the intersection. The third implication is the coadmissible-deletion shelling lemma.

## Reduced missing statement

The common-tree shellability theorem is therefore reduced to:

> In every proper nonempty retained common-tree facet collection produced by the deterministic peeling rule, the selected maximal-free-ridge facet is simultaneously non-cut in every face-star containing it.

This is stronger than being non-cut in the whole dual graph and stronger than possessing a free ridge. It is exactly the property measured by `check_peel_suffix_star_connectivity.py` after each deletion.
