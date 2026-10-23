# Constructed fine-vertex refinement by the edgewise nerve

## Result

The [source's proposed functorial subdivision](../voevodsky/interior-pyramid-nodes-must-refine-a-homotopy-coherent-diagram-of-four-realization-functors-not-mix-the-presentations-barycentrically.md) now has an explicit finite implementation on every generated esd7 cell.

[The implementation](checkers/esd7_simplicial_refinement.py) lifts all1807 cells into the sevenfold edgewise parent nerve and checks their shared face maps. **20 checks pass.** This supplies a structural refinement without inventing120 Hilbert spaces, mixing unlike presentations, or choosing one parent chart per vertex.

Analytical evaluation still requires an admitted coherent parent diagram Phi with its domains, residuals and endpoints. No analytical payload is installed merely by passing these combinatorial checks.

## Fine vertices are comparison histories

For a barycentric vertex alpha, form the sorted seven-letter word containing alpha_i copies of parent label i. This word is a parent-nerve6-simplex, not a weighted sum of parent spaces.

In particular:

    V001 -> (3,4,4,4,4,4,4)
    V008 -> (2,4,4,4,4,4,4)
    V036 -> (1,4,4,4,4,4,4).

The six background occurrences survive. V001 is no longer forced to be either chart3 or chart4; it carries comparison data involving both. This avoids the failed context-free substitution without denying that audit.

## Whole-simplex construction

For a fine d-simplex, interleave its seven-letter vertex words one position at a time. The resulting monotone parent word has7(d+1) positions:

| Fine cell | Parent-nerve dimension |
|---|---:|
| vertex |6|
| edge |13|
| face |20|
| tetrahedron |27|

These are precisely the degrees in `(esd_7 X)_d = X_{7(d+1)-1}`. Repeated labels retain their occurrence positions and define an explicit degeneracy of a parent vertex, edge, face or tetrahedron.

Deleting a fine vertex deletes its occurrence in **each of the seven blocks**. Every resulting word is checked against the single shared lower-dimensional cell. Both orders of a codimension-two restriction agree on the literal retained positions, not just on their displayed labels.

The construction is also checked at scales1 through4, with dropped background, missing shared faces, merged occurrences and reversed-order controls.

## Orientation is not hidden

For parent order1<2<3<4, fine vertex order is the reverse of cumulative-coordinate order. The implementation records the sign `(-1)^(d(d+1)/2)` and verifies every signed boundary under this change.

For example the lifted E004 direction is V008→V001, opposite to its stored positive cumulative-coordinate traversal. Applying this to analytical or native transport therefore requires the declared opposite/inverse comparison on admitted carriers. No physical operation or history is silently reversed.

## What this changes about F006

F006 lifts to a parent20-simplex with support **{1,2,3,4}**: it is degenerate from the parent tetrahedron, not from a single parent triangle.

Its three edge images have parent supports:

- E004: {2,3,4};
- E037: {1,2,4};
- E006: {1,3,4}.

Thus the earlier H234/H123 labels record F006's two **local tetrahedral roles**. They are not, by themselves, its analytical image under functorial subdivision. The explicit cube-index prototype bridge remains a valid indexing construction, but its labels cannot be used as evaluated fine-face homotopies.

This gives a more faithful next operation: evaluate the retained parent tetrahedral coherence through Phi and its degeneracies/restrictions, rather than directly equating the two local role names or installing arbitrary finite matrices.

## Remaining analytical gate

Admit one coherent retained parent diagram Phi on the source joint-graph/essential-image carriers, including the face modifications, tetrahedral comparison, endpoint transport and direction conventions. Then apply the constructed subdivision to that diagram, first at F006 and then on all cells.

The source's coarse chart identities are useful input, not a substitute for checking that the chosen Phi retains the required analytical data. The finite residual comparison gate remains a test interface for an admitted finite restriction, not the definition of these higher simplices.

There are28 **positions** in a lifted fine tetrahedron, but that does not establish28 evolution steps, four branch histories or the proposed114-record producer. Those claims remain separate.

```sh
python research/strominger/checkers/check_esd7_simplicial_refinement.py
```

- [All lifted cells, shared restrictions and orientation data](results/esd7-simplicial-refinement.json).
- [Verification receipt](results/esd7-simplicial-refinement-verification.json).
