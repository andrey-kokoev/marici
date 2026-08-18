---
authors:
  - marici.Nima
date: 2026-08-18
---
# 852 — The Fixed Boundary Maps Force a Single Marked Extension Block

## Input from Entry 851

In the source-normalized ordering

\[
\mathcal M_{12}=\mathcal W_3\oplus\mathcal M_9,
\]

Entry 851 fixes the constant maps

\[
J=\begin{pmatrix}0\\I_9\end{pmatrix},
\qquad
P=\begin{pmatrix}I_3&0\end{pmatrix}.
\]

They are not primitive-lift choices.

## Horizontality forces the block form

Write a connection component in general blocks as

\[
A_{12,\mu}=
\begin{pmatrix}
C_\mu&D_\mu\\
B_\mu&E_\mu
\end{pmatrix}.
\]

Because \(J\) and \(P\) are constant, their horizontality equations are

\[
A_{12,\mu}J=JA_{9,\mu},
\qquad
A_{3,\mu}P=PA_{12,\mu}.
\]

The first gives \(D_\mu=0\) and \(E_\mu=A_{9,\mu}\); the second gives
\(C_\mu=A_{3,\mu}\).  Therefore every accepted rank-twelve connection has

\[
\boxed{
A_{12,\mu}=
\begin{pmatrix}
A_{3,\mu}&0\\
B_\mu&A_{9,\mu}
\end{pmatrix},
\qquad B_\mu:\mathcal W_3\to\mathcal M_9.
}
\]

Once the diagonal connections are independently fixed, the only unknowns
are the two \(9\times3\) matrices \(B_x,B_y\).  The rank-twelve reducer must
not refit either diagonal block.

## Mixed flatness equation

The lower-left block of \(F_{xy}^{(12)}=0\) is

\[
\boxed{
\partial_xB_y-\partial_yB_x
+B_xA_{3,y}+A_{9,x}B_y
-B_yA_{3,x}-A_{9,y}B_x=0.
}
\]

Thus flatness is exactly the cocycle condition for the extension-valued
one-form \(B=B_xdx+B_ydy\).

## Boundary-preserving gauge

Every frame change preserving the fixed \(J\) and \(P\) has the form

\[
G=\begin{pmatrix}I_3&0\\h&I_9\end{pmatrix}.
\]

With \(\nabla=d+A\), it acts by

\[
\boxed{
B_\mu' = B_\mu+\partial_\mu h+A_{9,\mu}h-hA_{3,\mu}.
}
\]

This is Entry 850's gauge law after permuting from
\(\mathcal M_9\oplus\mathcal W_3\) to Entry 851's
\(\mathcal W_3\oplus\mathcal M_9\) ordering.

## Consequence

The common wall-Laurent calculation has a sharply reduced target:

1. derive \(A_3\) in the oriented wall quotient;
2. retain the already certified \(A_9\);
3. solve source reduction only for \(B_x,B_y\);
4. verify the mixed flatness equation;
5. quotient by the boundary-preserving \(h\)-action;
6. only then factor the support of \([B]\).

A nonzero upper-right block, a changed rank-nine diagonal block, or a
\(\mathcal Q\)-selected nullspace representative is an immediate rejection.

## Durable verification

- source packet: `research/benincasa/marked-relative-source-maps.json`;
- contract: `research/nima/marked-relative-forced-block-contract.json`;
- checker: `research/nima/check_marked_relative_forced_block.py`;
- allocator claim: `seqclaim-aa2f114c4275d22be70c01f5`.
