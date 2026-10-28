# Berry domain: a phase-bearing tetrahedron already present in the source

## Question

Can the first tower-cut test use an existing tetrahedral construction rather than impose a triangle on unrelated physical quantities?

SCC obligation: route/coherencer compatibility on four rank-one lines with nonzero pairwise overlaps. The proposed identification with a tower cut remains upstream of any claim of full domain recovery.

## Located constructors

`research/nima/agda/RetainedTetrahedralPackage.agda` supplies actual vertices, edges, faces, a horn-completion operation and recovery. Its `Cells.build` constructs a retained path-coherence tetrahedron; `recover-request` and `package-recovered` give the two recovery directions. This is concrete reusable machinery, not a missing generic tetrahedron constructor. The existing `ThreeWitnessRetainedCone`/`RetainedSquareConeClock` work also encodes a complete record at an apex with exact recovery. Neither construction alone identifies its supplied payload with a physical-law domain.

`research/voevodsky/checkers/check_electron_tetrahedral_spinor.py` already supplies four ordered unit normals

    (1,1,-1), (1,-1,1), (-1,1,1), (-1,-1,-1), each divided by sqrt(3),

and rank-one projectors P_i=(I-n_i.sigma)/2. These give four actual quantum lines, not four invented physical labels. The current calculation transcribes those definitions; it does not rerun the owner producer or derive its spinor inputs from WG.

The bounded search found no earlier packet explicitly identifying this Berry construction with the proposed formed-triangle cut. FCC references found in the lattice/band work concern a separate identification problem, not an established equivalence of this domain with an FCC lattice.

## Construction and fresh exact result

Use the existing projectors to compute

    B_ijk = Tr(P_i P_j P_k),
    h_ijk = B_ijk / |B_ijk|.

Each pair has Tr(P_i P_j)=1/3, so all six edges admit normalized overlap transport. The phases are the finite Pancharatnam/Bargmann invariants. They have the usual Berry interpretation on shortest projective-geodesic edges, with the overlap-product orientation convention used here; the inverse transport convention conjugates every phase.

| Ordered face | B | h |
| --- | --- | --- |
| 012 | i sqrt(3)/9 | i |
| 013 | -i sqrt(3)/9 | -i |
| 023 | i sqrt(3)/9 | i |
| 123 | -i sqrt(3)/9 | -i |

The tetrahedral boundary satisfies

    h_123 h_023^-1 h_013 h_012^-1 = 1.

This is not a numerical coincidence: write each h as the product of three oriented unit overlap phases. In the oriented boundary every edge occurs once in each direction, so they cancel. It is an Abelian boundary identity, not a theorem that each face has trivial holonomy.

The checker derives normalized eigenvectors from projector columns and tests invariance under independent vertex rephasings. No desired phase is used to construct the projectors or eigenvectors.

## Discriminating tests

1. Replacing a face by strict equality of its two transport routes predicts h=1. All four faces reject that prediction: their residuals are -1+i or -1-i.
2. Deleting face 012 while retaining the other three changes the oriented boundary phase from 1 to i.
3. Reversing each face orientation conjugates its phase, checked for all ordered triples.

The result supports a **phase-bearing triangular domain with tetrahedral consistency**, not a flat triangle of transport equalities. A path-horn filler in a base type cannot simply be interpreted as equality of Berry transports: curved connection transport need not be invariant under a homotopy of base paths. Its curvature contribution has to be retained in the interpretation.

Full projector-family data can determine the canonical Berry curvature, as the prior Benincasa packet already notes. This test does not claim that projectors inherently erase Berry information; it rejects an endpoint-only or strict-flat interpretation. Four sampled projectors with geodesic edges also do not determine arbitrary unsampled parameter paths or additional flat twists.

## Disposition and remaining binding

New bounded result: the existing four-face Pauli source already supports nontrivial Berry triangles with an exact tetrahedral boundary law. No new physical source was invented to fit the triangle.

The unresolved identification is specific: which actual serialization/deserialization cut exposes this projector/transport domain as the operator's formed triangle? The generic path-package and retained-cone constructors are located, but their domain-exposure map to this connection-bearing source has not been constructed here. This is not a counterexample to the governing conjecture, and no parent node is resolved by the finite calculation.

Verification: `uv run --with sympy python research/strominger/checkers/check_tetrahedral_berry_cut.py` exited zero via structured-command, execution `structured_command_execution:e_42200_1792519328970120300_18`. Receipt: `research/strominger/results/tetrahedral-berry-cut/verification.json`, including source hashes. SCC manifest: `research/strominger/scc-models/tetrahedral-berry-cut.json`. No Agda proof or physical experiment rerun.
