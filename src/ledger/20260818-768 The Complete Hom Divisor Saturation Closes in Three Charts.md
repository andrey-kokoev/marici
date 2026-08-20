---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 768 — The Complete Hom Divisor Saturation Closes in Three Charts

## Rational three-step construction

Starting from the twelve complete Hom factors, each factor was evaluated on

\[
\rho^k(u,v),\qquad k=0,1,2,3,
\]

with

\[
\rho(u,v)=
\left(
\frac{2u}{u-v},
\frac{2(2-v)}{u-v}
\right).
\]

Numerator and normalization denominator were retained separately.  Rational
sections were compared by exact cross multiplication over the large prime;
no numerical fitting or polynomial-list identification was used.

## Closure

For every labelled factor \(f_a\),

\[
\boxed{
f_a\circ\rho^3=f_a
}
\]

as a rational function, up to a nonzero scalar.  All twelve labels pass this
identity exactly.

The first three charts contain

\[
\boxed{36}
\]

distinct marked rational-section classes: one three-cycle for each of the
twelve source labels.  The fourth chart reproduces the first.

Thus the occurrence saturation is finite and closes after the expected
three charts.  Entry 767's six residual polynomials are not an indefinitely
growing family; they are affine representatives of these finite cyclic
orbits.

## Type qualification

The number \(36\) counts marked rational sections, not proven distinct
geometric support divisors.  Different sections can define the same divisor
after quotienting by chart units or normalization-boundary factors.

The raw cleared expressions contain 43 numerator forms and 13 denominator
forms before common-factor cancellation.  Those larger counts are
presentation artifacts and are not used as geometric ranks.

Therefore the established object is

\[
\boxed{
\text{finite three-chart labelled divisor correspondence},
}
\]

not a 36-cell carrier enlargement.

## Consequence

Local pole-order stabilization can now be organized over twelve labelled
three-cycles.  One may compute in one chart and transport the local indicial
data twice, provided normalization-boundary units and the Entry 766 sheared
filtration are retained.

The resonant grades

\[
15,\quad17,\quad28,\quad30
\]

return unchanged in the transported filtered frame.

## Evidence

- `research/benincasa/check_finite_cyclic_hom_divisor_saturation.py`;
- `research/benincasa/finite-cyclic-hom-divisor-saturation.json`;
- Entries 766--767;
- allocator claim `seqclaim-694a2f2cedd8fa05d3a59134`.
- epistemic event
  `ev-000000000382-7032fa9a-192b-40a5-bedc-aa626424a01a`.

## Next falsifier

Quotient the 36 marked sections by invertible chart units and factor the
normalization boundaries into irreducible support components.  Then compute
the local Hom indicial operator on one representative of each resulting
support orbit and test whether the complete pole orders stabilize.
