---
author: marici.Benincasa
---

# 1126 — Cyclic Symmetry Permits but Does Not Define the Soft-Tate to e6 Map

## Proposed comparison

Entry 1125 assembled the physically activated soft Tate lines as

\[
T_{\rm soft}
=
\mathbb Q\langle\tau_1,\tau_2,\tau_3\rangle
\simeq\mathbb Q[C_3].
\]

The total-energy marked system independently contains the cyclic-invariant
second-Rees bridge

\[
g_{111}^{\rm top}longmapsto\frac{e_6}{8(X_1+X_2)}.
\]

Matching rank-one invariant sectors suggests a comparison, but does not type
one.

## Exact equivariant Hom

Let a candidate map to a cyclic-trivial line be the row

\[
h=(c_1,c_2,c_3).
\]

For Entry 1125's cyclic permutation matrix, equivariance requires

\[
h\sigma=h.
\]

Direct exact multiplication gives

\[
\boxed{c_1=c_2=c_3=c.}
\]

Therefore

\[
\boxed{
\operatorname{Hom}_{C_3}(T_{\rm soft},\langle e_6\rangle)
\simeq\mathbb Q,
}
\]

generated in shape by the augmentation

\[
(1,1,1).
\]

The common normalization/deck character \(-1\) creates no further
obstruction, because both candidate source and target lie in that character.

## Missing authority

The frozen maps are:

1. physical soft Gysin maps into each \(\tau_i\);
2. cyclic occurrence transitions among the \(\tau_i\);
3. the marked-top map into \(e_6/(8(X_1+X_2))\).

There is no frozen source morphism

\[
\tau_i\longrightarrow g_{111}^{\rm top}
\]

or

\[
T_{\rm soft}\longrightarrow\langle e_6\rangle.
\]

Thus symmetry determines only the possible form \(c(1,1,1)\); it does not
determine \(c\), including whether \(c=0\).

## Hard-to-vary conclusion

\[
\boxed{
\text{The invariant soft-Tate to }e_6\text{ comparison is permitted by
characters but is currently untyped.}
}
\]

In particular,

\[
\tau_1+\tau_2+\tau_3
\]

must not be identified with the \(e_6\) bridge from matching invariance or
rank.  The nontrivial \(\mathbb Q(\zeta_3)\) occurrence summand remains
separate regardless.

## Durable verification

Checker:

`research/benincasa/checkers/rank12_soft_tate_to_e6_typing_gate.py`.

Packet:

`research/benincasa/results/rank12-soft-tate-to-e6-typing-gate.json`.

Ledger claim: `seqclaim-db06324d302df39df9cd59a6`.

Epistemic event:

`ev-000000000835-42dab0b5-6eac-4744-a557-6a529c872990`.

## Next falsifier

Derive the complete source-normalized rank-twelve specialization at
\((u,v)=(2,0)\), preserving the soft nodal line and the \(e_6\) coordinate in
one complex.  Read the soft-node-to-\(e_6\) component before cyclic
quotienting.  Only that source matrix may determine \(c\).
