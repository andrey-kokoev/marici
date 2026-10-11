# Six-belt test: whole triangles versus a truncated vertex star

## What was tested

Use the actual twelve-triangle boundary retained by the 1836-arrow proton-like Merkle package. This experiment asks only whether the proposed six-belt has a valid geometric/topological realization. It does not assign electric charge, construct an independent electron complex, or supply the maps needed for a categorical pullback.

The previous hydrogen counterexample concerned twelve point-position states. This test instead preserves a two-dimensional region, its boundaries and the removed corner pieces; it is not another twelve-point approximation.

## Exhaustive whole-triangle census

All 924 choices of six of the twelve original triangles were examined. Vertex links, edge multiplicities, supplied orientation, connectedness, boundary circles and Euler characteristic were checked.

| Six-whole-triangle result | Number |
| --- | ---: |
| Annulus | 0 |
| Disk | 98 |
| Other, including disconnected or nonmanifold selections | 826 |

Thus no literal selection of half the original triangles is an annular belt.

There are nevertheless exactly four simple six-cycles in the triangle-adjacency dual graph. Each consists of the six triangles incident to one original corner A, B, C or D. Their union is a disk: the central corner is filled in. A six-cycle in the dual graph must not be confused with an annulus made from the entire corresponding triangles.

## A genuine six-panel belt

For each original corner v, write its six incident triangles in their inherited orientation as (v,a,b). Choose a cut parameter 0<epsilon<1 and define

```text
p_a = (1-epsilon)*v + epsilon*a
p_b = (1-epsilon)*v + epsilon*b.
```

Remove the corner triangle (v,p_a,p_b), retaining it as explicit complementary data. The remaining panel is the quadrilateral (p_a,a,b,p_b). Six panels assemble into a connected annulus around v.

| Feature | Count for each belt |
| --- | ---: |
| Vertices | 12 |
| Edges | 18 |
| Quadrilateral panels | 6 |
| Euler characteristic | 0 |
| Boundary loops | 2 |
| Edges on each loop | 6 |

This gives four symmetry-related six-panel belts, one around each original tetrahedral corner. A face-center vertex has valence three and gives a three-panel belt instead. The distinction is determined by the retained triangulation, not by a postulated electric charge.

At epsilon=1/2, each panel retains three quarters of its source triangle. The six source triangles are half the shell, so the actual band occupies **3/8 of the total surface area**, not half. All source triangles have equal area, verified exactly. Subdividing the six quadrilaterals into simplices yields twelve belt triangles, not six.

At epsilon=0 the inner loop collapses; at epsilon=1 the band width vanishes. Both are excluded. Epsilon=1/3 also gives a verified annulus. The cut radius is a free geometric choice, not a quantized or physically selected parameter.

## Abstract seam test

Two copies of the annulus can be identified along one six-edge boundary with opposite induced orientations. The resulting abstract surface is an annulus with 18 vertices, 30 edges, 12 panels and two remaining six-edge boundary loops. Using the same induced orientation fails the oriented-chain cancellation check.

This only tests a candidate seam between abstract bands. The second band is not an independently derived electron structure. Opposite geometric orientation is not identified with opposite electric charge. A physical or categorical gluing still requires the second complex, typed interface maps, witness transport and a charge observable.

## Verification and artifact

All 20 checks passed, including exhaustive census, dual-cycle classification, all four belt geometries, boundary loops, cut degeneracies, equal-area accounting, triangular subdivision, oriented seam controls, honest-rehash geometry mutation and serialized replay.

The Merkle packet binds the unchanged original 1836-arrow package and the four belt records. Each record includes exact rational cut coordinates, source triangles, retained quadrilaterals and removed corner triangles. This retains the elementary subdivision data; it does not enumerate all possible inward folds of an unspecified tetrahedral complex. No new coefficient arrows or pruning-minimality claim for an enlarged network are inferred.

```text
python research/voevodsky/checkers/check_proton_six_belt.py
```

Artifacts:

- `research/voevodsky/results/proton_six_belt.json`: census, topology reports, tests and fingerprint.
- `research/voevodsky/results/proton_six_belt_store.json`: retained focus and exact belt geometry.
- `research/voevodsky/results/proton_six_belt.obj`: six-panel belt around A for visualization; verification uses rational JSON coordinates.

## Disposition

The six-belt proposal has a natural geometric interpretation **as a truncated vertex-star annulus**, not as six whole shell triangles. It is a candidate attachment interface. The next missing data are the electron-like complex and the two maps to a common interface required by the proposed pullback realization.
