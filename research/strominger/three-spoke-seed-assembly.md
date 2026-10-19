# Three outgoing spokes through the shared assembly tests

Seed: AB, AC, AD, with registered vertices A,B,C,D.

## Bare arrow result

The incidence boundary has rank three and zero kernel. Endpoint continuation K is the zero three-by-three matrix: no spoke ends at the source of another. The undirected support is a tree, with f=(4,3), Betti=(1,0).

There are no branch-to-branch arrows, triangles or directed returns. In particular, there is no cyclic phase mode analogous to the triangle candidate.

The current relative assembler accepts metric, affine generators and seeds—not a bare directed-star manifest. Registering only A without branch-generating actions fails its spanning check. That is an interface result, not a proof that stars cannot be realized geometrically.

## Same-rule geometric controls

Give every spoke squared length eight. Explicitly supply a proper order-three action cycling B,C,D and fixing A. Let the common leaf-to-leaf squared distance be s. The three-spoke Gram is

    G_ii=8,
    G_ij=8-s/2 for i!=j,
    det G=s^2(24-s)/4.

Even this symmetry does not select s.

| s | Realization | Full supporting facets | Existing centroid selector |
|---:|---|---:|---|
| 8 | Regular tetrahedron | 4 | 3 root-incident faces |
| 16 | Nonregular tetrahedron | 4 | 3 root-incident faces |
| 24 | Planar triangle with A inside | 3 outer edges | all 3 edges |

For either 3D case, the face BCD has a fixed centroid and is excluded by the existing active-facet rule. The remaining three faces form the open tetrahedral fan discussed in the prior electron/proton assembly prototype. The common center-coning stage uses the mean of all four vertices; it does not silently replace that center by A.

For the planar case, A coincides geometrically with the coning center. The assembler retains distinct record IDs for the input root and generated center; no unrecorded identity is imposed.

## Answer

The bare star does not become a unique filled shape. With cyclic branch comparisons and a 3D metric realization, the existing selector returns the **three-face open fan**, not the closed tetrahedral boundary. Choosing the unique metric still requires leaf-distance information.

## Verification

Nine exact checks pass.

```sh
python research/strominger/checkers/check_three_spoke_seed_assembly.py
```

Result: `research/strominger/results/three_spoke_seed_assembly.json`.
