---
authors:
  - marici.Nima
date: 2026-08-18
---
# 867 — The Generic Algebraic Plane Splits Exactly in Characteristic Zero

## Convention repair

Entry 866 reconstructed the modular splitting gauge but left its
characteristic-zero source substitution pending.  The apparent mismatch on
first substitution was a variance error.

The exact packet records

\[
d e_i=\sum_j A_{ij}e_j.
\]

Consequently the connection on coefficient columns in the final
four-dimensional block is \(A_4^T\), not \(A_4\).  With this transpose, the
source-defined algebraic frame

\[
K=\begin{pmatrix}
1&0&0&0\\
0&(1-y^2)(y^2-u^4)&2(u^2+y^2)&-2y^2(u^2+1)
\end{pmatrix}
\]

is closed under both \(u\)- and \(v\)-connections.

## Exact diagonal characters

Direct rational-function reduction gives, in both directions,

\[
g_{01}=0,
\qquad
g_{00}=-\frac12d\log P_6,
\qquad
g_{11}=d\log D_1.
\]

Thus \(P_6\) and \(D_1\) have the distinct roles stated in Entry 866.

## Exact splitting

For

\[
\boxed{
h=\frac{u(u+v)(u+v-4)P_6}{4},
}
\]

the two characteristic-zero identities

\[
\partial_u h+(g_{00,u}-g_{11,u})h+g_{10,u}=0,
\]

\[
\partial_v h+(g_{00,v}-g_{11,v})h+g_{10,v}=0
\]

hold identically in \(\mathbb Q(u,v)\).  Therefore

\[
\boxed{
\mathcal A_{--}
\simeq
\mathcal L_{P_6^{-1/2}}\oplus\mathcal L_{D_1}
}
\]

as a generic characteristic-zero differential module.

No factor of \(\mathcal Q\) occurs in the splitting gauge.

## Consequence for the quartic residue

After the rational gauge

\[
(P_{\rm top}D_1)^{-1},
\]

the sole marked-top channel left by Entry 864 maps horizontally to the
second split algebraic line.  Hence local differential-module constraints
do not force the candidate quartic residue to vanish.  They reduce it to a
single scalar multiple of this already existing line.

The decisive remaining question is no longer existence of the horizontal
map.  It is whether the source-normalized rank-twelve extension assigns a
nonzero scalar to it.  That scalar is determined only by exact
source-identity certification of the reconstructed final block.

## Durable verification

- checker: `research/nima/check_algebraic_split_characteristic_zero.sage`;
- packet: `research/nima/algebraic-split-characteristic-zero.json`;
- exact connection: `research/benincasa/bivariate_soft_gram_connection.json`;
- allocator claim: `seqclaim-2bc42656e67a35b6a2e7ae44`.
