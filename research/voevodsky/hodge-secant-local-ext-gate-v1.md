# Global iteration 32 (fourth series 1/10): local geometry and Ext of the corrected secant object

## Result: a concrete deformation input, not semiregularity

Work with the **auxiliary principally polarized fourfold** A0 in Markman's section12, not the fixed sixfold X or eightfold Y2. Assume the stated generic transverse theta-translate incidence, no fivefold intersections, and the proposed 3Theta correction from iteration31. Let D_i (indices modulo9) be the translates, Z_i=D_i intersect D_(i+1), Z=union Z_i, and let nu partially normalize306 isolated ordinary double points.

The incidence and local algebra give:

- nine double curves, each of genus37;
- 216 triple points of three consecutive surfaces;
- 432 isolated transverse two-surface nodes, of which306 are normalized and126 remain;
- for E=[O_A0 -> nu_*O_Ztilde] tensor O(3Theta), placed in degrees0,1,
  H0(E)=I_Z(3Theta), while H1(E) has length306;
- the sheaf Ext^3(nu_*O_Ztilde,O_A0) has length126;
- the **sheaf** Ext^2(E,E) has length1116: two at each normalized node and four at each remaining node, zero elsewhere.

In particular E is not itself a coherent sheaf in one degree, and the partially normalized surface sheaf is still not Cohen-Macaulay at126 points. The number1116 is **not** the dimension of global Ext^2(E,E), not the obstruction space of the eventual eightfold transform, and not evidence that an actual deformation is obstructed. No semiregularity or target-cycle claim follows.

## 1. Incidence, including the non-isolated triple-point correction

Under transversality, a point lying on at most four translates has regular local coordinates given by their defining equations. Its active surfaces correspond exactly to the edges of the nine-cycle contained in the set of those translates. Exhaustively enumerating subsets of size at most four gives:

- adjacent edges: nine triple-divisor intersections, the double curves;
- three consecutive edges: nine four-divisor intersection types, giving9*24=216 triple points;
- two edges neither adjacent nor distance two:9*(9-5)/2=18 isolated-node types, giving18*24=432 points.

Edges at distance two also meet at24 points, but those points lie on the surface between them. They are triple points, **not isolated two-surface nodes**. Counting them as independently normalizable nodes is wrong.

A double curve is a transverse complete intersection of three theta translates. Adjunction gives K_curve=3Theta restricted to it; deg K=3*Theta^4=72, hence genus37. Each such curve meets its two neighboring double curves at24 points each. Total incidence9*48/2=216 agrees with the triple-point census. The numeral24 uses the principal fourfold identity Theta^4=4!.

These are universal conclusions conditional on the stated smoothness/transversality, not a construction of a chosen ppav or explicit translate parameters.

## 2. Four local types and exact resolutions

Use R=C[[a,b,c,d]], m=(a,b,c,d), residue field k. Twists by O(3Theta) trivialize locally and do not affect these module calculations.

A smooth surface has ideal(a,b). Along a generic adjacent double curve,

    (a,b) intersect (b,c) = (b,ac),

so the union is a codimension-two complete intersection. At a triple point,

    (a,b) intersect (b,c) intersect (c,d) = (ac,bc,bd).

This is a height-two Hilbert-Burch ideal, with matrix

    [ b   0 ]
    [-a   d ]
    [ 0  -c ].

Its signed maximal minors generate that ideal; R/I is Cohen-Macaulay and the ideal has projective dimension one. The same projective-dimension bound holds at smooth and adjacent-double-curve points. Thus Ext^2(I,I)=0 at all these strata.

At an isolated node,

    I=(a,b) intersect (c,d)=(ac,ad,bc,bd),
    0 -> R/I -> R/(a,b) direct_sum R/(c,d) -> k -> 0.

The last map is the difference of residues. It proves depth(R/I)=1, versus dimension2. Duality of this sequence, with Ext^4_R(k,R)=k and codimension-two complete intersections on the middle term, gives Ext^3_R(R/I,R)=k. Normalization replaces R/I by the middle term, where that third Ext vanishes. Therefore the global dual-Ext sheaf has precisely the126 remaining points, each with length one.

## 3. The derived object retains a point-sheaf cohomology term

For the partial normalization, globally

    0 -> O_Z -> nu_*O_Ztilde -> Q -> 0,
    length Q=306.

The augmentation O_A0 -> nu_*O_Ztilde has kernel I_Z and cokernel Q. Consequently E has H0=I_Z(3Theta) and H1=Q(3Theta). Even normalizing every isolated node would not make this augmentation complex a sheaf: H1 would then have length432. Omitting normalization makes E an ideal sheaf, but loses the corrected secant character. None of these changes may be made silently.

A derived equivalence or a later external-product construction might produce a sheaf; its cohomological concentration must be checked rather than assumed. This analysis does not show that such a transform is impossible.

## 4. Local self-Ext^2: lengths two and four

At a normalized node resolve the two complete-intersection summands and cancel the diagonal R -> R^2 in the augmentation. A free model for E is

    R^2 --Dminus1--> R^4 --D0--> R,

in degrees-1,0,1, where

    Dminus1=[-b  0]       D0=[-a -b c d].
            [ a  0]
            [ 0 -d]
            [ 0  c]

The product is zero. The highest degree in Hom(E,E) is degree2, with module Hom(R^2,R)=R^2. All boundaries lie in m R^2, and D0 composed with arbitrary maps R^2->R^4 already gives all m R^2. Hence

    Ext^2_R(E,E)=k^2.

At an unnormalized node E is I. Tensoring the two Koszul ideal resolutions gives

    0 -> R --D2--> R^4 --D1--> R^4 -> I -> 0,
    D2=[b,-d,c,-a]^t,
    D1=[ d   b   0   0 ]
        [-c   0   b   0 ]
        [ 0  -a   0   d ]
        [ 0   0  -a  -c ].

The row of ideal generators is[ac,ad,bc,bd]. Both compositions vanish; the tensor resolution is exact because the two ideals use disjoint regular-variable pairs. Applying Hom(-,I), the final image is mI, since the entries of D2 generate m. Thus Ext^2_R(I,I)=I/mI=k^4. Completion faithfully detects these finite-length local modules.

There are no other nonzero stalks of sheaf Ext^2(E,E), by the projective-dimension-one models above. Its total length is

    2*306 + 4*126 = 1116.

The checker verifies the monomial-ideal intersections, Hilbert-Burch minors, polynomial matrix compositions, minimality/maximal-ideal generators and full incidence census. Exactness uses the written regular-sequence/Hilbert-Burch/tensor arguments, not merely vanishing matrix products.

## 5. The next missing maps, now more precisely identified

The local-to-global spectral sequence is

    H^p(A0, sheaf_Ext^q(E,E)) => Ext^(p+q)(E,E).

Its degree-two edge term H0(sheaf_Ext^2) has dimension1116, but outgoing differentials can land in H2(sheaf_Ext^1) and H3(sheaf_Hom). No surjectivity of the global edge map is assumed. Nonzero Ext groups parameterize possible obstruction receptacles; they do not prove that a deformation has nonzero obstruction.

Next compute the relevant global differentials/Atiyah evaluation for this **derived** fourfold object, and build its precise external-product/Orlov transform with a verified sheaf or perfect-complex deformation theorem. A derived equivalence preserves global Ext, not a naive stalkwise identification of the displayed local Ext sheaves. The weaker criterion in Question11.4 remains unproved. The parallel ramified genus16/8/4 matching route and direct cycles remain available.

Contract/checker/receipt: `hodge-secant-local-ext-gate.v1.json`, `check_hodge_secant_local_ext_gate.py`, `hodge-secant-local-ext-gate-v1.json` in the usual contracts/checkers/results directories. Prior primary sources and the iteration31 correction receipt are consumed freshly. Iteration31 and pins v1-v33 are retained. No actual geometry at the fixed target, new exceptional cycle, Hodge verdict or independent review is supplied.
