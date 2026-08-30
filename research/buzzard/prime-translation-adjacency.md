# Prime translation adjacency: Lean packet

Source: `research/grothendieck/prime-power-translation-adjacency-theorem.md`.

`finiteTranslationAdjacency` takes a finite real-weighted family of complex
matrices `S_i` and forms

\[
\sum_i w_i(S_i+S_i^*).
\]

`finiteTranslationAdjacency_isHermitian` proves this matrix is Hermitian. No
unitarity is needed for self-adjointness; bounded/unitary translation semantics
belong to the later representation interface.

On a finite squarefree Boolean sector, `primeAdjacencyWalshEigenvalue` is the
signed edge sum. The module proves:

- the coefficient-opposite polarity has eigenvalue `-∑ i, |w_i|`;
- every Walsh eigenvalue has absolute value at most `∑ i, |w_i|`;
- this is the least uniform bound;
- `D I + A` is nonnegative on every Walsh channel exactly when
  `∑ i, |w_i| ≤ D`.

Thus the shared edge budget is recovered as the exact spectral radius of the
source-typed finite adjacency, not as independent negative prime norms.

Typing boundary: weights are real; finite adjacency matrices are complex;
squarefree polarities are Boolean over an arbitrary finite label type. The
module does not construct translations on log-time function space, prove their
Fourier cosine symbols, encode the prime-power cutoff and von Mangoldt weights,
or pass to the completed unbounded limit. Prime-tower harmonics require a
convention-fixed translation-circle representation and are not treated as
independent coordinates.

Verification boundary: Nima's active no-build instruction remains in force.
Only bounded static scans were run; the module remains outside
`MariciFormal.lean`.
