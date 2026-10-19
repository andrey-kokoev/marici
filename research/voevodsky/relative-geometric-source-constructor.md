# A common relative geometric constructor from compact source records

For entrypoints, complete cycles and assembly measures, see the
[arrow assembly guide](../../docs/arrow-assembly.md).

## Mathematical rule

A source is (G, T, S, roles), where G is a rational positive-definite metric,
T is a finite-orbit family of proper affine G-isometries, and S is a list of seed
points. Roles distinguish carrier seeds, external-interface orbits, and a
retained attachment pole.

1. V = union of the T-orbits of the seeds.
2. H = the supporting facets of conv(V), calculated exactly from determinant
   signs. These experiments have simplicial facets.
3. E = supporting facets contained in an orbit marked external-interface.
4. L = H minus E; O = arithmetic mean of V; output the cones O*F for F in L.
5. An attachment-pole seed retains its unique opposite supporting facet as an
   attachment record without removing it. An ambiguous pole is rejected.

No particle name, expected facet count, target coordinate table, supplied face
list or supplied cell list is consumed by the constructor. The isometry and
metric obligations are checked before orbit generation. Nonspanning orbits and
non-simplicial supporting facets are explicitly rejected, not silently filled.
A finite-orbit resource bound is not an algebraic stopping rule.

Implementation: `checkers/assemble_relative_geometry.py`.

## Proposed source records

| Record | Seed points | Isometry generators | Interface role |
|---|---:|---:|---|
| `inputs/relative-proton.json` | 1 | 2 | Retain facet opposite the seed |
| `inputs/relative-neutron.json` | 2 | 1 | Reserve both three-point seed orbits as external interfaces |
| `inputs/relative-electron.json` | 1 | 1 | Retain facet opposite the seed |

The proton uses the original ABC and ADB permutations written as affine
isometries of a tetrahedral affine frame. Its Gram metric has diagonal 8 and
off-diagonal 4. The electron uses a five-cycle on an analogous four-dimensional
affine frame with the same Gram prescription. A second generator is unnecessary
for its point/facet orbit and is not included in the final source.

The neutron uses the stored scaled coordinate metric diag(3,1,1), the 120-degree
rim rotation, and seeds (0,7/20,1), (0,-7/20,-1). The gap 7/10 is explicit source
data, not a predicted dimensionless constant. Its two marked orbits reserve the
upper and lower cap facets, leaving the six side panels.

These are candidate geometric source presentations. Their dimension, metric,
symmetries and roles are declared data. They are not yet derived minimal
arrow-only definitions or a physical particle identification. No target lists
are hidden in a renderer or inside the common constructor.

## Fresh independent comparison

`checkers/check_relative_geometry_sources.py` calls the constructor first, then
separately reads the stored targets and searches exact distance-preserving vertex
correspondences. It verifies all pairwise squared distances, every coarse facet,
attachment interfaces, center distances, and the fine surface cells after the
same centroid subdivision on triangular facets.

| Source | Generated vertices | Supporting facets | Reserved facets | Admitted facets/cones | Stored fine cells matched |
|---|---:|---:|---:|---:|---:|
| Proton | 4 | 4 | 0 | 4 | 12 triangles |
| Neutron | 6 | 8 | 2 | 6 | 18 triangles |
| Electron | 5 | 5 | 0 | 5 | 5 tetrahedral boundary cells |

The electron cones are a stellar subdivision of the filled 4-simplex, not five
disjoint spatial volumes. The selected opposite facet matches its retained ABCD
cell. The proton's opposite facet matches the stored ABC attachment. Marks are
retained after symmetry generation; they are not assumed fixed by the full
construction symmetry group.

The fine subdivision is checked against stored cells, not inferred from the
number of generated facets. The constructor's coarse output, metric and center
are enough to reproduce this subdivision geometrically.

## Input-sensitivity controls

- Removing any retained generator makes its source fail the spanning test.
- Removing either neutron seed also fails the spanning test.
- Removing neutron external-interface roles produces eight cones, not six.
- Changing its gap preserves the six-panel incidence but fails the target metric.
- Erasing the electron attachment role preserves its shape but fails the marked
  comparison.
- Injecting a target-cell list into any input is rejected by the source schema.

All these controls passed. Necessary within these fixed records does not prove
minimality among all possible presentations.

## Reproduction and outputs

    python research/voevodsky/checkers/assemble_relative_geometry.py --source research/voevodsky/inputs/relative-proton.json --output research/voevodsky/results/relative-proton.json
    python research/voevodsky/checkers/assemble_relative_geometry.py --source research/voevodsky/inputs/relative-neutron.json --output research/voevodsky/results/relative-neutron.json
    python research/voevodsky/checkers/assemble_relative_geometry.py --source research/voevodsky/inputs/relative-electron.json --output research/voevodsky/results/relative-electron.json
    python research/voevodsky/checkers/check_relative_geometry_sources.py

Fresh comparison passed. `results/relative_geometry_sources.json` binds all
source, constructor, checker and target hashes. Individual `relative-*.json`
outputs contain the actual generated coordinates, metric, facets, marks and
cone cells.

## Remaining coefficient obligation

This constructor generates geometry, not the proton's coefficient protocol.
The established 1836 count has not been inferred from four generated cone cells
or from the source Gram basis. Attaching the original coefficient constructor
requires its declared frame, cyclic sector and staged feedback rule; equivalent
geometry alone does not fix a basis-dependent coefficient support count.
Likewise no neutron count or pentachoron-wide electron spinor operator is claimed.
