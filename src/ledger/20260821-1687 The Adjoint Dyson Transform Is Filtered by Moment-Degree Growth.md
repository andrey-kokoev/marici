# 1687 — The Adjoint Dyson Transform Is Filtered by Moment-Degree Growth

## Presentation-comparison falsifier

Entries 1649 and 1686 give finite presentations of two infinite coefficient
objects:

- the free-plus-cubic moment module;
- the cubic Dyson--Schmidt bond tower.

Construct a source-derived comparison rather than inferring equivalence from
finite presentability.

For an observable (O), the Heisenberg/Dyson expansion is

\[
O(t)=e^{tD}O
=\sum_{n\ge0}t^nO_n,
\qquad
O_n=\frac1{n!}D^nO,
\]

where

\[
D=p\partial_q-q^2\partial_p
\]

is the free-plus-cubic Hamiltonian derivation. The coefficients satisfy

\[
\boxed{
(n+1)O_{n+1}=DO_n.
}
\]

The free term preserves polynomial degree, while the cubic force term raises it
by at most one. Therefore

\[
\boxed{
\deg O_n\le\deg O+n.
}
\]

This gives a filtered transform

\[
\text{Dyson bond order }n
\longrightarrow
\text{moment degree shift }\le n.
\]

The exact sparse-polynomial checker verifies 45 initial monomials through degree
eight, 765 normalized Dyson recurrences, 765 filtration bounds, and 2,816
visited sparse coefficients through bond order sixteen.

## Narrow result

\[
\boxed{
\text{the adjoint Dyson transform is a source-derived filtered map into the moment module.}
}
\]

This explains why the two infinite presentations track the same dynamics at
different variances: bond order records interaction history, while moment
degree records observable complexity.

It does not prove injectivity, surjectivity, quasi-isomorphism, or equality of
their completions. Distinct Dyson histories may act identically on a chosen
observable sector, and not every formal moment sequence need arise from a
physical Dyson state.

## Durable artifacts

- `research/benincasa/checkers/dyson_to_moment_filtered_transform.rs`
- `research/benincasa/results/dyson-to-moment-filtered-transform.json`
- `research/benincasa/dyson-to-moment-filtered-transform.md`

## Next falsifier

Compute the first kernel and cokernel of the filtered transform at finite bond
and moment grades. Preserve source monomial labels. Determine whether the
failure is only filtration mismatch or whether a stable relative coefficient
class survives completion.