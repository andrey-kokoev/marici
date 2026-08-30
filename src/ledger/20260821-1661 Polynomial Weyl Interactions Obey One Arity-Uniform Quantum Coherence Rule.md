# 1661 — Polynomial Weyl Interactions Obey One Arity-Uniform Quantum Coherence Rule

## Generalization test

Entry 1660 proves complete quantum co-Hochschild closure for the cubic potential. Determine whether this is accidental or follows one rule for every polynomial interaction degree.

## Uniform normal-order formula

For

\[
H_{\rm int}=\frac{q^d}{d},
\]

the primitive force is

\[
Dp=-q^{d-1}.
\]

Exact normal ordering gives

\[
\boxed{
D(p^m)
=
\sum_{k=1}^{\min(m,d)}
(-i)^{k+1}\hbar^{k-1}
\frac{k!}{d}
\binom mk\binom dk
q^{d-k}p^{m-k}.
}
\]

The \(k=1\) term is the classical force contribution. The first fully central term occurs at \(m=d\), with magnitude

\[
\boxed{(d-1)!\,\hbar^{d-1}.}
\]

The checker verifies 2,850 normal-order coefficients and nineteen central terms for interaction degrees two through twenty.

## Coherence theorem

In the homogenized occurrence-resolved Weyl coalgebra,

\[
\Theta_D
=
\Delta D-(D\otimes1+1\otimes D)\Delta
\]

is the co-Hochschild coboundary of \(D\). Coassociativity gives

\[
\delta\Theta_D=\delta^2D=0.
\]

Therefore normal ordering can enrich the binary coefficients of \(\Theta_D\), but cannot generate an independent ternary obstruction while the coproduct remains correctly typed.

## Narrow result

\[
\boxed{
\text{Entry 1660 is the cubic instance of an arity-uniform polynomial quantum coherence rule.}
}
\]

Different interaction degrees change the finite normal-order coefficients and the first central filtration grade. They do not require new higher sewing laws.

This result is algebraic. It does not include renormalized products, derivative interactions, gauge constraints, or integrated loop coefficients.

## Durable artifacts

- research/benincasa/checkers/weyl_polynomial_interaction_rule.rs
- research/benincasa/results/weyl-polynomial-interaction-rule.json
- research/benincasa/weyl-polynomial-interaction-rule.md

## Next falsifier

Test derivative interactions containing both \(q\) and \(p\), where ordering affects the primitive force itself. Determine whether a symmetric/Weyl-ordered Hamiltonian still yields a well-defined derivation and co-Hochschild coboundary in the homogenized CCR coalgebra, or introduces a source-ordering ambiguity before Cut sewing.
