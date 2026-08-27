# One Green Fold Does Not Orient the Oscillatory Transform

## Hostile source

Consider the positive, even, strictly decreasing source on the positive chart

\[
\Psi(u)=e^{-u^2}+e^{-2u^2}.
\]

It has the same elementary regularity and monotonicity properties used in the
theta half-transform argument.

## Exactly one Green-curvature fold

For \(L=D^2-1/4\), put \(v=u^2\). Direct differentiation gives

\[
L\Psi(u)=e^{-2v}h(v),
\]

where

\[
h(v)=(4v-9/4)e^v+16v-17/4.
\]

Now

\[
h(0)=-13/2
\]

and

\[
h'(v)=e^v(4v+7/4)+16>0
\qquad(v\ge0).
\]

Therefore \(L\Psi\) has exactly one sign transition, from a negative central
band to a positive tail. This is the same unsigned fold type just proved for
the theta source.

## Exact off-axis transform zeros

Up to the nonzero factor \(\sqrt\pi\), the bilateral Fourier transform is

\[
F(z)=e^{-z^2/4}+\frac1{\sqrt2}e^{-z^2/8}.
\]

Its zeros satisfy

\[
e^{-z^2/8}=-\frac1{\sqrt2},
\]

and hence

\[
z^2=4\log2-8(2k+1)\pi i,
\qquad k\in\mathbb Z.
\]

Every such square has nonzero real and imaginary parts. Its square roots are
therefore off both coordinate axes. The completed oscillatory transform has
off-axis zeros despite the unique Green fold.

## Consequence

The following package is insufficient for zero confinement:

- positive even source;
- strict decrease on the positive chart;
- one negative Green-curvature band;
- positive Green-curvature tail;
- canonical polar boundary completion.

Entry 3263 remains a genuine theta theorem, but it cannot by itself orient the
oscillatory transform. The missing force must use arithmetic information absent
from a two-Gaussian mixture: the labelled lattice recursion, Poisson transport,
or their higher coherence cell before scalar aggregation.

This closes any attempted proof that promotes one-fold Green geometry alone
to RH.

