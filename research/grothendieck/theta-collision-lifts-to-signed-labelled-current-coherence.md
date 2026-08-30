# Theta collision lifts to signed labelled-current coherence

## Question

After scalar positivity, monotonicity, minimum phase, and strict log-concavity
all fail to exclude tangency, what does the collision become before the theta
winding labels are summed?

## Labelled source decomposition

On the positive chamber, retain the completed winding labels

\[
\Phi(u)=\sum_{n\ge1}\phi_n(u),
\]

with the exact translate law

\[
\phi_n(u)=n^{-1/2}\phi_1(u+\log n).
\]

For a finite support endpoint \(L\), define

\[
H_{n,L}(z)=\int_0^L\phi_n(u)e^{izu}\,du.
\]

Then

\[
H_L(z)=\sum_{n\ge1}H_{n,L}(z).
\]

The translate law gives the moving-interval representation

\[
H_{n,L}(z)
=n^{-1/2-iz}
\int_{\log n}^{L+\log n}\phi_1(v)e^{izv}\,dv.
\]

Thus a label is not merely a positive coefficient.  It contributes a
phase-rotated chord of one common primitive, with both endpoints shifted by
the arithmetic coordinate \(\log n\).

## Signed label currents

Integration by parts defines the source-native signed measure

\[
d\mu_{n,L}(t)
=-\phi_n'(t)\,dt+\phi_n(L)\delta_L(dt).
\]

Its total mass is \(\phi_n(0)\), and

\[
izH_{n,L}(z)
=
\int_{(0,L]}(e^{izt}-1)\,d\mu_{n,L}(t).
\]

Individual \(d\mu_{n,L}\) need not be positive.  Modular seam cancellation
allows the label derivatives at the fold to have mixed signs.  Positivity
appears only after codiagonal summation:

\[
\sum_{n\ge1}d\mu_{n,L}
=-\Phi'(t)\,dt+\Phi(L)\delta_L(dt)
=d\mu_L(t)>0.
\]

This is the exact location where label information and scalar minimum phase
separate.

## Collision before aggregation

Let

\[
g_{n,L}(x)=\int\sin(xt)\,d\mu_{n,L}(t).
\]

Then

\[
xC_L(x)=\sum_{n\ge1}g_{n,L}(x).
\]

Differentiating gives

\[
C_L(x)+xC_L'(x)
=
\sum_{n\ge1}g_{n,L}'(x).
\]

Hence the remaining double-zero collision is exactly

\[
\sum_{n\ge1}g_{n,L}(x)=0,
\qquad
\sum_{n\ge1}g_{n,L}'(x)=0.
\]

The scalar positive current can therefore have a multiple sine-transform zero
only if its signed labelled components cancel simultaneously in value and
tangent.

## Why labelled sign regularity does not immediately close it

The integral-square theorem proves all-order sign regularity of the labelled
point-evaluation kernel.  The collision map performs three additional
operations:

1. differentiate each label in the support coordinate;
2. integrate against oscillatory sine and cosine ports;
3. codiagonally sum every label.

None of these operations has yet been proved to preserve the labelled
Chebyshev orientation.  In particular, a positive sum after differentiation
does not reconstruct the signs of the summands, and an oscillatory integral is
not a positive minor-preserving map.

So the existing all-order theorem is relevant but not yet composable with the
collision readout.

## Required coherence theorem

Define the labelled collision vectors

\[
v_{n,L}(x)
=
\begin{pmatrix}
g_{n,L}(x)\\
g_{n,L}'(x)
\end{pmatrix}.
\]

The target is a source-derived cone, oriented-matroid covector, or constraint
operator that proves

\[
\sum_{n\ge1}v_{n,L}(x)\ne0
\]

whenever its first coordinate is constrained to vanish.  Equivalently, the
summed vector may cross the vertical axis but may not equal the origin.

The constraint must be genuinely cross-label.  A product of bounded
independent prime clusters inherits the singular-value collapse identified by
Kitaev.  Per-prime positivity, Adams relations within one prime, and primitive
or square typing cannot by themselves supply a uniform global gap.

## Hostile-source discriminator

The exponential and two-step hostiles have scalar positive currents but no
authorized winding-labelled decomposition satisfying:

- the translate law by \(\log n\);
- integral-square separation;
- Poisson reflection coherence;
- modular fold cancellation of signed derivative channels.

A successful theorem must reject those sources through one of these labelled
relations before using the scalar zero location.

## Deutsch--Popper conjecture

The completed theta label system transports its all-order integral-square
orientation through differentiation, oscillatory integration, and
codiagonalization strongly enough to forbid simultaneous cancellation of the
value and tangent collision channels.

The smallest falsifier is a finite label packet and one \((L,x)\) for which
the typed vector sum vanishes, or a negative cycle showing that no coherent
orientation survives the three operations.

## Result

The collision has now been lifted before scalar aggregation.  Scalar minimum
phase is created only after signed label currents are summed; arithmetic
rigidity exists only before that sum.  The singular remaining task is a
cross-label descent theorem proving that enough orientation survives to
exclude simultaneous value-and-tangent cancellation.
