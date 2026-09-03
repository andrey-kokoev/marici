# Uniform Markov Green completion pseudofunctor

## Question

Does the scalar Markov Green fragment admit a genuine finite-to-closed completion compatible with its contiguous inclusions and coherence cells?

## Claim boundary

This packet treats one-sided infinite scalar Markov chains with a uniform edge bound \(|a_i|\le\rho<1\). It does not cover arbitrary edge sequences approaching unit modulus, two-sided chains, or operator-valued kernels.

## Infinite certificate

For vertices \(i,j\in\mathbb N\), define

\[
G_{ij}=\prod_{k=\min(i,j)}^{\max(i,j)-1}a_k.
\]

Every finite principal block is the positive Markov Gram matrix. Moreover,

\[
|G_{ij}|\le\rho^{|i-j|}.
\]

The row and column sums are bounded by

\[
1+2\sum_{m\ge1}\rho^m
=\frac{1+\rho}{1-\rho}.
\]

The Schur test therefore defines a bounded self-adjoint positive operator \(G_\infty\) on \(\ell^2(\mathbb N)\). Positivity follows from positivity on finitely supported vectors, and the bounded form is already closed.

## Completion functor

Let \(G_n\) be the certificate on the first \(n+1\) vertices. Contiguous inclusion maps are coordinate isometries, and

\[
G_n=P_nG_\infty P_n.
\]

For each vector in \(\ell^2\), \(P_nG_\infty P_n\) converges strongly to \(G_\infty\). Thus the finite nested system has a canonical closed-form completion.

## Pseudofunctoriality

Composition of contiguous inclusions is literal coordinate inclusion. Completing after either parenthesization gives the same operator and the same inclusion isometry. The completion comparison, associator, and unitor cells are identities. Their pentagon and triangle equations hold strictly.

Contiguous restriction of the completed kernel agrees with completion of the restricted tail sequence, so the previously constructed Beck–Chevalley identity cells survive completion.

## Hostile boundary

Without a uniform \(\rho<1\), the geometric Schur majorant is absent. Constant edges \(a_i=1\) produce the all-ones kernel, which is not bounded on \(\ell^2(\mathbb N)\). Finite positivity alone therefore does not authorize completion.

## Disposition

The uniformly contractive scalar Markov sector instantiates a finite-to-closed completion pseudofunctor with strict coherence. This is a nontrivial completed subfragment of the candidate equipment; general completion remains open.

## Verification

- `research/voevodsky/checkers/check_uniform_markov_green_completion.py`
- `research/voevodsky/results/uniform_markov_green_completion.json`
