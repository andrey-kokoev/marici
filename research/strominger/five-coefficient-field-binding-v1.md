# Binding the five native coefficients to the transported field

Let B_r map a native five-component vector into its 36-component field at
origin r. For native coefficient permutation Pi and field transport U, require

```
U B_r = B_(r+1) Pi.
```

All statements below specify the field-frame convention; different conventions
are not silently equated.

## P: a fixed norm-preserving embedding exists

The geometric 36-component P reader transport has 18 signed two-cycles. The
native five-slot permutation has two two-cycles and one fixed coordinate.
Matching two field orbits to the coefficient pairs, and a normalized invariant
vector in a third orbit to the fixed coordinate, constructs a complex-linear
isometric B satisfying `UB=B Pi_P` exactly.

This is an existence construction, not a preferred geometric selection of the
three field orbits. Many embeddings satisfy the same transport constraint.

## N: the embedding must track phase under the ordered-corner convention

For the ordered-corner, co-moving field convention, U=I. A fixed B would obey
`B=B Pi_N`. Since Pi_N fixes slot 0 and swaps 1/3 and 2/4, this forces equal
columns within those pairs. Its rank is at most 3, so it loses two of the five
independent complex coefficients.

This rank-three bound concerns the fixed subspace of a five-slot permutation;
it is not a new derivation of the native rank-three field projector.

A phase-dependent binding avoids the loss:

```
B_(r+1) = B_r Pi_N
B_(r+1) Pi_N = B_r.
```

Two distinct exact norm-preserving seeds were constructed using five of six
native field slots having metric weight 1/2, with amplitudes scaled by sqrt(2).
Both preserve all five coefficients and satisfy the transport equation through
28 advances. Both return to their original embedding after two steps, while
absolute origin and operation history remain distinct.

The two successful seeds demonstrate nonuniqueness: transport plus norm alone
does not select the physical coupling. No five-dimensional L/G operators were
specified, so this does not claim the embeddings reduce the full projector
pair or derive the native five-slot dynamics from it.

## Outward-oriented alternative

With the outward-positive-character field convention, NN transport is
antiunitary. No nonzero pair of complex-linear bindings B_source,B_target can
intertwine an antiunitary map with the native complex-linear Pi on all complex
inputs: replacing x by ix gives opposite signs on the two sides.

An alternating semilinear chart convention could reconcile them, but is
additional structure. The native five-slot permutation itself was not changed.

## Disposition

There is an explicit norm-preserving, phase-aware algebraic connection that
retains all five coefficients. A fixed N identification in the ordered frame
cannot do so. The remaining derivation is a source-geometric choice of B_0,
compatible with PN/NE transfers and the native local modes, rather than an
arbitrary selection of field slots.

This is not yet a global sewn PNE field. Production/viewer unchanged.

```sh
python research/strominger/checkers/check_five_coefficient_field_binding.py
```

Evidence: `results/five-coefficient-field-binding/verification.json`.
