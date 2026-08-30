# Symmetric-window exterior flux: Lean packet

## Source boundary

This increment formalizes the exact finite cancellation in Grothendieck's
`newman-symmetric-window-flux-cancellation.md`. It does not claim the analytic
fourth-inverse-moment bound or an infinite-window limit.

## Formal objects and coefficient types

For an arbitrary commutative ring `K`, arbitrary index type `I`, finite index
set, and coordinate families `roots defect : I → K`, `finitePairing` is the
finite coordinate pairing. The leading exterior field is the scalar multiple
`-4 * moment2 * roots`.

## Theorems and hostile

- `leadingExterior_cancels_of_scaleOrthogonal` proves that the leading
  second-moment field pairs to zero with every scale-orthogonal defect.
- `exteriorFlux_reduces_to_remainder` proves the exact reduction of total
  exterior flux to its remainder.
- `symmetricPairForce_formula` and
  `symmetricPairForce_secondMoment_remainder` prove the exact rational
  pair-force and fourth-moment remainder identities under explicit pole and
  gap assumptions.
- `missing_scaleOrthogonality_hostile` uses one rational coordinate to show
  that without scale orthogonality the leading contribution is `-4`, not zero.

## Missing interfaces

The fourth-moment estimate needs an ordered normed field, positive exterior
ordinates, a uniform gap `X < Y`, absolute values, and finite-dimensional
Cauchy--Schwarz. The algebraic denominator assumptions are explicit in the
pair theorems.
The Xi specialization additionally needs source-derived real ordered roots;
it cannot be used to infer them. Boundary-layer and infinite-window arguments
remain analytic gates.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/SymmetricWindowFluxCancellation.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
