# Neutron upper/lower rims as a complex-plane encoding

## Conjecture and scope

Operator intuition: represent the same neutron construction in a complex plane instead of upper/lower geometry. Test exact recovery of the source vertices, metric, faces and cycle using the existing `mode-neutron.json`, not a newly fitted shape.

Rivals: a lossless vertex encoding; a full two-dimensional replacement; an encoding requiring retained cell provenance. All computations use rational pairs for Q(i sqrt(3)).

## Exact vertex representation

Set u=Z+i sqrt(3)X and h=7/20 from the source. The six vertices become the six roots of u^6=1. The two rim orbits are distinguished by u^3=+1 and u^3=-1. Decode each vertex by

    (X,Y,Z) = (imaginary_sqrt3_coefficient(u), h*u^3, real(u)).

The existing rotation becomes multiplication by conjugate(omega). It preserves u^3 and commutes exactly with decoding. Thus the upper/lower vertex label is recoverable from phase; it need not be an independent vertex label.

On these six points the original metric is

    d(u,v)^2 = |u-v|^2 + h^2*(u^3-v^3)^2.

All pairwise distances pass. Flat planar distances omit 4h^2=49/100 on every cross-rim pair. The value h remains supplied source data, not a consequence of the sixth roots.

## Reuse of the existing assembler

Decode the two source seeds, retain the source metric and action, and rerun `assemble_relative_geometry.assemble` and `evolve_relative_geometry_modes.evolve`. Both outputs agree exactly with the original outputs, including the cycle trace and the six-moving/two-fixed centroid selection.

This is an exact encoding/reconstruction, not evidence that the metric and action were derived from complex points alone.

As a competing interpretation, feed the two planar seed orbits, their induced proper rotation and the flat planar metric into the same assembler. It returns a filled **hexagon with six supporting edges**, not the three-dimensional carrier with eight supporting triangles. Equal counts of selected pieces do not identify those outputs.

## The full-cell obstruction

The vertex formula does not commute with affine averaging. Both cap centroids have u=0, but their heights are +h and -h. The source center also has u=0 and height zero. Hence u alone cannot reconstruct these three distinct points, and using Y=h*u^3 would incorrectly put both cap centroids at height zero.

For a barycentric point with weights lambda_i, retain

    u = sum_i lambda_i*u_i,
    eta = sum_i lambda_i*u_i^3,
    Y = h*eta.

In general eta is not u^3. This formula recovers all facet centroids and arbitrary affine combinations; the checker also samples every center-cone cell. Center contributions have eta=0. The rotation acts as (u,eta) -> (conjugate(omega)*u,eta).

This is the original three-real-dimensional geometry in a complex-plus-real representation. Alternatively one can retain the parent cell and barycentric history instead of eta, but that is still additional data beyond a single planar point. Faces remain named vertex collections, not automatically identifiable regions in a flat drawing.

## Disposition

**The six source vertices admit a lossless complex-plane encoding, with upper/lower recovered from cubic phase. The whole neutron carrier does not reduce to that plane alone.** Exact cells and assembly are recovered if the height moment or equivalent barycentric provenance is retained.

This provides a concrete phase-based representation of the existing rim split. It does not yet derive h, identify photons inside the belt, or establish a new interaction law.

## Implemented phase-input adapter

`checkers/assemble_cubic_phase_source.py` now accepts
`inputs/neutron-phase-source.json`: two phase seeds +1 and -1, a phase
multiplier and positive height scale, without upper/lower coordinate fields.
It retains the input, decodes to the existing source schema and calls the
unchanged shared `assemble` and `evolve` functions. Output includes separately
encoded vertex, center and facet-centroid height moments, plus cone incidence.
No default input or existing shared store was replaced.

Run commands are in [the assembly guide](../../docs/arrow-assembly.md).
`checkers/check_cubic_phase_source.py` passed all 15 controls, including exact
legacy geometry/cycle equality, metric sensitivity to height, reversed-action
trace sensitivity and rejection of zero height, identity action, nonreal cubic
seed phase, a nonspanning single rim and undeclared coordinate fields.
The first draft's nonreal-cube hostile used 1+i sqrt(3), whose cube is actually
real; it was corrected to 1+2i sqrt(3). Validation was not weakened.

Receipts: `results/cubic_phase_source_checks.json` and
`results/neutron-phase-assembly.json`.

## Verification

```sh
python research/strominger/checkers/check_neutron_complex_plane_encoding.py
```

All 15 exact checks passed. Receipt: `research/strominger/results/neutron_complex_plane_encoding.json`, including vertex encodings, all facet centroids, metric counterexamples, planar control counts and source hashes. No shared assembler was modified.
