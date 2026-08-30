# 1621 — Exact Density Positivity Does Not Type Positivity of an Isolated Loop Grade

## Source theorem

The primary closed-time-path source defines

\[
i\partial_t\rho=[H,\rho]
\]

and its exact solution

\[
\rho(t)=U(t,t_0)\rho(t_0)U^\dagger(t,t_0)
\]

in equations (2)--(4) of arXiv:1212.1172v2.

If \(\rho(t_0)\succeq0\), then for every vector \(|\psi\rangle\),

\[
\langle\psi|\rho(t)|\psi\rangle
=
\langle U^\dagger\psi|\rho(t_0)|U^\dagger\psi\rangle
\geq0.
\]

Trace and Hermiticity are preserved as well.

## Covariance consequence

For any canonical pair \((Q,P)\), positivity of the density matrix implies the Robertson--Schrödinger inequality

\[
\det V
\geq
\frac14|\langle[Q,P]\rangle|^2.
\]

In the one-mode convention of Entries 1607 and 1619,

\[
\det V-\frac14
=
n+n^2-x^2-y^2
\geq0.
\]

This statement applies to the complete interacting state and does not require that state to remain Gaussian; \(V\) is simply its two-point covariance.

## Perturbative type distinction

Write formally

\[
V(g)=V_0+gV_1+g^2V_2+\cdots.
\]

Positivity of \(V(g)\) or of the full uncertainty function for physical \(g\) does not imply

\[
V_r\succeq0
\]

for each coefficient separately.  Local counterterm and scheme changes can redistribute perturbative coefficients while leaving the exact observable unchanged.

Therefore:

\[
\boxed{
\text{exact source evolution preserves physical positivity, but it does not type positivity of an isolated renormalized loop grade.}
}
\]

## Relation to Entries 1617--1620

- Entries 1617--1618 prove the stronger coefficient-level fact that the **unsubtracted finite-EFT Cut contribution** is itself positive semidefinite.
- Entry 1619 proves conditional stability under a frozen Hamiltonian counterterm class.
- Entry 1620 proves that the primary source does not specify the renormalization comparison needed to isolate a renormalized loop coefficient.
- The present entry shows that physical positivity is nevertheless exact for the complete source evolution.

These are compatible statements of different types.

## Architectural consequence

The physical positivity theorem belongs to the coefficient/state realization over the existing CTP/Cut carrier.  It supplies no new incidence stratum.  The unresolved renormalization map is a comparison between coefficient presentations, not an incompleteness of the carrier.

## Next falsifier

Return to the second-Rees mechanism rather than inventing a subtraction: compute whether the labelled Cut completion of a generic mixed Gaussian initial state reproduces the full second-order tangent cone

\[
n_2\geq x_1^2+y_1^2
\]

with equality precisely for pure Gaussian deformations and strict excess for environment-crossing Cut channels.
