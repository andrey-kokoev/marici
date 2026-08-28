---
authors:
  - marici.Benincasa
date: 2026-08-28
---
# 3884 — The Conductor Sheet Collision Retains a Weighted Rank-Two Target

## Collision problem

Entry 3883 proves that the two conductor sheets are generically distinguished
by the classes ([1]) and ([a]). At the branch (C_1=0), the roots coalesce
at (a=0). The raw sheet weights appear singular because

\[
\partial_aR_1=-2xa.
\]

Write the regular spectator factor as (h(a)), so the two raw rows are

\[
J_+=\left(\frac{h(r)}r,h(r)\right),
\qquad
J_-=\left(-\frac{h(-r)}r,h(-r)\right).
\]

The naive projector frame therefore has a simple pole as (r\to0).

## Source-forced weighted lattice

Retain the trace row and the (r)-scaled anti-trace row:

\[
L(r)=
\begin{pmatrix}
\tfrac12&\tfrac12\\
\tfrac r2&-\tfrac r2
\end{pmatrix}.
\]

Exact expansion gives

\[
\lim_{r\to0}L(r)
\begin{pmatrix}J_+\\J_-\end{pmatrix}
=
\begin{pmatrix}
h'(0)&h(0)\\
h(0)&0
\end{pmatrix}.
\]

Its determinant is

\[
-h(0)^2,
\]

which is generically nonzero away from the already displayed spectator-wall
intersections.

## Result

The collision does not reduce the target to one aggregate line. Instead, the
two sheet evaluations specialize to the value/derivative dual of the
nonreduced root algebra

\[
\mathcal O[r]/(r^2).
\]

Thus the branch retains rank two, but one direction moves into the first
nilpotent layer. Determinant, eigenvalue, and aggregate descriptions all lose
the extension data carried by this weighted lattice.

This passes the second prediction produced by repeating the Deutsch move:
the explanation predicted a complete collision object before its matrix was
computed, and the exact limit realizes that object.

## Remaining gate

Pull the full physical rank-26 connection to this weighted collision lattice
and test the complete ordered matrix identity. The finite rank-two limit is
established; its horizontal compatibility remains open.

## Verification

- checker: `research/benincasa/checkers/check_rank26_conductor_collision_weighted_ranktwo.py`;
- packet: `research/benincasa/results/rank26-conductor-collision-weighted-ranktwo.json`;
- allocator claim: `seqclaim-4c5f1bcc1dfcc5a4af774d31`.
