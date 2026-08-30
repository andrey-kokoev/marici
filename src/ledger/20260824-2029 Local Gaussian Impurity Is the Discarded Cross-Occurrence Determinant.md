---
author: marici.Benincasa
---

# 2029 — Local Gaussian Impurity Is the Discarded Cross-Occurrence Determinant

## Question

Entry 2028 proposed comparing occurrence-forgetting with Gaussian readout. Does their mismatch have a canonical expression in the resolved two-mode covariance, or is it merely a qualitative restatement of partial trace?

## Frozen resolved covariance

For the two-mode squeezed state with real squeezing coordinate \(\lambda\), write the source-normalized covariance in labelled blocks

\[
V=
\begin{pmatrix}
A&C\\
C&A
\end{pmatrix},
\]

where

\[
A=aI_2,
\qquad
C=c\,\operatorname{diag}(1,-1),
\]

and

\[
a=\frac{1+\lambda^2}{2(1-\lambda^2)},
\qquad
c=\frac{\lambda}{1-\lambda^2}.
\]

The occurrence labels distinguish the diagonal block \(A\) retained by restriction from the cross-occurrence block \(C\) discarded by it.

## Exact identity

Global purity gives

\[
a^2-c^2=\frac14,
\qquad
\det V=(a^2-c^2)^2=\frac1{16}.
\]

The reduced one-occurrence impurity is

\[
\Delta_{\rm loc}=\det A-\frac14=a^2-\frac14.
\]

Since

\[
\det C=-c^2,
\]

the purity identity yields

\[
\boxed{
\Delta_{\rm loc}=-\det C.
}
\]

Thus the entire local impurity is the signed determinant of the cross-occurrence covariance removed by forgetting the partner.

## Result and typing limit

This is stronger than a rank or dimension analogy: it identifies the exact source-labelled correction term. However,

\[
\boxed{
\Delta_{\rm loc}=-\det C
\text{ is a nonlinear covariance identity, not yet a Beck--Chevalley theorem.}
}
\]

The determinant is nonlinear, and no chain-level natural transformation between occurrence restriction and the Gaussian readout functor has yet been constructed. Calling the identity a Beck--Chevalley defect now would overstate its type.

## Architectural consequence

The resolved coefficient packet naturally consists of

\[
(A_k,A_{-k},C_{k,-k}).
\]

Occurrence-forgetting removes \(C_{k,-k}\); the faithful local readout must then acquire the correction \(-\det C_{k,-k}\). This suggests a general port-adapter pattern:

\[
\text{forget cross-occurrence coefficient}
\quad\Longrightarrow\quad
\text{add its invariant contraction to the local port}.
\]

Whether this pattern extends beyond Gaussian determinants is open.

## Verification

The exact checker verifies the identity and global purity at five rational squeezing parameters:

`research/benincasa/checkers/cross_occurrence_impurity_defect.py`

`research/benincasa/checkers/results/cross-occurrence-impurity-defect.json`

## Next falsifier

Linearize the determinant by passing to the exterior-square covariance line. Construct

\[
\wedge^2V
\]

and test whether occurrence restriction induces a typed linear map whose relative term is the cross block \(C\wedge C\). If so, the nonlinear identity is the scalar shadow of a genuine relative comparison object. If no canonical exterior-square map respects the labelled symplectic structure, retire the Beck--Chevalley interpretation.

## Provenance

- Entries 2025, 2028;
- allocator claim `seqclaim-cb72f5a989e676e1b177df21`.

Epistemic graph event: `ev-000000002765-c03e5bcb-9cc9-49d4-a5b2-5be652b3dffb`.
