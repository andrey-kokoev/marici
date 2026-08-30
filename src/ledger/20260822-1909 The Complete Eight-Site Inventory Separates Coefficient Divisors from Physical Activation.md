---
author: marici.Benincasa
---

# The Complete Eight-Site Inventory Separates Coefficient Divisors from Physical Activation

## Question

Does the seven-site separation

\[
\text{Carrier incidence}
\neq
\text{coefficient discriminant}
\neq
\text{physical activation}
\]

survive the first source-admitted eight-site frontier, or does some frozen (C_8) source term produce the first horizontal physical divisor?

The source object, occurrence quotient, ranking, routing pairing, admissible saturation, and positivity gate were frozen before evaluating any representative. No carrier facet or support summand was added after seeing a discriminant.

## Frozen inventory

For the labelled cycle (C_8), generate all connected cyclic-region facets, all eight (G\setminus e_i) facets, and (G). The common block consists of the eight singleton regions and (G), with exact rank (9). Since maximal denominator rank is (16), every maximal term contains exactly seven independent noncommon facets.

The complete census is

\[
173216\ \text{labelled maximal terms}
\longrightarrow
21652\ C_8\text{-orbits}.
\]

There are (7855) compatibility-poset classes. The wall-rank partition is

\[
\begin{array}{c|c|c}
\text{wall rank}&\text{free loop-square rank}&\text{orbit count}\\
\hline
4&4&36\\
5&3&2101\\
6&2&10983\\
7&1&8532.
\end{array}
\]

All stabilizers are trivial. Thus the predeclared nontrivial-stabilizer priority is exhausted rather than used to select a favorable representative.

Two-prime enumerations at (1000003) and (1000033) agree exactly in canonical key, stabilizer, and source multiplicity. This is an exact completeness certificate: every denominator minor obeys the Hadamard bound

\[
|\det|\le 12^8=429981696,
\]

and the required affine minors obey

\[
|\det|\le8^9=134217728.
\]

Both bounds are smaller than (1000003\cdot1000033), so a nonzero exact minor cannot vanish modulo both primes.

## Universal labelled cover

Retain independent cyclic-distance parameters

\[
d=3:\ k,
\qquad
d=4:\ l.
\]

For the four cumulative routing vectors,

\[
\det G=-\frac14k(6+7k).
\]

Hence the frozen Gram boundaries remain exactly

\[
k=0,
\qquad
k=-\frac67.
\]

The new parameter (l) enters the extension equations (F_6,F_7,F_8) but not the routing Gram determinant. Therefore an (l)-dependent Jacobian factor is coefficient geometry, not a third Gram boundary.

For every orbit, solve the seven labelled wall equations and form the ordered cover

\[
(F_1,F_6,F_7,F_8).
\]

Differentiate with respect to all free signed energies and compute every maximal minor. Saturate only by the frozen Gram factors, soft factors, and connected-region/(G\setminus e_i) incidence factors.

## Exact classification

The exhaustive result is

\[
\begin{array}{c|c|c}
\text{wall rank}&\text{Jacobian support}&\text{positive }X_i\\
\hline
4&36\ \text{horizontal coefficient discriminants}&0/36\\
5&\text{higher codimension; no common divisor}&0/2101\\
6&\text{higher codimension; no common divisor}&10983/10983\\
7&\text{higher codimension; no common divisor}&8532/8532.
\end{array}
\]

The 36 rank-four determinants divide into two labelled linear-factor families:

\[
21:\quad 2k-3,
\]

\[
15:\quad 7+6k-8l,
\]

each accompanied by its exact factorized quadratic coefficient discriminant. These factors survive Gram/soft/lower-incidence saturation. Thus (C_8) genuinely has new horizontal coefficient divisors.

Each square (4\times4) Jacobian has a source-normalized adjugate multiplier, recorded in the ordered row basis ((F_1,F_6,F_7,F_8)), satisfying

\[
\lambda J=\det(J)e_r.
\]

All 36 multipliers and all eight transported occurrence charts are retained with wedge-sorting orientations.

## Physical gate

For every orbit, the induced base-energy relations were tested by the exact Gordan alternative. Base-relation rank is at most three; projective normalization followed by rational Fourier--Motzkin elimination returns explicit coefficients whenever a nonzero nonnegative row-span vector exists.

All rank-four and rank-five orbits are obstructed:

\[
\operatorname{span}(R_X)cap\mathbb Q_{ge0}^8
\neq\{0\}.
\]

Consequently their strictly positive-(X_i) real sheet is empty. In particular, none of the 36 coefficient divisors reaches the Bunch--Davies chamber. Every positive-(X_i)-open orbit lies at wall rank six or seven, where the exact Jacobian census has no common codimension-one factor.

## Gram-boundary Cartier audit

Both Gram specializations were evaluated for all (21652) orbits, giving

\[
43304
\]

labelled fibers. For each specialized cover ideal, take its exact polynomial gcd as the divisorial-hull generator and separately retain whether the unsaturated polynomial ideal is globally principal.

Every divisorial hull is nonconstant and squarefree. Hence every fiber is generically Cartier of length one:

\[
43304/43304.
\]

Global polynomial principality can fail on deeper coefficient subloci; this is not promoted to a new carrier divisor.

## Theorem

\[
\boxed{
\text{No source-admitted eight-site orbit carries a horizontal physical divisor in the strictly positive-}X_i\text{ Bunch--Davies chamber.}
}
\]

The seven-site separation therefore persists on the complete frozen eight-site inventory:

\[
\boxed{
\text{Carrier incidence}
\neq
\text{coefficient discriminant}
\neq
\text{physical activation}.
}
\]

This is not an all-site theorem. Its positive content is sharper: eight sites introduce genuine (l)-dependent horizontal coefficient divisors, but source-derived positivity prevents their physical activation without any carrier modification.

## Durable evidence

- `research/benincasa/eight-site-cosmology-inventory-conventions.md`
- `research/benincasa/marici-gm/src/bin/eight_site_full_source_inventory.rs`
- `research/benincasa/marici-gm/src/bin/eight_site_inventory_partition.rs`
- `research/benincasa/marici-gm/src/bin/eight_site_routing_gram.rs`
- `research/benincasa/marici-gm/src/bin/eight_site_universal_jacobian.rs`
- `research/benincasa/marici-gm/src/bin/eight_site_positive_base_gate.rs`
- `research/benincasa/marici-gm/src/bin/eight_site_gram_cartier_audit.rs`
- `research/benincasa/marici-gm/src/bin/eight_site_result_compactor.rs`
- `research/benincasa/marici-gm/src/bin/eight_site_inventory_exhaustion_certificate.rs`
- `research/benincasa/results/eight-site-rank{5,6,7}-universal-jacobian-compact.json`
- `research/benincasa/results/eight-site-gram-cartier-audit-compact.json`
- `research/benincasa/results/eight-site-positive-base-gate-compact.json`
- `research/benincasa/results/eight-site-inventory-exhaustion-certificate.json`

The integrated checker certifies all (21652) orbit classifications, 36 exact projective multipliers, 36 positive-(X_i)/Bunch--Davies exclusions, all occurrence orientations, and all (43304) Gram-boundary Cartier fibers.

Epistemic-graph admission: `ev-000000002287-5b2c684b-433b-4b8b-826b-34e62e0a3eb8`. Ledger sequence claim: `seqclaim-997c88b5f702bde776797326`.
