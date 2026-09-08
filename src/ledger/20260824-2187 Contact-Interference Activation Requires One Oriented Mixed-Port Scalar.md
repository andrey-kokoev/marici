---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2187 — Contact-Interference Activation Requires One Oriented Mixed-Port Scalar

## General mixed operator

Let

\[
H=
\begin{pmatrix}
h_{11}&h_{12}\\
h_{21}&h_{22}
\end{pmatrix}
\]

act on the two deletion-route labels. Pair the result with the standard sum
covector (sigma=(1,1)) and the hidden packet direction (p=(1,-1)^T).
Then

\[
\boxed{
\sigma Hp
=
h_{11}-h_{12}+h_{21}-h_{22}.
}
\]

Thus only the difference between the two column sums of (H) is physically
relevant for activating this packet.

## Minimal quotient

The four-dimensional space of (2\times2) operators has a
three-dimensional invisible kernel:

\[
\ker\Phi
=
\{H:\sigma Hp=0\},
\]

where

\[
\Phi(H)=\sigma Hp.
\]

Therefore

\[
\boxed{
\operatorname{Hom}(R_{\rm del},R_{\rm del})/\ker\Phi
\simeq\mathbb Q.
}
\]

The missing activation datum is only one scalar class, not an arbitrary new
matrix-valued coefficient system.

## Orientation character

Under exchange of the two deletion routes,

\[
p\mapsto-p,
\]

while (sigma) is invariant. Consequently

\[
\Phi(H)\mapsto-\Phi(H).
\]

The one-dimensional activation quotient is anti-invariant. A physical
normalization therefore requires a source-derived orientation of

\[
\text{grade-two spectator route}
\longleftrightarrow
\text{fully deleted contact route}.
\]

## Interpretation

Entries 2185–2186 show that ordinary contour doubling and branch-only
response cannot supply this scalar. Entry 2187 identifies the exact finite
datum a successful source extension must provide:

\[
\boxed{
\text{one oriented column-sum imbalance coupling deletion history to the
physical readout.}
}
\]

This is the smallest admissible target for a future Schwinger–Keldysh or
instrument construction. Any larger proposed structure must project to this
class and prove that the projection is source-normalized.

## Evidence

- Entries 2180 and 2185–2186
- `research/benincasa/checkers/minimal_mixed_route_activation_functional.rs`
- allocator claim `seqclaim-d58d9cf9038b43081c62781e`