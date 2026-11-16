# Ramsey R(3,7): exact Hall–exterior decomposition

## Standing hypothetical graph

Let G be 6-regular and triangle-free on 23 vertices and assume alpha(G)≤6. Fix v, write A=N(v) (six vertices), B=V(G)\(A∪{v}) (sixteen vertices), H=G[B]. For b∈B define T_b=N(b)∩A. Necessarily every a∈A belongs to exactly five T_b; |T_b|+d_H(b)=6; and T_b∩T_c=∅ whenever bc∈E(H).

## Exact independence formula

Since A is independent, an independent set of G containing v has at most 1+alpha(H) vertices, and an independent set avoiding v with B-part Y∈I(H) may contain exactly 6−|∪_{b∈Y}T_b| vertices from A. Thus

alpha(G) = max(1+alpha(H), 6 + max_{Y∈I(H)} (|Y|−|∪_{b∈Y}T_b|)).

Consequently alpha(G)≤6 if and only if alpha(H)≤5 and every independent Y in H has |Y|≤|∪_{b∈Y}T_b|. Since all subsets of an independent Y are independent, Hall's theorem says equivalently that every such Y admits a system of distinct representatives from its T_b. If M(T) is the transversal matroid of the supports, this is I(H)⊆I(M(T)).

## Local perfect matching

For b∈B, N_H(b) is independent, has cardinality 6−|T_b|, and all its supports lie within A\T_b. By the preceding Hall property these supports admit a perfect matching onto A\T_b. This is stronger than mere coverage by their union.

For a∈A, N(a)∩B is an independent five-set. Its supports match injectively into A and in particular cover at least five distinct labels. Define C on A by ab∈E(C) if a,b appear together in some T_c. Then every vertex of C has degree≥4, so the complement of C is a matching.

## Two-walk version (general degree d)

More generally, if G is triangle-free, d-regular, and alpha(G)≤d, for any v∈V(G) the pairs {a,b}⊆N(v) with (M_G^2)_{ab}=1 form a matching. Indeed if a had two such partners b,c, then the d−1 neighbors of a other than v together with b,c would be an independent (d+1)-set. The co-occurrence graph result is equivalent to this codegree-one matching statement.

## Exterior-algebra encoding

Work over the field of rational functions in algebraically independent variables z_{b,a}, for each a∈T_b. Let V have basis e_a (a∈A), and let u_b=Σ_{a∈T_b} z_{b,a} e_a. For every Y⊆B,

(∧_{b∈Y} u_b)≠0  iff  Y admits distinct representatives from its supports.

This follows because each coefficient in the wedge basis is a generic incidence-matrix determinant, a polynomial whose distinct matching monomials cannot cancel identically.

In particular the local perfect matching condition becomes

(∧_{a∈T_b} e_a) ∧ (∧_{c∈N_H(b)} u_c) ≠ 0 in ∧^6 V.

And every a∈A imposes the fivefold condition ∧_{b:a∈T_b}u_b≠0. If its five supports cover only four A labels, their wedge is identically zero, giving a direct contradiction. Exterior multiplication, not the exterior derivative or Stokes' theorem, is the relevant operation here.

## Computational cross-check, not a classification-free proof

The accompanying script rebuilds 1,961 support patterns from the earlier verified enumerator and tests necessary conditions. The three-label linear relaxation leaves 19 fractionally feasible patterns. Adding neighborhood-cover constraints leaves nine. All nine have a five-support star supported in at most four labels, so the fivefold exterior product must vanish. This is a numerical-LP-backed finite reduction; it has not removed the support-pattern enumeration. Original exact symbolic and rational proof archives remain the stronger certificate for the known Ramsey upper bound.

## Remaining mathematical target

Prove without enumerating support multisets that no sixteen-element support system with six labels, each occurring five times, can support a triangle-free graph H satisfying d_H(b)=6−|T_b|, disjointness of adjacent supports, alpha(H)≤5, and the transversal-matroid containment I(H)⊆I(M(T)). Any genuine new theorem will need a global incompatibility beyond local matching existence. Plücker relations or matroid-circuit packing are candidates; no such relation has yet been proved to force nonexistence.
