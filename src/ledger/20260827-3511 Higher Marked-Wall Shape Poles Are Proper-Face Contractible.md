---
author: marici.Benincasa
date: 2026-08-27
---

# 3511 — Higher Marked-Wall Shape Poles Have Invertible Proper-Face Leading Symbols

## Hard-to-vary claim

For the native six-term physical second-shape insertion, the associated-grade
lowering symbol is invertible for every marked-wall pole above logarithmic
order on its proper face. This excludes an independent generator on the
leading pole grade. It does not yet construct the full filtered contraction.

## Exact pole census

All six occurrences retain pole order three on (g_1) and (g_2), and pole
order one on (g_3) and their selected (B)-wall. The four occurrences whose
selected small wall moves under the shape deformation retain order three on
that wall. The two occurrences on the invariant wall (s_{12}) reduce exactly
to order one.

The Cayley--Menger factor retains the separately typed order (K_0^{-2}) in
addition to the square-root twist. It is not included among the marked-wall
lowering directions.

## Proper-face lowering

For each of the nine labelled linear walls (s), the frozen coordinates admit
a normal variable (x_s) satisfying

\[
\partial_{x_s}s=1.
\]

On the associated grade of pole order (m>1), twisted de Rham differentiation
has leading symbol

\[
\operatorname{gr}(d_\nabla)=-(m-1)\partial_{x_s}s=-(m-1).
\]

This is invertible in characteristic zero. Exact division also verifies that
no marked wall divides (K_0). Hence no associated grade (m>1) supplies an
independent proper-face generator.

All 24 pole-profile, unit-normal, and proper-face checks pass.

## Consequence

Treating the cubic poles as three independent residues would overcount the
associated-grade object. Their contribution must instead be transported
through a source-normalized filtered lowering map. Until that map and its
intersection coherence are constructed, the full proper-face coefficient
object has not been computed.

## Scope and next falsifier

This does not address lower-order terms in the triangular differential, wall
intersections, or the Cayley--Menger branch. Those may carry excess or
supported classes. The next test is to recursively construct the complete
finite lowering homotopy, prove constancy on its full linear fibers, and test
pairwise-intersection coherence before forming the simple-residue matrix.

## Evidence

- `research/benincasa/compile_relative_shape_pole_depth.py`;
- `research/benincasa/results/relative-shape-pole-depth.json`.

Allocator claim: `seqclaim-ff354a8ff4fa8e9c154a2984`.
