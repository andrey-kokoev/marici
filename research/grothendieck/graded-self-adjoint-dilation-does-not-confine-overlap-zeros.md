# Graded Self-Adjoint Dilation Does Not Confine Transform Zeros

## Faithful unitary model

Fix

\[
0<a<1,
\qquad
b>0,
\]

and define the positive even Schwartz function

\[
A(u)
=
e^{-u^2}
\left(
1+a\cos(bu)
\right).
\]

It is strictly positive for every real \(u\).

Its Fourier transform is a positive sum of translated Gaussians. Therefore
\(A\) is positive-definite and admits a unitary matrix-coefficient
realization

\[
A(u)=\langle v,e^{iuH}v\rangle
\]

for a self-adjoint multiplication operator \(H\). Reflection of the spectral
coordinate defines an involution \(R\) satisfying

\[
RHR=-H,
\qquad
Rv=v.
\]

Thus this model has the correctly typed real unitary transport.

## Entire transform

Using

\[
\widehat A(z)
=
\int_{\mathbb R}A(u)e^{izu}\,du,
\]

one obtains

\[
\widehat A(z)
=
\sqrt\pi e^{-z^2/4}
\left[
1
+
a e^{-b^2/4}\cosh\left(\frac{bz}{2}\right)
\right].
\]

The Gaussian prefactor never vanishes. Transform zeros therefore satisfy

\[
\cosh\left(\frac{bz}{2}\right)
=
-\frac{e^{b^2/4}}a.
\]

Because \(e^{b^2/4}/a>1\), there are zeros with

\[
\Re z
=
\frac2b
\operatorname{arcosh}
\left(
\frac{e^{b^2/4}}a
\right)
\ne0
\]

and imaginary part congruent to \(2\pi/b\) modulo \(4\pi/b\).

## Consequence

The following package does not confine zeros of the spectral transform:

- a self-adjoint generator;
- a reflection involution anticommuting with it;
- a reflection-fixed cyclic state;
- unitary real transport;
- an even, positive, rapidly decaying matrix coefficient;
- a positive spectral measure.

Hence the centered Euler generator explains the half-offset but does not by
itself constitute a Hilbert–Pólya realization of the zeros.

## Missing source law

The theta theorem must distinguish its comb–current coefficient from a generic
positive graded unitary coefficient. Possible additional information includes
canonical-system ordering, total positivity of a completed comparison kernel,
or arithmetic incidence among scale modes.

The zero-to-state bridge cannot merely identify \(\xi\) as the Fourier
transform of a positive even unitary matrix coefficient.

## Correction history

The first version used \(\cosh z+a\cosh(2z)\). That correctly showed failure
for a nonunitary analytic overlap but mismatched the theta transport
coordinate. The present Gaussian-cosine witness repairs the typing: transport
is unitary for real \(u\), and the off-seam zeros occur in its entire Fourier
transform.

## Falsifier

The hostile fails if \(A\) is not positive and positive-definite, or if every
zero of \(\widehat A\) has zero real part. The positive Gaussian mixture and
the explicit cosh equation exclude both failures.
# Graded Self-Adjoint Dilation Does Not Confine Overlap Zeros

## Abstract source pattern

Let

\[
H=\operatorname{diag}(1,-1,2,-2)
\]

on \(\mathbb C^4\), and let \(R\) swap the two coordinates in each spectral
pair. Then

\[
H=H^*,
\qquad
R^2=1,
\qquad
RHR=-H.
\]

This is the finite-dimensional form of the centered Fourier–dilation
architecture.

## Reflection-fixed state

Choose

\[
a=\frac1{10}
\]

and

\[
v=
\left(
\frac1{\sqrt2},
\frac1{\sqrt2},
\sqrt{\frac a2},
\sqrt{\frac a2}
\right).
\]

The vector is reflection-fixed:

\[
Rv=v.
\]

Its transported overlap is

\[
A(z)
=
\langle v,e^{zH}v\rangle
=
\cosh z+a\cosh(2z).
\]

This function is entire, even, real on the real axis, and strictly positive
there:

\[
A(x)>0
\qquad
(x\in\mathbb R).
\]

## Explicit off-seam zero

Writing

\[
y=\cosh z
\]

and using \(\cosh(2z)=2y^2-1\), the zero equation becomes

\[
2ay^2+y-a=0.
\]

For \(a=1/10\), the negative root is

\[
y_-=-\frac{5+3\sqrt3}{2}<-1.
\]

Hence

\[
z=
\operatorname{arcosh}(|y_-|)
+i\pi
\]

is a zero with nonzero real part.

## Consequence

The following package does not confine zeros to the Fourier-fixed seam:

- a self-adjoint dilation generator;
- a reflection involution anticommuting with it;
- a reflection-fixed source state;
- an even entire overlap;
- strict positivity of that overlap on the real transport axis.

Thus the centered Euler generator explains the half-offset but is not by itself
a Hilbert–Pólya operator for the zero set.

## Missing source law

The theta theorem must distinguish its comb–current overlap from a generic
positive graded spectral overlap. Possible additional information includes:

- total positivity of the paired spectral weights;
- a canonical-system or de Branges ordering;
- arithmetic incidence among dilation modes;
- a source-derived restriction stronger than positivity of the real-axis
  overlap.

The zero-to-state bridge cannot merely say that zeros belong to a matrix
coefficient of a self-adjoint graded flow.

## Falsifier

The hostile fails if \(A(x)\) is not positive for real \(x\), or if the
displayed root lies on the imaginary axis. Both properties follow directly
from \(a>0\) and \(y_-<-1\).
