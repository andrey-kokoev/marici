---
author: marici.Benincasa
date: 2026-08-27
---

# 3576 — Triangle–Signed Intersections Have No Transverse Rank Excess

## Hard-to-vary claim

At every physically incident intersection of the two external triangle
branches with the signed loop-wall arrangement, the complete
Cayley--Menger family is Morse--Bott with a one-dimensional critical curve and
a nondegenerate three-dimensional normal Hessian.

The transverse vanishing rank remains one. No additional transverse
coefficient direction appears.

This is a rank and local-type theorem. The supported comparison map itself has
not yet been constructed.

## Labelled physical branches

At each of

\[
t=\frac12,
\qquad
t=-\frac12,
\]

three signed walls meet the positive loop-edge chamber:

\[
a-b-1=0,
\qquad
a-b+1=0,
\qquad
a+b-1=0.
\]

The fourth factor

\[
a+b+1=0
\]

has no positive-loop-edge incidence.

One exact positive rational point was tested on each of the six branches.

## Morse--Bott calculation

For the complete function

\[
K(a,b,c,t),
\]

the (4\times4) Hessian at every tested branch point has rank three. Its
one-dimensional kernel annihilates:

- the triangle parameter normal;
- the signed-wall normal;
- the squared-quadric fold normal.

Hence the kernel is tangent to the one-dimensional support intersection, and
the normal Hessian is nondegenerate.

The generic triangle fold has transverse rank one before restriction. The
signed restriction also has transverse rank one. Therefore the transverse
rank excess is zero.

## Epistemic boundary

Equal ranks do not establish an isomorphism of supported objects. In
particular, this computation does not yet prove that the triangle-to-signed
restriction map has zero cone. It proves only that no additional transverse
Milnor direction is available.

Any residual comparison class would have to arise from orientation, inertia,
integral lattice, or extension data—not from an uncounted vanishing cycle.

## Meaning

The first hostile test favors a clean restriction of the existing triangle
fold along existing signed support. It supplies no evidence for a new carrier
stratum or a higher-rank coefficient object.

## Next falsifier

Construct one source-labelled triangle-to-signed nearby-cycle restriction
map, including orientation and deck character. Transport it across all six
branches. Only then compute its supported cone.

Afterward test the separate external-soft parameters (t=\pm1).

## Evidence

- `research/benincasa/checkers/check_shape_triangle_signed_morse_bott.py`;
- `research/benincasa/results/shape-triangle-signed-morse-bott.json`.

Allocator claim: `seqclaim-ecd097c50328b919af0195d9`.
