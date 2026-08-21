---
title: "An Asymmetric Momentum-Conserving Five-Site Physical Slice Is Frozen"
date: 2026-08-20
entry: 1257
status: active-source-compatible-physical-slice
author: marici.Benincasa
---

# 1257 — An Asymmetric Momentum-Conserving Five-Site Physical Slice Is Frozen

Sequence claim: `seqclaim-086e73f5759d31d6594bbfae`.

## Replacement resultants

Following Entry 1256's no-go theorem, relinquish exact cyclic symmetry and set

\[
\begin{aligned}
P_1&=(1,0,0),&
P_2&=(0,1,0),&
P_3&=(0,0,1),\\
P_4&=(1,2,3),&
P_5&=(-2,-3,-4).
\end{aligned}
\]

Then

\[
\boxed{\sum_{i=1}^{5}P_i=0.}
\]

All five resultants are nonzero.

## Routing nondegeneracy

Choose

\[
q_1=P_1,
\qquad
q_2=P_1+P_2,
\qquad
q_3=P_1+P_2+P_3.
\]

The routing Gram matrix is

\[
H=
\begin{pmatrix}
1&1&1\\
1&2&2\\
1&2&3
\end{pmatrix},
\qquad
\boxed{\det H=1.}
\]

The fifth focus uses

\[
q_4=P_1+P_2+P_3+P_4=-P_5
=-q_1-q_2+4q_3.
\]

Thus the physical three-variable Cayley--Menger contour is regular on this
integer routing chart.

## One physical parameter

Set

\[
X_1=\cdots=X_5=t.
\]

Since

\[
\max_i|P_i|=\sqrt{29},
\]

the literal real domain is

\[
\boxed{t\ge\sqrt{29}.}
\]

For each site, any \(t\ge|P_i|\) is realized by decomposing \(P_i\) into
external momenta with total magnitude \(t\); an opposite transverse pair can
increase that magnitude without changing the resultant.

## Symmetry audit

An exact enumeration of all 120 permutations preserving the labelled Gram
matrix finds only the identity. Hence

\[
\boxed{\operatorname{Stab}(P_1,\ldots,P_5)=1.}
\]

No cyclic or reflection quotient is admissible. All 180 OFPT terms, 26 marked
walls, and 32 Kummer characters must remain labelled in the physical period
calculation.

## Frozen period

The corrected physical target is

\[
\Pi_{C_5}^{\rm asym}(t)
=
\int_{\Gamma_3}
\frac{du_1\,du_2\,du_3}{\sqrt{\det H}}
\Omega_{C_5}(X_i=t,y(u;P)),
\qquad
\det H=1.
\]

This family is frozen before any new Landau elimination, period sampling, or
operator search.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_physical_slice.rs`
- `research/benincasa/results/five-site-asymmetric-physical-slice.json`

## Next falsifier

Recompute the one-wall Landau resultants for all 26 labelled source walls on
this asymmetric slice. Do not import the cyclic orbit reduction or any
threshold polynomial from Entries 1235--1244.

