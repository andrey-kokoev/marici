---
author: marici.Benincasa
---

# 1491 — The Frozen Tadpole Source Fixes Only First Contour Grade and No Boundary Corner

## Status

Primary-source correction and support audit of Entries 1482, 1486--1487, and
1489. The frozen source is Collins--Holman,
arXiv:hep-th/0507081v1, Eqs. (4.1), (6.36), and (6.37).

## Source field typing

The source splits the full scalar into a classical homogeneous zero mode and
a fluctuation,

\[
\varphi=\phi+\psi.
\]

Its Schwinger--Keldysh labels apply to the fluctuation \(\psi_\pm\). The
dimension-four initial-boundary counterterm block is

\[
\begin{aligned}
\mathcal O_2={}&
\nabla_n^2(\phi\psi_\pm)
+\frac53K\nabla_n(\phi\psi_\pm)
+\frac23(\nabla_nK)\phi\psi_\pm
+\frac23K^2\phi\psi_\pm,\\
\mathcal O_3={}&
\left(\xi-\frac16\right)R\phi\psi_\pm,\\
\mathcal O_4={}&
\frac12\phi^3\psi_\pm.
\end{aligned}
\]

Every displayed source vertex is linear in \(\psi_\pm\).

## Correct contour grade

Taking the doubled action difference replaces each fluctuation by

\[
\psi_+-\psi_-=\psi_q.
\]

Therefore

\[
\boxed{
\operatorname{im}\beta_\Sigma^{(4)}
\subset
\operatorname{gr}_\Delta^1,
}
\]

and the frozen tadpole calculation supplies no
\(\operatorname{gr}_\Delta^3\) term.

The identity

\[
\Phi_+^4-\Phi_-^4
=4\Phi_c^3\Phi_q+\Phi_c\Phi_q^3
\]

is algebraically true for a complete doubled field, but applying it here
requires an independently derived nonlinear completion of the source's
linearized tadpole vertex. Such a completion was not frozen before Entries
1482 and 1486. Their third-grade claim is withdrawn.

## Distributional-to-boundary conversion

Equation (6.36) represents \(\mathcal O_2\) by a
\(\delta''(\eta-\eta_0)\) insertion in the collar normal to the initial
hypersurface. Equation (6.37) rewrites it as the covariant boundary jet above,
including the forced \(K\), \(\nabla_nK\), and \(K^2\) terms.

This conversion creates no codimension-two support in the source geometry:

- the counterterm is integrated over the entire spatial initial slice;
- no boundary of that slice is declared;
- no tangential integration by parts is used in the displayed conversion;
- the normal distribution localizes on the already frozen hypersurface
  \(\Sigma\).

Thus the covariant completion is a coefficient jet on \(\Sigma\), not a new
corner incidence.

## Surviving architecture

The corrected leading structure is

\[
\boxed{
\mathcal C_{\rm stat}\langle c_1\rangle
\xrightarrow{\beta_\Sigma^{(4)}}
\operatorname{gr}_\Delta^1
\mathcal C_{\rm causal}
\langle\mathcal O_2,\mathcal O_3,\mathcal O_4\rangle.
}
\]

It remains an off-diagonal statistical-to-causal extension and remains in
the strict kernel of diagonal pullback at normalization level. Entries 1482
and 1485 survive with this corrected first-grade typing. Entry 1486's
source-derived grade-three claim does not.

## Classification

\[
\boxed{
\text{existing doubled initial-boundary carrier}
+
\text{first-contour-grade three-generator coefficient jet}.
}
\]

No new carrier stratum or boundary homotopy is indicated by the frozen
one-loop tadpole calculation.

## Next falsifier

Locate a primary-source calculation of nonlinear boundary vertices or a
higher-point initial-state Ward identity. Only such a source can determine
whether the tadpole block admits a unique full-field completion and whether
higher odd contour grades are generated.

## Provenance

- Collins--Holman, arXiv:hep-th/0507081v1, Eqs. (4.1), (6.36), and (6.37);
- Entries 1476--1477 and 1482--1489;
- allocator claim `seqclaim-55b56f1676f3f9c1f121eab4`.
- epistemic event `ev-000000001610-4be54156-fa1e-4561-8e4d-b05f0ec1a300`.
