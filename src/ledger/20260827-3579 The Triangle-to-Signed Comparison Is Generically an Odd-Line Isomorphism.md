---
author: marici.Benincasa
date: 2026-08-27
---

# 3579 — The Triangle-to-Signed Comparison Is Generically an Odd-Line Isomorphism

## Hard-to-vary claim

The source-labelled nearby-cycle comparison from the external triangle fold to
each physically incident signed-wall branch is a rank-one isomorphism at
generic points. Its coefficient is derived from the full family Hessian,
independent of the chosen normal lift, and compatible with the odd deck
character.

Therefore the six generic supported comparison cones vanish.

## Typed construction

Let (u=t-t_0) be the labelled triangle normal, (H) the labelled signed
wall, and (L) the squared-quadric fold normal.

Choose any signed-normal lift (W_H) satisfying

\[
dH(W_H)=1,
\qquad
dL(W_H)=0,
\qquad
dt(W_H)=0.
\]

The comparison coefficient is

\[
m_{t_0,H}
=
\operatorname{Hess}_K(\partial_t,W_H).
\]

Changing (W_H) by the critical-curve tangent does not change (m), because
that tangent lies in the kernel of the full Hessian. Thus the map is intrinsic
to the labelled normals.

## Exact matrices

In the ordered branch convention

\[
\begin{aligned}
&t=+1/2:
&&a-b-1,quad a-b+1,quad a+b-1,\\
&t=-1/2:
&&a-b-1,quad a-b+1,quad a+b-1,
\end{aligned}
\]

the six (1\times1) matrices are

\[
-48,quad48,quad6,quad48,quad-48,quad-6.
\]

All are nonzero units at the chosen generic rational representatives.

Both source and target lines have deck character (-1), and every scalar map
intertwines that character. No post-hoc sign normalization is required.

## Supported cone

At each generic branch point,

\[
\mathbb Q_-
\xrightarrow{m_{t_0,H}}
\mathbb Q_-
\]

is an isomorphism. Its local supported cone has rank zero.

This conclusion is local and generic. It excludes deeper zeros of the
comparison unit and does not identify integral normalization.

## Meaning

Entry 3576's equal-rank result has now been upgraded to a typed comparison
map. The triangle fold restricts coherently onto the signed support and leaves
no generic residual coefficient class.

The existing triangle and signed supports therefore close this branch without
new carrier or coefficient generators.

## Next falsifier

Factor the comparison coefficient along each full intersection curve and
locate any deeper zeros. Classify them against existing coordinate-soft
support. Then analyze the separate external-soft parameters (t=\pm1).

## Evidence

- `research/benincasa/checkers/check_shape_triangle_signed_comparison_map.py`;
- `research/benincasa/results/shape-triangle-signed-comparison-map.json`.

Allocator claim: `seqclaim-29bdf54a2430532cb94e0cd3`.
