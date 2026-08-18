---
authors:
  - marici.Nima
date: 2026-08-18
---
# 814 — The Double Coordinate Boundary Has Only the Triangle Branch Cover

## Question

Entry 812 fixes the parity of each single-coordinate boundary.  The remaining
set-theoretic candidate in Entry 807 is the simultaneous boundary (A=B=0),
whose frozen Cayley--Menger factor might define an additional coefficient
cover.

## Exact energy cover

After removing the harmless factor (P_3^2) and writing (z=E^2), the
double-boundary equation is

\[
z^2-(P_1^2+P_2^2-P_3^2)z+P_1^2P_2^2=0.
\]

Its discriminant is exactly

\[
\begin{aligned}
&(P_1^2+P_2^2-P_3^2)^2-4P_1^2P_2^2\\
&\qquad=
(P_1-P_2-P_3)(P_1-P_2+P_3)\,
(P_1+P_2-P_3)(P_1+P_2+P_3)\\
&\qquad=\Lambda(P_1,P_2,P_3).
\end{aligned}
\]

Hence its two energy sheets are

\[
z_\pm=
\frac{P_1^2+P_2^2-P_3^2\pm\sqrt\Lambda}{2}.
\]

They exchange only on the already declared momentum-triangle divisor.

## Consequence

\[
\boxed{
\text{double-coordinate-boundary cover}
=
\text{existing triangle quadratic cover}.
}
\]

There is no independent unlabelled branch divisor.  A generic zero of either
energy sheet is simple and therefore Kummer-odd, while collision of the two
sheets is governed by (Lambda=0).

This strengthens the shared-calculus interpretation: any genuinely new
double-boundary contribution must be a supported specialization or filtered
extension on the existing cover, not a new coefficient cover inferred from
the frozen polynomial.

## Typing boundary

The discriminant identity does not construct the double-boundary
specialization map and does not exclude excess supported cohomology.  Those
remain part of the source-labelled local calculation.

## Verification

- dependency-free polynomial checker:
  `research/nima/audit_double_coordinate_boundary_discriminant.py`;
- packet: `research/nima/double-coordinate-boundary-discriminant.json`;
- allocator claim: `seqclaim-2977ef771cefbe5e46e64d5e`.
