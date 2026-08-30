# Finite-parameter theta no-influx interface: Lean packet

## Source boundary

This increment reads Grothendieck's frozen packets
`completed-theta-truncations-turn-rh-into-zero-flow.md` and
`finite-theta-truncations-have-no-influx-from-infinity.md`. It formalizes the
logical consequence of uniform remote real/simple control on a compact
positive parameter interval. It does not assume or reprove the analytic
endpoint expansion or Rouché theorem.

## Formal objects and coefficient types

Parameter and zero types are arbitrary. `zeroAt L z` is a typed zero-family
relation; `height z : ℕ` supplies a discrete exhaustion proxy.
`RemoteZeroControl` contains one uniform radius and separate remote-reality
and remote-simplicity fields. `SpectralInflux` means nonreal zeros occur above
every radius in the admitted parameter region. `CollisionFree` is a separate
global simplicity condition.

## Theorems and hostiles

- `simpleZero_velocity_eq` proves the exact implicit velocity formula from
  the differentiated zero equation and a nonzero spectral derivative.
- `missing_simpleZero_hostile` shows that when both derivatives vanish, two
  distinct velocities satisfy the same chain equation.
- `no_spectralInflux_of_remoteZeroControl` proves that uniform remote reality
  rules out nonreal influx from infinity.
- `noInflux_does_not_imply_collisionFree` supplies a bounded family with a
  nonsimple zero and no influx.
- `collisionFree_does_not_imply_noInflux` supplies an unbounded family of
  simple nonreal zeros, proving the converse implication also fails.

Thus finite-λ no-influx and collision exclusion are independent conditions.
The singular initial boundary is outside the admitted compact positive
parameter region rather than silently treated as an ordinary parameter.

## Missing interfaces

For theta truncations, `Parameter` must be positive real support length and
`Zero` complex spectral position, with modulus as exhaustion. Establishing
`RemoteZeroControl` requires the twice-integrated endpoint expansion,
uniform positive lower bound for `Phi(L)`, uniform remainder estimates,
rectangular-contour Rouché counting, conjugation-invariant lattice disks, and
the simple-real uniqueness conclusion. The completed-support statement needs
compact-open convergence and Hurwitz with multiplicities. The `L↓0` rescaled
divisor and finite collision equations remain independent RH-bearing gates.
Instantiating the velocity law additionally needs differentiation under the
integral and the exact formulas for both partial derivatives.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/FiniteParameterNoInflux.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
