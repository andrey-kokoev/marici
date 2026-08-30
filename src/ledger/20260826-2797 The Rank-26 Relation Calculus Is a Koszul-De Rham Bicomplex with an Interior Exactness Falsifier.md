# 2797 — The Rank-26 Relation Calculus Is a Koszul–de Rham Bicomplex with an Interior Exactness Falsifier

> **Typing correction (Entry 2799):** ambient numerator enlargement alone
> does not create the missing mixed Leibniz squares. The conjecture must use a
> cofinal filtration in numerator degree, Cayley–Menger pole depth, and all
> labelled marked-pole depths. “Interior” below is superseded by this labelled
> multi-interior meaning.

## Explanatory retyping

Entries 2786 and 2791 counted large first-homology spaces after adjoining relation families one at a time. Those dimensions do not explain why another family should close the complex.

The source gives a stronger organization. The five marked denominators and Cayley–Menger polynomial generate a multiplication/Koszul direction. The two retained fiber derivatives generate a de Rham direction. IBP/multiplication coherence is their Leibniz comparison.

The total differential is governed by three source identities:

\[
fg=gf,
\]

\[
\partial_r(fg)=(\partial_rf)g+f\partial_rg,
\]

and

\[
\partial_a\partial_b=\partial_b\partial_a.
\]

## Source contract audit

Using the actual frozen polynomials

\[
K,q_1,q_2,q_3,q_{23},q_{31},
\]

the exact checker verifies:

- 756 multiplication commutators;
- 252 Leibniz squares;
- 126 mixed-partial squares.

Every identity vanishes. Thus the proposed total differential is source-derived rather than selected from the residual homology.

## Hard-to-vary conjecture

For every fixed numerator degree (d), the complete labelled Koszul–de Rham complex is exact at the first relation term once the ambient cutoff exceeds (d) by the maximal polynomial shift required by the differential.

Equivalently, finite first homology may live in the moving truncation boundary layer, but no nonzero fixed-degree interior class may persist under cutoff enlargement.

This is narrower than global exactness and stronger than expecting raw dimensions to decrease.

## Finite falsifier

1. Derive all mixed IBP/multiplication cells by Leibniz.
2. Build the complete total differential at successive ambient cutoffs.
3. Filter first homology by maximal numerator degree.
4. Freeze an interior degree bound before comparing cutoffs.
5. Follow classes under the actual cutoff-inclusion map.

A nonzero class supported below the frozen degree bound that persists through three successive admissible inclusions falsifies the conjecture.

A class that moves outward with the cutoff is boundary homology and does not falsify it.

## Prohibited repair

Do not add generators selected from the observed dimensions 7541 or 7770. Only source multiplication, Leibniz, commuting fiber derivatives, and independently derived cutoff-boundary maps are admissible.

## Artifacts

- `research/benincasa/check_rank26_koszul_derham_contract.py`
- `research/benincasa/rank26-koszul-derham-contract.json`
- `research/benincasa/rank26-koszul-derham-bicomplex-conjecture.md`

## Next calculation

Derive the labelled mixed IBP/multiplication differential and export its grading shifts. Before computing homology, determine the minimal safe interior margin forced by those shifts.
