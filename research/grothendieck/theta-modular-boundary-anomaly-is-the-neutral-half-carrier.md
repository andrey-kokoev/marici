# Theta modular boundary anomaly is the neutral half carrier

## Question

The Fourier--dilation calculation confined every archimedean anomaly to
relative boundary currents.  What do those currents become after the actual
theta modular completion?

## Completed theta Mellin split

Let

\[
\psi(x)=\frac{\vartheta(x)-1}{2}
=
\sum_{n\ge1}e^{-\pi n^2x}.
\]

In its initial convergence chamber,

\[
\Lambda(s)
=
\pi^{-s/2}\Gamma(s/2)\zeta(s)
=
\int_0^\infty\psi(x)x^{s/2}\frac{dx}{x}.
\]

Split at the self-dual point \(x=1\).  Theta reciprocity gives

\[
\psi(1/x)
=
x^{1/2}\psi(x)+\frac{x^{1/2}-1}{2}.
\]

Changing variables in the lower chamber and continuing the two elementary
integrals yields

\[
\Lambda(s)
=
I(s)+\frac1{s-1}-\frac1s,
\]

where

\[
I(s)
=
\int_1^\infty
\psi(x)
\left(
x^{s/2}+x^{(1-s)/2}
\right)
\frac{dx}{x}.
\]

The integral \(I\) is entire and visibly invariant under \(s\mapsto1-s\).

## Boundary currents become the half carrier

Apply the canonical completion

\[
\xi(s)=\frac12s(s-1)\Lambda(s).
\]

The two relative boundary currents satisfy

\[
\frac12s(s-1)
\left(
\frac1{s-1}-\frac1s
\right)
=
\frac12.
\]

Therefore

\[
\xi(s)
=
\frac12+\frac12s(s-1)I(s).
\]

The constant carrier previously isolated from the completed theta transform
is exactly the completed modular boundary anomaly.  It is not an arbitrary
normalization and not a bulk theta mode.

## What this explains

The source architecture now has a precise three-part derivation:

1. Fourier reversal makes the archimedean interior flat.
2. Cutting at the self-dual point exposes two relative endpoint currents.
3. Canonical completion fuses those currents into the neutral half carrier.

This explains why removing the constant carrier before studying the
Laguerre tower was the correct quotient.  The same boundary class was being
represented repeatedly in scalar derivatives even though its completed
section is constant.

## What it cannot prove

The half carrier is nowhere zero by itself, but its interference with the
entire tail can vanish.  The identity supplies no sign or transversality law
for

\[
\frac12+\frac12s(s-1)I(s).
\]

Moreover, the modular derivation holds for a broad class of self-reciprocal
sources after their corresponding endpoint term is installed.  It cannot by
itself reject hostile self-Fourier sources with off-critical zeros.

Thus the entire archimedean boundary lane is now classified:

- its bulk anomaly is zero;
- its relative anomaly is rank two before completion;
- its completed scalar image is the rank-one neutral carrier \(1/2\);
- none of these facts supplies zero confinement.

## Remaining source-specific location

Any RH-bearing boundary law must couple this neutral archimedean carrier to
arithmetic boundary data before scalar aggregation.  In the current typing,
the remaining candidates are the primitive and prime-square currents and
their mixed incidence with the modular seam.

The next useful calculation is not another archimedean Green identity.  It is
the finite-Euler comparison of the arithmetic boundary register with the
rank-two continuation register

\[
\left(
\frac1{s-1},-\frac1s
\right).
\]

A successful law must show that the scalar half carrier is the compression of
a richer labelled boundary pairing whose non-scalar component controls the
score residual.  If the arithmetic register couples only through the scalar
sum \(1/2\), this route also closes.

## Result

Theta modular completion maps the complete archimedean dilation anomaly to
the neutral constant carrier \(1/2\).  The unexplained force, if any, must
live in a pre-compression arithmetic--boundary relationship that this scalar
carrier forgets.
