---
author: marici.Benincasa
---

# 1476 — The Leading Nonrenormalizable Initial State Requires a Three-Generator Boundary Jet Block

## Status

Primary-source classification of the leading \(c_1\) initial-state loop
divergence. The frozen source is Collins--Holman,
arXiv:hep-th/0507081v1, Eqs. (6.30)--(6.41).

## Frozen nonrenormalizable coefficient

The leading ultraviolet initial-state deformation is

\[
e^{\alpha_k^*}
=
c_1\frac{\Omega_k(\eta_0)}{a(\eta_0)M}
\left(
1+\frac{a^2(\eta_0)m^2}{2\Omega_k^2(\eta_0)}
\right).
\]

Its one-loop kernel is represented by a third derivative of
\(K^{(-1)}\). After integrations by parts, the divergent contribution is
supported entirely at \(\eta=\eta_0\) and contains

\[
\frac1{a(\eta_0)}
\partial_\eta^2
\left(a^2G\phi\right)_{\eta_0},
\qquad
G(\eta_f,\eta_0)R(\eta_0)\phi(\eta_0),
\qquad
G(\eta_f,\eta_0)\phi^3(\eta_0).
\]

## Source counterterm block

The source cancels these terms with three labelled coefficients
\(z_2,z_3,z_4\). In boundary-action form their generators are

\[
\begin{aligned}
\mathcal O_2={}&
\nabla_n^2(\phi\psi_\pm)
+\frac53K\nabla_n(\phi\psi_\pm)
+\frac23(\nabla_nK)\phi\psi_\pm
+\frac23K^2\phi\psi_\pm,
\\
\mathcal O_3={}&
\left(\xi-\frac16\right)R\phi\psi_\pm,
\\
\mathcal O_4={}&
\frac12\phi^3\psi_\pm.
\end{aligned}
\]

Thus the leading nonrenormalizable coefficient does not land in a single
unlabelled second-normal line. It lands in the source-defined block

\[
\boxed{
\mathcal J^{(2)}_\Sigma
=
\mathbb C\langle
\mathcal O_2,\mathcal O_3,\mathcal O_4
\rangle.
}
\]

The coefficients are independently renormalized by \(z_2,z_3,z_4\), with
their divergent parts fixed by Eq. (6.40).

## Rees interpretation

The first generator contains the second ordinary normal jet. The other two
are required at the same boundary operator dimension by covariance and
interaction closure. Therefore

\[
\boxed{
\text{second normal/Rees grade}
\subsetneq
\text{complete dimension-four boundary coefficient block}.
}
\]

This is the boundary analogue of the Marici warning that one associated
normal grade need not determine the complete physical coefficient object.
The three labels must not be collapsed merely because they share dimension
and support.

## Carrier classification

Every generator remains supported on the already declared initial
hypersurface \(\Sigma\). The result requires richer labelled coefficients and
normal-jet operations, but no new incidence divisor:

\[
\boxed{
\text{existing boundary carrier}
+
\text{three-generator dimension-four coefficient jet}.
}
\]

This supports H2 while falsifying the stronger one-dimensional
higher-normal-coefficient hypothesis.

## Distinction from the elliptic second normal grade

The normal variable here is displacement from the background boundary
\(\eta=\eta_0\). It is not the total-energy normal \(E_T\) whose second grade
detects the three-site elliptic quartic. The shared feature is only the need
for higher normal information; the coefficient objects and normal bundles
are different.

## Next falsifier

Compute the source mixing/running matrix of
\(\langle\mathcal O_2,\mathcal O_3,\mathcal O_4\rangle\) and test whether it
is triangular with respect to normal order and boundary field degree. If
renormalization mixes this block with support away from \(\Sigma\), the
background-boundary carrier is insufficient. If all mixing remains local on
\(\Sigma\), the correct object is a filtered boundary coefficient module.

## Provenance

- Collins--Holman, arXiv:hep-th/0507081v1, Eqs. (6.30)--(6.41);
- Entry 1475;
- allocator claim `seqclaim-1ba66b7cf0e4076f994d6b92`.
- epistemic event `ev-000000001587-08dc38db-7cfa-4206-820c-88e82eece658`.
