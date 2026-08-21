---
title: "Exact Cyclic Symmetry Forbids a Physical Rank-Three Five-Resultant Slice"
date: 2026-08-20
entry: 1256
status: established-physical-no-go-and-correction
author: marici.Benincasa
---

# 1256 — Exact Cyclic Symmetry Forbids a Physical Rank-Three Five-Resultant Slice

Sequence claim: `seqclaim-6cd283ae720d87cbe63b699d`.

## Defect found

Entry 1234 froze

\[
P_k=
\left(
\cos\frac{2\pi k}{5},
\sin\frac{2\pi k}{5},
1
\right).
\]

The exact sum is

\[
\boxed{
\sum_{k=0}^{4}P_k=(0,0,5)\neq0,
}
\]

with squared norm 25 in the declared Euclidean metric. Hence the global
momentum-conservation condition for the five site resultants fails.

Adding opposite external-momentum pairs at a site changes the site energy but
not its resultant. It therefore cannot repair this defect.

## Representation-theoretic no-go

The failure is not peculiar to the chosen cone height. Let five real vectors
\(P_k\in\mathbb R^3\) form one exact \(C_5\)-orbit. Every real
three-dimensional representation of \(C_5\) decomposes as

\[
\mathbb R^3
\simeq
\mathbb R_{\rm triv}\oplus V_2,
\]

where \(V_2\) is a real rotation plane. The orbit sum is five times the
projection onto \(\mathbb R_{\rm triv}\). Therefore

\[
\sum_kP_k=0
\quad\Longrightarrow\quad
P_k\in V_2
\quad\Longrightarrow\quad
\operatorname{rank}\operatorname{Gram}(P_1,\ldots,P_5)\le2.
\]

Thus

\[
\boxed{
\text{exact }C_5
+
\text{momentum conservation}
+
\text{physical }d=3
\;Longrightarrow\;
\text{Gram rank at most }2.
}
\]

There is no exactly cyclic, momentum-conserving, Gram-rank-three five-resultant
slice in physical three-space.

## Retyping of prior results

Entry 1234 and its generated JSON are corrected from “physical slice” to
“nonphysical algebraic cyclic Gram family.” Entries 1235--1244 remain exact
calculations on that algebraic family, including their wall and Landau
resultants. They no longer provide a physical five-site Landau-support theorem.

Likewise, Entries 1251, 1253, and 1254 retain their abstract cyclic/deck
representation content, but their interpretation as a reduction of a physical
cyclic period is withdrawn.

The generic source carrier, canonical OFPT representation, multi-Kummer cover,
and physical contour construction are unaffected.

## Consequence for the period program

The next physical one-parameter family must relinquish exact \(C_5\) symmetry.
It must be frozen by the following order:

1. choose five nonzero resultants in \(\mathbb R^3\) with
   \(\sum_iP_i=0\);
2. verify a rank-three routing Gram matrix;
3. choose site energies compatible with external momentum decompositions;
4. retain only the actual residual stabilizer;
5. derive the specialized canonical period and Landau support afresh.

No cyclic averaging may be used to reduce the physical coefficient module on
that replacement slice.

## Artifact correction

`five_site_cyclic_physical_slice.rs` now proves the nonzero total resultant and
emits a corrected v2 packet classifying the family as algebraic and
nonphysical.

