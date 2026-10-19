# Native neutron field: geometric weights and attachment gate

## Exact reconstruction

The native N field was rebuilt from the retained belt vertices, oriented
triangles, spatial frame and cyclic character. The construction did not import
selected mode numerators or fit the tensor weights.

The belt consists of six triangular faces, each split into three centroid-edge
patches. Each of the resulting 18 patches contributes its two real in-plane
axes, carrying complex amplitudes:

```
18 patches x 2 intrinsic components = 36 coordinates.
```

A spatial order-three rotation partitions the six parent faces into three
rotating adjacent pairs. Each pair contains six small triangles, hence twelve
intrinsic coordinates:

```
3 sectors x (6 patches x 2 axes) = 3 x 12.
```

The source convention chooses one of two geometrically available invariant
adjacent-face matchings; this choice remains explicit, rather than being
selected from the desired coefficient counts.

## Deriving the unequal weights

For each triangle, its ordered corners give real vectors r and s such that
its complex cyclic mode is `r + i sqrt(3) s`. Let

```
a = s.s
b = r.s
v = r - (b/a) s
beta = v.v
```

Then s and v are orthogonal in-plane directions. In numerator coordinates,
the mode components and metric are

```
z = (b + i sqrt(3) a, beta)
metric = diag(1/a, 1/beta).
```

These formulas derive the actual native metric and all twelve nonuniform
probabilities `|z_i|^2 / (d_i * sectorNorm)`. They exactly match the earlier
tensor-grid receipt. The three sector probabilities are uniform 1/3 because
rotation carries each derived plane frame to the next sector's frame.

## Operator reconstruction

Writing S for one sector's norm and d_i for its metric denominators:

```
L_ij = z_i conjugate(z_j) / (S d_j)   within each sector; zero otherwise
G_ij = 1/3                           between matching slots of three sectors
Return = GL = LG.
```

Every entry agrees exactly with the native 36-coordinate L, G and return
operators. L retains one mode per sector (rank 3); G aligns corresponding
slots across sectors (rank 12). This supplies a geometric origin for the
weights that prevented a simple relabelling of P into N.

The support-grid rows are now identified with the twelve slots of a reference
face pair: six patches times two intrinsic axes. The three columns are its
three rotating sector placements. They are not the three ambient spatial
components used in P's grid.

## What attaches, and what still does not

P's native field lives on a triangulated tetrahedral surface. N's native field
lives on a six-face belt with two triangular boundary rims. Its parent complex
has V=6, E=12, F=6, Euler characteristic 0. The two rims are the U and L vertex
triples. A single tetrahedral reader's closed boundary has different topology.

Therefore the neutron **geometric field and native weights are reconstructed**,
but not yet sewn to the single N facet of T by a source-derived restriction map.
The belt can serve as an internal geometric fiber over a reader presentation;
saying so is an organizational possibility, not a construction of that map.

The next missing datum is the belt-to-reader/facet interface and its compatibility
with P/N transport. The rank exchange alone does not determine this interface.

## Verification

```sh
python research/strominger/checkers/derive_neutron_belt_field_attachment.py
```

Evidence: `results/neutron-belt-field-attachment/verification.json`.

This reconstructs the existing native belt construction and binds its geometric
slots to the recently derived tensor grid. Underlying geometry, character,
frame and grouping conventions remain explicit source inputs. Production and
viewer unchanged.
