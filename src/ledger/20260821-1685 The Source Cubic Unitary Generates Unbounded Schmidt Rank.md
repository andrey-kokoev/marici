# 1685 — The Source Cubic Unitary Generates Unbounded Schmidt Rank

## Entanglement-rank falsifier

Entry 1684 shows that finite global density rank does not control reduced rank.
Test whether the actual scalar-cubic interaction preserves a finite
Schmidt-rank sector before partial trace.

Across the observed/internal bipartition

\[
q_1\mid(q_2,q_3),
\]

the interaction unitary is

\[
U(t)=e^{-igtq_1q_2q_3}.
\]

Its exact expansion is

\[
\boxed{
U(t)
=
\sum_{n=0}^{\infty}
\frac{(-igt)^n}{n!}
q_1^n\otimes(q_2q_3)^n.
}
\]

Acting on a generic product vector

\[
f(q_1)g(q_2,q_3),
\]

the two families

\[
q_1^nf(q_1)
\quad\text{and}\quad
(q_2q_3)^ng(q_2,q_3)
\]

are linearly independent. Hence the order-(K) Dyson truncation has coefficient
matrix with (K+1) nonzero diagonal entries and Schmidt rank

\[
\boxed{K+1.}
\]

The exact checker verifies 257 truncations through (K=256), 33,153 labelled
Schmidt terms, and 97 explicit matrix-rank calculations.

## Narrow result

\[
\boxed{
\text{the source cubic unitary has no uniform finite Schmidt-rank closure.}
}

At generic nonzero coupling and time, the complete analytic expansion has
infinite Schmidt rank. Therefore neither finite Schmidt rank nor finite reduced
density rank can serve as the closed quantum process coefficient family.

Exceptional wavefunctions annihilated by polynomial relations may have lower
rank; the claim is generic, not universal at every state.

## Durable artifacts

- `research/benincasa/checkers/cubic_unitary_schmidt_rank.rs`
- `research/benincasa/results/cubic-unitary-schmidt-rank.json`
- `research/benincasa/cubic-unitary-schmidt-rank.md`

## Next falsifier

Determine whether the resulting infinite Schmidt spectrum has a finite
differential or tensor-network presentation compatible with the moment-module
presentation of Entry 1649. Test whether Dyson order supplies a canonical bond
filtration whose Cut contraction is associative and positive.
