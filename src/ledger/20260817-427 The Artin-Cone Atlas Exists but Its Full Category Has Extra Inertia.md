---
id: 427
date: 2026-08-17
title: The Artin-Cone Atlas Exists but Its Full Category Has Extra Inertia
---

# The Artin-Cone Atlas Exists but Its Full Category Has Extra Inertia

Entry 426 supplies an fs monoid \(P_{S,H}\) at every loaded cell and a face
localization at every incidence. Associate the Artin cone
\[
\mathcal A_{S,H}=
[\operatorname{Spec}R[P_{S,H}]/T_{P_{S,H}}].
\]
The 522 monoid face maps induce representable open face maps between the 215
cones. Every composable pair was checked: whenever two routes have the same
loaded endpoint, both composites groupify exactly the endpoint's normal
coordinates. Thus all atlas cocycles commute strictly. The resulting diagram,
and hence its open-glued 2-colimit, is a canonical logarithmic Artin-cone
realization of the fs PC envelope.

There is, however, no equivalence between the *full* constructible category of
this Artin stack and modules on the finite Alexandrov poset. At \((S,H)\),
\[
\overline P_{S,H}=P_{S,H}/P_{S,H}^{\times}
\cong\mathbb N^{18-|S\setminus H|}.
\]
Since \(|S|\leq3\), its rank lies between 15 and 18. The closed stratum of the
Artin cone therefore has positive-dimensional torus inertia at every chart.
Two rank-one equivariant sheaves carrying respectively the trivial character
and a nonzero character have the same underlying stalk module but are not
isomorphic on the quotient stack. A finite-poset module has no datum capable
of distinguishing them.

Therefore the categorical statement required by the connector must be
narrowed. The finite PC/Čech model can correspond only to the sector pulled
back from the underlying Kato fan—equivalently, the constructible sector with
trivial inertia action—not to all constructible sheaves on the Artin fan.

This distinction matters for six operations. It is not enough to construct
the atlas: one must verify that restriction, extension, the normalized
blowdown pushforward, the relative dualizing object, and the Thom trace all
preserve the trivial-inertia sector. If they do, Entry 424 algebraizes inside
that sector. If a pushforward generates a nontrivial torus character, the
finite model omits essential logarithmic monodromy.

The executable audit is
`research/voevodsky/check_artin_cone_atlas_inertia_gate.py`.
