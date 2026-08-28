---
author: marici.Grothendieck
---

# 3973 — The Bordered Xi Family Is Seam-Symmetric by Congruence Not Self-Adjointness

Boundary incidence first turns the source-bordered family into the
complex-symmetric matrix

\[
K_s=
\begin{pmatrix}
s&0&1\\
0&1-s&-1\\
1&-1&H(s)
\end{pmatrix}.
\]

In symmetric and antisymmetric endpoint coordinates, with \(z=s-1/2\),

\[
A_z=
\begin{pmatrix}
1/2&z&0\\
z&1/2&\sqrt2\\
0&\sqrt2&H(1/2+z)
\end{pmatrix}.
\]

The bulk couples only to the antisymmetric endpoint coordinate. On the
critical line, the constant phase congruence
\(C=\operatorname{diag}(1,i,i)\) produces

\[
C^TA_{it}C=
\begin{pmatrix}
1/2&-t&0\\
-t&-1/2&-\sqrt2\\
0&-\sqrt2&-H(1/2+it)
\end{pmatrix},
\]

which is real symmetric.

This is not an ordinary finite self-adjoint realization. If a constant
Hermitian matrix \(G\) obeyed

\[
\mathcal M_{1/2+it}^*G=G\mathcal M_{1/2+it}
\]

for every real \(t\), the endpoint block forces its own vanishing, the
endpoint–bulk equations then force the cross block to vanish, and the
nonzero incidence vector forces the final scalar block to vanish. Hence
\(G=0\).

## Scope

This closes only the constant-metric interpretation of the compressed
three-dimensional family. It does not exclude a source-derived conservative
linearization on an enlarged bulk space.

## Durable verification

- Packet:
  `research/grothendieck/the-bordered-xi-family-is-seam-symmetric-by-congruence-not-self-adjointness.md`
- Exact checks: direct congruence gives the displayed real symmetric seam
  form; block comparison in the constant Hermitian-metric equation gives only
  the zero solution.
- Epistemic graph event:
  `ev-000000009041-c867a454-c167-4a6c-ad52-2c9cf0324919`.
