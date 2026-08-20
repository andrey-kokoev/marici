---
title: "The Two Local Kummer Generators Are Tetrahedral Normal Functions"
date: 2026-08-20
entry: 1191
status: superseded-as-cokernel-not-cohomology
sector: cosmology
---

# 1191 — The Two Local Kummer Generators Are Tetrahedral Normal Functions

Sequence claim: `seqclaim-69329b7f15da4e2203bef611`.

> **Supersession notice.** The tetrahedral form exposed a missing
> fourfold-concurrence cell. Whenever that cell is off the branch, its
> boundary kills the displayed generator. Entry 1192 performs the full
> pair--triple--quadruple calculation; only its residual (H^2), not these
> raw cokernel generators, is a surviving coefficient candidate.

## Representative six-mark term

Take the first six-geometric-mark source term. Entry 1190 gives a
two-dimensional deck-anti-invariant cokernel. Compute the left nullspace of
the exact anti-invariant pair-to-triple incidence matrix, retaining the
source labels.

The result has two primitive generators. Each is supported on four triples
with coefficients

\[
\boxed{(1,-1,1,-1).}
\]

They are the alternating faces of a labelled four-mark tetrahedron. For
example, the first generator is supported on

\[
\begin{aligned}
&(G\setminus e_{12},g_1,g_{14})
-(G\setminus e_{12},g_1,g_4)\\
&\quad +(G\setminus e_{12},g_{14},g_4)
-(g_1,g_{14},g_4).
\end{aligned}
\]

The second has the same form with the source occurrence
\(g_{134}/g_2\) and \(g_3\).

## Geometric typing

An off-branch triple contributes the deck-anti-invariant degree-zero divisor

\[
\delta_{ijk}=[p_{ijk,+}]-[p_{ijk,-}].
\]

On a smooth elliptic pair curve, its Abel--Jacobi image is nonzero whenever
the two points are distinct. On a split rational pair, the analogous class
lives in the generalized Jacobian/Kummer torus.

Therefore each cokernel generator defines a source-labelled normal-function
candidate

\[
\boxed{
\nu_a
=
\sum_{ijk}c^{(a)}_{ijk}\,operatorname{AJ}(\delta_{ijk}),
\qquad a=1,2.
}
\]

This is the correctly typed possible extension between the surviving
elliptic \(W_5\) systems and the two-dimensional Kummer quotient.

## What incidence does not decide

The incidence matrix proves that the two tetrahedral combinations survive
as coefficient cokernels. It does not prove that their Abel--Jacobi images
are nonzero after all four terms are transported into a common Jacobian.

Thus

\[
\boxed{
W_{6,-}\ne0
\quad\not\Rightarrow\quad
\text{nontrivial Gauss--Manin extension}.
}
\]

Nor may the normal functions be compared by choosing unrelated origins on
the five elliptic pair curves.

## Next falsifier

Construct the common relative Jacobian/1-motive of the six-mark incidence
diagram. Transport the four divisors in each tetrahedral generator through
the source residue maps, and compute \(\nu_1,\nu_2\) there. Acceptable
outcomes are:

- both vanish by an exact reciprocity relation;
- one or both define nontrivial sector-specific extensions;
- the source does not provide the comparison maps needed to place the four
  divisors in one Jacobian.

No scalar connection or new support divisor should be fitted to decide this.

## Evidence

- `research/benincasa/checkers/four_site_qg_kummer_normal_functions.py`
- `research/benincasa/results/four-site-qg-kummer-normal-functions.json`
- Entries 1189--1190.
