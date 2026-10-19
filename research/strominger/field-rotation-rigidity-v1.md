# Rotations of the 36-component coherence fields

## The question has three meanings

1. **Internal stabilizer:** change the field while keeping its metric and
   structural operators fixed.
2. **Fixed geometric automorphism:** rotate a carrier onto itself, carrying
   its patches and vector components with it.
3. **Covariant reorientation:** rotate the entire carrier, frames and operators
   together. Any SO(3) reorientation preserves its internal geometric relations,
   but this is not a symmetry commuting with fixed operators, nor an admitted
   motion through a fixed tessellation.

This test classifies the first two. The third is ordinary rigid-body covariance,
not evidence for additional native progression directions.

## Internal freedom shrinks as structure is retained

The exact joint L/G sector dimensions are P: (1,11,2,22) and N: (1,2,11,22).
Consequently both projector-only stabilizers are abstractly

```
U(1) x U(11) x U(2) x U(22), real dimension 610.
```

These are field-basis freedoms, not 610 spatial directions.

For the continuous identity component that fixes each patch support:

| Retained data | P | N |
|---|---|---|
| Metric, L/G, patch support blocks | U(1) x U(2), dimension 5 | U(1)^7, dimension 7 |
| Also P tangent/normal splitting | U(1)^3 | Already intrinsic tangent planes |
| Also ordered corner-cycle operators | Common U(1) only | Common U(1) only |

For P, G forces every patch unitary to be the same unitary V in its co-moving
three-dimensional frame. L requires V to preserve one complex line, leaving
U(1) x U(2). Preserving the normal line splits the remaining two-dimensional
space into two one-dimensional lines.

For N, G ties three copies of each reference patch. In each of six reference
patches there are two unitary eigenphases. L's coherent selected vector has
nonzero support on every patch and forces its six selected-line phases to
agree; the six orthogonal-line phases remain independent.

Thus a **five-real-parameter P stabilizer does appear at an intermediate level**.
Its four U(2) parameters plus one selected-line phase are internal freedoms of
an incomplete structural specification, not the proposed five-dimensional
configuration space. The ordered corner data removes the extra freedom.

### Why the cycle constraint is genuinely stronger

The P corner cycle is X C X^{-1}, where X contains the actual ordered triangle
corners. Its three simple eigenvectors are not mutually orthogonal; their
metric-overlap graph is connected on every patch. A commuting unitary can only
multiply each eigenvector by a phase, and preservation of each nonzero overlap
forces those phases to coincide.

The N intrinsic two-dimensional cycle has eigenvalues omega and conjugate
omega. Its two eigenvectors have nonzero metric overlap on all 18 patches.
Their phases must therefore coincide as well. Native G/L transport then ties
the patch phases into one common phase.

These corner cycles encode the oriented algebraic construction; they are not
claimed to be Euclidean rigid rotations or native P/N reader-advance operations.
The rigidity conclusion explicitly assumes this ordered data is retained.

The checker also constructs actual patch-local unitary hostiles on both
carriers: they preserve metric, L and G but fail the cycle commutator. The
additional constraint is therefore not redundant.

## Fixed geometric symmetries

All 24 P vertex permutations and all 720 N vertex permutations were tested
against the actual squared distances and carrier faces. Their induced complete
field maps were then tested exactly against the native metric and L/G.

| Native geometry | Metric/face isometries | Linear projector and forward-cycle symmetries |
|---|---:|---:|
| P tetrahedron | 24 | 12, tetrahedral rotation group A4 |
| N belt | 12 | 6, dihedral rotation group D3 |

The proper P group has one identity, three order-two and eight order-three
elements. N has one identity, three order-two and two order-three elements.

P's other 12 isometries preserve the projectors only with antiunitary conjugation;
they reverse the corner cycle. N's six improper isometries exchange the declared
adjacent-face matching: even antiunitary conjugation preserves the return line
and G but fails L. Keeping only the return vector would miss this obstruction.

Markings restrict these groups further. Requiring the fixed P body C/M role
partition leaves two proper elements. Requiring the fixed N reader's four-body
C/M partition leaves only the identity. These tests do not include every outside
context, and geometric symmetry still does not certify native path availability.

## New obstruction: PN cannot identify the geometric C3 actions

Suppose an invertible conversion S satisfies both

```
S G_P = L_N S
S U_P = U_N S,
```

where U_P and U_N are geometric order-three rotations of their carriers.
Then the restrictions to the corresponding three-dimensional projector images
would be similar and must have the same trace.

Exact calculation gives

```
trace(G_P U_P) = 3
trace(L_N U_N) = 0.
```

This was checked for all eight P and both N geometric order-three actions.
P's co-moving alignment modes are fixed; N's three local sector modes cycle.
The contradiction is independent of the chosen PN complement-frame rotations.

Therefore the earlier algebraic PN candidate is **not** an identification of
these geometric rotations. It may transport a P geometric symmetry into a
different internal N action preserving the projectors, but that is not yet
shown to preserve the detailed N patch/corner structure.

## Sharp next question

Which part of the PN interface must change when a geometric P rotation becomes
an internal N transformation: patch assignments, cyclic orientation, sector
matching, or the L/G exchange itself?

That is now a more discriminating question than counting ambient dimensions.
There is no derived family of four continuous internal rotations preserving
all the presently retained structure.

## Replay and scope

```
python research/strominger/checkers/check_field_rotation_rigidity.py
python research/aspect/scc/scc.py validate research/strominger/scc-models/field-rotation-rigidity-v1.json
python research/aspect/scc/scc.py check field-rotation-rigidity-v1
```

Exact native replay, SCC validation and model check pass. Receipts are in
`results/field-rotation-rigidity/verification.json` and `scc-check.json`.
The prospective scope is in `field-rotation-rigidity-protocol-v1.md`.

This is an attachment-transport/readout-compatibility result for the supplied
native decorated geometries. It does not establish physical spin, new spacetime
dimensions, a 5D configuration manifold, or permitted forward spatial moves.
Production/viewer and ledger4326's frozen checkpoint are unchanged.
