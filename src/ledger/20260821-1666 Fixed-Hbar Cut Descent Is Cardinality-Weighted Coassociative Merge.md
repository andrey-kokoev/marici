# 1666 — Fixed-Hbar Cut Descent Is Cardinality-Weighted Coassociative Merge

## Falsifier

Entry 1657 shows that the specialization ideal

\[
(\hbar-\hbar_0)
\]

is not a coideal for the primitive additive coproduct. This prevents naive
addition of two fixed-(\hbar) systems. Determine whether physical descent is
nevertheless coherent when the carrier retains the number of labelled
occurrences in each block.

## Cardinality-weighted merge

For (N) occurrences set

\[
Q_N=\frac1{\sqrt N}\sum_{i=1}^Nq_i,
\qquad
P_N=\frac1{\sqrt N}\sum_{i=1}^Np_i.
\]

The fixed central character is preserved:

\[
[Q_N,P_N]
=
\frac1N\sum_{i=1}^N[q_i,p_i]
=i\hbar.
\]

Two blocks of sizes (m,n) merge by

\[
(Q_m,P_m),(Q_n,P_n)
\longmapsto
\sqrt{\frac m{m+n}}(Q_m,P_m)
+
\sqrt{\frac n{m+n}}(Q_n,P_n).
\]

For a leaf inside the first block, squared weights compose as

\[
\frac m{m+n}\frac1m=\frac1{m+n},
\]

and similarly in the second block. Induction therefore makes every leaf
weight (1/N), independently of binary bracketing.

The exact rational checker enumerates every ordered binary bracketing through
twelve occurrences:

\[
82{,}500\text{ bracketings},
\qquad
78\text{ leaf-weight audits}.
\]

Every occurrence count produces one squared-coefficient vector, and every
vector sums to one.

## Narrow result

\[
\boxed{
\text{fixed-}\hbar\text{ physical Cut descent is coassociative when block cardinality is retained.}
}
\]

The failure of an unweighted binary normalization is information loss: it
forgets occurrence cardinality. Since labelled occurrences and their finite
sets are already native to the resolved carrier, no new carrier primitive is
required. The square-root weights are sector-specific coefficient data.

This does not construct interacting dynamical pushforward, prove complete
positivity, or identify a continuum renormalization prescription.

## Durable artifacts

- `research/benincasa/checkers/fixed_hbar_cardinality_merge.rs`
- `research/benincasa/results/fixed-hbar-cardinality-merge.json`
- `research/benincasa/fixed-hbar-cardinality-merge.md`

## Next falsifier

Test compatibility of the cardinality-weighted fixed-(\hbar) merge with the
scalar-cubic co-Leibniz coherence. Transport Entry 1655's binary defect through
two unequal block mergers and compare the two three-block parenthesizations.
Any residual depending on the merge tree is a genuine coefficient-level
associator; exact equality closes fixed-(\hbar) descent through the first
nonlinear interaction grade.
