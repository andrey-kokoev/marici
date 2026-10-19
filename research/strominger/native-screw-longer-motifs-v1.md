# Longer winding motifs on the existing native screw mesh

## Test

The previous one-block strand test is extended to **two-, three- and four-block motifs**. Paths use only edges of the existing certified occupied patch. They progress strictly along the screw axis, wind monotonically in one angular direction, and may use axial edges that pause angular motion. Nonzero angular winding is required.

This tests the larger-motif option. **No additional radial layer is admitted or tested in this run.**

Candidates are enumerated by exhaustive traversal of the finite axial directed acyclic graph, with no search cap. Every opposing-sign pair is checked for exact periodic segment intersection. Receipts retain both the candidate paths and a collision witness for every pair.

For odd screw periods, two copies yield a translational period. Such continuation is used as a geometric periodicity test, not as admission of additional occupied bodies beyond the finite patch. Actual native edges are checked throughout every complete repetition that fits within the four-block core. The result concerns periodic motifs, not arbitrary finite open curves with unrelated endpoints.

## Measured results

| Motif length | Candidate paths | Opposite-handed pairs tested | Disjoint pairs |
|---|---:|---:|---:|
| 2 blocks | 8 | 16 | 0 |
| 3 blocks | 40 | 399 | 0 |
| 4 blocks | 82 | 1,677 | 0 |

In total: **130 candidate paths and 2,092 opposing-pair tests**, all with collision witnesses. Unequal counts of positive and negative candidates reflect the finite occupied-edge coverage; they are not a claim of physical chirality selection.

The mesh classification covers 55 surface edges and 10 axis-crossing edges.

## Structural obstruction

The mesh explains why a longer motif alone does not solve this problem.

Let a and d be the established screw-axis point and direction. Define transverse coordinates

```
X(v) = dot(v-a, (1,-1,1,-1))/2,
Y(v) = dot(v-a, (0,1,0,-1)).
```

Every occupied vertex projects to one of the four corners

```
(1,0), (0,1), (-1,0), (0,-1).
```

Every native edge either:

- connects opposite corners and crosses the screw axis; or
- remains on a face of the same diamond-prism surface, `abs(X)+abs(Y)=1`.

The checker verifies this classification for every occupied edge. Consequently all native-edge paths that avoid the axis remain on **one common cylindrical surface**. Increasing the motif length does not create radial separation.

## Why opposite periodic windings must meet on that surface

A strictly axial-monotone path has one transverse position at each axial coordinate z. Parametrize the diamond perimeter continuously by an angle, and lift each path's angle to a real function theta(z).

Over a common translational period L, the angle difference between two paths changes by

```
2*pi*(winding_number_1 - winding_number_2).
```

If the winding numbers differ, continuity forces that difference to equal an integer multiple of 2*pi somewhere. At that z the paths have the same perimeter position, hence the same geometric point. Opposite nonzero winding numbers necessarily differ.

Thus, within this axial-monotone periodic category, the obstruction persists beyond the explicitly enumerated motif lengths. This is a written topological argument supported by exact mesh checks, not a proof-assistant certificate.

Reversing travel along one curve changes neither its geometric image nor its intersection set. A separating sheet cannot remove an existing intersection without rerouting a curve.

## Scope and next required change

The test does not rule out arbitrary nonmonotone routes, interior-cell curves, a different screw axis, or a genuinely expanded occupied mesh. It also does not establish any field-transfer law along the geometric paths.

The concrete requirement for a radial-layer attempt is now clear: obtain a second radial route **off the existing diamond-prism surface**, using explicitly admitted native cells and contact witnesses. Merely drawing an outer helix, relabelling a reference vertex as occupied, or lengthening the same surface motif would not satisfy that requirement.

Production geometry, isotope constraints and the viewer are unchanged.

## Reproduce

```
node research/strominger/checkers/check_native_screw_patch.mjs
python research/strominger/checkers/check_native_screw_longer_motifs.py
```

Output: `research/strominger/results/native-screw-longer-motifs/verification.json`.

The checker reruns the shorter strand audit, verifies the source receipt hashes, classifies all occupied edges, enumerates the larger motifs and records exact pairwise collision witnesses.
