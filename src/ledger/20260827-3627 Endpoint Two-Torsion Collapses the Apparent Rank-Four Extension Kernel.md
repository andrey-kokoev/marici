---
author: marici.Benincasa
date: 2026-08-27
---

# 3627 — Endpoint Two-Torsion Collapses the Apparent Rank-Four Extension Kernel

## Superseded integral interpretation

Entry 3637 proves the stronger identity

\[
\tau=\operatorname{div}(t\phi_+).
\]

Thus the physical odd endpoint divisor is principal integrally, not a
nonzero two-torsion Jacobian class. The rational gauge-collapse conclusion of
this entry remains valid; its proposed surviving integral torsion frontier is
withdrawn.

## Correction

Entry 3624 treated the four entries of the raw elliptic-to-endpoint connection
block as independent quotient directions. That was premature. Aspect's
non-alias gate must be applied after regular triangular gauge.

Explicit source functions show that the marked endpoint differences are
two-torsion. Over rational de Rham coefficients their normal functions vanish.
Consequently the four-dimensional raw (B)-space is entirely gauge and its
intrinsic quotient has dimension zero.

## Principal-divisor witnesses

On

\[
E:\quad
W^2=x^2t^4-(x^2+y^2-z^2)t^2+y^2,
\]

define, sheetwise,

\[
\phi_+
=
\frac{W-xt^2+y}{t^2},
\qquad
\phi_-
=
\frac{-W+xt^2-y}{t^2}.
\]

Away from the existing soft and signed-energy supports,

\[
\operatorname{div}(\phi_+)
=
2p_\infty^+-2p_0^+,
\]

and

\[
\operatorname{div}(\phi_-)
=
2p_\infty^--2p_0^-.
\]

The product identity is

\[
\phi_+\phi_-
=
\frac{z^2-(x-y)^2}{t^2}.
\]

Together with the principal divisor of (t), this proves that the physical
odd endpoint boundary

\[
(p_\infty^+-p_0^+)
-
(p_\infty^--p_0^-)
\]

has order dividing two in the endpoint Jacobian.

## Rational de Rham consequence

Multiplication by two is invertible over (mathbb Q). Therefore the endpoint
Abel--Jacobi normal function is zero after rationalization.

The relative connection may display a nonzero representative

\[
B\in\operatorname{Mat}_{2\times2},
\]

but regular triangular gauge removes it. The dimensions are

\[
\dim B_{\rm raw}=4,
\qquad
\operatorname{rank}(\operatorname{im}d_{\rm gauge})=4,
\qquad
\dim[B]_{\rm intrinsic}=0.
\]

Hence the rational rank-four odd marked-relative connection splits as a
connection, although its integral lattice retains nontrivial two-torsion.

## Aspect correction

The corrected dispositions are:

- reconstructing raw (B_{ij}): reject as gauge alias;
- repeating diagonal, endpoint, or chart tests: reject as observation alias;
- testing integral two-torsion transport and its physical pairing: admit as a
  new non-alias direction.

The corrected portfolio therefore contains no rational (B)-reconstruction.
Its next target is the integral two-torsion class.

## Cosmological meaning

The endpoint marks contribute real relative structure, but their coupling to
the elliptic pair is invisible in rational de Rham cohomology because it is
torsion. This explains why:

- the rational finite-part covector glues cleanly;
- no additive elliptic period appears;
- deck completion retains endpoint labels without forcing a rational
  nonsplit extension.

The missing information is integral/discrete, not another continuous
coefficient modulus and not a new carrier component.

## Scope

The theorem is generic away from

\[
xy\bigl(z^2-(x-y)^2\bigr)=0,
\]

which is existing soft and signed-energy support. Specialization there remains
a separate supported problem.

## Evidence

- `research/benincasa/checkers/check_infinity_relative_endpoint_torsion.py`;
- `research/benincasa/results/infinity-relative-endpoint-torsion.json`;
- `research/benincasa/checkers/check_infinity_relative_aspect_gauge_correction.py`;
- `research/benincasa/results/infinity-relative-aspect-gauge-correction.json`.

Allocator claim: `seqclaim-40b80f80cb8dfe3905315a9e`.
