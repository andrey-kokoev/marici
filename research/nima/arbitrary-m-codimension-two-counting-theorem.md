# Arbitrary-rank codimension-two facet counting

For type `A_m`, partition the associahedron facets into positive-root diagonals

\[
P_{ij}=(i-1,j+1),\qquad 1\le i\le j\le m,
\]

and negative-simple fan diagonals

\[
N_k=(k,m+2),\qquad 1\le k\le m.
\]

A codimension-two facet intersection is exactly an unordered pair of noncrossing diagonals. Its root-lane counts are

\[
\#PP=2\binom{m+2}{4},\qquad
\#PN=\frac{m(m-1)(m+1)}{3},\qquad
\#NN=\binom m2.
\]

The `NN` formula follows because all fan diagonals are mutually compatible. For `PN`, `P_{ij}` crosses precisely the fan diagonals `N_k` with `i <= k <= j`; summing the `m-(j-i+1)` compatible fan choices over all intervals `[i,j]` gives the displayed cubic. For `PP`, direct interval-endpoint enumeration of distinct noncrossing pairs gives `m(m-1)(m+1)(m+2)/12 = 2*C(m+2,4)`. The executable checker independently enumerates every diagonal pair rather than assuming these formulas.

At `A3` this gives `PP=10`, `PN=8`, and `NN=3`, hence 21 strata. Their parent facets divide into 12 pentagon-square and 9 pentagon-pentagon incidences.

Verification is exact for `m=2..20` in:

- `research/nima/checkers/check_arbitrary_m_codim2_facet_incidence.py`
- `research/nima/results/arbitrary-m-codim2-facet-incidence.json`

This counts and labels every residue test. It does not construct the canonical residues or prove their cancellation.
