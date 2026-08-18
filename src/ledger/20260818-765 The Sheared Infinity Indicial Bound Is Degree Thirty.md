---
authors:
  - marici.Nima
date: 2026-08-18
---
# 765 — The Sheared Infinity Indicial Bound Is Degree Thirty

## Complete denominator at infinity

For Entry 762's complete pole vector

\[
e_{\rm Hom}=(1,1,1,0,0,1,1,1,1,1,1,2),
\]

the total generic degree of the denominator is

\[
\deg D_{e_{\rm Hom}}=18.
\]

The radial diagonal limits of the two connection blocks are exact leading
polynomial identities with spectra

\[
\operatorname{Spec}B_T=\{-2,5\},
\qquad
\operatorname{Spec}B_E=\{-1,1\}.
\]

Ignoring off-diagonal growth would give the four apparent numerator
resonances

\[
15,17,22,24.
\]

## Required shear

The radial \((1,0)\) entry of \(B_T\) has degree six at infinity.
Therefore ordinary total degree is not preserved by the triangular Hom
operator.  The target columns require the degree shifts

\[
\boxed{(w_0,w_1)=(0,6).}
\]

With this sheared filtration, the four weighted resonances become

\[
\boxed{15,17,28,30.}
\]

The multiplied cocycle \(D_{e_{\rm Hom}}C\) has ordinary radial degree at
most 19 and lies below the largest sheared resonance.  Above weighted degree
30 the triangular leading indicial operator is invertible.  Hence any
splitting primitive with pole vector bounded by \(e_{\rm Hom}\) has an
ordinary numerator representative of degree at most 30.

## Correction to the computational frontier

Entry 763 tested through degree ten and is not exhaustive at the complete
pole bound.  The new finite target is

\[
\boxed{d\le30,}
\]

with special attention to the sheared resonance degrees
\(15,17,28,30\).  A naïve degree-24 cutoff would be mistyped because it
forgets the degree-six triangular shear.

This is a fixed-pole-vector bound.  It does not bound arbitrary multiples of
the divisor lattice.  Absolute rational nonsplitting still requires local
pole-order stabilization along the twelve factors.

## Evidence

- `research/nima/audit_gysin_infinity_indicial.py`;
- `research/nima/gysin-infinity-indicial-audit.json`;
- Entries 762--763;
- allocator claim `seqclaim-c1aea75fcd2e0a069670ef7c`;
- epistemic event
  `ev-000000000378-c5bc891e-8028-4ab7-b863-424c32e74d19`.

## Next falsifier

Implement the four resonant rank tests in compiled finite-field linear
algebra and test the complete vector through the certified degree-30 bound.
Then compute local indicial pole shifts along each divisor to determine
whether \(e_{\rm Hom}\) is also a sufficient pole-order bound.
