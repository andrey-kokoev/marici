# The Frontier Current Is the Unique Minimal Fourier-Fixed Boundary State

## Minimal ansatz

Consider even quartic-Gaussian states

\[
f(\rho)
=
\left(
a\rho^4+b\rho^2+c
\right)
e^{-\pi\rho^2}.
\]

Use the Fourier convention

\[
\widehat f(\xi)
=
\int_{\mathbb R}f(\rho)e^{-2\pi i\rho\xi}\,d\rho.
\]

The Gaussian differentiation formulas give

\[
\widehat{\rho^2e^{-\pi\rho^2}}
=
\left(
\frac1{2\pi}-\xi^2
\right)
e^{-\pi\xi^2},
\]

and

\[
\widehat{\rho^4e^{-\pi\rho^2}}
=
\left(
\xi^4-\frac3\pi\xi^2+\frac3{4\pi^2}
\right)
e^{-\pi\xi^2}.
\]

## Fourier-fixed classification

Requiring \(\widehat f=f\) gives one coefficient condition:

\[
b=-\frac{3a}{2\pi},
\]

while \(c\) remains free. Thus the even quartic-Gaussian Fourier-fixed sector
is two-dimensional:

\[
f(\rho)
=
\left[
a\left(
\rho^4-\frac3{2\pi}\rho^2
\right)
+c
\right]
e^{-\pi\rho^2}.
\]

## Boundary nullity selects one line

The lattice origin contributes no frontier current precisely when

\[
f(0)=0.
\]

This forces \(c=0\). Hence every nonzero state satisfying Fourier fixedness,
evenness, quartic minimality, and boundary nullity is a scalar multiple of

\[
\rho^2
\left(
2\pi\rho^2-3
\right)
e^{-\pi\rho^2}
=
F(\rho).
\]

Requiring a positive outer lobe fixes the scalar orientation.

## Meaning

The frontier profile is not one convenient test function among many at its
complexity level. It is the unique minimal nontrivial state compatible with:

- even real Gaussian locality;
- Fourier eigenvalue \(+1\);
- a null sampling origin;
- positive orientation at large radius.

The two-dimensional fixed sector consists of a neutral Gaussian carrier and
one boundary-current direction. Origin nullity removes the carrier and leaves
the current.

## Hostile higher modes

Higher-degree Fourier-fixed Gaussian polynomials can satisfy the same visible
symmetries and add new Mellin zeros. The degree-twelve hostile carrier lives in
that larger sector. It is rejected by minimality, but minimality must be
authorized by the theta differential source rather than imposed because the
minimal state gives the desired function.

Here that authority is available: the explicit theta current is obtained from
the first scale derivative of the Gaussian lattice source and has quartic
degree before any zero analysis.

## Scope boundary

Canonical minimality blocks higher-mode hostile additions to the local current.
It still does not prevent the unique current's arithmetic matrix coefficient
from vanishing off the seam.

## Falsifier

The classification fails if there is a second linearly independent even
quartic-Gaussian Fourier fixed point with \(f(0)=0\). The coefficient equations
show there is not.
