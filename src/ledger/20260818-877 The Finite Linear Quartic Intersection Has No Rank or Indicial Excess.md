---
authors:
  - marici.Nima
date: 2026-08-18
---
# 877 — The Finite Linear Quartic Intersection Has No Rank or Indicial Excess

## The last finite proper stratum

The remaining nondeep rational intersection from Entry 863 is

\[
L:=u+v-2=0,
\qquad
(u,v)=(8/5,2/5)\in\mathcal Q.
\]

Entry 864 computed its indicial spectrum, but no generic-\(L\) comparison
had been made.

## Replicated source signature

The complete 132-equation, 372-unknown labelled source system was evaluated
at six generic points of \(L\) and at the quartic intersection.  Across two
independent large primes, every sample has

\[
\boxed{
(\operatorname{rank}M,\text{fixed mask},\text{pivot hash})
=(114,3,18185588823731398584).}
\]

Thus imposing \(\mathcal Q\) creates no source-rank, fixed-coordinate, or
pivot-chart change on the finite linear carrier.

## Exact generic indicial spectrum

Restricting the exact connections to the generic function field of \(L\)
gives

\[
\chi_{R_9}(x)=x^7(x+1)(x+2),
\]

\[
\chi_{R_3}(x)=x^2(x+\tfrac12),
\]

and

\[
\chi_{\operatorname{Hom}}(x)
=x^{14}(x+1)^2(x+2)^2
(x-\tfrac12)^7(x+\tfrac12)(x+\tfrac32).
\]

These are exactly the polynomials computed at \((8/5,2/5)\) in Entry 864.
Therefore

\[
\boxed{
\mathcal Q\cap L
\text{ has neither rank nor indicial spectral excess over generic }L.}
\]

## Consequence

Together with Entries 873--876, every source-defined proper quartic stratum
identified in Entry 863 has now been classified:

- generic \(D/H\) intersections add no rank or spectral data;
- the finite \(L\) intersection adds no rank or spectral data;
- \((0,2)\) doubles an existing exceptional direction;
- the two new directions above \((2,2)\) are regular points of an existing
  resonant exceptional connection.

No algebraic connection-support lane for \(\mathcal Q\) remains in this
marked-relative system.  A nonzero physical role would require additional
source-derived chain data rather than another quotient, gauge, or carrier
refinement.

## Durable verification

- source checker:
  `research/benincasa/marici-gm/src/bin/nima_marked_extension_linear_divisor_excess.rs`;
- source packet:
  `research/nima/marked-extension-linear-divisor-excess.json`;
- indicial checker:
  `research/nima/check_linear_quartic_intersection_indicial_excess.sage`;
- indicial packet:
  `research/nima/linear-quartic-intersection-indicial-excess.json`;
- replication primes: 2305843009213693951 and 2305843009213693723;
- SageMath: version 10.7;
- allocator claim: `seqclaim-f3e981260927012caf0a0bab`.
