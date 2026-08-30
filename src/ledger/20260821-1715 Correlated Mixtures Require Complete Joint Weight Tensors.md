# 1715 — Correlated Mixtures Require Complete Joint Weight Tensors

## Correlated-label falsifier

Entry 1714 proves closure for independent product mixtures.  Admit arbitrary
correlations among the finite mixture labels.

## Two blocks

For two label sets, the complete coefficient is a joint nonnegative table

\[
\pi_{jk}.
\]

The generator is the corresponding weighted sum over the existing labelled
pairs.  One-site marginals do not determine it: diagonal and anti-diagonal
binary tables can have identical marginals but different collective
displacement moments.

Hidden common-cause labels add no observable datum after pushforward; summing
over the hidden label produces the same `pi_jk` and the same generator.

## Three blocks

Pair tables are not sufficient.  The even- and odd-parity distributions on
three binary labels have identical pair marginals but distinct joint support.
Therefore the required coefficient is the complete tensor

\[
\boxed{
\pi_{jkl}.
}
\]

This is the finite-mixture analogue of Entry 1677's complete joint cumulant
tensor.

## Zero marginal

If a row vanishes as

\[
\pi_{jk}=\varepsilon r_k,
\]

then conditioning retains

\[
\boxed{
\frac{r_k}{\sum_lr_l}.
}
\]

The exceptional datum is the projective row direction `[r]`.  It is
path-dependent after forgetting the approach direction, but canonical on the
simplex-face Rees chart.

## Narrow result

\[
\boxed{
\text{correlated finite mixtures close under Cut only after retaining the complete joint weight tensor and its simplex-face Rees data.}
}
\]

No new Cut carrier stratum is needed.  The enlargement is entirely in the
sector-specific coefficient object.

## Durable artifacts

- `research/benincasa/checkers/correlated_mixture_joint_weights.rs`
- `research/benincasa/results/correlated-mixture-joint-weights.json`
- `research/benincasa/correlated-mixture-joint-weights.md`

## Next falsifier

Test nested conditioning on two simultaneously vanishing marginals.  Determine
whether projective row directions glue by ordinary iterated simplex blowups or
whether their overlap carries a nontrivial extension class.  Preserve all
joint label occurrences.
