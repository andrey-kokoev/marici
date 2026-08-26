# Valuation square current and quarter-density lift: Lean packet

## Source boundary

This increment formalizes the finite coefficient identities in Grothendieck's
`exclusion-plus-valuation-degree-renormalizes-to-the-square-current.md` and
`positive-staircase-curvature-forces-a-quarter-density-lift.md`.

## Formal objects and coefficient types

The valuation layer uses natural-number multiplicities. Primitive exclusion is
one at valuation zero and zero otherwise; valuation degree is the valuation;
renormalization subtracts the universal identity multiplicity using natural
subtraction. The square current is valuation minus one.

The transport audit uses rational exponents. A depth-`k` quadratic transport
with exponent `alpha` has exponent `2*alpha*k`; the desired linear
half-density staircase exponent is `k/2`.

## Theorems and hostile examples

- `boundary_plus_degree_is_gapped` proves the unrenormalized local channel is
  at least one.
- `renormalized_eq_squareCurrent` proves exact equality with the
  square-and-higher multiplicity.
- `squareCurrent_kernel_iff_squarefreeLocal` identifies the local kernel with
  valuations zero or one.
- `squarefree_nonfaithful_hostile` shows a nonvacuum squarefree label survives
  in that kernel.
- `allDepth_matching_iff_quarterDensity` proves that matching every depth is
  equivalent to transport exponent one quarter.
- `naiveHalfDensity_depthTwo_hostile` detects the direct half-density error at
  the first square channel.

The results preserve two distinctions: a positive gapped unrenormalized port
becomes nonfaithful after universal-line subtraction, and a linear amplitude
cannot be used unchanged as a quadratic transport coefficient.

## Missing interfaces

The arithmetic specialization needs finite prime factorizations and the
identity between valuation and counts of prime-power divisibility projections.
The operator specialization needs the positive-integer `ℓ²` space, commuting
valuation number operators, convergence/domain control for the projection sum,
and logarithmic prime weights. A source-authorized determinant, Pfaffian, Fock,
or correspondence construction producing the quarter-density lift is absent.
No scalar-zero confinement conclusion follows from these coefficient identities.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/ValuationSquareCurrent.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
