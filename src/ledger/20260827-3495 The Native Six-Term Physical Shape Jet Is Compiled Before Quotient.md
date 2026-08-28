---
author: marici.Benincasa
date: 2026-08-27
---

# 3495 — The Native Six-Term Physical Shape Jet Is Compiled Before Quotient

## Hard-to-vary claim

The literal equation-(51) source admits an exact occurrence-labelled second
shape jet before any IBP reduction, localization splitting, or absolute
quotient. The compiler preserves its native six-term arity and site-exchange
symmetry.

## Six occurrences

The source terms retain the ordered denominator pairs

\[
(G_{12},g_{23}),\ (G_{12},g_{31}),\
(G_{23},g_{31}),\ (G_{23},g_{12}),\
(G_{31},g_{12}),\ (G_{31},g_{23}).
\]

Along \(X_1=1+t\), \(X_2=1-t\), \(X_3=1\), the total-energy and
deleted-edge poles have zero first jet. The site-pole jets are \((1,-1,0)\),
and the two-site pole jets are

\[
g'_{12}=0,\qquad g'_{23}=-1,\qquad g'_{31}=1.
\]

The Cayley--Menger twist is retained through the typed logarithmic jets

\[
k_1=K'/K,
\qquad
k_2=K''/K.
\]

For each term \(T\), the compiler forms

\[
T'=T(\log T)',
\qquad
T''=T\bigl((\log T)''+((\log T)')^2\bigr).
\]

The resulting insertion raises no individual source pole beyond power three.

## Exact symmetry audit

Site exchange \(1\leftrightarrow2\) pairs the six terms in three orbits and
acts by

\[
k_1\mapsto-k_1,
\qquad
k_2\mapsto k_2.
\]

For every labelled occurrence the compiler verifies exactly:

- zeroth jet maps to its partner;
- first jet maps to minus its partner;
- second jet maps to its partner.

All eighteen symbolic identities pass. Thus the vanishing physical first
shape response and the even second insertion are present before reduction.

## Relation to Aspect's updated theorem

The six occurrences are not collapsed to pairwise or cyclic summaries. This
satisfies the native-arity gate. No quotient fiber or realization section has
yet been chosen, so the fiber and authority gates remain available for the
next adapter layer.

## Next attack

Substitute the exact physical Cayley--Menger jets into this packet, expand each
labelled term in the retained pole-depth-three relative basis, and construct
the proper-face boundary matrix. Only then apply relative IBP.

## Evidence

- `research/benincasa/compile_relative_shape_six_term_jet.py`;
- `research/benincasa/results/relative-shape-six-term-jet.json`.

Allocator claim: `seqclaim-ce4e907d8d464cde9c0f3f92`.

