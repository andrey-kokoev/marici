---
title: "The Five-Cycle Incidence Predicate Equals the Source OFPT Predicate"
date: 2026-08-20
entry: 1250
status: established-source-equivalence
author: marici.Benincasa
---

# 1250 — The Five-Cycle Incidence Predicate Equals the Source OFPT Predicate

Sequence claim idempotency key:
`marici-benincasa-five-cycle-eq33-predicate-equivalence-20260820`.

## Source formula

For the physical-pole representation of a cosmological-polytope canonical
form, Benincasa--Torres Bobadilla, arXiv:2112.09028, Eq. (33), fixes

\[
\mathcal G_\circ
=
\{\mathcal G,\{\mathfrak g_s\}_{s\in\mathcal V}\}
\]

and sums over sets \(\mathcal G_c\) of compatible subgraphs. For a graph with
\(n_e\) edges, each term contains \(n_e-1\) additional denominators. This is
the OFPT recursion representation.

## Exact predicate comparison at five sites

For the five-cycle, Entry 1199 fixes

\[
(G,g_1,g_2,g_3,g_4,g_5),
\]

which is exactly \(\mathcal G_\circ\), and chooses four additional facets,
which is exactly

\[
n_e-1=5-1=4.
\]

Its checker accepts a four-set \(T\) precisely when:

1. the four source facets have a nonempty common source-vertex set;
2. that set has affine dimension
   \[
   (2n-1)-4=5,
   \]
   hence projective codimension four in \(\mathcal P_{C_5}\);
3. the ten complete denominator normals have rank ten.

Conditions 1--2 are exactly the source compatibility condition that the four
facets meet on the cosmological polytope in expected codimension. Condition 3
adds the required nondegeneracy of the corresponding rational term.

Therefore the 180 accepted sets are exactly the \(\mathcal G_c\) terms in the
source Eq. (33) representation for this labelled five-cycle.

## Coefficient normalization

Entry 1246 proves

\[
|\det M_T|=2^5
\]

for every accepted term. After the shared ambient-orientation normalization,
the source Eq. (33) assigns every term unit coefficient. Thus the canonical
function is now serialized, up to the one global convention already common to
the lower-arity packets:

\[
\boxed{
\Omega_{C_5}(X,y)
=
\frac{1}{G\prod_{i=1}^{5}g_i}
\sum_{T\in\mathfrak T_{180}}
\frac{1}{\prod_{q\in T}q(X,y)}.
}
\]

No fitted numerator or term coefficient is used.

## Corrections to the preceding frontier

- Entry 1245 correctly identified that incidence data alone did not authorize
  a canonical sum; the missing authority is now supplied by Eq. (33).
- Entry 1248 remains superseded for the reason in Entry 1249.
- The source-normalized five-site scalar period is now a valid computational
  input.

## Next finite target

Compile the 180-term sum on the Entry 1217 multi-Kummer cover and perform a
first exact reduction before creative telescoping:

1. combine terms by their three geometric marked profiles without identifying
   labelled occurrences;
2. verify cyclic covariance of the rational form;
3. remove only source-common factors;
4. measure the reduced numerator and denominator degree on the frozen cyclic
   slice;
5. choose a Gauss--Manin or telescoping basis from that measured complexity.

## Artifact update

`research/benincasa/results/five-cycle-ofpt-packet.json` now records the
Eq. (33) provenance, fixed \(\mathcal G_\circ\), compatible-set size, exact
predicate, normalized weight, and canonical-function status.
