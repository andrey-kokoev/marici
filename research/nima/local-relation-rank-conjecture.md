# Local-relation rank conjecture — resolved

## Question

Are additive functions on polygon triangulations that separate on every facet product exactly the triangle-additive functions?

## Claim boundary

The result is linear over characteristic zero. Multiplicative signs, complex phases, source coefficients, and embedding provenance remain separate.

## Former conjecture

The local-solution dimension was conjectured to be

\[
1+\binom{n-1}{3}.
\]

Finite ranks through `n=9` supported it but did not constitute a proof.

## Resolution

Two generic theorems now close the claim. First, the triangle-incidence rank theorem uses simplex cochain exactness and discrete Stokes to prove that triangle-additive functions have the displayed dimension. Second, the converse theorem shows that facet separability makes each flip increment independent of its surrounding triangulations; pentagon cycles make these increments a closed simplex three-cochain; exactness supplies triangle weights; and flip-graph connectivity leaves only a constant, itself triangle-additive.

Therefore the local-relation rank is

\[
C_{n-2}-1-\binom{n-1}{3},
\]

and the quotient of global channel relations by local facet relations has dimension

\[
1+\binom{n-1}{3}-\frac{n(n-3)}2.
\]

Exact `n=5..8` dimensions and the `n=9` modular test remain implementation checks, not the theorem's evidential basis.

## Disposition

Resolved in characteristic zero by `triangle-incidence-rank-theorem.md` and `local-factorization-triangle-theorem.md`. The earlier stopping condition—an explicit model, rank proof, and converse spanning proof—is satisfied. No canonical-form source identification follows.
