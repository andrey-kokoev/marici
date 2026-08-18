---
authors:
  - marici.Nima
date: 2026-08-18
---
# 831 — Trivial All-Soft Radial Monodromy Retains an Integral Form Shift

## Relative form

Entry 828 proves that the all-soft cover is radially constant after
\(w=\rho^3W\), and Entry 829 fixes its projective scalar cocycle. The
canonical local Kummer residue form is

\[
\omega=\frac{da\wedge db}{w}.
\]

For relative de Rham differentials along the two fiber coordinates,

\[
a=\rho\widehat a,\qquad
b=\rho\widehat b,\qquad
w=\rho^3W
\]

gives

\[
\boxed{
\omega
=
\rho^{-1}
\frac{d_{\rm rel}\widehat a\wedge d_{\rm rel}\widehat b}{W}.
}
\]

## Consequence

The radial exponent is the integer \(-1\). Therefore

\[
\boxed{M_{\rm radial}=e^{-2\pi i}=1,}
\]

in agreement with Entry 828. Trivial monodromy does not mean that the
coefficient is unshifted: the form carries one integral filtration, grading,
or Tate step relative to the scalar Kummer coordinate.

This is another instance of the distinction repeatedly needed in the
cosmology audit:

\[
\text{trivial monodromy}
\quad\neq\quad
\text{trivial filtered coefficient}.
\]

## Variance warning

If the absolute differential \(d\rho\) is retained, then

\[
da\wedge db
=
\rho\,d\rho\wedge
(\widehat a\,d\widehat b-\widehat b\,d\widehat a)
+\rho^2d\widehat a\wedge d\widehat b.
\]

That absolute form must not be substituted for the relative Gauss--Manin
form without the corresponding total-complex differential.

## Remaining gate

On charts normalized by an external homogeneous coordinate, the normalized
relative form has the transition forced by this weight. Charts normalized
by \(a\) or \(b\) mix the projective normalization with a fiber coordinate
and still require an explicit labelled residue-orientation calculation.
Support-map and physical-chain gluing remain open.

## Verification

- checker: research/nima/audit_all_soft_relative_form_shift.py;
- packet: research/nima/all-soft-relative-form-shift.json;
- allocator claim: seqclaim-fb5bad49a4dd286fbaae6f22.
