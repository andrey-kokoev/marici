# 1684 — Finite-Rank Density Operators Are Not Closed Under Cut Reduction

## Quantum finite-family falsifier

Entry 1683 closes finite atomic states under the classical process operations.
Test the source-typed quantum candidate of finite-rank density operators.

The source Cut and intervention constructions of Entries 1632 and 1641 include
physical partial trace. Exact unitary evolution preserves density-operator
rank, but partial trace need not.

For

\[
|\psi_N\rangle
=
\sum_{i=1}^N|i\rangle_P\otimes|i\rangle_E,
\]

the global positive operator

\[
|\psi_N\rangle\langle\psi_N|
\]

has rank one. Its environmental partial trace is

\[
\operatorname{Tr}_E
|\psi_N\rangle\langle\psi_N|
=I_N,
\]

which has rank (N).

The exact checker verifies all cutoffs

\[
1\le N\le128,
\]

with reduced ranks (1,ldots,128).

Moreover, the normalized infinite-Schmidt vector

\[
|\psi\rangle
=
\sum_{n=1}^{\infty}2^{-n/2}|n,n\rangle
\]

has reduced density matrix

\[
\rho_P
=
\sum_{n=1}^{\infty}2^{-n}|n\rangle\langle n|,
\]

which is trace class, positive, and infinite rank. The checker verifies sixty
strictly positive finite prefixes and tails.

## Narrow result

\[
\boxed{
\text{finite-rank density operators are not closed under source Cut reduction.}
}
\]

Global rank-one purity does not bound reduced rank; the missing coefficient is
Schmidt-spectrum data. Consequently finite rank cannot replace the filtered
quantum moment/state object as the closed cosmological process coefficient.

This does not say every cubic Cut produces infinite Schmidt rank. It excludes
finite global rank as a uniform closure principle.

## Durable artifacts

- `research/benincasa/checkers/finite_rank_density_cut_failure.rs`
- `research/benincasa/results/finite-rank-density-cut-failure.json`
- `research/benincasa/finite-rank-density-cut-failure.md`

## Next falsifier

Test finite Schmidt-rank or finite coherent-mixture families under the actual
cubic unitary before partial trace. Determine whether the source interaction
generically generates unbounded Schmidt rank at arbitrarily small nonzero time,
or whether a source symmetry protects a finite entanglement sector.