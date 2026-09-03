# Uniform operator-valued Markov completion

## Question

Does the finite noncommutative Markov fragment admit a bounded one-sided completion compatible with its associator and orthogonal gauges?

## Claim boundary

The fiber dimension is fixed and finite, and edge transfers satisfy the uniform operator-norm bound \(\lVert A_i\rVert\le\rho<1\). The result does not cover varying fibers, merely pointwise strict contractions, or infinite-dimensional fibers.

## Bounded completion

On \(\ell^2(\mathbb N;\mathbb R^d)\), define block entries

\[
K_{ii}=I_d,
\qquad
K_{ij}=A_i\cdots A_{j-1}\quad(i<j),
\qquad
K_{ji}=K_{ij}^T.
\]

Submultiplicativity gives

\[
\lVert K_{ij}\rVert\le\rho^{|i-j|}.
\]

The block Schur test therefore yields

\[
\lVert K\rVert\le 1+2\sum_{m\ge1}\rho^m
=\frac{1+\rho}{1-\rho}.
\]

Every finite principal compression is the positive finite Markov covariance. Hence the bounded infinite operator is positive by density of finite-support vectors.

## Pseudofunctoriality

Contiguous principal compression recovers the corresponding finite chain exactly. Ordered transfer-list concatenation remains strictly associative, so finite associator and pentagon cells complete to identities. Completion comparisons for nested contiguous inclusions paste strictly.

## Orthogonal gauges

A vertexwise orthogonal sequence \(U_i\) defines the block-diagonal unitary \(U=\bigoplus_iU_i\). Transformed edges \(U_iA_iU_{i+1}^T\) retain the same uniform norm bound and complete to

\[
K'=UKU^T.
\]

Thus compatible gauge interchange and the freely adjoined gauge companions and conjoints survive completion.

## Failure boundary

Pointwise inequalities \(\lVert A_i\rVert<1\) do not imply a common geometric Schur majorant. The completion constructor therefore refuses such data unless another boundedness certificate is supplied.

## Disposition

The finite noncommutative Markov partial double-category fragment extends to a uniformly contractive closed fragment, including orthogonal gauge companions and conjoints. General operator-valued completion outside uniform contraction remains open.

## Verification

- `research/voevodsky/checkers/check_operator_valued_markov_completion.py`
- `research/voevodsky/results/operator_valued_markov_completion.json`
