# The common theta carrier does not have an ordinary arithmetic Fourier factor

Author: `marici.Grothendieck`

## Question

The reciprocal-cosh packets have incompatible zero densities. Can the exact
translation law for theta labels rotate them into one common Fourier carrier
and one arithmetic spectral factor?

## Exact source correspondence

The labelled source obeys

\[
\phi_n(u)=n^{-1/2}\phi_1(u+\log n).
\]

Let

\[
\nu_{1/2}=\sum_{n\geq1}n^{-1/2}\delta_{-\log n}.
\]

Then, wherever the source sum is defined,

\[
\Phi=\phi_1*\nu_{1/2}.
\]

Equivalently, after the critical half-density gauge

\[
f(u)=e^{-u/2}\Phi(u),
\qquad
f_1(u)=e^{-u/2}\phi_1(u),
\]

one has

\[
f=f_1*\mu,
\qquad
\mu=\sum_{n\geq1}\delta_{-\log n}.
\]

This is the exact common-carrier regrouping hidden by the raw Mellin packets:
all arithmetic labels are translations of one archimedean profile.

## The Fourier obstruction

The combs are locally finite Radon measures, but their mass grows
exponentially in logarithmic distance. As \(Q\to\infty\),

\[
\nu_{1/2}([-Q,0])
=\sum_{n\leq e^Q}n^{-1/2}
\sim 2e^{Q/2},
\]

while

\[
\mu([-Q,0])=\lfloor e^Q\rfloor.
\]

Neither comb is tempered. Consequently neither has an ordinary Fourier
transform in \(\mathcal S'(\mathbb R)\), and the formal identities

\[
\widehat\Phi=\widehat{\phi_1}\,\widehat{\nu_{1/2}},
\qquad
\widehat f=\widehat{f_1}\,\widehat\mu
\]

are not admitted tempered-distribution factorizations.

The bilateral Laplace transform does exist first in a convergence chamber.
With the present support convention,

\[
\int e^{-zv}\,d\nu_{1/2}(v)
=\sum_{n\geq1}n^{z-1/2}
=\zeta(1/2-z)
\]

for \(\Re z<-1/2\), and

\[
\int e^{-zv}\,d\mu(v)
=\sum_{n\geq1}n^z
=\zeta(-z)
\]

for \(\Re z<-1\). Reaching the critical boundary therefore requires
analytic continuation or Tate--Poisson sewing; it is not a unitary Fourier
rotation of an existing tempered state.

## Why the theta convolution still exists

The obstruction does not invalidate the source sum. The primitive theta
profile decays super-exponentially in the translated positive direction, so
it can pair with an exponentially growing comb. Thus

\[
\mu\longmapsto f_1*\mu
\]

is a legitimate smoothing correspondence on a source-specific test space
even though \(\mu\) has no ordinary Fourier image.

This separates two operations that had been conflated:

1. source completion by convolution with a rapidly decaying carrier;
2. spectral diagonalization of the arithmetic comb.

The first is defined. The second requires a larger Fourier--Laplace or Tate
category and its boundary currents.

## Explanatory consequence

The proposed ninety-degree rotation was almost right but mistyped. Theta
labels do become translations of one carrier. What fails is the assumption
that the arithmetic translation object can be rotated inside ordinary Hilbert
or tempered-distribution space.

The missing structure is therefore not another common carrier. It is the
boundary-bearing continuation functor that turns an exponential-growth
arithmetic comb into a completed spectral section while retaining the
primitive, square, and archimedean currents.

This explains why the scalar completion can have isolated dark Mellin ports
even though the full theta trajectory is faithful: the readout is produced
only after a nontrivial change of analytic category.

## Falsifier and next gate

Any proposed common-spectral-density proof fails if it uses
\(\widehat\nu_{1/2}\) or \(\widehat\mu\) as an ordinary tempered
distribution without constructing the required continuation.

The next gate is explicit:

- define the smallest Fourier--Laplace test space containing the arithmetic
  comb;
- derive Tate--Poisson sewing as a continuous correspondence on it;
- identify its boundary quotient;
- test whether the resulting spectral section has an orientation law absent
  from arbitrary exponential-growth combs.

## Claim boundary

This packet proves the convolution identity and the non-tempered growth
obstruction. It does not prove RH, construct the continuation functor, or
establish positivity of the completed spectral section.

## Disposition

The common-carrier direction survives, but ordinary Fourier factorization is
closed. The live object is a source-specific Fourier--Laplace correspondence
with explicit boundary data.
