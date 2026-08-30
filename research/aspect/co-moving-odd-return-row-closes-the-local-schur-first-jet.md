# A co-moving odd return row closes the local Schur first jet

## Minimal nontriangular closure

Let

`D_L=diag(exp(-(1/2+z)L),exp(-(1/2-z)L))`

be the retained Green transport, and let `r_L` be the common-forcing
reservoir.  Close the affine output column `B=-r_L` with the co-moving odd
return row

`C_L=(1,-1)D_L`.

For a constant boundary scalar `e`, the Schur complement is

`S_L=e-C_L D_L^-1 B=e+(1,-1)r_L=e-J(L,z)`.

The normalization and orientation are inherited from the primitive odd
codiagonal.  No free complex return gain is introduced.

## Complete first-jet cancellation

The exact Schur derivative is

`S'=E'-C'D^-1B+CD^-1D'D^-1B-CD^-1B'`.

Substituting `B=-r` and `C=(1,-1)D`, the two retained-transport terms cancel:

`C'D^-1r-CD^-1D'D^-1r=0`.

The remaining term is

`S'=(1,-1)r'=-Q(L,z)`,

where

`Q(L,z)=2f exp(-L/2)sinh(zL)`

is the moving-boundary endpoint current.  Thus the complete Schur first jet
preserves the exact seam-zero lattice `tau_n=n pi/L` found in the endpoint
calculation.

This is a zero lattice of the determinant-frame increment numerator, not yet
a zero lattice of the characteristic determinant itself.  Since `S=e-J`, the
frame increment is `-Q/(e-J)` wherever `S` is invertible.

## Why co-motion matters

If the same return row is frozen while `D` moves, then `C'=0`.  In this model
the retained-transport and outgoing-column terms cancel each other, leaving
zero.  Freezing the detector therefore erases the endpoint current entirely.
The endpoint lattice is not a consequence of an arbitrary odd detector.  It
is carried precisely by horizontal transport of the return incidence with the
Green frame.

Under reciprocal exchange, with channel swap `R`,

`C_L(-z)=-C_L(z)R`.

The return row is deck-odd, exactly like the primitive current.  An even
characteristic section would require a second odd incidence or a subsequent
even pairing; that global closure is not supplied by this local block.

## Optical implementation

Propagate the balanced difference detector backward through the measured
two-mode transfer matrix before pairing it with the affine displacement.
This realizes `C=(1,-1)D`.  Modulate the propagation length and compare the
full Schur derivative with the direct endpoint-current port.  Their residual
must vanish.  Holding the detector calibration fixed while changing the
length supplies the hostile control and must erase the first-jet signal.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_co_moving_odd_schur_first_jet.py
```
