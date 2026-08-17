---
id: 412
date: 2026-08-17
title: The Jordan Cap Matches the Geometric Tate Extension and Has Zero Associator
---

# The Jordan Cap Matches the Geometric Tate Extension and Has Zero Associator

Entry 411 isolated a one-dimensional relative group
\[
H^2(X;\mathbb F_{3,\rm or})\cong\mathbb F_3.
\]
The class to evaluate is not the order-three extension itself. Both the
geometric filtration and the Jordan/Tate model carry a nonzero extension.
The obstruction is their **difference**.

Entry 102 fixes the based orientation-twisted Tate generator
\[
\beta_\triangle=+1
\in
\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\rm or})\cong\mathbb Z/3.
\]
Entry 115 constructs the actual boundary-triad support filtration and proves
\[
\rho_{\rm PL}^{\rm car}(e_F)=\beta_\triangle.
\]
Therefore the local comparison class is
\[
\omega_{\rm car}
=\rho_{\rm PL}^{\rm car}(e_F)-\beta_\triangle
=0.
\]

No global correction revives it:

- Entry 398 proves that the three geometric connectors assemble through the
  full Čech \(1\to3\to3\to1\) complex with unit Smith factors and zero
  residual cyclic holonomy.
- Entries 403--404 give zero square curvature and a strict unimodular
  PC-to-Jordan square comparison.
- Entry 408 gives integral \(D_8\)-covariant cap witnesses, so transport
  contributes no further sign or denominator class.

Consequently the remaining cap coordinate of Entry 411 is
\[
\boxed{a_{\rm Jordan}=0\in\mathbb Z/3.}
\]
The filtered atlas therefore extends across the Jordan cap at the carrier
and primitive associated-grade level.

## Interpretation and scope

The order-three Tate class has not disappeared. It is the nontrivial gluing
between the primitive and \(A_2\) contact grades. What vanishes is the
**mismatch** between its geometric realization and the canonical Jordan
realization. Thus the full structure is filtered and integrally nonsplit,
but it has no additional order-three associator.

This does not yet construct the full loaded PC chain map. Entry 115's spatial
extraordinary-costalk comparison remains a separate coefficient-level gate.
The conclusion here is confined to the carrier and the already normalized
primitive associated grade.

The executable audit is
\`research/voevodsky/check_jordan_cap_order_three_associator.py\`.
