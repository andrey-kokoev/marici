# Gaussian-translate density arrow

## Question

If all Gaussian translate Gram matrices are positive, what additional density statement is needed to reach the full Weil test space?

## Claim boundary

This proves abstract density in Schwartz space and positivity extension by continuity. It does not identify the arithmetic kernel with the required Gram matrices or prove them positive.

## Translate density

Let

\[
g(x)=e^{-x^2/2}.
\]

Every derivative \(g^{(k)}\) is a Schwartz-topology limit of finite forward-difference combinations of translates \(g(x-jh)\). Moreover,

\[
g^{(k)}(x)=(-1)^k\operatorname{He}_k(x)g(x).
\]

The Hermite–Gaussian functions span a dense subspace of \(\mathcal S(\mathbb R)\). Therefore the finite linear span of translates of a single Gaussian is already dense in Schwartz space. Varying widths is unnecessary for abstract density, although widths may remain part of the materialized arithmetic parameterization.

## Positivity transfer

Suppose \(q\) is a continuous Hermitian form on Schwartz space and every finite matrix

\[
G_{ij}=q(T_{a_i}g,T_{a_j}g)
\]

is positive semidefinite. Then every finite translate combination has nonnegative quadratic form. Density and continuity extend this inequality to every Schwartz test function.

The checker verifies seven Hermite derivative identities, 28 exact finite-difference moment cancellations, and finite Gram-to-quadratic positivity.

## Disposition

The abstract density arrow is closed. The remaining arithmetic gate has two coupled parts:

- identify the materialized two-variable explicit-formula kernel with these translate Gram matrices for a continuous completed Weil form;
- prove every such matrix positive semidefinite.

No additional family-density conjecture is needed once that identification is made in Schwartz topology.

## Verification

- `research/voevodsky/gaussian-translate-density-arrow-v1.json`
- `research/voevodsky/checkers/check_gaussian_translate_density_arrow.py`
- `research/voevodsky/results/gaussian_translate_density_arrow.json`
