# Markov Green analytic associator and pentagon

## Question

Does the sourced scalar Markov Green constructor instantiate an analytic associator and pentagon rather than only a symbolic coherence token?

## Claim boundary

This packet proves coherence only for normalized one-dimensional Green chains with declared path-product completion and \(|a_i|<1\). It does not extend to unrestricted Green amalgamation or operator-valued kernels.

## Certificate bundle

A chain certificate is

\[
C(a_1,\ldots,a_n)
=
\left(G_{n+1},\det G_{n+1},\mathcal E\right),
\]

where

\[
(G_{n+1})_{ij}
=
\prod_{k=\min(i,j)}^{\max(i,j)-1}a_k,
\qquad
\det G_{n+1}=
\prod_{k=1}^n(1-a_k^2),
\]

and \(\mathcal E\) is the ordered edge list. Concatenation is admitted only when interface normalizations agree and the concatenated edge list is retained.

## Associator

For three composable certified segments, both parenthesizations produce the same ordered edge list. Every cross pairing is the product over the unique intervening sublist, so the completed Gram matrices and determinant witnesses agree entrywise. The associator is therefore the identity isometry on the common Gram realization, not merely equality of endpoint correlations.

## Pentagon

For four segments, each of the five parenthesizations maps to the same certificate

\[
C(a_1,a_2,a_3,a_4).
\]

Every associator edge in Mac Lane's pentagon is the identity on this certificate. The two pentagon composites are equal identity isometries. Positivity is preserved because the determinant remains the positive product \(\prod_i(1-a_i^2)\).

## Hostile test

If one route replaces a nonadjacent pairing by a value not equal to its path product, its matrix differs from the canonical certificate even when adjacent pairings and dimensions agree. Such a route has no associator cell in this restricted analytic sector.

## Disposition

The scalar Markov Green sector instantiates sourced analytic certificate closure, strict associators, and the pentagon law. This is one genuine sub-equipment fragment. It does not close interchange, general Beck–Chevalley, operator-valued Green composition, or finite-to-closed completion.

## Verification

- `research/voevodsky/checkers/check_markov_green_analytic_pentagon.py`
- `research/voevodsky/results/markov_green_analytic_pentagon.json`
