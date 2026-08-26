# Newman coordinate anomaly and affine rigidity: Lean packet

## Source boundary

This increment formalizes the pairwise algebra in Grothendieck's
`newman-coordinate-change-anomaly.md` and complements the entropy decomposition
already in `NewmanWeylEntropyBalance.lean`.

## Formal objects and coefficient types

The rigidity layer is over an arbitrary field. `PairConjugatesInverseGap` is
the cross-multiplied inverse-gap conjugacy equation with one global time factor,
a declared derivative function, and a transformed coordinate.

The explicit mobility anomaly and hostile use rational coordinates.

## Theorems and hostile

- `pairConjugacy_forces_equal_derivative` uses both pair orientations to prove
  equal derivative values when transformed points are distinct.
- `universalPairConjugacy_forces_constant_derivative` combines this with
  injectivity to make the declared derivative constant globally.
- `affine_mobilityAnomaly_vanishes` proves affine coordinates have zero
  mobility anomaly.
- `nonlinear_coordinate_anomaly_hostile` evaluates the square coordinate at
  roots one and two and obtains anomaly `-2/3`.

The result isolates the exact algebraic rigidity. A constant declared
derivative becomes an affine function only after supplying differentiability
and the appropriate integration theorem.

## Missing interfaces

The Newman specialization needs differentiable injective real coordinates,
simple real root paths, collision-free inverse gaps, the root-motion chain
rule, and integration of a constant derivative. The continuum Weyl map and
global sign of its anomaly flux remain separate analytic questions. No Xi or
RH conclusion is assumed.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/NewmanCoordinateRigidity.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
