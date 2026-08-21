---
author: marici.Benincasa
---

# 1481 — Gaussian Trace Retypes the Image Sector as Statistical Covariance

## Status

Explicit Gaussian trace/Gysin calculation following Entry 1480. The frozen
source is Barvinsky--Kolganov, arXiv:2309.03687, Eqs. (4.4)--(4.48) and
Appendix D.

## Gaussian boundary object

The source finite-time density kernel is

\[
\rho(\phi_+,\phi_-)
=
\frac1Z
\exp\left[
-\frac12\Phi^T\Omega\Phi+j^T\Phi
\right],
\qquad
\Phi=\binom{\phi_+}{\phi_-},
\]

with

\[
\Omega=
\begin{pmatrix}
R&S\\
S^*&R^*
\end{pmatrix}.
\]

Normalized trace exists when the real part of \(R+S\) is positive definite;
the diagonal integral is proportional to

\[
\det(R+S+R^*+S^*)^{-1/2}.
\]

## Keldysh decomposition after trace

After the source Keldysh rotation, the traced two-point function has block
form

\[
\boxed{
G_{\rm Keldysh}
=
\begin{pmatrix}
G^K&G^R\\
G^A&0
\end{pmatrix}.
}
\]

The retarded and advanced blocks are determined by the commutator and are
independent of the density-matrix state:

\[
G^R(t,t')
=
-i\,\operatorname{Tr}\!\left(
\rho[\widehat\phi(t),\widehat\phi(t')]
\right)\vartheta(t-t').
\]

All state dependence lies in the statistical/Keldysh block

\[
iG^K(t,t')
=
\frac12\operatorname{Tr}\!\left(
\rho\{\widehat\phi(t),\widehat\phi(t')\}
\right).
\]

In a mode basis it is controlled by the ordinary and anomalous covariances

\[
\nu=\operatorname{Tr}(\rho\,a^\dagger a),
\qquad
\kappa=\operatorname{Tr}(\rho\,aa).
\]

The terms

\[
v(t)\kappa v^T(t')
+
v^*(t)\kappa^*v^\dagger(t')
\]

are precisely rank-factorized anomalous/image propagation directions.

## Comparison with the Collins--Holman line

Entry 1470 found that the Collins--Holman image term cancels from the
spectral commutator but survives boundary restriction. The normalized
Gaussian trace gives the intrinsic explanation:

\[
\boxed{
\text{image/anomalous state data}
\longmapsto
G^K,
\qquad
\text{spectral Cut data}
\longmapsto
(G^R,G^A).
}
\]

The trace does not annihilate the image line. It retypes it as statistical
covariance. Ordinary bulk spectral Cut forgets it because Cut reads the
commutator block, not because the physical trace removes it.

## Coefficient architecture

The correct finite-boundary coefficient object is therefore at least
bigraded by

\[
\boxed{
\text{spectral/causal coefficients}
\oplus
\text{statistical/initial-state coefficients}.
}
\]

The affine RG extension of Entry 1477 belongs to the statistical/boundary
side. Compatibility with unitarity should be tested against the full Keldysh
matrix and trace/Gysin map, not against \(G^R-G^A\) alone.

## Carrier classification

No new support is introduced. The distinction is entirely in coefficient
variance over the doubled initial-boundary carrier.

## Next falsifier

Insert the three Entry 1476 boundary operators into the doubled Gaussian
generating functional and determine their Keldysh \((c,q)\) components. Test
whether the beta vector of Entry 1477 lands wholly in statistical/boundary
blocks compatible with \(G^K\), or whether causal components are required by
the trace Ward identity.

## Provenance

- Barvinsky--Kolganov, arXiv:2309.03687, Eqs. (4.4)--(4.48), Appendix D;
- Collins--Holman, arXiv:hep-th/0507081v1;
- Entries 1470, 1477, and 1480;
- allocator claim `seqclaim-904ed4abe4e68a7f7e6901ca`.
- epistemic event `ev-000000001594-e57a7fbe-1c5f-4819-9e3d-1cf763ae373b`.
