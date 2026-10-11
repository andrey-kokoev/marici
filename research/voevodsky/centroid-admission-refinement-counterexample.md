# Centroid admission fails an ordinary subdivision test

## Hypothesis tested

A cell belongs to the moving assembly iff its centroid has a nonzero mode under
at least one source generator; otherwise it remains an interface record.

Test whether this gives the same admitted geometric support before and after a
geometry-preserving subdivision. This is a stronger test than repeating the
three successful target reconstructions.

## Exact experiment

Generate each complete source hull without explicit neutron exclusions. Replace
each simplicial facet by its centroid subdivision. For every parent, exact Gram
determinants certify nondegenerate children of equal intrinsic volume, whose
union is the same facet. The mean of the child centroids is the parent centroid.

Compare:

    select parent facets, then subdivide admitted facets
    subdivide all facets, then select child cells

The same nonnegative centroid-displacement score is used in both orders. No
target face lists are read by the test.

| Source | Select then subdivide | Subdivide then select | Same support? |
|---|---:|---:|---|
| Proton | 12 triangles | 12 triangles | yes |
| Neutron | 18 triangles | 24 triangles | **no: caps reappear** |
| Electron | 20 tetrahedral pieces | 20 tetrahedral pieces | yes |

Electron counts here are a new subdivision of its five boundary tetrahedra,
not a replacement for the stored five-cell description or a coefficient count.

## Neutron counterexample

Each original cap centroid lies on the fixed rotation axis and has score zero.
After subdividing a cap into three triangles, every child centroid is off-axis
and has exact score 1/3. All six children of the two caps therefore become
active. No point, boundary, metric or underlying geometric facet was changed by
the subdivision, yet the rule fills both previously excluded interfaces back in.

The active side faces generate eighteen children in either order. The discrepancy
is exactly the six newly admitted cap children, not a rounding error or merely a
difference in mesh resolution on the same selected surface.

Thus the **unqualified cellwise rule is not a subdivision-independent geometric
admission law**. If cell resolution is intended as substantive source data, that
must be stated explicitly; it cannot be called intrinsic to the geometric shape.

## Narrower rule that survives this control

Select at the level of maximal supporting facets, not arbitrary mesh cells.

The checker independently regroups child simplices by their supporting planes,
using point coordinates and determinant signs, not retained parent labels. The
volume-weighted centroid of each recovered group restores the parent centroid.
Selection after this regrouping yields 12,18,20 children, respectively.

This is a positive test for a **different, facet-level hypothesis**. It matches
the level at which the original constructor operated. It is not proof of its WG
derivation or a reason to hide the counterexample to the broader cellwise claim.

## Verification

    python research/voevodsky/checkers/check_centroid_admission_refinement.py

Fresh run verified the counterexample and the regrouping control.
Receipt: `results/centroid_admission_refinement.json`, including source hashes,
parent/child centroids, exact scores and implementation hashes.

The reversible phase encode/decode checks remain valid. What fails is extending
the selection criterion from canonical supporting facets to arbitrary cells.
