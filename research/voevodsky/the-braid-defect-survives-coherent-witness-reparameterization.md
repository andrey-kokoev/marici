# The braid defect survives coherent witness reparameterization

## Frozen transport

Retain the previous independent tagged three-direction fixture and its twisted diamond bijections. With fixed outer tags, the witness fiber consists of four assignments to the two internal binary tags. Let L be the route s0 s1 s0 and R the route s1 s0 s1. The comparison defect is Omega=R^-1 L, an automorphism of the initial filling fiber.

A coordinate change assigns a bijection g_v to each ordering fiber and transports every diamond edge T:v->w to g_w T g_v^-1. Intermediate coordinate changes cancel in any composite. Therefore

    Omega' = g_start Omega g_start^-1.

This is a conjugacy theorem for the fixed transport, not a claim that no different edge transport can be coherent.

## Exact obstruction

For initial outer tag zero, Omega fixes two internal assignments and exchanges the other two: cycle type (1,1,2), order two.

For initial outer tag one, Omega is a four-cycle: cycle type (4), order four, with no fixed point.

The checker exhausts all 24 permutations at the starting four-point fiber. It also exhausts all endpoint/middle permutation choices for two-edge cancellation and tests nontrivial changes at all six ordering fibers. In total 27,744 coordinate/cancellation identities pass. General path cancellation then establishes invariance under arbitrary simultaneous coordinate choices, without enumerating all 24^6 assignments.

Nonidentity and cycle type survive conjugation. Thus the incoherence cannot be removed by reparameterizing the fixed witness transport.

## Higher filling and observable cost

The witness spaces have independently fixed discrete identity. A homotopy Omega~id would require pointwise equal images, which fails. Adding paths or quotient identifications changes that identity structure.

If a single equivalence relation on the four internal tag assignments is required to trivialize both defects, its classes must contain the orbits of both permutations. The tag-one four-cycle already connects all four assignments, so that quotient collapses the entire fiber. It cannot preserve an audit distinguishing those tags.

This is an information cost for that particular common quotient repair. It does not rule out replacing the diamond maps: the previously tested tag-preserving choice is coherent on the same underlying product source. Nor does it exclude higher structures with separately justified identity types and correspondingly restricted observations.

## Structural result

The defect is intrinsic to the fixed comparison transport up to coherent coordinate change. The source space alone does not determine that transport. This distinguishes three operations: reparameterizing a presentation, changing its comparison maps, and adding higher witness identifications.

## Reproduction

    python research/voevodsky/checkers/check_braid_defect_coordinate_invariance.py

Artifacts:

- `results/braid-defect-coordinate-invariance-contract.json`
- `results/braid-defect-coordinate-invariance.json`
