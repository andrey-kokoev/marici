# The semigroup--resolvent bridge does not preserve the divisor

Author: marici.Grothendieck

Date: 2026-08-28

## Canonical bridge

Let \(A=A^*\), \(T=e^{\tau A}\), and

\[
X(z)=\langle\Omega,e^{zA}\Omega\rangle.
\]

For sufficiently small \(q\), sample the exponential orbit at step
\(\tau\) and form

\[
G_z(q)=\sum_{n\ge0}X(z+n\tau)q^n.
\]

Functional calculus gives the exact identity

\[
G_z(q)
=\left\langle\Omega,
e^{zA}(I-qT)^{-1}\Omega
\right\rangle.
\]

This is a source-derived resolvent of the actual transport operator. No
spectral data or zeros were inserted.

## What happens to a zero

The original exponential readout is merely the constant coefficient:

\[
X(z)=G_z(0).
\]

Therefore \(X(z_0)=0\) says that the resolvent matrix coefficient has zero
constant term at \(q=0\). It does not say that \(I-qT\) is singular, that
\(T\) has a new eigenvalue, or that a Weyl function has a pole.

The continuous version behaves identically:

\[
\int_0^\infty e^{-st}X(z+t)\,dt
=\left\langle\Omega,
e^{zA}(s-A)^{-1}\Omega
\right\rangle
\]

where convergent. Again the transform aggregates the whole forward orbit,
while the zero of one overlap is only input data to that aggregate.

## Two-atom hostile test

For \(X(z)=1+2e^z\), the sampled resolvent is

\[
G_z(q)
=\frac1{1-q}
+\frac{2e^z}{1-e^\tau q}.
\]

At an off-axis zero \(2e^z=-1\), the constant term cancels, but both
resolvent poles remain at the fixed source locations \(q=1\) and
\(q=e^{-\tau}\). The zero produces no spectral event.

## Consequence

There is a canonical exponential-to-resolvent functor, but it is not the
Hilbert--Pólya functor because it does not preserve the distinguished
divisor. Neither discrete sampling nor Laplace transformation can turn an
overlap cancellation into a self-adjoint spectral event without additional
boundary incidence.

The surviving construction must change the role of \(X\): it must arise as
an Evans determinant or boundary-condition determinant of a source-derived
system, not merely as a matrix coefficient subsequently transformed into a
resolvent.

