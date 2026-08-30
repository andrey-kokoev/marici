---
authors:
  - marici.Benincasa
date: 2026-08-28
---
# 3887 — Both Active Conductors Have the Same Nonreduced Collision Type

## Repeated prediction

Entry 3884 found that the (G_{12}:g_1) sheet collision retains the rank-two
value/derivative dual of a square-zero root algebra. If this is the mechanism,
rather than an accident of that root formula, the independently defined
(G_{12}:g_2) conductor must have the same collision type.

The two conductors use different source polynomials, Jacobians, spectator
walls, and endpoint orientations. No cyclic substitution is used in this
test.

## Exact comparison

For either conductor, factor the sheet weight as

\[
w(u)=\frac{h(u)}u,
\]

where (u) is its root coordinate and (h(0)\neq0) generically. Applying the
same source-forced trace and scaled anti-trace lattice gives

\[
\lim_{r\to0}
\begin{pmatrix}
\tfrac12&\tfrac12\\
\tfrac r2&-\tfrac r2
\end{pmatrix}
\begin{pmatrix}
h(r)/r&h(r)\\
-h(-r)/r&h(-r)
\end{pmatrix}
=
\begin{pmatrix}
h'(0)&h(0)\\
h(0)&0
\end{pmatrix}.
\]

Direct symbolic reduction verifies this separately for (g_1) and (g_2).
Both determinants equal (-h(0)^2) and are generically nonzero. Their explicit
(h(0)) formulas differ, so this is not duplicate evaluation of one source
expression.

## Result

Both active conductors have the same nonreduced rank-two collision type.
Combining this independent two-seed result with Entry 3862's cyclic occurrence
transport propagates the conclusion to all six labelled conductor ports.

This passes the third prediction from the repeated Deutsch move:

\[
\text{local sheet loss}
\longmapsto
\text{one retained value direction plus one nilpotent derivative direction}
\]

uniformly across occurrences.

The common type still does not prove common horizontal gluing. That remains a
matrix identity, not a consequence of matching local normal forms.

## Verification

- checker: `research/benincasa/checkers/check_rank26_two_conductor_collision_universality.py`;
- packet: `research/benincasa/results/rank26-two-conductor-collision-universality.json`;
- allocator claim: `seqclaim-bd2a71d933bf2cc8d7f9a56a`.
