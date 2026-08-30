---
title: "Ordinary Wall Specialization Forgets the Unique Resonant Direction"
entry: 1768
date: 2026-08-21
status: established-typing-gate
---

# 1768 — Ordinary Wall Specialization Forgets the Unique Resonant Direction

## Question

Entry 1767 identifies one relative-sign Hom resonance over each exceptional
divisor above

\[
P_6\cap D
\qquad\text{and}\qquad
P_6\cap H.
\]

Can the existing ordinary finite-field specialization determine whether the
source extension occupies that slot?

## Labelled quotient coordinates

Use the frozen order

\[
(q_{\rm top},q_{\rm wall1},q_{\rm wall2}).
\]

Entry 873 gives the generic (D)-wall fixed mask

\[
5=(101)_2.
\]

Thus (q_{\rm wall1}) is not fixed across the primitive exact-lift
nullspace.  Entry 1767 identifies precisely (q_{\rm wall1}) as the unique
(-\tfrac12) source direction resonant with the relative-sign algebraic line
over (P_6\cap D).

Likewise, the generic (H)-wall fixed mask is

\[
3=(011)_2.
\]

Thus (q_{\rm wall2}) is not fixed, and Entry 1767 identifies precisely
(q_{\rm wall2}) as the resonant direction over (P_6\cap H).

## Result

\[
\boxed{
\text{Ordinary wall specialization forgets exactly the unique resonant
source coordinate at both intersections.}
}
\]

Therefore evaluating a chosen primitive witness on either wall cannot decide
the exceptional extension class.  The ambiguity is not incidental workflow
noise; it occurs in the exact coordinate required by the indicial theorem.

## Required next object

The finite falsifier must retain both labelled normals before specialization:

\[
\operatorname{Rees}_{(P_6,D)}C_{132},
\qquad
\operatorname{Rees}_{(P_6,H)}C_{132},
\]

where (C_{132}) denotes the complete source reduction system.  It must:

1. preserve the labelled top, wall-1, and wall-2 quotient coordinates;
2. retain the entire primitive exact-lift module;
3. derive the exceptional transition rather than choose a witness;
4. project the exceptional associated grade to the unique Hom kernel of
   Entry 1767.

A nonzero projection establishes a supported relative-sign coefficient
extension over the existing carrier.  A zero projection closes the route.

## Durable artifacts

- checker: `research/benincasa/checkers/p6_wall_rees_necessity.rs`;
- result: `research/benincasa/results/p6-wall-rees-necessity.json`;
- convention note: `research/benincasa/p6-wall-rees-necessity.md`;
- allocator claim: `seqclaim-401295932a05aee682c3e176`.

