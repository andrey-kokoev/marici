# Vector-KK gain-chain uniqueness audit: WP1140

## Question

Does carrying the vector-KK row through the gain chain uniquely fix its
event-cell parameters?

## DPC resolution

- **Problem:** determine whether the source-derived vector row supplies a
  common gain-chain authority.
- **Conjecture:** the vector-KK row can be carried through the common
  event-cell gain chain.
- **Rivals:** unique vector event cell; WP1075 target gain; pure-rate
  laundering; no common gain chain.
- **Risky consequences:** \(\eta=c=1/2\) from monitor rows,
  \(g=1,\mathcal L=1/5\) from coherent rows, rejection of \(g=3/2\) on the
  same cell, and rejection of same-\(S\) laundering.
- **Falsification attempt:** reconstruction is unique with \(g=1\), while the
  WP1075 target gain \(3/2\) changes the retained rows to
  \(S=9/20,D=3/5\).
- **Residual:** a physical16 production packet may source a different event
  cell or derive the target gain.
- **Disposition:** accept a unique conditional vector carrier, but reject it
  as source-derived gain authority.

## Exact reconstruction

WP1064 retains \(S=1/5,D=2/5,M=1/4,N=1/2\). The typed reconstruction forces

\[
\eta=c=\frac12,
\qquad
g=1,
\qquad
\mathcal L=\frac15.
\]

A pure-rate pair \((g,\mathcal L)=(1/2,4/5)\) reproduces \(S-B\) but gives
\(D=4/5\), not \(2/5\).

Checker: `research/flavor/checkers/wp1140_vector_kk_gain_chain_uniqueness.py`

Result: `results/wp1140_vector_kk_gain_chain_uniqueness.json`
