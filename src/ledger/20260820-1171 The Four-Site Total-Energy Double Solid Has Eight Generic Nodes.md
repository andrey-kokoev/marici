---
title: "The Four-Site Total-Energy Double Solid Has Eight Generic Nodes"
date: 2026-08-20
entry: 1171
status: active
sector: cosmology
---

# 1171 — The Four-Site Total-Energy Double Solid Has Eight Generic Nodes

Sequence claim: `seqclaim-d09b25de091e1e52904fbbeb`.

## Global singular-locus equation

The four-site \(q_G\)-residue infinity branch is

\[
B_4=-\frac14\Delta^TH\Delta,
\qquad
H=\operatorname{adj}(G),
\]

with

\[
\Delta=(y_2^2-y_1^2,y_3^2-y_2^2,y_4^2-y_3^2).
\]

Assume \(\det G\ne0\). An exact support-pattern rank audit of the gradient
equations shows that, generically, the only branch singularities satisfy

\[
\Delta=0.
\]

No coordinate-support branch survives on the generic Gram locus.

## The sign orbit

Projectively,

\[
\Delta=0
\quad\Longleftrightarrow\quad
y_1^2=y_2^2=y_3^2=y_4^2.
\]

After fixing the overall projective sign, this gives

\[
\boxed{
[1:\epsilon_2:\epsilon_3:\epsilon_4],
\qquad
\epsilon_i\in\{\pm1\}.
}
\]

There are eight points. The sign-deck group \(C_2^3\) acts regularly on
them.

At each point the difference-coordinate Jacobian is invertible and Entry
1168's Hessian calculation applies. Hence the total-energy quartic double
solid has

\[
\boxed{8\text{ generic threefold }A_1\text{ nodes}.}
\]

The positive physical radial chain reaches exactly the identity occurrence

\[
[1:1:1:1].
\]

The other seven are algebraic deck translates, not additional ends of the
literal positive chain.

## Meaning

The local vanishing-cycle packet is naturally an eight-element labelled
occurrence orbit before global relations are imposed. This does not imply
that the global vanishing lattice has rank eight: relations among the eight
local cycles are controlled by the defect of the nodal double solid and must
be computed globally.

The singularities arise from the existing squaring/deck map and
Cayley--Menger branch. They require no new carrier stratum.

## Next falsifier

Compute the global defect map among the eight local vanishing cycles. In
particular, determine the rank and \(C_2^3\)-character of the smoothing
vanishing lattice and the change from the smooth benchmark \(b_3=20\) to a
small or divisorial resolution. Keep the positive physical occurrence
separate from the full deck orbit.

## Evidence

- `research/benincasa/checkers/four_site_qg_global_node_census.py`
- `research/benincasa/results/four-site-qg-global-node-census.json`
- Entries 1167--1170.
