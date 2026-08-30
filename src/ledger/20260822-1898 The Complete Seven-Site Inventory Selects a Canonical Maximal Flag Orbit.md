# Entry 1898 — The Complete Seven-Site Inventory Selects a Canonical Maximal Flag Orbit

## Frozen inventory

Enumerate every seven-site source term from the complete cosmological-
polytope facet set. Each term contains the universal prefactor

\[
G\prod_{i=1}^7g_i
\]

and six additional frozen facets. Admission requires simultaneously:

\[
\text{affine zero-face rank}=7,
\qquad
\text{denominator-row rank}=14.
\]

No candidate coefficient geometry is inspected during this census.

## Complete result

The exact search finds

\[
14728
\]

labelled source terms, grouped into

\[
2104
\]

free \(C_7\) orbits. The counts and selected orbit agree over the independent
primes (1000003) and (1000033). The selected representative additionally
passes an integer rank computation.

## Predeclared complexity score

The frozen lexicographic score is

\[
(\text{wall count},\text{strict nesting depth},
\text{separated nonadjacent region pairs},\text{labelled orbit size}).
\]

Its maximum is

\[
(6,5,0,7).
\]

There are 88 tied maximal orbits. Therefore the Carrier data do not define a
unique notion of “most complex” at this resolution. No further complexity
statistic is fitted after seeing the tie.

For the required single attack target, use the neutral convention of choosing
the lexicographically least canonical labelled key among the 88 tied orbits.
This convention carries no claim of greater physical or geometric complexity.

## Selected orbit

The resulting representative is

\[
\boxed{
G-e_{12}\mid
g_{134567}\mid
g_{14567}\mid
g_{1567}\mid
g_{167}\mid
g_{17}.
}
\]

The five connected-region walls form a strict flag

\[
\{1,7\}
\subset
\{1,6,7\}
\subset
\{1,5,6,7\}
\subset
\{1,4,5,6,7\}
\subset
\{1,3,4,5,6,7\}.
\]

The orbit is free under \(C_7\), has source multiplicity seven, affine face
rank seven, and exact denominator rank fourteen.

## Consequence

This orbit is a legitimate source object for the seven-site coefficient
falsifier. Unlike the rejected incidence of Entry 1897, its Cayley--Menger
geometry may now be constructed without adding a carrier cell.

## Next falsifier

Derive the six wall equations in labelled loop-energy variables, construct a
source-admissible full-rank seven-point cover, and determine whether the flag
leaves a nontrivial critical projection after pullback.

## Durable verification

- `research/benincasa/marici-gm/src/bin/seven_site_full_source_inventory.rs`
- `research/benincasa/results/seven-site-full-source-inventory.json`
- `research/benincasa/results/seven-site-full-source-inventory-p1000003.json`
- `research/benincasa/results/seven-site-full-source-inventory-p1000033.json`
- allocator claim: `seqclaim-1120986b7a9248eca787f3f4`
- epistemic event: `ev-000000002266-fd493191-f413-45e3-a381-057cc2875d97`
