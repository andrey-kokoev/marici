# 1714 — Finite Mixture Generators Close under Labelled Cartesian Cut Product

## Mixture-Cut falsifier

Entry 1713 identifies a finite log-sum-exp coefficient completion for one
physical non-Gaussian input.  Test closure under independent Cut assembly.

## Product mixture

For independent mixture labels

\[
j\in J_X,
\qquad
k\in J_Y,
\]

the product density state has components

\[
\boxed{
J_{XY}=J_X\times J_Y.
}
\]

Their weights and collective displacements are

\[
p_{jk}=p_jq_k,
\qquad
\mu_{jk}=w_X\mu_j+w_Y\nu_k.
\]

Substituting these data into Entry 1713's finite exponential sum gives the
complete merged cubic generator.  If two numerical displacements coincide,
their source occurrence labels remain distinct; no post hoc quotient is taken.

For three blocks, either nested Cartesian product yields the same labelled
triples and the same final cardinality-weighted displacement.  The checker
verifies the exact rational weight composition on a nontrivial three-block
family.

## Narrow result

\[
\boxed{
\text{finite Gaussian-mixture coefficient objects are closed under independent Cut by labelled Cartesian product.}
}
\]

The number of coefficient components multiplies, but this is ordinary tensor
product growth inside the sector-specific coefficient object.  No new carrier
cell or associator is required.

## Durable artifacts

- `research/benincasa/checkers/finite_mixture_cut_descent.rs`
- `research/benincasa/results/finite-mixture-cut-descent.json`
- `research/benincasa/finite-mixture-cut-descent.md`

## Next falsifier

Admit correlated mixture labels.  Determine whether a joint weight table on
`J_X times J_Y` is sufficient, including zero-probability support and
conditioning, or whether hidden common-cause labels require a refinement of
the coefficient object.  Do not infer independence from product indexing.
