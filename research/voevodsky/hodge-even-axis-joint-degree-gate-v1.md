# Global iteration 41 (fourth series 10/10): prune the joint elliptic map for Y3

## Result and scope

Start from freshly validated iteration40, not a hypothetical new target. X, alpha, actual Y3 and its degree256/phase768i/denominator768/four-channel maps stay fixed. Suppose the exact principally polarized Y3 is realized as a smooth etale cyclic-four Prym C17->D9->B5. Its actual elliptic axes give the maps

    phi_+:C->E_i, deg=8; phi_-:C->E_i, deg=12,
    phi_+ rho=i phi_+, phi_- rho=-i phi_-.

Let V be the normalization of their joint image Gamma in E_i^2, and delta=deg(C->V). Then:

1. delta divides gcd(8,12), so delta=1,2 or4.
2. **delta=4 is impossible for this fixed principal Y3.** A two-dimensional anti-invariant Prym would have a two-primary induced polarization, incompatible with Y3's actual elliptic surface Euler characteristic24.
3. **delta=2 is not excluded**, but forces V9 and a degree-two polarized isogeny from a ramified Prym P(V9/W1), branched at16 points, to Y3. It further forces C17 to be bielliptic and the entire original tower to be the scalar elliptic-isogeny pullback described below.
4. delta=1 requires Gamma to have arithmetic genus97 and total normalization defect80. In the delta=2 branch, those numbers are25 and16, with V of genus9.

The fixed principal Y3 is also **not a smooth canonical Jacobian**, by a fresh application of polarized Torelli and its degree-four elliptic axis. This is not the old degree-two Y2 exclusion transported across an isogeny.

No curve, joint map degree, source Picard class, principal Prym match or exceptional cycle has been supplied. In particular the surviving scalar branch is not discarded using Y2's degree-two obstruction: Y3 meets its lower bound4.

## 1. The joint degree and the anti-invariant subvariety

Use the simultaneous translations already justified in iteration40 to remove affine constants. The diagonal automorphism(i,-i) preserves Gamma, so rho descends to V as an automorphism of order4. Its square h_V is a nontrivial involution, since both elliptic projections are nonconstant and negated by h=rho^2. Put W=V/<h_V> and P_V=P(V/W)=im(1-h_V) in J(V). The finite map a:C->V intertwines these involutions, so a*:P_V->P(C/D)=Y3 has finite kernel.

The two elliptic projections of V have independent pullback images in P_V: if the images coincided, an isogeny of square-lattice elliptic curves would intertwine i with -i, impossible in End^0(E_i)=Q(i). Their images under a* span the whole actual elliptic isotypic surface B3 of Y3. The fixed isogeny type of Y3 is X6 x E_i^2, with X simple. By Poincare reducibility its connected anti-subobject P_V therefore has dimension **2 or8**, not an arbitrary dimension between them. In dimension2 the image is exactly B3; in dimension8 it is all Y3.

Riemann-Hurwitz gives g(V)<=1+16/delta. For delta=4 this is5, so only dimension2 can occur. For delta=2 it is9. If dim(P_V)=8, the only possibilities are

| g(V),g(W) | branch points V/W | ramification C/V |
|---|---|---|
| 8,0 | 18 | 4 |
| 9,1 | 16 | 0 |

The latter vanishing will be essential to the group argument; etaleness of a is not assumed before this reduction. No Galois assumption on a is made in the degree-four case.

## 2. The actual restricted polarization, and the factor-three obstruction

Write L_V=Theta_V restricted to P_V, with no principal-half normalization. For any involution on a principally polarized Jacobian, the orthogonal complement of P_V is its connected invariant part. Thus

    ker(lambda_LV)=P_V intersect P_V^perp

is killed by2: on that intersection the involution is both plus and minus identity. In dimension2 the elementary divisors are1 or2, and

    chi(L_V) in {1,2,4}.

This argument applies whether V/W is ramified or etale. It does not silently assume a principal Prym polarization in an arbitrary branch count.

For the etale original C/D the actual inclusion satisfies Theta_C|Y3=2Xi3. Functoriality of Jacobian polarizations gives (a*)*Theta_C=delta Theta_V. If P_V has dimension2 and b:P_V->B3 denotes the induced isogeny, consequently

    b*(Xi3|B3)=(delta/2)L_V,
    deg(b)*chi(Xi3|B3)=(delta/2)^2 chi(L_V).

Joint lattice saturation in iteration39 gives the **actual**, not merely isogenous, product with degrees4,6. Hence chi(Xi3|B3)=4*6=24, not the polarization-homomorphism degree24^2. The possible degrees of b would be

| delta | chi(L_V)=1,2,4 |
|---|---|
| 2 | 1/24, 1/12, 1/6 |
| 4 | 1/6, 1/3, 2/3 |

None is a positive integer. Equivalently the right side is two-primary and cannot absorb the factor3 in24. Thus dim(P_V)=2 is impossible in BOTH nonbirational cases. In particular delta=4 is completely excluded.

This obstruction uses Y3's precise saturated principal restriction. It would fail for a different surface Euler characteristic (for example4), or an unrelated source polarization with a factor3. It is not an exclusion of all degree-four joint maps in the iteration40 Kummer family before target matching.

## 3. A new Jacobian exclusion for Y3; eliminate the genus-eight alternative

Use the retained primary Milne *Jacobian Varieties*, Theorem12.1(a,b), PDF page38, freshly read and hashed again. If the canonical Jacobian of a smooth genus-eight curve were Y3, its actual polarized native automorphism squaring to -Id would, by strong Torelli and the uniqueness of the nonhyperelliptic sign, force the curve to be hyperelliptic.

The actual elliptic theta-degree-four inclusion gives a curve map of degree4 (Jacobian adjunction, NOT the Prym multiplier2). Together with the hyperelliptic degree-two map it is birational onto its joint image: a common degree2 factor would force a nonconstant map P1->E, impossible in characteristic zero. Adjunction on P1 x E gives genus at most2*4-1=7, contradicting8. Thus the fixed principal Y3 is not a canonical smooth Jacobian. Arbitrary isogenies to Jacobians are not excluded.

Return to delta=2 with dim(P_V)=8. In the (g(V),g(W))=(8,0) alternative, P_V=J(V), L_V=Theta_V principal. The induced b:J(V)->Y3 has b*Xi3=Theta_V, so deg(b)=1, an excluded canonical principal Jacobian presentation. Independently, V is hyperelliptic because W=P1, and its first elliptic map has degree8/2=4, giving the same genus contradiction directly.

Only V9/W1 with16 branch points remains. For this ramified double cover, q*:J(W)->J(V) is injective; duality then gives connectedness of the norm kernel. (A nontrivial pullback kernel would give an unramified factor of a double cover, contrary to ramification.) Its intersection with P_V is q*J(W)[2], so ker(lambda_LV) has four points and L_V has type(1^7,2), chi=2. Since b*Xi3=L_V, **deg(b)=2**. This is a genuinely polarized isogeny, not an inverse cohomology map.

This genus9/1, sixteen-branch auxiliary source must not be confused with the earlier two-top-branch genus16/8/4 construction. Neither source has been produced or matched here.

## 4. Degree two forces a bielliptic top and a scalar pullback square

Now a:C17->V9 is an etale quadratic map. Let sigma be its deck involution. Because rho descends to V, it normalizes the order-two deck group, hence commutes with sigma. Also sigma!=h: h acts nontrivially on V. Thus h,sigma generate a Klein four group. With W=V/h_V of genus1, the dimensions of H^0(K_C) by their two signs are

    (h+,sigma+) =1,
    (h+,sigma-) =8,
    (h-,sigma+) =8,
    (h-,sigma-) =0.

The middle two entries come from g(C/h)=9 and g(C/sigma)=9; the last follows from g(C)=17. Therefore beta=h sigma has invariant dimension1. Its quotient

    T=C/<beta>

is elliptic, and C->T is a degree-two bielliptic map branched at32 points.

The group generated by rho and sigma is C4 x C2. Put Z=V/<rho_V>=C/<rho,sigma>. Rho_V has no fixed point: a fibre of the etale double map a has two points, so a hypothetical rho_V-fixed point would make rho permute that pair; rho^2=h would fix both, contradicting freeness of h on C. The same holds for rho_V^3. The involution h_V has16 fixed points. Group Riemann-Hurwitz on V9 therefore gives

    16=4(2g(Z)-2)+16, hence g(Z)=1.

The map T->Z has degree4 with cyclic group generated by rho modulo beta. Both curves are elliptic, so it is an etale cyclic-four isogeny after choices of origins. The map B5=C/<rho> -> Z is double and branched at8 points. The two subgroups <rho>,<beta> meet trivially and generate C4 x C2, so the original cover is the normalized fibre product

    C17 = B5 x_Z T,
    B5->Z elliptic double cover branched at8,
    T->Z etale cyclic-four elliptic isogeny.

This is precisely a scalar elliptic-isogeny pullback shape. Z and T are not asserted to be the square-lattice target E_i. It is a conditional restriction, **not** a supplied curve and **not** an exclusion of all scalar roots for Y3. The earlier Y2 argument used theta degree2; Y3's minimum4 does not contradict the scalar lower bound. No finite root-label census is asserted without fixing the elliptic/base/level parameters.

## 5. The birational branch and the singularity budget

The off-diagonal correspondence phi_+,* phi_-* vanishes by opposite rho characters. Indeed i A=A(-i) in End^0(E_i)=Q(i) implies A=0. Passing from C to V divides this pairing by delta, so it remains zero there. This is important: the two elliptic targets ARE isogenous; no false non-isogeny shortcut is used to remove correspondence terms.

For Gamma in E_i^2, the two projection degrees are8/delta,12/delta. The Neron-Severi Hermitian matrix is diagonal with these two entries interchanged. Surface adjunction, with canonical class zero, therefore yields

    p_a(Gamma)=1+96/delta^2.

For delta=1 the normalization is C17, so p_a=97 and the sum of local normalization defects is80. For surviving delta=2 its normalization is V9, so p_a=25 and the defect sum is16. These are lengths of the normalization quotient sheaf, not counts of ordinary nodes or distinct singular points. No existence or nonexistence of a curve with these defects has been proved.

The map B5 to the quotient surface S from iteration40 has the SAME generic degree delta. This follows by comparing the two faithful C4 function-field extensions C/B and V/Z. Consequently:

- delta=1: B5 is birational to its image in S; that image normalization has genus5.
- delta=2: B5 double-covers its image normalization Z, which is elliptic, not genus5.

The iteration40 equations remain valid in either case. Its phrase “genus-five curves on S” must not be read as requiring a birational genus-five image: the surviving scalar branch is a genus-five curve mapping two-to-one to an elliptic image. This turn makes that search distinction explicit.

## 6. Next executable split and trust

Proceed in either live branch:

1. Birational branch: seek the required genus-five normalization on S, lifting to a (projection8,12) curve in E_i^2 with defect sum80 and all Kummer/connectedness/joint-kernel checks.
2. Scalar branch: use the explicit elliptic-isogeny pullback square, demand the two elliptic maps/joint degree2, the ramified V9/W1 induced type(1^7,2) and degree-two polarized isogeny to Y3; solve the remaining actual period/correspondence matching. Do not discard it using an unchanged Y2 theta degree.

Then use the retained four cycle channels and phase-correct denominator768 transfer; neither branch has supplied a target exceptional cycle. Direct cycles and other ramified/generalized/isogenous sources remain open. The actual theta singularity dimension is still unknown.

Contract: `research/conjecture_net/contracts/hodge-even-axis-joint-degree-gate.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_even_axis_joint_degree_gate.py`.
Receipt: `research/voevodsky/results/hodge-even-axis-joint-degree-gate-v1.json`.

Trust: written Poincare reducibility, Jacobian/Prym adjunction, restricted-polarization kernel, strong Torelli, curve normalization and finite-group quotient proofs; exact genus/Euler/character/group/defect controls and freshly hashed primary Torelli plus Y3/Kummer receipts. Finite controls do not construct actual functions, Picard classes, curves or period matches. This is not proof-assistant certification or independent review. Iteration40 and immutable pins v1-v43 are preserved. X/alpha and all unrestricted witness obligations remain fixed and open; no Hodge verdict is supplied.
