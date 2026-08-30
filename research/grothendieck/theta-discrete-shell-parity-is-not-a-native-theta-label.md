# Theta discrete shell parity is not a native theta label

## Bounded question

Can the odd-to-even coefficient gate of the finite reciprocal shell model be
transferred directly to the completed theta source?

## Typing audit

The toy model

\[
\sum_k c_k\cosh(kz)
\]

is the bilateral Laplace transform of a discrete measure supported at integer
spectral positions \(u=\pm k\). Its odd/even sign at \(z=a+i\pi\) comes from

\[
\cos(k\pi)=(-1)^k.
\]

The index \(k\) is therefore a support coordinate.

The completed theta source instead has the continuous transform

\[
F(z)
=
\int_{\mathbb R}\Phi(u)e^{zu}\,du,
\]

with arithmetic decomposition

\[
\Phi(u)=\sum_{n\ge1}\phi_n(u).
\]

Here \(u\) is the continuous spectral support coordinate, while \(n\) is an
arithmetic lattice label inside the density. Parity of \(n\) does not reproduce
parity of a discrete support point \(u=k\).

## Native oscillatory orientation

At \(z=a+ib\), the continuous source phase is governed by

\[
\cos(bu),
\qquad
\sin(bu).
\]

The native analogue of toy-shell parity is therefore the moving partition of
the \(u\)-axis into consecutive sign bands of width

\[
\frac{\pi}{|b|},
\]

not an odd/even partition of theta labels.

This band system depends canonically on the spectral ordinate \(b\). Treating
theta labels \(n\) as odd and even shell positions would identify two
different types and manufacture a false coefficient compiler.

## Reconnection to the earlier obstruction

The canonical adjacent-band transport was already tested with all theta labels
retained. On the central labelled fiber, its required pointwise density
domination fails because the transported negative term has a nonzero boundary
ratio while the compensating factor tends to zero.

Thus the discrete paired-shell result does not evade the earlier
adjacent-band falsifier. After correct typing, it lands on the same continuous
oscillatory transport problem.

## What survives

The toy calculation still contributes two valid lessons:

1. transported positivity acquires an alternating orientation;
2. cancellation must be established on a canonical block rather than on
   individual positive atoms.

But the theta block must be constructed from continuous phase bands while
retaining the arithmetic label fiber. The surviving candidate is the
conditional or larger-block residual after integrating the midpoint coordinate
without erasing labels.

## Result

Odd/even discrete shell pairing is not a source-native theta operation. Its
direct application is prohibited by a support-versus-label type mismatch.

The next legitimate attack returns to the exact labelled continuous-band
residual:

\[
R_{nm}(D)
=
H_{nm}(D)+H_{nm}(D+\pi/b).
\]

One must derive a canonical larger block or conditional transport whose sign
follows from theta source geometry. The toy coefficient inequality may serve
as an analogy only after such a source-derived block is defined.

## Sharp falsifier

Any proposed theta parity compiler that assigns signs by arithmetic label
\(n\bmod2\) must prove that this sign equals the transform phase orientation
for all continuous \(u\) in that label fiber. Since each positive
\(\phi_n(u)\) occupies a continuum of \(u\), the identification fails.
