# The endpoint-split Gaussian-atom jet is an L2-history-valued holomorphic graph

## Why the entire unsplit tower is not a history state

For

\[
H_x(t)=2\exp(e^{2x}(t-\pi)),
\]

the value at `t=0` tends to `2` as `x -> -infinity`, so the unsplit section is
not in `L2(R_x)`.  For `Re(t)>pi` it also grows superexponentially as
`x -> +infinity`.  Hence `O(C_t)` is a valid pointwise jet carrier but cannot
be tensored naively with the whole-line C_FP history pivot.

## Endpoint split

Retain

\[
h_0(x)=H_x(0)=2e^{-\pi e^{2x}}
\]

as the endpoint/boundary coordinate and define

\[
\widetilde H_x(t)=H_x(t)-H_x(0)
=2e^{-\pi e^{2x}}(e^{e^{2x}t}-1).
\]

Fix `0<r<pi` and let `O_0(D_r)` be the holomorphic functions on the disc
`|t|<r` vanishing at zero, with its compact-open Frechet topology.  On every
smaller closed disc `|t|<=r'<r`, `widetilde H` and all of its `x` derivatives
are square-integrable in `x`: at `-infinity` the subtraction gives
`O(e^(2x))`, while at `+infinity` the bound `Re(t)<=r'<pi` leaves exponential
factor `exp(-(pi-r')e^(2x))`.

Thus the physical bulk jet is an element of the projective graph carrier

\[
\mathcal X_r
=H^1(\mathbb R_x;\mathcal O_0(D_r)),
\]

under the seminorms obtained by taking the `H1_x` norm uniformly on compact
subdiscs.

## Boundary-corrected connection

Subtracting the endpoint equation from

\[
\partial_xH=(2t-2\pi)\partial_tH
\]

gives

\[
\partial_x\widetilde H
=(2t-2\pi)\partial_t\widetilde H
+2\pi\,\partial_t\widetilde H(0).
\]

The final term is the endpoint return needed to keep the right side zero at
`t=0`.  Derivative evaluation at zero is continuous on `O(D_r)` by Cauchy
estimates.  Therefore

\[
\widetilde\nabla_x
=\partial_x-(2t-2\pi)\partial_t
-2\pi\operatorname{ev}_0\partial_t
\]

is a continuous map from the declared graph domain to the corresponding
`L2_x`-valued holomorphic carrier, and `widetilde nabla_x widetilde H=0`.

## Claim boundary

This constructs a common whole-line history/jet graph for the single Gaussian
atom only after separating its non-L2 endpoint mode. It is not yet the
completed theta forcing: each labelled theta summand has an additional
polynomial prefactor and the sum over labels requires normal-convergence
bounds. It does not yet prove that arithmetic incidence and Schur return
extend continuously, nor that the projective limit `r -> pi` is nuclear or
determinant class.

## Disposition

For this Gaussian atom the correct domain is not `H1(R) tensor O(C)`, but the
endpoint-split projective family `H1(R;O_0(D_r))`, `r<pi`, together with the
retained endpoint coordinate. The boundary correction is forced. Promoting
this local model to the completed theta source remains open.
