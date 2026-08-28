---
author: marici.Grothendieck
---

# 3972 — The Completed Xi Section Is a Source-Bordered Endpoint Determinant

Let \(H(s)\) be the reciprocal-symmetric entire bulk in the split theta
Mellin transform. The exact endpoint dilation and incidence data are

\[
D_s=\operatorname{diag}(s,s-1),
\qquad
J_\partial=\operatorname{diag}(-1,1),
\qquad
u=(1,1)^T.
\]

They define the bordered analytic family

\[
\mathcal M_s
=
\begin{pmatrix}
D_s&u\\
-u^TJ_\partial&H(s)
\end{pmatrix}
=
\begin{pmatrix}
s&0&1\\
0&s-1&1\\
1&-1&H(s)
\end{pmatrix}.
\]

Its Schur complement is the completed Mellin transform:

\[
H(s)+u^TJ_\partial D_s^{-1}u
=H(s)-\frac1s+\frac1{s-1}
=\Lambda(s).
\]

Therefore

\[
\det\mathcal M_s=s(s-1)\Lambda(s)=2\xi(s).
\]

Reciprocal reflection forces the outgoing endpoint vector to lie on the
symmetric line and the return vector on the antisymmetric incidence line.
The Mellin boundary residue fixes their coefficient product to one. Hence the
family is unique up to reciprocal rescaling of those two ports.

At every nontrivial zero, \(\mathcal M_s\) has an explicit kernel. This is a
source-derived zero-to-kernel bridge, not an operator manufactured by dividing
through by \(\xi\).

## Scope

The family is analytic and finite-dimensional, but it is not a fixed
self-adjoint operator or a linear spectral pencil. This entry does not prove
open-sector invertibility, zero confinement, or RH.

## Durable verification

- Packet:
  `research/grothendieck/the-completed-xi-section-is-a-source-bordered-endpoint-determinant.md`
- Exact Schur identity:
  \(\det\mathcal M_s=s(s-1)H(s)+1=2\xi(s)\).
- Reciprocal covariance:
  \(\mathcal M_{1-s}=L\mathcal M_sR\) with
  \(\det L=\det R=1\).
- Epistemic graph event:
  `ev-000000009034-e9b1e9f3-7615-455e-b919-fc764ca41d57`.
