# Xi-torsion lift iteration 11: Bohr recovery is not an O-module topology because multiplication by the Xi-normal coordinate destroys almost periodicity

## Correction to the proposed torsion argument

The mean-square Bohr topology of iteration 10 is excellent for recovering
coefficients of

\[
G(z)=\sum_\nu d_\nu e^{z\lambda_\nu}.
\]

It is stable under spectral differentiation because

\[
\partial_zG
=
\sum_\nu\lambda_\nu d_\nu e^{z\lambda_\nu}.
\]

But the Xi-torsion argument also needs multiplication by a local coordinate

\[
u=z-z_0.
\]

On a vertical line `z=R+it`, this sends a character to

\[
(R-z_0+it)e^{R\lambda}e^{it\lambda}.
\]

The factor `t` is unbounded, and its mean-square Bohr norm diverges. Therefore
the recovered exponential-sum space is not an `O_(z_0)`-module.

## Failure of the Weyl setup

The identity

\[
[D,U]=1
\]

requires both differentiation `D` and multiplication `U` to act continuously
on the quotient. Iteration 10 supplies `D` but not `U`. Consequently the
mean-square bordered quotient is not a valid recipient for

\[
\operatorname{Tor}_1^O(Q,O/(\tau))
\]

and the Weyl--Cauchy torsion proof from iteration 7 cannot be run there.

This is independent of the favorable `p^(-3/2)` square-summability budget.

## Multiplication by tau is worse

The Xi factor `tau(z)` is not a finite Bohr character polynomial in the
endpoint frequencies. Multiplying an endpoint exponential sum by `tau`
corresponds, on the transform side, to convolution with the theta spectral
distribution. It generally leaves the discrete-frequency source range.

Thus horizontality under differentiation does not imply that
`J_B(K_B)` is an analytic submodule of the bordered target.

## Local versus global observability conflict

Two useful topologies are now distinct:

1. **Global vertical-line Bohr topology:** gives stable coefficient recovery but
   is not closed under multiplication by the spectral coordinate.
2. **Local analytic-germ topology:** is an `O`-module and supports divisor
   torsion, but restriction to a finite spectral neighborhood does not stably
   recover logarithmic frequencies whose gaps tend to zero.

Simply intersecting the two graph topologies does not fix the problem, because
`U` still fails to preserve the global Bohr seminorm domain.

## What remains valid

- Algebraic frequency uniqueness and opposite-chart recovery remain proved.
- `H_border` belongs to a mean-square Fourier-recoverable linear range for the
  mixed loading.
- The range is horizontal under the connection.
- No conclusion about Xi-divisor torsion follows from that range topology.

Hence objectives 1 and 2 can coexist as statements about a differential linear
space, but objective 3 is not equivalent unless the source range is also an
analytic module.

## Possible repairs

A successful topology must either:

1. enlarge the source from discrete measures to their polynomial-jet module,
   retaining derivatives of point masses so multiplication by `z` is typed;
2. use a weighted finite-window observer that admits coordinate multiplication
   and prove a uniform nonharmonic-frame estimate; or
3. construct a separate strict local analytic module and a compatible map from
   the globally recoverable coefficients.

The first is the most concrete next test: adjoining frequency-derivative jets
turns `z e^(z lambda)` into a labelled first-jet atom rather than ejecting it
from the source category.