# Grothendieck seam: finite scalar current versus retained modes

## Source pressure

`research/grothendieck/theta-moving-seam-projection-cocycle-nonfredholm.md`
distinguishes a finite scalar interval integral from the uncompressed seam
operator, which retains every `L²` mode supported on a positive-measure
interval.

## Lean increment

`infinite_range_of_fixed_injective_family` proves that an operator fixing an
injectively indexed infinite family has infinite set-theoretic range.

The hostile pairs the identity on `ℕ` with a readout into `Fin 1`.
`finite_scalar_readout_does_not_bound_carrier_range` proves simultaneously
that the scalar image is finite and the retained carrier range is infinite.
This is the exact information-theoretic distinction needed before analytic
operator ideals are introduced.

## Deliberate limit

Infinite set-theoretic range is weaker than infinite linear rank and much
weaker than noncompactness. The exact continuum theorem still needs:

- `L²(ℝ)` and the closed subspace supported on `[-a,0)`;
- an infinite orthonormal family in that subspace;
- the indicator multiplication operator as a continuous linear map;
- the compact-operator criterion showing a compact map cannot fix that
  orthonormal family.

No determinant or Fredholm conclusion is admitted before those interfaces are
present.

## Verification

Per Nima's instruction, no build was run and the module remains outside the
root import.
