# 1707 — The First Third Cumulant Is Trivial under the Covariance Deck Action

## Odd-coefficient falsifier

Entry 1706 closes the even cubic pair coefficient on nested covariance
costalks.  Test the first connected third cumulant from Entry 1692.

## Two independent characters

The source cubic orbit satisfies

\[
\kappa_3(-t)=-\kappa_3(t).
\]

The covariance Rees cover independently acts by

\[
u\longmapsto-u.
\]

With `t` fixed, this action does not change the source third cumulant.  Hence

\[
\boxed{
(\chi_t(\kappa_3),\chi_u(\kappa_3))=(-1,+1).
}
\]

Its labelled Cut restriction is simply the restriction of all three occurrence
slots of the cumulant tensor.  No component-sign choice enters.

## Narrow result

\[
\boxed{
\text{the first non-Gaussian third cumulant is odd under cubic reversal but trivial under the covariance deck and its soft costalk.}
}
\]

Therefore no mixed coefficient extension appears in the frozen product family.
A nontrivial coupling would require a source-derived map between cubic-flow and
covariance normals; Entries 1675 and 1699 show that no such comparison is
currently typed.

This is not a global splitting theorem for arbitrary non-Gaussian states.

## Durable artifacts

- `research/benincasa/checkers/third_cumulant_covariance_sign.rs`
- `research/benincasa/results/third-cumulant-covariance-sign.json`
- `research/benincasa/third-cumulant-covariance-sign.md`

## Next falsifier

Leave the product family by allowing the covariance degeneration and cubic
coupling to share one source parameter.  Freeze an explicit one-parameter
Hamiltonian/density family first, then test whether its mixed second normal
grade produces a canonical coupling.  Do not identify the parameters by hand.
