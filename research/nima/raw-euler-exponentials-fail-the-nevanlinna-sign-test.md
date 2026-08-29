# Raw Euler exponentials fail the Nevanlinna sign test

The passive-boundary route faces an immediate local falsifier. After the seam rotation
\[
s=\frac12+iz,
\]
a prime Mellin atom becomes
\[
p^{-s}
=
p^{-1/2}e^{-iz\log p}.
\]
Let \(L=\log p>0\), \(z=x+iy\), and \(c>0\). Then
\[
c e^{-iLz}
=
c e^{Ly}\bigl(\cos(Lx)-i\sin(Lx)\bigr),
\]
so
\[
\operatorname{Im}\bigl(c e^{-iLz}\bigr)
=
-c e^{Ly}\sin(Lx).
\]
Its sign oscillates with \(x\) in every horizontal line of the upper half-plane.

Therefore a raw Euler atom is neither Nevanlinna nor anti-Nevanlinna. The obstruction already appears in the one-point diagonal test; no two-point Pick calculation is needed.

Reciprocal symmetrization does not automatically repair this. For example,
\[
e^{-iLz}+e^{iLz}=2\cos(Lz),
\]
and
\[
\operatorname{Im}\cos(Lz)
=
-\sin(Lx)\sinh(Ly),
\]
which again changes sign with \(x\). The odd combination has the same problem in its other component.

Consequently the arithmetic boundary relation \(\Theta(z)\) cannot simply be the finite Euler exponential packet, entry by entry, if the programme expects a Hilbert-space passive realization. One of three additional structures is required:

1. A source-derived linear-fractional transform converts the Euler packet into a Herglotz or anti-Herglotz function.
2. The Euler exponential is the transfer function of a conservative time-delay system, whose natural positivity belongs to a Schur kernel rather than a Nevanlinna kernel.
3. The relevant realization is indefinite, leading to a generalized Nevanlinna class and a Pontryagin or Krein state space.

The second route is especially natural. For \(\operatorname{Im}z>0\),
\[
e^{iLz}
\]
is contractive because
\[
|e^{iLz}|=e^{-Ly}<1.
\]
Thus the correctly oriented delay atom belongs to the scalar Schur class. Its de Branges--Rovnyak kernel
\[
K_S(z,w)
=
\frac{1-S(z)S(w)^{*}}{-i(z-\bar w)}
\]
has the appropriate positivity after the standard half-plane normalization.

A Cayley transform
\[
\Theta(z)
=
i\,(I+S(z))(I-S(z))^{-1}
\]
then converts a Schur function into a Nevanlinna function wherever \(I-S(z)\) is invertible. The sign and reciprocal orientation must be chosen from the source, not selected to force positivity.

This suggests a revised constructor chain:
\[
\text{Euler delay packet}
\to
\text{contractive scattering function }S(z)
\to
\text{source Cayley boundary relation }\Theta(z)
\to
\text{self-adjoint passive dilation}.
\]

For the primitive atom, the half-density coefficient \(p^{-1/2}\) supplies additional strict contraction. Along Adams iteration, the previously derived supercontraction further improves the Schur margin. The live difficulty is assembly: sums of Schur functions need not be Schur, whereas direct sums, cascades, and Redheffer products preserve passivity under typed interconnection.

Thus prime assembly must occur at the conservative-system level, not by scalar addition of delay transfers.

The smallest hostile is the direct sum of scalar Euler coefficients formed as an ordinary scalar sum. Every local delay atom is contractive, but their sum exceeds the unit disk and the Cayley transform loses Nevanlinna positivity.

The next source test is now sharply changed:

> Does the arithmetic constructor assemble Euler atoms as a passive scattering network whose transfer function is Schur, with the arithmetic boundary relation obtained by a source-authorized Cayley transform?

If not, the standard Hilbert boundary-triple route is unavailable in its present form. If yes, seam confinement follows from passivity after the correct scattering-to-impedance conversion.
