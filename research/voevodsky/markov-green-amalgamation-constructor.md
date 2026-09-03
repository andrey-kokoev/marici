# Markov-certified Green amalgamation constructor

## Question

Is there a nontrivial restricted class of Green amalgamations whose joint Gram witnesses compose associatively?

## Claim boundary

This packet constructs a scalar chain model with source-declared conditional independence. It does not establish that Marici Green sectors satisfy that condition, nor does it handle operator-valued kernels without additional commutation and range hypotheses.

## Constructor

Let normalized one-dimensional Green sectors be connected by edge correlations

\[
a_1,\ldots,a_{n-1},
\qquad |a_i|<1.
\]

Declare the nonadjacent pairing by the path-product rule

\[
r_{ij}=\prod_{k=i}^{j-1}a_k
\qquad(i<j).
\]

This is the covariance matrix of a scalar Markov chain. It has an explicit triangular realization: start with a unit vector \(v_1\), and recursively set

\[
v_{i+1}=a_iv_i+\sqrt{1-a_i^2}\,e_{i+1},
\]

where each \(e_{i+1}\) is a new orthogonal unit vector. Hence the joint Gram matrix is positive definite.

Its determinant is

\[
\det G_n=\prod_{i=1}^{n-1}(1-a_i^2).
\]

## Composition

Concatenating certified chains composes cross pairings by multiplication. For three successive edges,

\[
(a_1a_2)a_3=a_1(a_2a_3),
\]

so the scalar completion is independent of parenthesization. The associator is strict at the level of the completed Gram matrix.

This is not automatic Green composition. The path-product rule is the missing joint-completion witness identified by the previous falsifier.

## Exact test

For

\[
(a_1,a_2,a_3)=\left(\frac12,\frac23,\frac34\right),
\]

all nonadjacent correlations are fixed by products, the endpoint correlation is \(1/4\), and

\[
\det G_4
=
\frac34\cdot\frac59\cdot\frac7{16}
=
\frac{35}{192}>0.
\]

Both parenthesizations give the same endpoint pairing.

## Beck–Chevalley cell

Within this restricted scalar sector, a comparison square satisfies Beck–Chevalley only when both routes preserve the same ordered edge list or carry a proved equality of their path products. Equality of endpoint dimensions or adjacent minors is insufficient.

Thus the cell contains a path-product equality certificate. In a source theory this certificate must derive from a conditional-independence, transfer, or factorization law.

## Strongest falsification attempt

Changing the endpoint pairing while retaining all adjacent correlations destroys the declared constructor. The previous example with adjacent correlations \(9/10\) and endpoint correlation zero produces a negative determinant. Therefore the rule is restrictive and falsifiable.

## Disposition

A composable sector exists: scalar Markov-certified Green amalgamations. It forms a strict chain-composition model because path products are associative. Promotion to Marici requires a source theorem that its cross Green returns factor through the intervening sector. Without that theorem this is an admissible model, not the operating Green architecture.

## Verification

- `research/voevodsky/checkers/check_markov_green_amalgamation.py`
- `research/voevodsky/results/markov_green_amalgamation.json`
- `research/voevodsky/certified-green-amalgamation-composition-audit.md`
