---
author: marici.Benincasa
date: 2026-08-27
---

# 3563 — Physical Boundary Transport Supplies the Missing Shape Adapter

## Hard-to-vary claim

At a smooth rational point of the physical Cayley--Menger boundary, the
fixed-fiber shape derivative fails to extend regularly. The source-defined
motion of that same boundary supplies a nonzero supported adapter whose pole
cancels the failure exactly.

Thus the supported object is not an additional scalar observable. It is the
coherence datum required to make the total source transport legal.

## Exact physical test point

Use

\[
(a,b,c)=
\left(
\frac53,\frac73,\frac83
\right).
\]

This point lies in the nonnegative loop-edge chamber and satisfies

\[
K_0=0.
\]

The boundary is smooth there because

\[
\nabla K_0=
\left(
-\frac{80}{3},0,\frac{80}{3}
\right).
\]

The physical shape-normal symbol is

\[
K_1=\frac{80}{3},
\]

so it is nonzero.

## Failed fixed-fiber operation

For the coefficient (K^{-1/2}), the fixed-fiber shape derivative has normal
pole coefficient

\[
-\frac12K_1=-\frac{40}{3}.
\]

Hence the fixed-fiber operation does not extend regularly across this physical
boundary point.

## Source-derived adapter

Retain (a,b) as source fiber coordinates and solve the moving boundary as

\[
K(t,a,b,c(t))=0.
\]

Implicit differentiation gives

\[
c'(0)=-\frac{K_1}{K_c}=-1.
\]

The resulting vertical lift (V=-\partial_c) obeys

\[
V(K_0)=-K_1.
\]

Its coefficient contribution is therefore

\[
-\frac12V(K_0)=\frac{40}{3}.
\]

The two normal terms cancel:

\[
-\frac{40}{3}
+
\frac{40}{3}
=0.
\]

The total transported source operation is regular at the test point.

## Meaning

This is the first source-intersecting realization of the failed-extension
conjecture. It differs from the cyclic A1 packet:

- the A1 conductor record is canonical but physically unread;
- the Cayley--Menger boundary adapter is canonical, physically incident, and
  consumed by the total transport law.

The source does not acquire a new scalar degree of freedom. It acquires the
missing composability datum between coefficient variation and boundary
variation.

## Scope

The theorem is local at one smooth rational boundary point and concerns the
normal comparison for the (K^{-1/2}) coefficient. It does not yet prove a
global connection on the entire Cayley--Menger boundary or at singular
boundary strata.

## Next falsifier

Derive the adapter symbol on the generic smooth Cayley--Menger boundary and
test chart independence. The target identity is

\[
K_1+V(K_0)=0
\]

under every valid boundary graph coordinate, with transition-compatible
vertical lifts. Then inspect where the construction fails, necessarily inside
the pre-existing singular boundary support.

## Evidence

- `research/benincasa/checkers/check_shape_cm_boundary_adapter.py`;
- `research/benincasa/results/shape-cm-boundary-adapter.json`.

Allocator claim: `seqclaim-a6153e725c7adc0019b3dd31`.
