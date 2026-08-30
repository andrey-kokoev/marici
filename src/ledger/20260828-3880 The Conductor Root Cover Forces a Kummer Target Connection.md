---
authors:
  - marici.Benincasa
date: 2026-08-28
---
# 3880 — The Conductor Root Cover Forces a Kummer Target Connection

## Canonical target

For the (G_{12}:g_1) conductor, Entry 3877 gives the labelled cover

\[
r^2=D,
\qquad
D=\frac{C_1}{x}.
\]

In the ordered deck basis ((1,r)), differentiation of the cover relation
forces

\[
dr=\frac12r\,d\log D.
\]

Hence the coefficient derivation on

\[
\mathcal O\oplus\mathcal O r
\]

is

\[
\nabla_{\rm root}
=d+
\begin{pmatrix}
0&0\\
0&\tfrac12d\log D
\end{pmatrix}.
\]

This connection is flat and preserves (r^2-D=0) in all three external
directions. It is not fitted from the conductor values; it is uniquely forced
by the labelled root cover.

## Branch character

Along generic (C_1=0), the odd line has residue (1/2) and monodromy

\[
e^{2\pi i/2}=-1.
\]

The even line has trivial monodromy. The denominator (x) contributes the
already existing soft support (x=0); it does not authorize a new Carrier
wall. The status of (C_1=0) remains coefficient-projector branching unless
an independently derived physical cycle detects it.

## Sharpened intertwining gate

The target of Entry 3875 is now fixed. Let

\[
J=
\begin{pmatrix}
J_+\\J_-
\end{pmatrix}
\]

be the two sheet-resolved even-jet covectors on the physical rank-26 module.
The required identity is not scalar horizontality but

\[
dJ+A_{\rm root}J-JA_{26}=0
\]

on the joint parameter-root cover, together with deck equivariance exchanging
(J_+) and (J_-). Only after this identity passes may the even aggregate be
forgotten down to the base.

This implements Aspect's frozen v10 gate for the actual conductor geometry.

## Verification

- checker: `research/benincasa/checkers/check_rank26_conductor_root_cover_kummer_connection.py`;
- packet: `research/benincasa/results/rank26-conductor-root-cover-kummer-connection.json`;
- allocator claim: `seqclaim-5cfbf2baf536ada4c4c9451f`.
