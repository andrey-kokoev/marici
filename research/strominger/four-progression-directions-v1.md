# How many native progression directions form?

## Result: two spatial progressions plus realization

The current source grammar supplies three independent repeatable directions,
not four, for its mobile reader markings. The distinction is between an
ambient coordinate direction and a direction that the allowed operations can
actually generate.

A depth-12 native-path search tested all 24 saved seed markings separately.
A repeatable macrostep must restore the full five-point P reference up to a
spatial translation and restore its five-coefficient permutation. Its absolute
origin is retained, not reset.

| Seed markings | Restored spatial displacement rank | Spatial-plus-origin rank |
|---:|---:|---:|
| 8 | 2 | 3 |
| 16 | 0 | 1 |

Each discovered basis word was replayed from its own endpoint. Every replay
repeated the same displacement and origin increment. Twenty-four pairwise
macrostep squares reached exactly the same full packet in either order; their
operation words remain distinct histories.

## Three explicit generators

For marking [0,1,2,3], use the four spatial lattice coordinates whose sum is
fixed. Three independent restored-window advances are:

| Generator | Spatial displacement | Origin increment | Native word length |
|---|---|---:|---:|
| Vertical | (0,0,0,0) | 2 | 2 |
| A | (-2,0,2,0) | 6 | 10 |
| B | (-1,-1,1,1) | 6 | 10 |

The vertical word is two P-reader advances. A repeats
`PN, NN, NN, inverse-PN, P-reader` twice. B repeats
`PN, NN, N-reader, inverse-PN, P-reader` twice.

Their combined displacement/grade vectors have rank three. The two spatial
moves also advance realization; subtracting vertical vectors to draw a
horizontal basis is a linear-span operation, not permission to reverse grade.
These generators do not establish reversible control or independent clocks.

## Why the third spatial progression is absent

The fixed octahedral subdivision distinguishes the height function

```
h(x)=x0+x2.
```

For a mobile reader, M0 and M1 lie in one plane `h=m`. Every live native P/N
successor keeps both M occurrences in that same plane. In particular, every
admitted NN advance adds its new M vertex within that plane. A terminal E
window supplies no further progression.

This was tested exhaustively on translation classes, not merely inferred from
failure to find a longer path:

- both regular-tetrahedron orientations, all 24 ordered markings: 48 P charts;
- all four split-octahedron components and all ordered markings: 48 admitted
  N charts after native reference completion;
- all their native outgoing operations;
- all origin-zero and coefficient-frame representatives suffice because
  availability depends on the marked geometry, while these operations simply
  advance the unrestricted nonnegative origin and permute coefficients.

Integer sum-zero translations add the same constant to all h values and commute
with the local constructors. These are all source primitive templates. The
local preservation checks therefore support induction over arbitrary live
native words under the fixed grammar. Nonplanar N charts have no reader/NN
advance; P re-reading preserves its fixed M pair.

Any restored translated window must consequently obey

```
sum(delta x)=0
and delta x0+delta x2=0.
```

Those are two independent constraints on four lattice displacement coordinates,
leaving two spatial directions. Appending realization gives at most three.
The explicit macrosteps attain that bound in the mobile class.

Changing window shape can visit offsets from the plane, and the collection of
reachable body centroids can have ordinary spatial rank three. That does not
supply a repeatable drift out of the plane: the marked M occurrences remain
constrained. The test does not exclude separately defined internal cycles; it
shows they cannot be inferred as a third generated spatial progression.

## Consequence for the proposed configuration-space dimension

Rigid translation covariance of the tessellation is not controllability of a
window by native moves. Translating a whole decorated neighborhood to another
M-plane remains possible mathematically; the native trajectory does not thereby
acquire a move between the planes.

The presently derived affine progression span has rank three inside the
rank-four ambient space of three spatial displacements plus realization.
This is a codimension-one **displacement constraint**, not yet a continuous
configuration manifold. It does not establish a 5D space with four tangent
progression directions.

A fourth direction would require either a native plane-crossing/subdivision
change with a checked marked field interface, or an independently specified
internal progression coordinate. Neither may be supplied merely by rotating
the entire diagram or relabelling a coefficient slot.

## Verification

```sh
python research/strominger/checkers/check_four_progression_directions.py
python research/aspect/scc/scc.py validate research/strominger/scc-models/four-progression-directions-v1.json
python research/aspect/scc/scc.py check four-progression-directions-v1
```

The Python wrapper freshly replays both Node probes and independently verifies
the witness ranks over rational arithmetic. SCC classifies the task as forward
realization; manifest validation and the bounded model check pass. They are not
physical truth certificates.

Receipts: `results/four-progression-directions/verification.json`,
`leaf-invariant.json`, `rank-verification.json`, and `scc-check.json`.
Protocol: `four-progression-directions-protocol-v1.md`.

Production/viewer unchanged. This follow-up does not alter ledger 4326's frozen
research checkpoint or promote the earlier torus prototype to established geometry.
