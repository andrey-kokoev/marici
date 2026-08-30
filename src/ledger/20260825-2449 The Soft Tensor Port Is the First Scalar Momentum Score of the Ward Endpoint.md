---
author: marici.Benincasa
date: 2026-08-25
---

# 2449 — The Soft Tensor Port Is the First Scalar Momentum Score of the Ward Endpoint

## Question

Entry 2448 closes the generic Gram wall away from soft support. At tensor
momentum $q=0$, however, Entry 2446's longitudinal endpoint lift contains an
apparent $1/q$ pole and the TT direction is undefined. Is this a new
soft--Gram obstruction?

## Ward endpoint expansion

Let the scalar two-point coefficient be isotropic,

\[
\langle\varphi_k\varphi_{-k}\rangle=F(k),
\]

and put

\[
q=\epsilon n,
\qquad
k_2=k,
\qquad
k_3=-k-q.
\]

The primary Ward identity of Entry 2446 has endpoint target

\[
J_i(q)
=-kappa
\left[
k_iF(|k+q|)+(-k_i-q_i)F(k)
\right].
\]

Its exact first soft expansion is

\[
\boxed{
J_i(q)
=-kappa\epsilon
\left[
k_i\frac{F'(k)}k(k\mathbin\cdot n)-n_iF(k)
\right]
+O(\epsilon^2).
}
\]

The zeroth grade vanishes. Therefore Entry 2446's apparent $1/q$ endpoint
lift is removable on the source Ward target.

## Soft tensor lift

A symmetric lift of the first grade is

\[
T^{\rm soft}_{ij}
=-kappa
\left[
\frac{F'(k)}k k_i k_j-F(k)\delta_{ij}
\right].
\]

Contracting with $n_j$ reproduces the Ward target. TT projection relative to
$n$ kills the isotropic $F(k)\delta_{ij}$ term exactly, leaving

\[
\boxed{
\Pi_{\rm TT}T^{\rm soft}
=-kappa\frac{F'(k)}k
\Pi_{\rm TT}(k\otimes k).
}
\]

Thus the soft tensor port is the first radial momentum score of the scalar
two-point coefficient.

For the conformally coupled scalar normalization $F(k)=k$, one has
$F'(k)=1$. In a frame with soft direction $n=\hat z$ and hard momentum in the
$(x,z)$ plane, the plus response is

\[
-\frac{\kappa k_x^2}{2k}.
\]

It is nonzero generically and vanishes only when the hard momentum is
parallel to the soft direction, an existing collinear Gram locus.

## Result

\[
\boxed{
\text{the leading soft tensor class is recovered by the existing scalar
momentum-score/Ward endpoint port.}
}
\]

There is no new soft--Gram Carrier support and no unresolved $1/q$ residue at
this grade.

## Scope

This is the universal leading soft theorem. It does not fix subleading soft
orders or the finite renormalized part of a loop-corrected scalar two-point
function. Those require their own source normalization and cannot be inferred
from $F(k)=k$.

## Durable evidence

- `research/benincasa/check_soft_tensor_ward_score_recovery.py`;
- `research/benincasa/soft-tensor-ward-score-recovery.json`;
- Baumann et al., arXiv:2005.04234v3, equation (4.30);
- Entries 2446 and 2448;
- sequence claim `seqclaim-73c928c064d14c6bb3a983cb`.

## Next falsifier

Transport the surviving tensor trace and the Ward endpoint score through the
marked localization sequence and total-energy nearby cycle. Then test their
compatibility with the elliptic degeneration and existing Landau support.
