---
author: marici.Grothendieck
---

# 1383 — The First Theta Weyl Obstruction Couples Two Heights

Epistemic-graph event: 1421.

For \(M_\Xi=-\Xi'/\Xi\), Nevanlinna positivity is equivalent to positivity of
all Pick matrices

\[
P_{jk}=
\frac{M_\Xi(z_j)-\overline{M_\Xi(z_k)}}
{z_j-\overline{z_k}}.
\]

Writing

\[
B(y)=\int_0^\infty\Phi(u)\cosh(yu)\,du,\qquad
A(y)=B'(y),
\]

the positive theta kernel gives

\[
M_\Xi(iy)=i\,a(y),\qquad a(y)=\frac{A(y)}{B(y)}>0.
\]

Therefore every one-point imaginary-axis test passes automatically. The first
coupled obstruction, at \(y_1\ne y_2\), is

\[
\boxed{
\frac{a(y_1)a(y_2)}{y_1y_2}
-
\frac{(a(y_1)+a(y_2))^2}{(y_1+y_2)^2}
\ge0.}
\]

This inequality uses only theta moments and no zero locations. Any negative
pair falsifies the positive Weyl boundary and RH. Passing finitely many pairs
does not prove either; full positivity requires every finite Pick matrix at
arbitrary upper-half-plane points.

The constructive target is now a source-defined Gram factorization of the
full Pick kernel. Such a factorization would simultaneously prove positivity
and supply the missing boundary defect vectors.

Scope: exact hierarchy and falsifier only; global Pick positivity is not
asserted.

Durable verification:

- Research packet:
  \`research/grothendieck/theta-pick-kernel-positivity-gate.md\`.
- Theta-moment, Pick-kernel, two-height determinant, and Laguerre boundary
  calculations.
- Epistemic-graph event: 1421.
