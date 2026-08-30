# 1676 — Cardinality-Weighted Merge Preserves Every Cumulant Species

## Non-Gaussian normalization test

Entry 1654 gives a finite species presentation for cumulant Cut sewing. Entry
1666 introduces cardinality-dependent normalization needed for fixed-(\hbar\)
descent. Test whether this normalization mixes cumulant orders.

For independent blocks of sizes (m,n), let

\[
Q_{m+n}
=\alpha Q_m+\beta Q_n,
\qquad
\alpha=\sqrt{\frac m{m+n}},
\qquad
\beta=\sqrt{\frac n{m+n}}.
\]

Homogeneity and independence give

\[
\kappa_r(Q_{m+n})
=\alpha^r\kappa_r(Q_m)
+\beta^r\kappa_r(Q_n).
\]

For a leaf inside the first block, squared coefficients compose as

\[
\left(\frac m{m+n}\right)^r\frac1{m^r}
=\frac1{(m+n)^r}.
\]

Thus every merger tree assigns each leaf coefficient (N^{-r/2}) at cumulant
order (r).

The exact rational checker verifies cumulant orders one through twelve and
occurrence counts one through twelve:

\[
144\text{ species/count pairs},
\qquad
936\text{ leaf coefficients},
\qquad
990{,}000\text{ ordered binary bracketings}.
\]

## Narrow result

\[
\boxed{
\text{cardinality-weighted fixed-}\hbar\text{ merge preserves every cumulant species.}
}
\]

Normalization does not mix cumulant orders. It equips the order-(r) species
with the coefficient character

\[
\left(\frac{\text{block size}}{\text{total size}}\right)^{r/2}.
\]

Therefore Entry 1654's species presentation survives normalized Cut descent;
no new carrier generator is required.

This statement assumes independent blocks. Correlated non-Gaussian blocks
require mixed cumulants across occurrence labels.

## Durable artifacts

- `research/benincasa/checkers/cardinality_weighted_cumulant_species.rs`
- `research/benincasa/results/cardinality-weighted-cumulant-species.json`
- `research/benincasa/cardinality-weighted-cumulant-species.md`

## Next falsifier

Admit mixed cumulants between two non-Gaussian blocks. Test whether retaining
the complete labelled joint cumulant tensor makes cardinality-weighted nested
mergers associative, as full covariance did in Entry 1669, or whether partition
incidence creates a new coherence class.
