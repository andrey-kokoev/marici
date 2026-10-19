# Global iteration 35 (fourth series 4/10): an actual auxiliary ramified trigonal family and equivariant etale tetragonal transfer

## Substantive result

The genus16/8/4 alternative is no longer just a Riemann-Hurwitz pattern. We give a smooth connected complex auxiliary cyclic-quartic tower

    C16 -> D8 -> B4,

with branch monodromies(1,3), a trigonal map D8->P1 whose ramification avoids the two top-double-cover branch points, and those points in different trigonal fibres. We verify Lange-Ortega's actual primary hypotheses. Its symmetric-cube construction transfers this tower to a **free cyclic-quartic etale tower**

    Y17 -> T9 -> Z5,

where T9 is tetragonal, not a newly asserted trigonal curve. The induced principally polarized Prym isomorphism is K=Q(i)-equivariant by the defining correspondence. Both descriptions satisfy Schoen's primary Theorem2.0, giving algebraicity of the auxiliary determinant plane.

This is a geometric existence construction using a line-bundle square root on B4, not a fully coordinatized selected quartic cover. It does **not** supply a K-equivariant isogeny to the fixed target Y2, its period matching, a target cover or a target exceptional cycle. The remaining target-matching gate is genuine.

## 1. A concrete smooth connected trigonal bottom curve

Take the compact spectral curve B over P1_x with affine equation

    F(x,y)=y^3-3y+b(x)=0,   b(x)=x^6+3x-2.

Here y is a fibre coordinate for O(2). On the other base chart s=1/x, v=s^2 y, the equation is

    v^3-3s^4 v+1+3s^5-2s^6=0.

At s=0 it has three distinct roots v^3=-1, so B is smooth and the degree-three projection is unramified at infinity. Its finite discriminant, up to a nonzero factor, is Delta=4-b(x)^2, of degree12. The exact rational gcd of Delta and Delta' is1. At its roots y=+/-1 and b'(x) is nonzero, so B is smooth with twelve simple trigonal ramification points. Riemann-Hurwitz gives genus4.

For completeness, this cubic is irreducible over C(x), not merely over Q(x). Any rational root is a polynomial since it is integral over C[x], and has degree at most2. Write it as a*x^2+b1*x+c. Coefficients of degrees6,5,4 force a^3=-1, b1=0, c=0. The degree2 coefficient then forces a=0, a contradiction. A reducible cubic over a field has a root. This proves connectedness; the checker verifies the coefficient implications symbolically over Q, not by testing finitely many candidate roots.

Name four points:

    P=(0,-1), p=(0,2), Q=(1,1), q=(1,-2).

The fibres are 2P+p and 2Q+q. P,Q have trigonal ramification index2, whereas p,q are unramified. Consequently

    div(x/(x-1))=2P+p-2Q-q.

## 2. The genus-eight trigonal double cover

Let D be the normalization of B in the quadratic extension

    u^2=x/(x-1).

Only the odd valuations at p,q ramify. Thus D is smooth and connected, D->B is branched precisely at p,q, and g(D)=8. Its involution eta sends u to -u. The map

    h:D->P1_u

has degree3. It is the normalized base change of the trigonal map B->P1_x by the rational degree-two cover x=u^2/(u^2-1).

Over x=0, the ramified point P splits into two points after normalization, while the point p has a single ramified lift p_D. The map h is unramified at all three points in this u=0 fibre: locally at p, u is a parameter; locally at P the two normalized branches have u proportional to the local parameter. The same holds over x=1 and u=infinity. In particular p_D and q_D are unramified for h and lie in different fibres. The remaining ten simple ramification values of B lift in pairs, giving twenty simple ramification points for h, consistent with genus8.

The involution does not fix the trigonal base pointwise: h eta=a h with a(u)=-u. This distinction is essential for the extra action below.

## 3. A genuine cyclic-quartic top cover, not the naive fourth root

Set N=O_B(Q+q-P), of degree1. The displayed principal divisor gives N^2=O_B(p+q), and the double cover defined by N and this section is exactly D.

Choose a line bundle M of degree1 with

    M^2=N(q).

Such M exists: multiplication by2 on Pic^0(B) is surjective over C. Its square-root torsor has 2^(2*4)=256 elements. This is a count of line-bundle roots, **not** of distinct unmarked curves, target covers or matches. Choose the induced isomorphism M^4=O_B(p+3q). Normalize the cyclic fourth-root construction for the section with divisor p+3q. It produces a smooth connected curve C with deck generator rho of order4, ramified only at p,q, totally of index4 there. Connectedness follows already from a local monodromy generator at p.

The intermediate double-cover line is M^2(-q)=N, so C/<rho^2> is our specified D, not just some genus-eight double cover. Riemann-Hurwitz gives g(C)=16. The double map f:C->D branches only at p_D,q_D. We have rho^2 equal to the deck involution sigma of f, and rho induces eta on D.

**Do not replace this construction by w^4=x/(x-1).** That naive fourth root also has index-two ramification at P,Q and has genus18. The line-bundle square-root choice removes precisely this unwanted ramification while retaining the prescribed middle cover. The checker retains this hostile numerical control.

No explicit divisor representing a selected M has been computed. The proven surjectivity of the Picard square map supplies geometric existence of the auxiliary covers; it does not provide coefficients for a selected cover over a specified number field. The concrete B already makes the construction nonempty. Smooth coefficient variations give auxiliary families; no moduli dominance is asserted.

## 4. Fresh primary verification of Lange-Ortega

Retained primary source: Lange-Ortega, *The trigonal construction in the ramified case*, arXiv:1902.00251v1 (1 February2019). PDF and full extracted text, with hashes, are in `inputs/hodge-ramified-trigonal-v1/`.

The introduction/PDF pp1-2 defines **general** here to mean that the two double-cover branch points lie in different trigonal fibres, with branch locus disjoint from trigonal ramification. It does not mean a generic point of the entire curve moduli space. Section2, diagram(2.1), defines

    Y=(f^(3))^-1(g1_3) inside Sym^3(C).

Lemma2.1 makes its complement involution tau= sigma^(3) fixed-point free. Propositions2.3-2.5 give connectedness, smoothness and genus2g(D)+1=17 under the checked general hypotheses. The quotient T=Y/tau is a smooth tetragonal curve of genus9. Theorem5.1, PDF pp11-13, identifies P(Y/T) and P(C/D) as principally polarized abelian varieties.

Our p_D,q_D meet exactly these hypotheses, so this theorem actually applies to the auxiliary construction. Proposition5.2 gives two tetragonal fibres of type(2,2). The authors explicitly do not know the exact image of the general construction; we do not claim its map is surjective, nor use it to infer target Prym membership from dimensions.

## 5. The extra order-four action survives here: explicit proof

The primary theorem's bare ppav statement alone does not automatically preserve arbitrary extra cyclic actions. For this family we can prove it using the construction.

Since f rho=eta f and eta preserves the trigonal pencil up to a, the automorphism rho^(3) of Sym^3(C) preserves Y. Let R be its restriction. Then

    R^2=(rho^2)^(3)|Y=sigma^(3)|Y=tau.

Because tau is fixed-point free, no nonidentity element of <R> can fix a point: a fixed point for R or R^3 would also be fixed by R^2. Thus R has order4 and acts freely. On T=Y/<R^2>, its induced involution is free too. Indeed a fixed quotient point would require R y=y or R y=R^2 y, either of which forces an R-fixed point. Hence Z=Y/<R> is smooth of genus5 and Y->Z is an etale cyclic-quartic cover. This proves the genera17/9/5 and the cyclic action, not just their numerical compatibility.

As a finite local control over either fixed trigonal-base value, four section states can be labelled(a,b) in {0,1}^2 with R(a,b)=(b,1-a), or its inverse. Its square is complement and its orbit has length4. This is a control for the possible special-fibre behaviour; the global freeness proof is the R^2=tau argument plus the primary lemma, not a finite enumeration of every geometric fibre.

The Prym isomorphism in Theorem5.1 is induced by the divisor-sum correspondence Y->Sym^3(C)->J(C), translated and factored through the Abel-Prym map. On Jacobians the constant translations disappear. The sum correspondence intertwines R and rho. The surjective map (1-tau):J(Y)->P(Y/T) commutes with R, so its Prym factor also intertwines R and rho (precompose the desired equality with this surjection). Therefore the actual ppav isomorphism

    P(Y/T) -> P(C/D)

is K-equivariant for i acting by R and rho, respectively. Both squares are -1 on the corresponding Prym. This verifies the extra-action gate for **this constructed family**, not for every application of the theorem.

There is no conflict with the prior genus-nine trigonal/free-involution exclusion: T9 is tetragonal, and no trigonal structure on it has been supplied or required.

## 6. Schoen applies to both auxiliary realizations

Use the previously retained and freshly checked primary Schoen1988 Theorem2.0, PDF pp11-12, not an unverified addendum or a generic-fourfold inference.

For C16->B4 the primitive rank h is8 and the two monodromies are(1,3), a simple paired orbit (r=1). For Y17->Z5 it is h=2*5-2=8 with no branch points (r=0). The primary theorem explicitly makes simplicity automatic for r=0 or1. Thus its algebraic-cycle theorem applies in both cases. The usual algebraic Jacobian/primitive-projector correspondences retained in iteration31 transfer this determinant subspace from the eighth power of the curve to the primitive Prym.

In the etale description every nontrivial character has four holomorphic differentials; the primitive characters i,-i therefore give type(4,4). The Prym dimension is8, H1 has K-rank8 and its K-determinant plane has rational dimension2. The two descriptions are identified equivariantly by the preceding argument. Thus **auxiliary determinant-class algebraicity** is established by the primary theorem on these geometrically existing auxiliary objects.

This does not identify that plane with the fixed Y2 plane via an actual algebraic correspondence. There is no cycle on Y2 or X in the output. The root contract's available target witnesses remain empty. A selected M, explicit cycle equations and coefficients have not been computed; auxiliary algebraicity is a theorem-level existence result.

## 7. Next gate and verification boundary

The executable continuation is no longer to repeat the ramified genus census or merely assume extra-action preservation. Seek an actual member with a specified K-equivariant rational H1 isomorphism/isogeny to Y2 and an algebraic correspondence, or compute a genuine factor/period obstruction to that match. The original X, alpha, all four target transfer channels, determinant/denominator48 data and prior target censuses are unchanged. Other objects, restricted commutative deformation theorems, direct cycles and theta data remain alternatives.

Contract: `research/conjecture_net/contracts/hodge-ramified-trigonal-family.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_ramified_trigonal_family.py`.
Receipt: `research/voevodsky/results/hodge-ramified-trigonal-family-v1.json`.

Imports not discharged by finite arithmetic: normalization and cyclic-cover line-bundle construction; surjectivity of the complex Picard square map; Riemann-Hurwitz; the cited Lange-Ortega and Schoen theorems; functorial Jacobian/Prym correspondences. Exact controls certify discriminant/irreducibility identities, branch positions, divisor identities, local group action and source freshness, not formal proof-assistant certification or independent review. Iteration34 and pins v1-v36 are retained. No target match, exceptional target cycle, all-cycle obstruction or Hodge verdict is claimed.
