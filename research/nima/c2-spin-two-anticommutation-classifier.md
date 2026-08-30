# Exact classifier for orthogonal (C_2) spin-two sheet actions

## Problem

Classify real (2\times2) matrices (R) satisfying

\[
R^TR=I,qquad R^2=I,qquad R^TQR=-Q,
\]

for a nonzero symmetric traceless spin-two form (Q).

Because an orthogonal involution obeys (R^{-1}=R=R^T), the last
condition is equivalent to

\[
RQ=-QR.
\]

## Complete classification

Choose an orthogonal eigenbasis for (Q):

\[
Q=\mu
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad \mu\ne0.
\]

Write

\[
R=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

The anticommutator is

\[
RQ+QR
=
2\mu
\begin{pmatrix}a&0\\0&-d\end{pmatrix},
\]

so (a=d=0).  Orthogonality gives (b^2=c^2=1), and the involution
condition gives (bc=1).  Hence

\[
\boxed{
R=
\pm\begin{pmatrix}0&1\\1&0\end{pmatrix}.
}
\]

In an arbitrary basis, if (U^TQU=\mu\operatorname{diag}(1,-1)), then

\[
R=U
\left[
\pm\begin{pmatrix}0&1\\1&0\end{pmatrix}
\right]U^T.
\]

These are precisely the two reflections across the bisectors of the
principal quadrature axes.

## Mandatory (C_4) guard

If (R^2=I) is omitted, the quarter-turns

\[
\pm\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\]

also satisfy (R^TQR=-Q), but obey (R^2=-I).  They are (C_4) vector
actions, not (C_2) sheet actions.

## Higher-dimensional catalog criterion

For real symmetric (Q), an orthogonal anticommuting map sends

\[
E_\lambda(Q)\longrightarrow E_{-\lambda}(Q).
\]

Therefore an orthogonal involution (R) with (RQ=-QR) exists exactly
when every nonzero eigenvalue has a matched opposite eigenspace:

\[
\dim E_\lambda(Q)=\dim E_{-\lambda}(Q).
\]

The zero eigenspace may carry any orthogonal involution.  When
(Q^2=I), this reduces to equality of the (+1) and (-1)
multiplicities and realizes a module for the corresponding real
Clifford algebra.

## Reusable compiler certificate

```json
{
  "schema": "marici.c2_spin_two_classifier.v1",
  "dimension": 2,
  "q_signature": [1, 1],
  "requirements": [
    "R^T R = I",
    "R^2 = I",
    "R^T Q R = -Q"
  ],
  "solution_count_in_q_eigenbasis": 2,
  "solutions": [
    [[0, 1], [1, 0]],
    [[0, -1], [-1, 0]]
  ],
  "c4_false_positives_rejected": true
}
```

The accompanying checker uses exact integer arithmetic and has no
external dependencies.

