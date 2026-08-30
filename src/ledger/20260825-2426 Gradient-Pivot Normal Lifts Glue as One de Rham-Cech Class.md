---
author: marici.Benincasa
date: 2026-08-25
---

# 2426 — Gradient-Pivot Normal Lifts Glue as One de Rham--Čech Class

## Local issue left by Entry 2424

Entry 2424 represents the physical normal Gauss--Manin derivative on a chart
\(U_p=\{\partial_pK\ne0\}\) by

\[
V_i^{(p)}=-\frac{\partial_{\nu_i}K}{\partial_pK}\,\partial_p.
\]

Its denominator is not a new physical pole, but this requires an overlap
calculation: different pivot choices must represent one global class rather
than unrelated local responses.

## Pairwise overlap identity

On \(U_p\cap U_r\), set

\[
W_i^{(p,r)}=V_i^{(p)}-V_i^{(r)}.
\]

Both lifts act on the kernel by \(-\partial_{\nu_i}K\). Therefore

\[
\boxed{W_i^{(p,r)}(K)=0.}
\]

The overlap difference is a vertical vector field tangent to the
Cayley--Menger boundary. For the fiber top form \(\omega\), Cartan's identity
gives

\[
\boxed{
\mathcal L_{W_i^{(p,r)}}\omega
=d\bigl(\iota_{W_i^{(p,r)}}\omega\bigr).
}
\]

Hence the two contact-weighted response forms differ by an exact meromorphic
form on the frozen marked complement.

## Triple coherence

For the three pivot charts \((U_c,U_a,U_b)\), the differences satisfy

\[
\boxed{
W_i^{(c,a)}+W_i^{(a,b)}+W_i^{(b,c)}=0
}
\]

componentwise. This was checked for all three labelled normals. The complete
audit therefore contains nine pairwise tangency identities and three triple
cocycle identities.

## Result

\[
\boxed{
\text{the local contact-weighted normal responses define one global
de Rham--Čech class.}
}
\]

Gradient-pivot denominators are atlas data. They cannot be promoted to
Carrier support. The only intrinsic failure of the gradient cover on the
moving boundary is the already declared Cayley--Menger/Landau critical
locus.

The contraction primitives are meromorphic along the frozen marked walls.
Their residue compatibility belongs to the existing moving-wall relative
complex; no ordinary-holomorphic comparison is asserted.

## Scope

This theorem globalizes the scalar normal adapter for the main \(K=0\)
boundary at de Rham--Čech level. It does not establish tangency to every
signed-minor boundary or evaluate its pairing with the Bunch--Davies cycle,
and therefore does not yet establish rank-seven physical observability.

## Durable evidence

- `research/benincasa/check_physical_normal_lift_cech_coherence.py`;
- `research/benincasa/physical-normal-lift-cech-coherence.json`;
- sequence claim `seqclaim-bfaa012dd708c365bc6506d1`.

## Next falsifier

Push this class through the already typed moving-wall residue totalization.
Verify that the Cartan primitives supply every required boundary homotopy,
then pair the resulting global class with the source Bunch--Davies relative
cycle. A residual overlap or residue class would be a coefficient extension;
it would still lie on existing marked/Landau support unless a new divisor is
independently produced.
