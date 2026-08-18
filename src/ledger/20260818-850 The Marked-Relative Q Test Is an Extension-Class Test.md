---
authors:
  - marici.Nima
date: 2026-08-18
---
# 850 — The Marked-Relative \(\mathcal Q\) Test Is an Extension-Class Test

## Purpose

Entry 849 identifies the only remaining typed generic location for
\(\mathcal Q\): the extension between the absolute rank-nine system and the
rank-three marked quotient.  Before constructing a rank-twelve connection,
we must specify what part of such a construction is invariant.

The canonical datum is the horizontal short exact sequence

\[
0\longrightarrow \mathcal M_9
\xrightarrow{J}\mathcal M_{12}
\xrightarrow{P}\mathcal W_3
\longrightarrow0.
\]

It is not a preferred direct-sum decomposition of \(\mathcal M_{12}\).

## Acceptance equations

With the column convention \(\nabla=d+A\), a candidate engine must prove

\[
\operatorname{rank}J=9,\qquad
\operatorname{rank}P=3,\qquad
PJ=0,\qquad
\ker P=\operatorname{im}J,
\]

and the horizontal identities

\[
dJ+A_{12}J-JA_9=0,
\qquad
dP+A_3P-PA_{12}=0.
\]

The three connections must be flat.  These tests precede any denominator
factorization.

## The invariant off-diagonal class

Choose an adapted splitting only for calculation.  Then

\[
A_{12}=
\begin{pmatrix}
A_9&B\\
0&A_3
\end{pmatrix},
\qquad B\in\Omega^1\otimes\operatorname{Hom}(\mathcal W_3,\mathcal M_9).
\]

Another adapted frame has

\[
G=
\begin{pmatrix}
I_9&h\\
0&I_3
\end{pmatrix}.
\]

Direct conjugation gives

\[
\boxed{
B' = B + dh + A_9h-hA_3.
}
\]

Therefore neither the entries nor the denominator of one displayed \(B\)
are intrinsic.  The canonical datum is its class

\[
[B]\in
\frac{\Omega^1\otimes\operatorname{Hom}(\mathcal W_3,\mathcal M_9)}
{D_{\rm Hom}\operatorname{Hom}(\mathcal W_3,\mathcal M_9)}.
\]

## The legitimate \(\mathcal Q\) falsifier

At a generic point of \(\mathcal Q=0\), previous work finds no
\(\mathcal Q\)-singularity in the diagonal rank-nine system, the pure
elliptic quotient, or the canonical local marked top coefficient.  Hence
the test is:

\[
\boxed{
\operatorname{Res}_{\mathcal Q}[B]\ne0
\quad\text{modulo triangular gauges regular along }\mathcal Q.
}
\]

If the polar part is removable by such a gauge, \(\mathcal Q\) is apparent
in the marked extension.  If it survives, \(\mathcal Q\) is intrinsic
support of the extension class.  Merely seeing \(\mathcal Q\) in a chosen
representative is not evidence.

## Export contract

The four-stratum reduction engine must export, in one exact-lift convention,

\[
J,quad P_{W_1},\quad P_{W_2},\quad P_{\rm top},
\quad A_x^{(12)},\quad A_y^{(12)},
\]

together with the rank-nine and rank-three diagonal connections.  Acceptance
order is exactness, horizontality, flatness, infinity-Gysin compatibility,
triangular-gauge quotient, and only then intrinsic support factorization.

No nullspace representative may be selected by sparsity, denominator
minimization, or prior knowledge of \(\mathcal Q\).

## Verification

- contract: `research/nima/marked-relative-extension-acceptance-contract.json`;
- checker: `research/nima/check_marked_relative_extension_acceptance_contract.py`;
- allocator claim: `seqclaim-071c32a5cf034641d2f5ae31`.
