# Moving-window field transport and orientation

## Native geometric probe

Enumerated native paths to depth six from all 24 seed markings and computed
the signed affine determinant between ordered four-vertex source/target cells.
The spatial hyperplane is represented by its first three coordinates; determinant
ratios do not depend on that common coordinate choice.

- 312 P same-body advances: orientation preserving.
- 224 N same-body advances: orientation preserving.
- 224 NN spatial advances: orientation reversing.

These are bounded edge checks, not counts of distinct global physical histories.
The earlier depth-28 test established preservation of the ordered cell metrics.

## Full P transport constructed

Under the marked P same-body advance, the tetrahedron's vertices undergo the
proper rotation `(A C)(B D)`. Applying this rotation to patch labels and their
three spatial vector components gives an explicit 36-by-36 signed-permutation
operator U. Exact checks show

```
U* U = I
U^2 = I
L U = U L
G U = U G
N U = U N.
```

This transports all amplitudes, not only the surviving line. It is a genuine
field symmetry derived from the geometric patch construction. Neither U squared
nor the geometric return resets absolute origin or erases history.

## NN transport depends on the orientation convention

An improper spatial isometry transports an outward ordered triangle into an
inward ordered triangle. There are two distinct conventions:

### Carry the ordered corners

Transport their order and the derived plane axes unchanged. Then the
co-moving field coordinates have U=I, and the geometric L/G/metric constructor
is unchanged. A face-orientation sign flips at each NN move and must remain in
the chart data. This is a linear field convention, not a fixed-outward one.

### Restore outward orientation and retain the positive cyclic character

Reverse the two outer corners after reflecting. If the old ambient mode is
`r + i sqrt(3) s`, the new one is `O r - i sqrt(3) O s`. In the derived intrinsic
axes its numerator is

```
z_new = D conjugate(z_old),  D = diag(-1,+1) per patch.
```

This was recomputed directly from all 18 reflected belt patches, not merely
assumed as an operator transformation. All induced metric denominators agree.
The resulting operators satisfy

```
L_new = D conjugate(L_old) D
G_new = G_old
N_new = D conjugate(N_old) D.
```

The spatial-only linear map D fails the L intertwining equation; an exact
coefficient witness is retained. The antiunitary map `D conjugation` intertwines
all three full 36-coordinate operators and preserves the real diagonal metric.
Two copies of this abstract reflection map square to identity. This is not a
claim that two arbitrary spatial NN steps return to the same location.

## Consequence for the conjecture

The local field structure repeats under translations, and full P reader
transport is constructed. For NN moves, “same structure” must specify whether
the chart carries its ordered orientation or restores outward orientation.
The first admits linear co-moving transport with an orientation bit; the
second uses the checked conjugating transport.

The native five-slot NN action is a complex-linear permutation. This work does
not reinterpret it as antiunitary. A binding between those five coefficients
and the 36-component field, selecting a compatible convention and checking
path compositions, remains open. No global PNE field or torus topology follows.

```sh
node research/strominger/checkers/probe_reader_transport_orientation.mjs
python research/strominger/checkers/check_reader_field_transport.py
```

Evidence: `results/reader-field-transport/orientation.json` and
`field-verification.json`. Production/viewer unchanged.
