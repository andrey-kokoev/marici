# Theta parabolic forcing residual: Lean packet

## Source boundary

This increment formalizes the finite adjoint-line statement from
Grothendieck's `theta-forcing-is-the-exact-parabolic-confinement-residual.md`.
It does not solve or assume the tail differential equation.

## Formal objects and assumptions

Over an arbitrary commutative ring, a two-channel tail covector is a row with
endpoint and constant coordinates. `tailAdjointAction z f` is right
multiplication by the triangular generator

\[
\begin{pmatrix}-z&-f\\0&0\end{pmatrix}.
\]

`SpansInvariantAdjointLine action ell` supplies an explicit scalar rate whose
multiple equals the transported covector.

## Theorems and hostile

- `endpointTailCovector_invariant_iff_forcing_zero` proves that the endpoint
  covector `(1,0)` spans an invariant line exactly when `f=0`.
- `constantTailCovector_always_invariant` proves that `(0,1)` remains
  invariant for every forcing value.
- `nonzero_forcing_breaks_endpoint_but_not_constant` instantiates `z=2`,
  `f=1` over the rationals. Replacing the failed endpoint readout by the
  surviving constant channel would change the observable.

## Missing interfaces

The continuous theorem needs differentiable state and moving-covector
families, a typed nonautonomous generator, existence/uniqueness for the
evolution equation, and the exponential nonvanishing consequence for an
independently nonzero anchor. The theta specialization needs the source tail
integral and proof that its forcing coordinate is the completed density. A
reciprocal enlarged flag cancelling all labelled residuals is an active
RH-strength conjectural input and is not assumed. A covector reconstructed
from the final scalar solution is explicitly inadmissible source authority.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/ParabolicForcingResidual.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
