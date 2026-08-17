---
id: 409
date: 2026-08-17
title: The Primitive Verdier Quotient Types the Crosscap Holonomy
---

# The Primitive Verdier Quotient Types the Crosscap Holonomy

The full occurrence-resolved road object at a cut \(D\) is
\[
P_D=\mathbb Z^3,\qquad
\epsilon_D=(1,1,1):P_D\to\mathbf1,
\]
with contact kernel \(A_2=\ker\epsilon_D\). Each chart restriction selects
one road section \(s_i:\mathbf1\to P_D\).

In the full category, no \(s_i\) is an inverse to \(\epsilon_D\):
\(s_i\epsilon_D\) has rank one, while \(P_D\) has rank three. Its defect
\[
\operatorname{id}_{P_D}-s_i\epsilon_D
\]
has image in \(A_2\). Thus the obstruction to inversion is exactly the
two-dimensional contact sector, not a denominator or a missing sign.

Let
\[
\mathcal D_{\rm prim}
=
\mathcal D_{\rm occ}/\langle A_2\rangle
\]
be the Verdier quotient by the thick contact subcategory. Then
\[
\epsilon_Ds_i=\operatorname{id}_{\mathbf1},\qquad
s_i\epsilon_D=\operatorname{id}_{P_D}
\quad\text{in }\mathcal D_{\rm prim}.
\]
Moreover \(s_i-s_j\) factors through \(A_2\), so all three roofs define the
same inverse. Cyclic road transport merely permutes these representatives.
This gives integral, choice-independent equivalences in the primitive
associated grade without constructing a forbidden \(C_3\)-equivariant
section in the full lattice category.

Entry 406 selected the orientation character on the primitive line.
Consequently the now-typed rank-one transition system has multiplicative
holonomy
\[
\boxed{\operatorname{Hol}(\gamma)=-1}
\]
on the Möbius core. Entry 408 gives \([\partial O]=2[\gamma]\), hence
\[
\boxed{\operatorname{Hol}(\partial O)
=\operatorname{Hol}(\gamma)^2=+1.}
\]
The additive and multiplicative descriptions therefore agree: the primitive
additive period is one on the core and two on the boundary, while its
orientation exponential is minus one and plus one respectively.

## Scope

This is the first typed multiplicative holonomy, but only in
\(\mathcal D_{\rm prim}\), the primitive associated-grade quotient. It does
not promote the road legs to equivalences in the full occurrence-resolved
PC category, where \(A_2\) is real QTDS contact data. A full multiplicative
atlas would require a recollement or filtered enhancement that retains
\(A_2\) while exposing the primitive quotient, rather than killing it.

The executable audit is
\`research/voevodsky/check_primitive_road_verdier_holonomy.py\`.
