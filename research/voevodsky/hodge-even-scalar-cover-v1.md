# Global iteration 22 (third series 2/10): an actual scalar tower, and why it fails

## Result and scope

Construct an explicit smooth connected etale cyclic-quartic tower C17->C9->C5 in the scalar elliptic-base-change family. Its primitive Prym is isogenous to Q4 squared, with Q4 an actual fourfold Prym from an explicit genus-seven to genus-three map. It cannot be isogenous to fixed A=X6 x B2.

More generally the same exclusion holds for a scalar elliptic-base-change tower when elliptic inversion has a verified order-two lift fixing the double-cover coordinate. It applies to the even branch equations below, **not every scalar root or every inversion-invariant branch set**. The four scalar labels and 512 nonlifting labels in the prior conditional census are not globally removed: the base curve and branch section vary.

This is actual auxiliary curve geometry, not a matching curve for Y2, an exceptional cycle or a Hodge verdict.

## 1. A cyclic-four isogeny over Q

Take

    E: y^2=x^3+7x^2+x,  P=(1,3).

The tangent slope at P is three, so 2P=(0,0), a nonzero two-torsion point. Thus P has exact order four. The quotient by <P> can be computed as two successive two-isogenies:

    x1=x+7+1/x,  y1=y*(1-1/x^2),
    E1: y1^2=x1*(x1-5)*(x1-9),
    u=x1-9,
    x2=u+13+36/u,  y2=y1*(1-36/u^2),
    Eprime: y2^2=x2*(x2-1)*(x2-25).

The source and targets are nonsingular elliptic curves. The maps extend from these rational formulas to isogenies of their smooth projective models. P maps to (9,0) on E1, and the second isogeny kills that point. The composite psi:E->Eprime has cyclic kernel <P> and degree four.

In particular, writing

    N=x^4+9x^3+16x^2+9x+1,
    D=x*(x-1)^2,

one has x2=N/D and

    y2=y*R/S,
    R=(x^2-1)*(x^4-4x^3-30x^2-4x+1),
    S=x^2*(x-1)^4.

The checker clears denominators and verifies the full elliptic equation as a polynomial identity, verifies gcd(N,D)=1, and doubles P exactly. Degree four follows also from the degree-four rational x-map. In characteristic zero this elliptic isogeny is etale.

## 2. Explicit smooth tower

Let C5 be the smooth projective normalization with function field

    y2^2=x2*(x2-1)*(x2-25),
    z^2=x2^4-2.

The four roots of x2^4=2 are distinct and avoid the elliptic two-torsion x-values 0,1,25. Hence z defines a double cover of Eprime branched at eight distinct points, with no branch at infinity (the pole order is eight). Riemann--Hurwitz gives genus five.

Define C9=C5 x_Eprime E1 and C17=C5 x_Eprime E using the isogenies above. These base changes are smooth and etale over C5. They are connected: the pulled-back double cover of either elliptic source has respectively sixteen or thirty-two simple branch points, so its defining function is not a square. Their genera are nine and seventeen.

The resulting C17->C5 is a connected etale cyclic-four cover, not merely a list of abstract torsion labels. Translation by P on E acts on C17, fixing z, and generates its deck group. Its square is the involution of C17/C9. These covers belong to the prior pulled scalar-root family (the corresponding order-four elliptic class M squares to the two-isogeny class zeta).

For an entirely polynomial presentation put w=D^2*z. Then C17 has function field

    y^2=x^3+7x^2+x,
    w^2=F(x)=N(x)^4-2*D(x)^4.

Always use the smooth projective normalization, not a potentially singular affine intersection at poles. The checker proves F has degree sixteen, is squarefree and is coprime to the elliptic cubic.

The deck involution z->-z of the elliptic double cover acts as a scalar on the primitive Prym: its invariant Jacobian part is the elliptic E, on which translations act trivially. Thus its invariant part has no intersection with the anti-rho^2 primitive part. This is a genuine scalar case from the preceding audit, not one of the already excluded mixed cases.

## 3. An extra involution that really exists

Elliptic inversion lifts to

    tau:(Q,z)->(-Q,z)

on C17 because psi is a group homomorphism and the branch function depends only on the target x-coordinate. In the polynomial model it is (x,y,w)->(x,-y,w). In particular **tau^2=Id**, not a possible order-four lift inferred from branch invariance alone.

Let rho:(Q,z)->(Q+P,z). Actual curve automorphisms satisfy

    tau rho tau=rho^-1.

Tau commutes with h=rho^2, so preserves the primitive Prym P8=Prym(C17/C9). On it rho^2=-Id and tau rho=-rho tau. The abelian images of 1+tau and 1-tau sum isogenously to P8, intersect in two-torsion, and rho identifies them. Each has dimension four. Therefore P8 is isogenous to Q4 x Q4.

A nonzero homomorphism from simple fixed X6 into a fourfold is impossible by dimension. Thus this actual P8 cannot be isogenous to A, independently of polarization or the Gaussian marking. The actual construction does not repair its applicability failure.

## 4. An explicit fourfold Prym quotient

The tau quotient is the hyperelliptic genus-seven curve

    H7: w^2=N(x)^4-2*D(x)^4.

On it h acts by (x,w)->(1/x,w/x^8), from translation by (0,0) on E. Its quotient is

    H3: v^2=(u^2+13u+36)^4-2*u^4,
    u=(x-1)^2/x,  v=w/x^4.

The degree-eight polynomial of H3 is squarefree, so its genus is three. The displayed map is degree two (x satisfies x^2-(u+2)x+1=0) and satisfies the equations identically after clearing denominators. It has four branch points by Riemann--Hurwitz. Consequently Q4 may be taken up to isogeny as Prym(H7/H3). Pullback on Jacobians identifies its image with the tau-even primitive part, and rho identifies the two primitive parts. This supplies a concrete lower-dimensional geometric factor, not an assertion that it equals X or detects alpha.

## 5. Precisely which family is excluded

For any cyclic-four elliptic isogeny psi:E->Eprime and a double cover of the form z^2=p4(x2) with simple eight-point branch divisor avoiding degeneracy, the same formulas for inversion on the double-cover coordinate give an actual order-two tau and the same square-fourfold obstruction. More generally it suffices to verify such an order-two lift and its inversion relation; mere invariance of a branch set is not enough. A lift can otherwise have a different square or action on the cover coordinate.

This is a restriction on a **subfamily of branch sections**, not the deletion of any of the four formal elliptic root labels over all possible C5. An explicit family with asymmetric sections

    z^2=p4(x2)+y2*q2(x2)

is not covered by this proof unless an appropriate lift is separately verified. On a Weierstrass elliptic curve these terms have pole order at most eight and are natural next inputs; simple zeros, connectedness, automorphisms and target matching must all be checked. No such matching or generic simplicity is claimed here.

The nonlifting 512-root branch also remains open, as do nonbielliptic intermediates and other Prym/direct-cycle geometries. The conditional necessary-condition census remains 516 labels / 258 inverse pairs; those numbers are not an unmarked moduli count. Actual theta dimension, exceptional algebraic cycles, all-cycle annihilation and independent review remain unavailable. All four f-pullback exceptional channels are still required.

Contract: `research/conjecture_net/contracts/hodge-even-scalar-cover.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_even_scalar_cover.py`.
Receipt: `research/voevodsky/results/hodge-even-scalar-cover-v1.json`.

    python research/voevodsky/checkers/check_hodge_even_scalar_cover.py

Trust boundary: original written elliptic-isogeny and normalized-cover construction, exact polynomial identities and squarefreeness, standard complex curve/elliptic group and abelian decomposition arguments. Finite controls do not formally verify these imports or constitute independent review. No new literature-exhaustion claim is made. The iteration-21 predecessor and pins v1-v22 are preserved unchanged.
