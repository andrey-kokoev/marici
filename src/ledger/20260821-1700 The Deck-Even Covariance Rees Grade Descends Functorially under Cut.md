# 1700 — The Deck-Even Covariance Rees Grade Descends Functorially under Cut

## Frontier

Entry 1699 keeps the conditioning and cosmological time-root covers distinct.
Without identifying them, test whether the deck-even covariance Rees grade is
compatible with the shared labelled Cut calculus.

## Congruence transport

Let

\[
\Xi=u\otimes u
\]

be Entry 1698's exceptional tensor.  For any labelled linear Cut map `T`, the
resolved normal transports as

\[
u\longmapsto Tu.
\]

Hence

\[
\boxed{
\Xi\longmapsto T\Xi T^T
=\operatorname{Sym}^2(Tu).
}
\]

For composable Cut maps `T,S`,

\[
S(T\Xi T^T)S^T
=(ST)\Xi(ST)^T.
\]

Thus nested Cut transport is strictly functorial.  Rank one, positive
semidefiniteness, and deck invariance are preserved.

## Narrow result

\[
\boxed{
\text{the even covariance Rees grade is a functorial coefficient object for the existing labelled Cut carrier.}
}
\]

No new carrier operation or higher coherence cell is required.  This is an
internal covariance-sector theorem; Entry 1675's prohibition remains in force,
so it does not construct a mixed energy--covariance comparison.

## Durable artifacts

- `research/benincasa/checkers/symmetric_square_cut_functoriality.rs`
- `research/benincasa/results/symmetric-square-cut-functoriality.json`
- `research/benincasa/symmetric-square-cut-functoriality.md`

## Next falsifier

Test the odd resolved-normal line itself under Cut transport.  Determine
whether occurrence-compatible sign choices propagate one global deck sign on
connected trees, as in the cosmological time-root test, while keeping the two
local systems formally distinct.
