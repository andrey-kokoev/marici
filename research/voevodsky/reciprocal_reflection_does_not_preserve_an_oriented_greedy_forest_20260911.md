# Reciprocal reflection does not preserve an oriented greedy forest

## Question

Does the explicit reciprocal-invariant grade and adjacent-pair ordering make the greedy global forest itself equivariant under reciprocal reflection?

## Claim boundary

No in general. The grade is invariant, but every total-order tie break chooses one member of a reciprocal pair first. When the two oriented edges have the same endpoints, the first can enter the forest and the second becomes a chord. Reflection swaps their roles. This refutes invariant forest coordinates, not the invariant cycle space or continuity of either forest presentation.

## Minimal obstruction

Take two vertices and two oppositely oriented edges

\[
e:0\to1,
\qquad
\bar e:1\to0.
\]

Both have the same grade. A greedy forest processing \(e\) first admits \(e\) and rejects \(\bar e\) as a chord. Reciprocal reflection exchanges the edges, so it sends the chosen forest to the distinct forest containing \(\bar e\). No spanning tree consisting of one edge is fixed by this free transposition.

Consequently adjacency of reciprocal pairs in the order does not imply reflection invariance of the greedy forest.

## Correct equivariance object

Let \(T\) be one greedy forest and \(RT\) its reflected forest. Reflection gives a commuting comparison

\[
Z_T
\xrightarrow{R_T}
Z_{RT}
\]

between the two chord-coordinate presentations. On the invariant cycle space \(Z_1(G)\), reflection is canonical. Coordinates become equivariant only after retaining the change-of-basis map between forest presentations.

If an ambient edge form \(W\) is reflection invariant, then the induced cycle forms satisfy congruence under this comparison. Thus norms of represented cycles are preserved even though the chosen chord vector changes.

## Consequence for the candidate order

The grade \(W_*=\log(npq)\) remains reciprocal invariant and still proves the half-line continuity bound. The proposed orientation tie break supplies a well-order but not an invariant forest. Its correct output is a forest-presentation groupoid containing \(T\), \(RT\), and their integral cycle-coordinate comparison.

A fixed forest can be reflection invariant only under additional graph structure ensuring a fixed spanning forest exists. That condition fails in the minimal reciprocal-pair graph and cannot be assumed globally.

## Disposition

Withdraw any implication that the explicit order makes the greedy forest reflection invariant. Retain the projective cycle space as canonical and transport forest coordinates through first-class change-of-basis maps. The next checker should validate the reflected-forest comparison and metric congruence rather than equality of coordinate vectors.
