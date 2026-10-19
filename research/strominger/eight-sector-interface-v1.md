# Eight-sector refinement interface

## Construction

The three diagonal subdivisions of the source octahedron have a common eight-sector refinement: join its center to each of its eight boundary triangles. Every tetrahedron in any diagonal subdivision is exactly two of these sectors.

This common refinement is used as a **comparison workspace**. The original native primitives, reader contexts and transfer witnesses remain the source objects; no new occupied cell is introduced.

Each sector has volume 1/6 in the source FCC units, and each original diagonal component has volume 1/3. The checker verifies containment through the diagonal midpoint, the exact volume sum and all three pair partitions.

## Four complete charts

Label the sectors by their outward face-normal signs `(sx,sy,sz)` in `{−1,+1}^3`.

For diagonal i, pair sectors differing only in sign i. For each pair use

```
average   = (f_plus + f_minus)/sqrt(2)
difference = (f_plus - f_minus)/sqrt(2).
```

The chart has four average and four difference entries. Coordinates are mass-normalized: the factor sqrt(2) agrees with splitting each coarse cell into two equal-volume sectors. A physically constant coarse payload c embeds as c/sqrt(2) in each normalized fine slot, giving average c and difference zero.

There is also an antipodal chart pairing sigma with -sigma. It is the same combinatorial pairing used by the cube-to-tetrahedron vertex collapse. Its pairs are labelled using the source root tetrahedron, so its A4 action matches the source endpoint labels rather than relying on an arbitrary cube ordering.

Write `A_i=H_i/sqrt(2)`, where H_i is the explicitly stored integer sum/difference matrix. The transition between charts is

```
T_(j<-i) = H_j H_i^T / 2.
```

All 16 transitions are orthogonal, and all 64 composition triangles commute exactly. A closed chain of chart changes returns the complete data, not merely its averages.

## Symmetry

The actual proper root-tetrahedron rotations induce permutations of the eight sectors. Their 144 products are checked. Retaining the transformed diagonal index gives 48 indexed-chart equivariance checks: twelve actions on each of the four charts.

For the antipodal chart, the same four-vertex permutation acts separately on its average and difference blocks. For coordinate-diagonal charts, the symmetry also moves the diagonal choice and may reverse the sign convention for a difference.

Separately, the twelve affine FCC torus actions pass 48 indexed-chart checks and 144 composition checks retaining cover-center displacement. Translations move the octahedron's center; they do not rotate its relative sector normals. Their action is not substituted by a proper root rotation carrying the same four-class permutation.

These symmetry checks concern sector indices and recorded poses. The N payload remains in its supplied source ordered frame. This does not identify the native N geometric C3 action with the P endpoint action.

## Actual neutron coefficients and fields

A fresh native generator supplies four N reader contexts around the octahedron, with absolute origins 0,1,2,3 and complete marked references. Their PN/NN construction witnesses are retained. These are available reader contexts, not an asserted E-exit-certified assembly.

The coefficient tests use both existing phase-dependent N bindings

```
E_r = E_0 Pi_N^r,
E_(r+1) Pi_N = E_r,
E_r* M_N E_r = I5.
```

The two seeds remain explicit and noncanonical. Each maps the full five coefficients into the actual 36-component N field with its source metric M_N.

Two input tasks are tested:

1. **Independent records:** four independent five-coefficient states, with their supplied source contexts. This is a 20-complex-dimensional input, not a claim that arbitrary such assignments satisfy one common construction history.
2. **One coherent native NN chain:** coefficients are obtained from one root vector using the actual native packet permutations. In the declared co-moving bindings, all four fields agree, and changing pairing creates no difference signal.

For both seeds, both tasks and all four charts, decoding recovers all coefficients and original source contexts exactly. Norms are preserved. The 288-coordinate sector-field workspace does not imply 288 independent input degrees of freedom: the independent-reader input lies in a constrained 20-dimensional image.

Full 36-component N fields outside those five-coefficient images are also tested. Chart changes commute with uniform application of the actual N L, G and corner-cycle operators. This is an operator-preserving comparison of payloads, not a new cross-carrier PN law.

Realization origins and reference provenance travel in an explicit source-context sidecar. They are not inferred from the periodically repeating embedding matrices. Folding origins modulo two is rejected by the decoder's source-context check.

## What the difference data prevent

Average-only transitions lose information:

- each averaging projection has rank four;
- two different coordinate averaging projections compose to rank two;
- all three compose to rank one;
- stacking all three sets of averages has rank seven, not eight.

The common invisible mode is `sx*sy*sz`. Even all three coarse average readouts cannot recover it.

An explicit source-coarse state is preserved by its original averaging projector and killed by a different one: squared norm eight becomes zero. Dropping differences also fails recovery on the independent five-coefficient reader fixtures. This is not just a counterexample involving unrelated arbitrary fine data.

Thus a successful round trip must retain the differences or an equivalent complete record of them. The coherent NN-chain fixture illustrates a special subspace on which they happen to vanish; it does not justify deleting them from the general interface.

## Transporting native NN channel maps

The existing identity `E_(r+1) Pi_N=E_r` supplies the co-moving field action for each of the three NN steps. Represent each step as a partial channel map between source-reader summands and conjugate it into each chart.

All twelve transported maps recover the source map exactly. However, some touch all four target coarse pairs, even among the three coordinate-diagonal charts. Lossless field transport therefore does not imply that the original face-pair locality remains face-pair locality after regrouping.

These partial channel maps are not unitary evolution on the whole direct sum. They describe a specified native source-to-target channel and its support in another complete comparison chart.

## Consequence

The refinement-indexed **read-only comparison interface is constructed** for the declared coefficient/field task. It preserves the old native chart, full coefficients, norm and source history while allowing the complete A4-indexed family of descriptions.

The source grammar is unchanged. A target chart's average entries are not automatically four independently admitted target-native particles or readers. The measurable next issue is the locality and incidence of transported native operations, rather than whether changing descriptions must lose information.

## Reproduce

```
python research/strominger/checkers/check_eight_sector_interface.py
```

Outputs:

- `research/strominger/results/eight-sector-readers/verification.json`
- `research/strominger/results/eight-sector-interface/verification.json`

The latter stores pairings, chart matrices, transition matrices, loss witnesses, coefficient recovery results and transported NN support. Native geometry and reader contexts are freshly generated; all matrix, volume and coefficient calculations are exact.
