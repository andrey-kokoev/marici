# 1668 — The Independent Gaussian Wick Cut Defect Descends with Cardinality Weighting

## Pushed-forward falsifier

Entry 1667 closes the abstract three-block associator before internal
pushforward. Test whether Entry 1650's concrete scalar-cubic Wick defect remains
natural after the fixed-\(\hbar\), cardinality-weighted normalization of Entry
1666.

For an internal occurrence of variance \(\nu\),

\[
[C,D](p_1q_3)=-\nu q_2.
\]

For \(N\) independent internal occurrences, set

\[
Q_N=\frac1{\sqrt N}\sum_iq_i.
\]

Its variance is

\[
\nu_N=\operatorname{Var}(Q_N)
=\frac1N\sum_i\nu_i.
\]

If blocks of sizes \(m,n\) have collective variances \(\nu_m,\nu_n\), the
cardinality-weighted merger gives

\[
\nu_{m+n}
=\frac{m\nu_m+n\nu_n}{m+n}.
\]

Every binary merger tree therefore yields the same leaf average. The exact
rational checker verifies:

\[
36\text{ variance patterns},
\qquad
247{,}500\text{ ordered binary bracketings},
\]

through twelve internal occurrences.

## Narrow result

\[
\boxed{
\text{the independent Gaussian Wick Cut defect is natural under cardinality-weighted fixed-}\hbar\text{ merge.}
}
\]

No new support-sensitive correction or ternary carrier cell appears at this
grade. The variance is sector-specific coefficient data transported by the
existing occurrence cardinality.

This statement assumes independence between the merged internal blocks. It
does not erase Entry 1652's correlated conditional-pushforward correction.

## Durable artifacts

- `research/benincasa/checkers/cardinality_weighted_wick_cut.rs`
- `research/benincasa/results/cardinality-weighted-wick-cut.json`
- `research/benincasa/cardinality-weighted-wick-cut.md`

## Next falsifier

Admit a nonzero cross-covariance between two internal blocks. Derive its exact
transport under cardinality-weighted merge and compare nested conditioning in
both merger orders. Determine whether the full covariance matrix suffices for
strict descent or whether the first conditional coherence carries additional
support data.
