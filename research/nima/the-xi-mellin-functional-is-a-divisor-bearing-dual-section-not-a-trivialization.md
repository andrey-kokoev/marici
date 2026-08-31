# The Xi Mellin functional is a divisor-bearing dual section, not a trivialization

## Line-theoretic audit

Let \(\mathcal L\to U\) be a holomorphic line bundle.  A trivialization is a
fibrewise isomorphism

\[
\tau:\mathcal L\xrightarrow{\sim}U\times\mathbb C.
\]

If \(v(s)\) is a nowhere-zero section, then

\[
\tau_s(v(s))\ne0
\]

for every \(s\in U\).  A trivialization cannot map a nonzero line vector to
zero.

## Current Euler-line factors

On the native critical-strip charts, the declared local factors are
nowhere-zero:

- \(\det_3(I-L_\pm(s))\ne0\);
- primitive and square anomaly transition exponentials are units wherever
  defined as line frames;
- reciprocal clutching maps are invertible;
- the archimedean factor
  \(B_\infty(s)\) is nonzero on \(0<\operatorname{Re}s<1\).

Their tensor product supplies a regular determinant-line carrier and local
nonvanishing frames.  It cannot by itself supply the Riemann divisor.

## Consequence for the Mellin--Poisson map

Suppose the theta Mellin--Poisson functional

\[
\tau_s:\mathcal L_s\to\mathbb C
\]

satisfies

\[
\tau_s(v(s))=\xi(s)
\]

for a nonzero source frame \(v(s)\).  At a zero \(s_0\) of \(\xi\),

\[
\tau_{s_0}(v(s_0))=0.
\]

Since \(\mathcal L_{s_0}\) is one-dimensional and \(v(s_0)\ne0\), this forces

\[
\tau_{s_0}=0
\]

as a covector.  Therefore \(\tau\) is not a trivialization.  It is a
holomorphic section of the dual line \(\mathcal L^*\) whose own divisor is the
Xi divisor.

Equivalently, one may regard \(\xi\) as a distinguished section of a
trivialized scalar line.  In either presentation, the divisor is carried by a
section, not by an everywhere-invertible frame map.

## Correction to the identity-theorem argument

Agreement with the Euler expression on \(\operatorname{Re}s>1\), together
with Poisson continuation, uniquely determines the scalar section \(\xi\).
It does not prove that the comparison to a kernel-bearing determinant section
is a unit.  The identity theorem identifies holomorphic scalar sections after
they have been placed in the same line; it does not turn a vanishing covector
into a bundle trivialization.

Thus uniqueness of analytic continuation closes scalar provenance but not
divisor-free line comparison.

## Where the divisor must enter

Because the Euler \(\det_3\) carrier and its transitions are zero-free, the
nontrivial divisor must enter through one of two typed objects:

1. the vanishing theta Mellin dual section \(\tau\);
2. a coupled boundary-complex determinant section compared to \(\tau\) by a
   divisor-preserving morphism.

No product of the already established unit frames can create the divisor.

## Kernel consequence

A zero of the dual section \(\tau_s\) supplies no kernel state by itself.  At
\(s_0\), it says that the entire one-dimensional covector vanishes.  To obtain
a state, one needs a source complex whose determinant section corresponds to
\(\tau\), or a chain-level comparison to the closed boundary pencil.

This is exactly the missing G4 arrow; calling \(\tau\) a trivialization hid it.

## Correct terminology

Use:

- **carrier trivialization** for an everywhere-invertible line-frame map;
- **theta Mellin dual section** for \(\tau\);
- **Xi section** for its scalar coordinate in a chosen carrier frame;
- **divisor-preserving comparison** for a morphism to a Fredholm determinant
  section.

Do not call the vanishing Mellin functional a trivialization on a region
containing Xi zeros.

## Disposition

The theta--Poisson construction uniquely produces the scalar Xi section and
its divisor-bearing dual-line presentation.  It does not provide a
nowhere-zero trivialization or a kernel-bearing determinant complex.  G4
remains open at the divisor-preserving chain comparison.  No RH conclusion is
authorized.
