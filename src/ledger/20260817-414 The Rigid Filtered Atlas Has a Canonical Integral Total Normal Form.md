---
id: 414
date: 2026-08-17
title: The Rigid Filtered Atlas Has a Canonical Integral Total Normal Form
---

# The Rigid Filtered Atlas Has a Canonical Integral Total Normal Form

Entry 413 proves that the filtered Jordan atlas exists and has no residual
order-three or endpoint-parity choice. The first explicit realization step
is therefore forced: totalize the geometric Tate carrier of Entry 115 with
the normalized three-normal Cartier packet.

Write
\[
C_{\rm Tate}=
[\mathbb Z_{\rm or}\xrightarrow{N}\mathbb Z^3
\xrightarrow{1-r}\mathbb Z^3\xrightarrow{\epsilon}\mathbb Z]
\]
and let \(K_{\rm Cart}\) be the exterior Koszul packet on the three positively
oriented Cartier units. In bidegree \((p,q)\), set
\[
\mathcal T_{p,q}=C_{{\rm Tate},p}\otimes K_{{\rm Cart},q},
\qquad
d_{\rm Tot}=d_{\rm Tate}+(-1)^p d_{\rm Cart}.
\]

The total chain ranks are the convolution
\[
(1,3,3,1)*(1,3,3,1)
=\boxed{(1,6,15,20,15,6,1)}.
\]
Writing every basis and every block explicitly gives
\[
\operatorname{rank}(d_1,\ldots,d_6)
=\boxed{(1,5,10,10,5,1)}.
\]
All matrix entries lie in \(\{0,\pm1\}\), and the Koszul sign makes every
mixed square anticommute, so \(d_{\rm Tot}^2=0\).

## Integral contraction

Choose the first positively oriented Cartier basis vector \(e_1\). Exterior
multiplication by \(e_1\) contracts the Cartier complex because
\[
\iota_{(1,1,1)}(e_1\wedge-)
+e_1\wedge\iota_{(1,1,1)}=\operatorname{id}.
\]
On a Tate-degree-\(p\) tensor, the total contraction is
\[
H=(-1)^p(1\otimes e_1\wedge-).
\]
The checker verifies basiswise over \(\mathbb Z\) that
\[
d_{\rm Tot}H+Hd_{\rm Tot}=\operatorname{id}.
\]
Thus the 64-generator normal form is split exact with an explicit integral
contraction. No division by two or three and no rational projector occurs.

This contraction does not erase the local order-three road extension.
It applies after the positively oriented Cartier unit has been evaluated in
the normalized finite packet. The filtered road recollement still records
the nonsplit \(A_2\)-to-primitive extension described in Entries 409--413.

## Boundary of the result

The result supplies the unique integral block-and-sign normal form that the
full loaded PC realization must carry. It is not yet the desired occurrence-
resolved map into Entry 143's extended Čech target. The remaining construction
is now concrete: totalize the already proved normalized-blowdown connector
of Entries 396--398 with the endpoint/Tor suspension of Entries 399--400 and
the Cartier comparison, then compare its 64 normalized generators with the
corresponding occurrence/Čech summands.

The executable audit is
\`research/voevodsky/check_filtered_atlas_total_normal_form.py\`.
