# What one five-cell presentation can mean as a 4-simplex

The source `five-side-oct-comparison-domain.mjs` supplies five distinct cell occurrences connected by four oriented shared-face incidences. For the fixed example retained in `results/su32-block-dictionary-v1/verification.json`, the five cell centres have affine rank three. Neither the centres nor the union of whole cells is a geometric four-dimensional simplex.

There is an explicit **formal path-nerve interpretation**: take the free category on the oriented incidence graph. A four-arrow path defines a 4-simplex in its nerve. Its five vertices are cell occurrences; its four generating edges are the original incidences. Its other six edges are retained composite words, not additional native faces. Its triangular faces express word concatenation. The higher simplex is supplied by this declared nerve construction, not by a recovered native payload or filling law.

Deleting a stage from a face does not delete its history. For example, the edge from stage 0 to stage 4 retains all four source arrows inside its composite word.

## Exact gluing discriminator

The checker chooses two actual source presentations differing only at the middle cell. They share four cell names, but their middle two-arrow composites differ. Their source comparison map remains null.

| Intersection rule | Vertices | Edges | Triangles | Tetrahedra |
|---|---:|---:|---:|---:|
| Preserve complete composite words | 4 | 2 | 0 | 0 |
| Identify faces by vertex names alone | 4 | 6 | 4 | 1 |

The history-preserving intersection is two disjoint edges. Treating it as a tetrahedral face would identify distinct composites merely because their endpoints agree—precisely the comparison the source has not supplied.

All 120 pairs among the sixteen presentations of this one cone share at least the initial and final cell. Their shared-cell counts are 68 pairs with two, 32 with three, and 20 with four. Thus these particular blocks do not have pairwise single-vertex contacts under the cell-occurrence interpretation. This is not an exhaustion of other cones or proposed block types.

## Dictionary and remaining boundary

- A **spatial block** is a union of whole native cells; it is not this formal simplex.
- A **path-nerve block** retains one composable incidence history and its composite-word faces.
- A **native comparison** between different histories requires additional source binding; formal composition does not provide it.

The concrete record/continuation test for the same pair is in `su32-comparison-license-v1.md`.

Reproduce with `node research/strominger/checkers/check_su32_block_dictionary.mjs`. No native filled 4-simplex or higher comparison is asserted.
