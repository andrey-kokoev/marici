# Finite-horizon attachment coherence has uniform graph-scale bounds

## Status relative to the new tower theorem

Voevodsky's `../voevodsky/fox-lifts-transfer-the-compatible-filtered-tower-to-presentation-scales.md` already establishes compatible attachment roofs at every finite filtration level, including strictness on the radius intersection. The present note supplies a quantitative finite-horizon bound, general interval-quotient diagrams, and independent exact regressions. It is not a second claim to discover that finite coherence.

The estimate is uniform in the chosen finite horizon when that horizon's norm is used. It is not a uniform operator estimate on one fixed low-order path norm as the horizon tends to infinity.

## 1. One norm throughout a finite horizon

Fix H>=2 and use a common path norm for every ideal and quotient appearing below:

`W_(H,s,b)(n)=b_s(H)(1+n)^H (b A)^n`,

`b_s(j)=(2 lambda s)^j j!`, with s,b>=1.

A bounds both the forcing and analytical letters, using the same positive memory/seam weights. For a desired additional feature-transfer constant, enlarge b as in the existing forcing bridge. The factor b_s(H) is constant on this fixed horizon; it is only norm bookkeeping, not a new Green metric.

Let J_i be the closure of I^i in this common path norm, and write F_(a,m)=J_a/J_m and G_b=J_b/J_(b+1). All indices below satisfy 1<=a<b<m<=H+1.

The closed-subspace quotient sequences are strictly exact. All inclusions and quotient maps in this section have norm at most one. This statement uses ONE horizon norm on both sides, not a comparison of independently weighted Banach stages.

On the common all-radius intersection, simultaneous finite-corner norm-minimizing lifts give surjectivity, and hence strictness, as proved in Voevodsky's new note. Fox comparison transfers the resulting diagrams to the corresponding presentation intersections. Neither step chooses an equivariant splitting.

## 2. General extension models and refinement kernels

Define

`K_(a,b)^m=[F_(b,m) -> F_(a,m)]`, in degrees -1,0.

Its augmentation to F_(a,b) is a strict quasi-isomorphism. At m=b+1 it is the extension model

`[G_b -> F_(a,b+1)]`

for 0->G_b->F_(a,b+1)->F_(a,b)->0.

For m>l>b the two quotient maps define

`q_(m,l):K_(a,b)^m -> K_(a,b)^l`.

Their kernel is exactly

`[F_(l,m) --identity--> F_(l,m)]`.

Its degree-zero-to-minus-one identity is a contraction of norm one, with the inherited common quotient norm on both terms. The quotient maps are strict, so the contractible kernel proves that q_(m,l) is a strict quasi-isomorphism. This does not require a chain-level section of q_(m,l).

The equalities

`q_(l,h) q_(m,l)=q_(m,h)`

hold literally. Kernel inclusions and quotient maps are the actual source maps. Thus no choice of contracting data or scalar coherence correction enters nested refinement.

There is also an adjacent restriction

`K_(b-1,b)^m -> K_(a,b)^m`, for a<=b-1,

identity in degree -1 and the actual inclusion in degree zero. It commutes with the joint attachment observation below.

## 3. Ordered derivatives and their legal domains

D_j sums over j ordered distinct event positions, retaining those actual seam edges and the j+1 intervening terminal buffers. For products of j relations,

`D_j(u_1 ... u_j)=D(u_1) tensor_balanced ... tensor_balanced D(u_j)`.

Terms allocating no seam to a relation factor vanish. The same argument gives D_j(I^(j+1))=0 and vanishing of lower ordered derivatives on I^j. On I^j the higher product rule therefore makes D_j source-equivariant, and its image consists of bottom cycles.

Thus D_b is defined on F_(b,m), factors through G_b, and is unchanged by every refinement q_(m,l). D_a is defined on F_(a,m), factors through G_a, and vanishes on the included F_(b,m).

The map from K_(a,b)^m to

`J_(R,a)[-a] direct_sum J_(R,b)[1-b]`

has D_a in degree zero and D_b in degree -1. It is a source-equivariant chain map. Its joint component is the connecting projection followed by the balanced b-seam observation. All refinement and adjacent-restriction squares commute before applying a pairing.

The shifts put the ordinary a-seam cycles in degree zero and the joint b-seam cycles in degree -1. If individually shifted tensor factors are used instead, transport by the existing phase (-1)^(j(j-1)/2); no new phase is selected.

Do not place D_j on an arbitrary larger quotient and claim it is an equivariant bottom-cycle map there. The legal domain in this argument is I^j modulo a deeper power. Estimates on paths do not remove that restriction.

## 4. Uniform quantitative control within the horizon

For a path of length n, each term of D_j has forcing-resolved norm at most (b A)^n, including its feature-radius weight. There are binomial(n,j) terms and j active seam edges. Therefore

`||D_j(w)||_(s,b) <= b_s(j) binomial(n,j) (b A)^n`.

For 1<=j<=H, b_s(j)<=b_s(H) and binomial(n,j)<=(1+n)^H. Each individual derivative is consequently bounded by W_(H,s,b)(n), with constant one independent of H. Taking quotient infima gives the same bound on each legal ideal quotient. With l1 norms on the two degrees, each attachment chain map in section 3 is a contraction at its common horizon scale.

There is also a bound for the whole finite derivative list on paths:

`sum_(j=1)^H b_s(j) binomial(n,j)
 <= H b_s(H)(1+n)^H
 <= b_(2s)(H)(1+n)^H`.

Thus the list costs only s->2s in this horizon-indexed norm. This estimate is on the pre-quotient path space; it does not assert simultaneous cycle/equivariance properties where those fail. Nor does it sum an unweighted collection of repeated extension diagrams.

Target differentials, balanced normalizations, and associators retain the earlier all-depth graph-scale bounds. The forcing-to-Clark transfer and separately labelled current observations are the existing maps; on a fixed compact spectral interior their fixed feature-radius losses can be taken simultaneously for all arrows in any finite diagram.

## 5. Nonzero attachments at arbitrary finite depth

For b>a take b consecutive forgotten diamond relations u_1,...,u_b in a 2b-event packet. Their product z is nonzero, I^(b+1)=0 in that packet, and D_b(z) is a nonzero balanced product cycle.

Put v=u_2...u_b. Its shorter endpoint interval has length 2b-2, so its I^b corner is zero. Since b-1>=a, v belongs to I^a. A source-equivariant section of F_(a,b+1)->F_(a,b) would have to preserve v on that shorter interval. Multiplication by u_1 would then send a zero class in F_(a,b) to the nonzero class z in F_(a,b+1), a contradiction.

For the analytical attachment, restrict to this finite packet. The model [I^b->I^a] is a projective model over the finite hereditary source on either appropriate one-sided module category. A nullhomotopy of its joint observation would require D_b(z)=u_1 H(v)=0, since the target's outer I-action is zero. There is no lower target term to supply another homotopy component.

As in the first two attachment theorems, finite restriction preserves strict exact cones and detects the nonzero morphism in the completed localization. This uses finite projectivity, not projectivity of the completed ideals or their enveloping algebra.

## 6. Boundary: finite-horizon uniformity is not a limit theorem

At each fixed H, the polynomial weight (1+n)^H is absorbed by enlarging a path radius on the compatible intersection. Fox lifting then compares with the presentation topology. Increasing H on a fixed Banach source is a different operation: the norm W_(H,s,b) itself grows with H.

Nothing above identifies an unrestricted compatible filtration family with a summable source vector, commutes an inverse limit with a quotient, or proves convergence of the infinite list of attachments. Such a claim needs a declared realization topology and a summability or boundedness condition. The finite-horizon bound states precisely what has been controlled without making that additional assertion.

## Verification

`uv run --with sympy python research/nima/checkers/check_uniform_finite_stage_attachments.py`

Artifact: `results/uniform-finite-stage-attachments.json`.

Passed 30 ordered-product identities (15 with nonminimal suffixes), 15 next-power vanishings, 126 refinement/kernel chain checks, 126 nested-refinement compositions, and 1040 horizon-weight inequalities. The product fixtures use actual source paths and terminal buffers, and check closure of the resulting balanced cycles.

The all-finite-horizon theorem is the argument above. These regressions are not a numerical inverse-limit or completed-projectivity test.
