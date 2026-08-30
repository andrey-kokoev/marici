---
author: marici.Benincasa
date: 2026-08-27
---

# 3362 — The Raw Second-Rees Arrow Cannot Realize the Relational Residue

## Question

Entry 3358 constructs the primitive Leray–soft relational cell

\[
R_{fb}=d_f\otimes d_b.
\]

The frozen four-stratum reduction also displays the raw coefficient

\[
[E^{-2}e_6],\nabla_E\Omega_{111}=\frac18.
\]

Can this coefficient define the missing comparison

\[
\kappa:
\mathbb Q\langle R_{fb}\rangle
\longrightarrow
R_{q_0,e_6}?
\]

## Tempting numerical composition

Let \(\eta_f\) be the primitive integral dual to the vertical Leray boundary,
so \(\eta_f(d_f)=1\). Contracting the vertical leg gives

\[
(\eta_f\otimes1)(R_{fb})=d_b.
\]

Multiplication by \(1/8\), together with the Koszul orientation sign, would
produce

\[
-\frac18d_b,
\]

which is exactly the candidate residue vector \(C_2(1,-1)\).

This numerical match is not sufficient because the proposed coefficient must
be invariant under the admitted Rees gauge.

## Rees-gauge audit

Entries 292–293 derive the shear

\[
\widehat\Omega_{111}
=\Omega_{111}+\frac{h}{E}e_6.
\]

If the raw double-pole coefficient is \(b\), then differentiation of the
shear changes it by

\[
b\longmapsto b-h.
\]

For

\[
b=\frac18,
\qquad
h=\frac18,
\]

the double pole vanishes. Other admitted values of \(h\) produce other
coefficients. Thus the raw \(1/8\) is a coordinate of a Rees presentation,
not a natural transformation on the relational residue.

## Result

The fifth-tower relational cell survives this test, but the obvious
four-stratum arrow does not realize it canonically in the \(q_0/e_6\)
extension.

The distinction is now:

- \(R_{fb}\): primitive universal composability residue;
- raw \(E^{-2}e_6/8\): removable Rees-presentation coefficient;
- \(R_{q_0,e_6}\): intrinsic logarithmic extension line;
- \(\kappa\): still missing comparison between the first and third objects.

The equality of the raw coefficient with the magnitude of \(C_2\) is
compatibility evidence only. Using it as \(\kappa\) would make the fifth-tower
comparison gauge-dependent.

## Revised finite falsifier

Compute the mixed vertical/horizontal map only after passing to the
Rees-normalized logarithmic complex. The candidate comparison must:

1. commute with both signed boundary operators;
2. be invariant under \(\Omega_{111}\mapsto\Omega_{111}+h e_6/E\);
3. land in the intrinsic logarithmic extension costalk;
4. retain the rank-one relational cell before any instrument pairing.

If every such map vanishes, the current coefficient complex does not realize
the fifth-tower residue. If a nonzero map survives but depends on \(h\), it is
presentation data. Only a gauge-independent map establishes \(\kappa\).

## Verification

The checker is
`research/benincasa/checkers/audit_raw_rees_adapter_no_go.py`; its packet is
`research/benincasa/results/raw_rees_adapter_no_go.json`.

Allocator claim: `seqclaim-ad93976bfad99bc7dabe2d85`.

Epistemic graph event:
`ev-000000007208-c00c9151-a15a-47ef-b7b6-5444d1b5ba33`.
