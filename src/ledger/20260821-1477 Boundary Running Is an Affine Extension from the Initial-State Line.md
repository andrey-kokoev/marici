---
author: marici.Benincasa
---

# 1477 — Boundary Running Is an Affine Extension from the Initial-State Line

## Status

Leading-order renormalization-group typing of Entry 1476's dimension-four
boundary coefficient block. The frozen source is Collins--Holman,
arXiv:hep-th/0507081v1, Eqs. (6.39)--(6.43).

## Source running

Let

\[
Z_\Sigma^{(4)}
=
\mathbb C\langle z_2,z_3,z_4\rangle
\]

denote the three labelled counterterm coefficients associated respectively
with the covariantly completed second normal jet, curvature coupling, and
cubic boundary interaction. The source derives

\[
\widehat\beta_2
=
\frac{\lambda_Rc_1}{32i\pi^2}+\cdots,
\]

\[
\widehat\beta_3
=
\frac{\lambda_Rc_1}{16i\pi^2}+\cdots,
\]

\[
\widehat\beta_4
=
\frac{\lambda_R^2c_1}{16i\pi^2}+\cdots.
\]

At this order, the displayed running is not an autonomous matrix acting on
\((z_2,z_3,z_4)\). It is a source map from the leading initial-state
coefficient line:

\[
\boxed{
\beta_\Sigma^{(4)}:
\mathbb C\langle c_1\rangle
\longrightarrow
Z_\Sigma^{(4)},
\qquad
c_1\longmapsto
\begin{pmatrix}
\lambda_R/(32i\pi^2)\\
\lambda_R/(16i\pi^2)\\
\lambda_R^2/(16i\pi^2)
\end{pmatrix}c_1.
}
\]

## Triangular coefficient object

The renormalized boundary sector is therefore an affine/triangular extension

\[
0
\longrightarrow
Z_\Sigma^{(4)}
\longrightarrow
\mathcal E_{c_1}
\longrightarrow
\mathbb C\langle c_1\rangle
\longrightarrow0,
\]

with the beta vector supplying the extension data at the calculated order.
It should not be replaced by three unrelated running constants, nor by one
scalar second-normal coefficient.

The ratios of the first two components are fixed:

\[
\widehat\beta_3=2\widehat\beta_2+\cdots,
\]

while the cubic component carries one additional bulk coupling. This records
the distinct field-degree variance of \(\mathcal O_4\).

## Support and filtration

The map preserves the initial hypersurface support and the boundary operator
dimension. It mixes normal order with curvature and field degree inside the
same dimension-four coefficient grade, but it does not mix into a bulk or
new incidence support.

Thus the source yields

\[
\boxed{
\text{boundary filtration preserved}
+
\text{nontrivial affine coefficient extension}.
}
\]

This is stronger than mere locality: it exhibits the explicit mechanism by
which ultraviolet initial-state data is converted into a local boundary
coefficient module.

## Scope

The source gives the displayed leading terms only. It does not establish that
higher-loop running remains triangular or that no \(z_i\)-to-\(z_j\) mixing
appears later.

## Next falsifier

Compare this affine RG extension with Cut sewing. For a labelled internal
edge ending on \(\Sigma\), test whether applying the beta map before Cut and
after resolved endpoint restriction gives the same three-component vector.
Failure by a local boundary homotopy would be coefficient extension data;
failure requiring new support would threaten the shared carrier calculus.

## Provenance

- Collins--Holman, arXiv:hep-th/0507081v1, Eqs. (6.39)--(6.43);
- Entries 1475--1476;
- allocator claim `seqclaim-4e4b0768027cefabb4d3c5d3`.
- epistemic event `ev-000000001589-a6a8bf92-026c-4c34-b046-70d5066314c9`.
