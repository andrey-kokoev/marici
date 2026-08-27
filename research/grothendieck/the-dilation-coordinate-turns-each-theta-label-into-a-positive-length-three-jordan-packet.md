# The Dilation Coordinate Turns Each Theta Label into a Positive Length-Three Jordan Packet

## The apparent signed grade

On the positive modular chamber the completed theta forcing is

\[
\Phi(u)=e^{u/2}\sum_{n\geq1}
\left(4x_n(u)^2-6x_n(u)\right)e^{-x_n(u)},
\qquad
x_n(u)=\pi n^2e^{2u}.
\]

In the moment frame this is the signed readout

\[
\Phi=4M_2-6M_1.
\]

That sign is real, but it is not the final source geometry.

## Source-native coordinate and half-density

Put

\[
y=e^{2u}-1,
\qquad
\lambda_n=\pi n^2.
\]

Then `y` is nonnegative on the positive chamber and

\[
e^{u/2}=(1+y)^{1/4}.
\]

Remove this common quarter-density by defining

\[
\Psi(y)=(1+y)^{-1/4}\Phi\left(\frac12\log(1+y)\right).
\]

Each arithmetic label becomes

\[
\Psi_n(y)
=
e^{-\lambda_n}
\left(A_{0,n}+A_{1,n}y+A_{2,n}y^2\right)e^{-\lambda_n y},
\]

where

\[
\begin{aligned}
A_{0,n}&=4\lambda_n^2-6\lambda_n,\\
A_{1,n}&=8\lambda_n^2-6\lambda_n,\\
A_{2,n}&=4\lambda_n^2.
\end{aligned}
\]

The arithmetic support gap gives

\[
\lambda_n=\pi n^2>\frac32.
\]

Therefore every coefficient is strictly positive. The signed two-grade
moment readout has become a positive length-three Jordan packet for every
label.

## Finite differential closure

For

\[
e_{n,j}(y)=y^j e^{-\lambda_n y},
\qquad
j=0,1,2,
\]

ordinary differentiation obeys

\[
\partial_y e_{n,j}
=
j e_{n,j-1}-\lambda_n e_{n,j}.
\]

Thus each label is a three-dimensional invariant Jordan block. In the
original logarithmic coordinate, differentiation raised the infinite moment
grade. The dilation coordinate rotates that infinite raising presentation
into a finite nilpotent chain.

This is the promised extra comparison channel: the coefficient sign cannot
be interpreted before carrying the coordinate and half-density that generated
the completed source.

## What this does not yet prove

The positive exponential endpoint theorem was derived for scalar modes under
a constant-coefficient logarithmic tail operator. Under the coordinate change,

\[
\partial_u=2(1+y)\partial_y,
\]

and half-density conjugation adds its own connection term. Therefore the old
rank-two Gram formula cannot simply be copied onto the Jordan packets.

The next exact calculation is the Green identity for one positive
three-dimensional block under the transported operator. It must decide
whether the nilpotent off-diagonal entries contribute:

- an additional positive square;
- an exact endpoint current; or
- an indefinite residual.

The single-label block at `lambda=pi` is the smallest hostile test. Failure
there closes this extension without requiring any arithmetic aggregation.

## Result

The negative coefficient in `4M_2-6M_1` is repaired labelwise by the
source-native dilation coordinate, the quarter-density, and the arithmetic
support wall `lambda >= pi`. The theta source belongs to a positive
length-three exponential Jordan cone, although not to the scalar positive
exponential cone. The remaining obstruction is the transported Green form of
that Jordan cone.

