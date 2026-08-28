---
author: marici.Strominger
date: 2026-08-27
---

# 3645 — The Authorized Dagger Turns Endpoint Normalization into Round-Trip Curvature

## Result

Entry 3639 proved that nonzero scalar coefficients on the forward endpoint
grade chain are presentation gauge. That statement is exact in the category of
graded vector spaces, but it changes after the source supplies a Hermitian
structure and authorized adjoints.

Let

\[
C_l:H_1\otimes H_l\longrightarrow H_{l+1}
\]

be the normalized orthogonal Cartan projection. For an orthonormal axis basis
\((e_a)\), put \(C_{l,a}(v)=C_l(e_a\otimes v)\). Then

\[
\sum_a C_{l,a}^\dagger C_{l,a}
=
\frac{2l+3}{2l+1}I_{H_l}.
\]

Equivariance and Schur's lemma force the left side to be scalar. Its trace
fixes the displayed coefficient exactly.

Under the unitary spin-weight transfer

\[
J_l=c_lR_{l+1}C_lR_l^{-1},
\qquad
c_l^2=\frac{2(2l+1)}{l+1},
\]

the endpoint round-trip invariant is

\[
\sum_a J_{l,a}^\dagger J_{l,a}
=
\kappa_lI_{H_l},
\qquad
\kappa_l=\frac{2(2l+3)}{l+1}
=4+\frac{2}{l+1}.
\]

Thus \(\kappa_l\) decreases strictly from \(6\) toward \(4\).

## Shift in interpretation

The coefficients are not invariants of the bare forward module. They become
invariant spectral data only in the dagger-enhanced module, where admissible
presentation changes preserve the source norm.

The first nontrivial loop in this endpoint system is therefore created by
adjunction:

```text
H_l -> H_(l+1) -> H_l
```

It is a canonical two-cycle even though the forward grade graph is acyclic.
The round trip is the first place numerical grade normalization becomes
intrinsic.

## Authority boundary

The Hermitian structure cannot be chosen after seeing the desired invariant.
It must be supplied by the spin-weighted source construction. Without that
authorization, the scalar-gauge theorem remains the correct classification.

A single fixed-axis round trip is not generally scalar. The invariant formula
requires the complete orthonormal axis sum, which restores rotational
equivariance.

## Scope

This result is a theorem for the normalized Cartan endpoint dagger module. It
does not classify affine torsion extensions, physical higher-spin dynamics, or
cross-sector endpoint comparisons.

## Evidence

- `research/strominger/the-authorized-dagger-turns-grade-normalization-into-round-trip-curvature.md`;
- `research/strominger/checkers/endpoint_dagger_round_trip_curvature_checks.py`;
- `research/strominger/results/endpoint_dagger_round_trip_curvature_checks.json`.

The exact checker passes 7 of 7 gates through degree 50.

Allocator claim: `seqclaim-6df1cbb29cc50f10c138b063`.

