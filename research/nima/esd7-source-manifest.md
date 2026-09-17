# Machine-readable `esd_7(Delta^3)` source manifest

The repository already contained a complete Freudenthal census in `research/voevodsky/checkers/check_esd7_explicit_analytical_census.py`. The manifest builder enriches that census with the data required by the Tate-torus comparison.

Generated artifact:

- `research/nima/results/esd7-source-manifest.json`

It contains all 1,807 nondegenerate cells:

\[
(f_0,f_1,f_2,f_3)=(120,560,784,343).
\]

Every cell records:

- stable identifier and dimension;
- cumulative and barycentric vertex coordinates;
- signed simplicial boundary;
- image and orientation sign under quarter rotation `rho`;
- image and orientation sign under reciprocal reversal `omega`.

The builder verifies:

\[
\partial^2=0,
\qquad \rho^4=1,
\qquad \omega^2=1,
\]

as well as full boundary resolution and the expected f-vector.

## Explicit designation profile

Because the universal-category note did not specify a smaller named subset, this manifest adopts the maximal canonical profile:

- all 784 oriented triangles are designated quotient triangles;
- all 343 oriented tetrahedra are designated octahedral cells;
- no vertices are declared zero.

This is a valid concrete realization profile, but it must not be confused with evidence that an unstated intended profile was identical. If later research names a smaller subset or zero vertices, only the `designation_profile` needs refinement; the geometric census, incidence, rotation, reversal, and signs remain available.

Regenerate with:

```text
python research/voevodsky/checkers/check_esd7_explicit_analytical_census.py
python research/nima/build_esd7_source_manifest.py
```
