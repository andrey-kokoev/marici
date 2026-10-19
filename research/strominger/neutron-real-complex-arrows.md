# Neutron candidate as arrows in R plus C

## Definition

Define a geometric candidate in R ⊕ C. Write a point as (r,z), with

    h = 7/20,
    omega = -1/2 - i sqrt(3)/2,
    A=(h,1),       B=(h,omega),      C=(h,omega²),
    D=(-h,-1),     E=(-h,-omega),    F=(-h,-omega²).

The directed arrow family is

    A -> B -> C -> A,
    D -> E -> F -> D.

These six correspondences together determine one affine action, rather than six unrelated generators:

    (r,z) -> (r,omega z).

Use A and D as carrier seeds. The supplied metric is

    distance² = (r-s)² + |z-w|².

In exact rational coordinates z=a+i sqrt(3)b, its matrix is diag(1,1,3). Height h and endpoint coordinates are explicit input, not inferred from arrow incidence. Real separation is retained coordinate data; there is no separately invented arrow translating between rims. Calling this the neutron candidate refers to its exact agreement with the repository's prior neutron geometry, not a derivation of physical neutron identity.

Input: `inputs/neutron-real-complex-arrows.json`.

## One shared process

`checkers/assemble_real_complex_arrows.py` has no neutron branch. Its generic source accepts any fixed number of real and complex coordinates and a positive declared imaginary-square parameter. Each arrow family must permute all declared points and uniquely determine an affine action. Exact elimination reconstructs that action and checks every arrow, rather than silently filling unspecified matrix entries.

It then calls the unchanged

- `research/voevodsky/checkers/assemble_relative_geometry.py:assemble`;
- `research/voevodsky/checkers/evolve_relative_geometry_modes.py:evolve`.

Those same backends serve the prior proton/electron geometric examples. The frontend was also tested on a pure-complex hexagon and a pure-real tetrahedron. The real/complex split is a coordinate representation, not a particle selector.

This is a constrained affine arrow frontend, not an assembler for arbitrary graphs. It accepts no supplied faces, target counts or particle-specific coefficients. It rejects insufficient spanning data and inconsistent or improper actions.

## Verified result

Exact source comparison with `research/voevodsky/inputs/mode-neutron.json` passes after the invertible coordinate permutation (X,Y,Z) -> (Y,Z,X). The inferred matrix, metric, seeds, complete geometric output and complete centroid-cycle output agree in that common basis.

- Six generated vertices.
- Eight supporting triangular facets.
- Six moving carrier facets and six center cones in the cycle-selected output.
- Two fixed cap facets classified as external interfaces by the existing wrapper.
- Three scheduled applications return the centroid state.

The unselected geometric output and the cycle-selected output are both retained; the latter does not silently overwrite the former. The return length is a finite action count, not a physical time.

## Why retain the real coordinate?

Both cap centroids have complex coordinate zero. Their real coordinates are +h and -h, while the center has real coordinate zero. A planar point alone loses that distinction. Dropping the real dimension and rerunning the exact same frontend/backend produces a hexagon with six supporting edges, not the neutron candidate.

All affine combinations interpolate r and z separately. Unlike the predecessor cubic vertex encoding, no nonlinear vertex formula is applied to centroids.

## Verification

```sh
python research/strominger/checkers/assemble_real_complex_arrows.py --source research/strominger/inputs/neutron-real-complex-arrows.json --output research/strominger/results/neutron-real-complex-assembly.json
python research/strominger/checkers/check_neutron_real_complex_arrows.py
```

Twenty controls passed, including complete prior-output equality, cap separation, reversed-arrow trace sensitivity, real-scale sensitivity, two dimension/type controls, and rejection of hidden faces, nonpermutations, inconsistent affine arrows, improper reflections, insufficient spanning data, missing seed orbits and degenerate metric.

Receipts: `results/neutron-real-complex-assembly.json` and `results/neutron-real-complex-checks.json`. Shared scientific scripts and stores were not modified.

This establishes a common geometric assembly path. It does not assign coefficient-network stages, atomic weight, energy, charge or a physical particle classifier.
