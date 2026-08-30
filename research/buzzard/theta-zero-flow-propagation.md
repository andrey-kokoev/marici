# Theta zero-flow propagation boundary: Lean packet

## Source boundary

This increment reads Grothendieck's frozen
`small-theta-windows-have-a-globally-real-divisor.md` together with the prior
finite-parameter no-influx packet. The analytic results are represented as
separate premises. No collision-exclusion conclusion is assumed.

## Formal objects and assumptions

`ZeroFormationBoundary` is indexed by `Nat`, representing a discrete ordered
chain of finite support windows. Its three predicates record an off-seam zero,
a finite collision, and influx through the selected exhaustion boundary. The
`formation` field says that an off-seam zero at the next stage must be inherited
from the previous stage or explained by one of the latter two mechanisms.

`InitiallyReal`, `CollisionFreeFlow`, and `NoInfluxFlow` are distinct
propositions. There is no coefficient type: this is the logical propagation
layer after the complex-analytic zero-family results have supplied those
predicates and the formation alternative.

## Theorem and hostile countermodels

`offSeam_absent_of_initial_noInflux_collisionFree` proves by induction that
initial reality, absence of influx, and collision freedom imply absence of
off-seam zeros at every finite stage.

Three finite-state models show that every premise is necessary:

- `collision_gate_cannot_be_omitted` starts real and has no influx, then creates
  an off-seam zero through a collision;
- `noInflux_gate_cannot_be_omitted` starts real and is collision-free, then
  creates an off-seam zero through influx;
- `initial_reality_gate_cannot_be_omitted` has neither collision nor influx but
  begins with an off-seam zero.

Thus the frozen small-window and no-influx theorems do not prove the remaining
collision condition. After accepting the analytic formation alternative, that
condition is the sole open formation gate in this reduction.

## Missing analytic interfaces

A faithful theta instantiation still needs a continuous positive-real support
parameter, complex zeros with multiplicity, local continuation of simple zeros,
the first-bad-parameter argument, and the proof that first off-seam formation is
exhausted by collision or influx. The frozen source packet supplies the
small-window Rouché theorem, remote Rouché control, and Hurwitz bridge at the
mathematical level, but those analytic proofs are not encoded in Lean here.
Finite exclusion of simultaneous vanishing of the two collision integrals is
explicitly open and must not be imported as a premise disguised as theta
structure.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/ThetaZeroFlowPropagation.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
