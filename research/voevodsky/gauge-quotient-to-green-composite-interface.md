# Gauge-quotient to Green composite interface

## Question

Does the existing gauge-presentation-to-Carrier quotient compose with the Markov Carrier-to-Green realization on a typed analytic domain?

## Claim boundary

The result concerns framed metric-transition Markov presentations modulo vertexwise orthogonal frame changes. It does not cover arbitrary gauge presentations or non-Markov quotient Carriers.

## Presentation and quotient

A framed presentation contains invertible frames \(R_i\) and normalized contraction transfers \(A_i\). Vertexwise orthogonal matrices act by

\[
R_i\mapsto R_iO_i,
\qquad
A_i\mapsto O_i^TA_iO_{i+1}.
\]

The quotient Carrier has invariant data

\[
M_i=R_iR_i^T,
\qquad
C_i=R_iA_iR_{i+1}^T.
\]

These data retain the ordered Markov incidence and typed transfer information needed by the realization bridge.

## Two routes

There are two routes from framed presentation to finite Green form.

1. Construct the normalized path-product kernel \(K^0\), then apply block frame congruence:

\[
K^{\mathrm{fr}}=RK^0R^T.
\]

2. Descend to metric-transition Carrier data \((M_i,C_i)\), then reconstruct long blocks by

\[
K_{ij}=C_iM_{i+1}^{-1}C_{i+1}\cdots M_{j-1}^{-1}C_{j-1}.
\]

Substitution telescopes to

\[
K_{ij}=R_i(A_i\cdots A_{j-1})R_j^T.
\]

Thus the routes agree exactly. The comparison cell is identity and invertible.

## Naturality

The comparison is invariant under orthogonal frame changes and natural under contiguous and ordered-subset restriction. Under uniform completion hypotheses, the same equality holds on finite compressions and descends to the bounded completed operator.

## Incidence consequence

Within the framed Markov domain, the composite

\[
\texttt{gauge_presentation}
\longrightarrow
\texttt{carrier}
\longrightarrow
\texttt{finite_green}
\]

is now typed and realized. This upgrades hypergraph connectivity to an actual composable analytic route for the gauge/carrier/Green portion of the pyramid.

## Remaining boundary

The result does not make every `over_quotient` output a Markov Carrier. Admission requires the invariant metric-transition coordinates, contraction inequality, ordered incidence, and source provenance. Physical interpretation remains absent.

## Disposition

The gauge-to-Green composite interface is verified on the framed metric-transition Markov subcategory, with an invertible identity comparison between framed construction and quotient-then-realization.

## Verification

- `research/voevodsky/checkers/check_gauge_quotient_green_composite.py`
- `research/voevodsky/results/gauge_quotient_green_composite.json`
