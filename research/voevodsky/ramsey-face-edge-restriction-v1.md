# Four PN facets do not glue by literal role restriction

## Scope fixed before testing

This is a lower-gate audit for `face-chart-transition-descent`, not a resolution of that parent. The prospective contract is `contracts/ramsey-face-edge-restriction-attempt.v1.json`; the SCC freeze is `scc-freezes/ramsey-face-edge-restriction-v1.1e8f1f286d2532a8.json`.

Take the revision-19 validated-port artifact unchanged: 48 eligible ports over 24 markings. Choose one eligible port for each of the four geometric facets. There are 12 choices per facet. Restriction means evaluating the chart's retained C/M function on the shared geometric edge, and then on a vertex. The PN certificate remains attached to its parent triangle: there is no assumed two-M PN operation on a vertex or edge.

## Successful lower cells

The four facets have six pairwise edge intersections and four triple vertex intersections. All 288 face-edge-vertex evaluation chains agree with direct face-vertex evaluation within their respective charts. Full parent records remain in the digest-pinned input artifact; this audit does not replace them with role readouts.

These are mathematical restriction functions and runtime checks, **not yet native restriction constructors**. Revision 19's native P/E packages do not automatically promote these functions into native law-compatibility cells.

## First missing cell

Of all 20,736 four-port covers, none agree on every shared-edge role function. In the first cover (charts 0,2,0,1 for facets opposite vertices 0,1,2,3), the first two charts disagree at vertex `0,0,1,0` of their common edge: C versus M. Both parent triangles remain individually PN-eligible. Geometry alone would accept this overlap and therefore cannot certify strict role compatibility.

The obstruction is independent of the enumeration. If all edge restrictions agree, every vertex receives a well-defined role from the three incident facets. Let m be the number of globally M vertices. Counting M incidences over the four facets gives 3m, since each vertex occurs in three facets. Each PN facet has exactly two M vertices, so the same count is 8. No integer m satisfies 3m=8.

This re-expresses the earlier global-frame obstruction at the actual edge restriction gate; it is not a new refutation of general chart descent.

## Verification and boundary

`checkers/check_ramsey_face_edge_restriction.py` passes its frozen SCC challenge and writes `results/ramsey-face-edge-restriction-v1.json`. The checker independently enumerates global role assignments as well as four-chart covers. It reads the existing source-bound input artifact; it does not rerun the sector producer or provide a new kernel proof. SCC `survives` describes the obstruction-checking harness, not survival of the prospective existence claim.

The next cell must therefore be a genuinely context-indexed edge compatibility object retaining both parent packets and triangle permits, not equality of their restricted role functions. It must specify how those edge objects restrict to triple vertices and what native coherence witnesses compare those routes. Merely bundling the incompatible records with P supplies retention but not that compatibility law.

The parent remains open. No net revision, graph publication, whole-space admission, physical role-change claim, or Git checkpoint is made by this audit.
