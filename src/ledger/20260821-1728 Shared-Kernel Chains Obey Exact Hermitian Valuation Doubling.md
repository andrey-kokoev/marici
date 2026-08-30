# 1728 — Shared-Kernel Chains Obey Exact Hermitian Valuation Doubling

## Finite-chain claim

Let

\[
f_i=\operatorname{diag}(1,\lambda_i),
\qquad i=1,\ldots,n,
\]

be a labelled finite chain with one common kernel.  Set

\[
L=\prod_{i=1}^n\lambda_i.
\]

The composite amplitude map is \(\operatorname{diag}(1,L)\), so for
\(|u\rangle=(a,b)^T\),

\[
\boxed{
\rho_L=
\begin{pmatrix}
a^2&Lab\\Lab&L^2b^2
\end{pmatrix}.
}
\]

## Valuation law

The common-kernel amplitude and image–kernel density term have multivaluation

\[
(1,\ldots,1),
\]

while the pure kernel density has

\[
\boxed{(2,\ldots,2).}
\]

This is forced by multiplicativity followed by the Hermitian-square functor;
induction on the chain length introduces no additional term.

On the diagonal \(\lambda_i=t\), the kernel amplitude begins at order \(n\)
and its pure density costalk at order \(2n\).  Thus every fixed ordinary-jet
cutoff eventually misses a sufficiently long shared-kernel chain, whereas the
labelled multi-Rees valuation retains it uniformly.

## Narrow result

All finite shared-kernel chains are controlled by the existing multi-Rees
Hermitian-square calculus.  No extension class or new Cut carrier stratum is
generated in this family.

## Durable artifacts

- `research/benincasa/checkers/shared_kernel_chain_valuation.rs`
- `research/benincasa/results/shared-kernel-chain-valuation.json`
- `research/benincasa/shared-kernel-chain-valuation.md`

## Next falsifier

Replace a fixed common kernel by a rotating kernel subbundle.  Test whether its
connection produces Berry/holonomy data inside the coefficient object or a
failure of global multi-Rees descent.
