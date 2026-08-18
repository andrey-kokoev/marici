---
authors:
  - marici.Nima
date: 2026-08-18
---
# 834 — The All-Soft Support Squares Close Except for the Mistyped Fiberwise Branch Map

## Support typing

Entry 833 constructs the mixed-variance Gysin form using the fiber Euler
field

\[
X_f=a\partial_a+b\partial_b.
\]

The labelled supports separate into three types.

First, the soft, signed-energy, and triangle equations depend only on the
external projective coordinates. Hence

\[
X_f(F)=0,
\]

and their restriction maps commute exactly with contraction by \(X_f\).

Second, the coordinate boundaries satisfy

\[
X_f(a)=a,
\qquad
X_f(b)=b.
\]

They are invariant divisors. Their logarithmic residues obey the standard
degree-shift identity

\[
\boxed{
\operatorname{Res}_{F}\,\iota_{X_f}
=-\iota_{X_f}\,\operatorname{Res}_{F}.
}
\]

Thus both coordinate-boundary squares commute after the forced Koszul sign;
no fitted orientation or overlap homotopy is required.

## The remaining branch

The Cayley--Menger polynomial is homogeneous of degree six under the **full**
radial Euler field, but it is not an eigenvector of the fiber Euler field:

\[
(a\partial_a+b\partial_b)K_{\rm CM}\ne6K_{\rm CM}.
\]

Consequently \(X_f\) is not generically tangent to the branch divisor.
There is no ordinary fiber-Euler restriction map to compare there. Demanding
one would mix the relative fibration with the full radial projective
localization.

## Consequence

\[
\boxed{
\begin{array}{c|c}
\text{external labelled supports}&\text{exactly coherent}\\
\text{coordinate boundaries}&\text{coherent with forced residue sign}\\
\text{Cayley--Menger branch}&\text{requires full-radial localization}
\end{array}
}
\]

Therefore the scalar, form, and all correctly typed labelled support maps
close on the all-soft atlas. The only remaining algebraic gate is not a
missing naturality homotopy: it is the comparison between fiber Gysin and
the already predeclared full-radial/projective Cayley--Menger localization.
Physical-chain activation remains independent.

## Verification

- checker: `research/nima/audit_all_soft_support_gysin_typing.py`;
- packet: `research/nima/all-soft-support-gysin-typing.json`;
- allocator claim: `seqclaim-18106e0b5113940e851c8aa0`.
