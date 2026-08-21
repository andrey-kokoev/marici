---
author: marici.Benincasa
---

# 1489 — Self-Adjoint Bilocal Boundary Kernels Occupy Only First Contour-Conormal Grade

## Status

Exact extension of Entry 1487 from local potentials to quadratic derivative
and bilocal boundary kernels.

## Frozen quadratic kernel

Let \(K\) be a source-defined self-adjoint kernel on the initial boundary,
possibly containing tangential or normal derivatives, and write

\[
S_K[\phi]=\frac12\langle\phi,K\phi\rangle_\Sigma.
\]

The doubled unitary contribution is

\[
S_K[\phi_+]-S_K[\phi_-].
\]

With

\[
\phi_\pm=\phi_c\pm\frac12\phi_q,
\]

self-adjointness gives the exact polarization

\[
\boxed{
S_K[\phi_+]-S_K[\phi_-]
=\langle\phi_q,K\phi_c\rangle_\Sigma.
}
\]

No expansion or derivative truncation is used.

## Conormal grade

The polarized kernel has exactly one quantum leg. Therefore

\[
\boxed{
S_K[\phi_+]-S_K[\phi_-]
\in
\operatorname{gr}_\Delta^1,
}
\]

and

\[
\operatorname{gr}_\Delta^m(S_K[\phi_+]-S_K[\phi_-])=0
\qquad(m\neq1).
\]

Derivative order in \(K\) does not create higher contour-conormal grade.
This separates two filtrations that could otherwise be confused:

\[
\text{spacetime jet order of }K
\quad\neq\quad
\text{quantum-leg/conormal order}.
\]

## Statistical contrast

A general Gaussian density-matrix kernel is not required to be an undoubled
action difference. Its Keldysh decomposition can contain deck-even covariance
data and therefore contributes to \(G^K\). The exact grade-one theorem applies
to the causal/unitary quadratic block, not to the statistical block.

## Integration-by-parts qualification

If proving self-adjointness requires integration by parts on a boundary with
corners or further marked strata, the discarded endpoint terms must be
retained as support morphisms. Such terms could enlarge the supported
coefficient complex, but they do not alter the deck parity of the bulk
quadratic kernel.

## Consequence

All three source-fixed generators in Entry 1476 remain entirely in first
contour-conormal grade: each is linear in \(\psi_\pm\). No higher contour
grade is fixed by the computed leading \(c_1\) tadpole block. A
cubic-quantum component would require an independently derived nonlinear
completion of \(\phi^3\psi_\pm\).

No new causal generator or coherence cell is required at this algebraic
stage.

## Next falsifier

Audit the actual covariantly completed second-normal operator on the finite
initial hypersurface without discarding integration-by-parts endpoint terms.
Classify every surviving term as:

- existing initial-boundary carrier;
- a pre-existing soft/corner support;
- causal coefficient data in first contour grade;
- genuinely new supported incidence.

Only the last outcome would force a carrier extension.

## Provenance

- Entries 1476 and 1485--1487;
- allocator claim `seqclaim-a494c8f2f883b79dbd738877`.
- epistemic event `ev-000000001607-733a6e68-085a-44b9-8170-6be54ad559ec`.
