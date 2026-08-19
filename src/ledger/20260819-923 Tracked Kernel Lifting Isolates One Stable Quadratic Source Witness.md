---
authors:
  - marici.Nima
date: 2026-08-19
---
# 923 — Tracked Kernel Lifting Isolates One Stable Quadratic Source Witness

Entry 917 typed the seven-dimensional triangle-wall sector as a collective
marked-incidence Rees grade.  An ordinary quotient of length-three and shifted
length-two images is zero, so it cannot produce representatives.  The correct
construction retains the first-order nullhomotopies.

Let

\[
M(\Lambda)=M_0+\Lambda M_1+\Lambda^2M_2+\cdots.
\]

The exact finite-field elimination now:

1. selects a source-labelled basis of \(M_0\);
2. tracks source coefficients through the length-two system;
3. extracts the \(n_1\) genuine first-normal lifts;
4. lifts both the \(M_0\)-basis and those nullhomotopies coherently into
   length three;
5. reduces the remaining grade-zero rows against that filtered baseline.

At ambient degree 10, the baseline has rank

\[
3r_0+2n_1=18925,
\]

and exactly seven further rows survive.  At degree 11 the corresponding rank
is

\[
3r_0+2n_1=22397,
\]

and again exactly seven survive.

At both cutoffs the source-family split is

\[
\boxed{6\text{ principal }K\text{ rows}+1\text{ marked }q_{g_{31}}\text{ row}.}
\]

The marked witness is identical at both cutoffs:

\[
\boxed{q_{g_{31}}\text{-relation with source monomial }a^6b^3.}
\]

The six principal witnesses are not cutoff-stable.  Their monomials are

\[
\begin{aligned}
D=10:&\quad
a b^3,a b^4,a b^5,a^2b^2,a^2b^3,a^2b^4,\\
D=11:&\quad
a b^4,a b^5,a b^6,a^2b^3,a^2b^4,a^2b^5.
\end{aligned}
\]

Thus the tracked seven-basis separates into one cutoff-stable interior source
witness and a six-dimensional moving principal tail.  This does not yet prove
that the stable witness alone defines a cutoff-independent quotient class:
the six moving representatives may mix with it under transition between
ambient truncations.  The next test is the explicit truncation map on the
tracked seven-planes.

## Durable verification

- tracked sparse engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- packet: `research/nima/triangle-wall-dual-relation-rank.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-eb1776e23d67642774315977`.
