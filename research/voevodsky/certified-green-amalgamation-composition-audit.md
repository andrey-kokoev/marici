# Composition audit for certified Green amalgamations

## Question

Do pairwise cross-pairing certificates compose automatically into the partial double category required by the Green attachment architecture?

## Claim boundary

This packet tests scalar positive Green forms. It does not exclude composition rules carrying a full joint Gram witness or a source-derived conditional-independence law.

## Proposed certificate

For two normalized complements, a scalar cross pairing \(r\) is positive-admissible when

\[
\begin{pmatrix}1&r\\r&1\end{pmatrix}\ge0,
\]

or equivalently \(|r|\le1\). One might conjecture that composable certified pairs can be glued using only their pairwise certificates.

## Strongest falsification attempt

Take three normalized one-dimensional complements with

\[
r_{12}=r_{23}=0.9,
\qquad r_{13}=0.
\]

Both adjacent certificates pass because their \(2\times2\) determinants equal \(0.19\). But the joint Gram matrix

\[
G=
\begin{pmatrix}
1&0.9&0\\
0.9&1&0.9\\
0&0.9&1
\end{pmatrix}
\]

has determinant \(-0.62\), so it is not positive semidefinite. Pairwise admissibility therefore does not compose.

The failure is repaired in this scalar chain by the additional choice

\[
r_{13}=r_{12}r_{23}=0.81,
\]

for which the determinant becomes \(0.0361>0\). This product rule is extra coherence data; it is not implied by the two adjacent certificates.

## Exact residual

Composition requires the missing nonadjacent cross pairing and a proof that the full block Gram matrix has the required positivity and radical behavior. Pairwise certificates do not determine either.

In operator form, a composite certificate must include a full positive block completion or an equivalent Schur-complement witness. If a source supplies a conditional-independence factorization, the induced cross block may be canonical; otherwise multiple completions or no completion may exist.

## Beck–Chevalley consequence

A Beck–Chevalley cell cannot be declared from the boundary square alone. It must compare two certified composite completions and include the higher cross-pairing witness. Equality of pairwise restrictions is insufficient.

## Disposition

Automatic composition of certified Green amalgamations is rejected. The surviving architecture is an equipment whose horizontal composites are defined only with a full joint Gram/completion witness. Associativity is then a theorem about compatible block completions, not a formal property of pairwise data.

## Verification

- `research/voevodsky/checkers/check_certified_green_amalgamation_composition.py`
- `research/voevodsky/results/certified_green_amalgamation_composition.json`
- `research/voevodsky/green-isometry-pushout-falsification.md`
