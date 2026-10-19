# Bounded Gauss-map test: an exact Gram bound, not universal orthogonality

## Decision

Execute the operator-selected alternative, not the queued polystable-bundle control. The test derives a sharper necessary positivity inequality for effective classes on the fixed X, but finds NO new all-cycle vanishing theorem. Plucker decomposability does not force the relevant canonical-form pairing to vanish. By the agreed stopping criterion, close this bounded branch rather than extend it into more reader/positivity controls.

This does not rule out a future source-specific theorem about Gauss images. It says the tested local equations and canonical-form positivity do not supply one. No confirmation-directed search is reactivated.

## Exact marked canonical-form reader

Keep U=R+iI, the Gaussian action, the polarization E and complex integration orientation from the fixed-source certificate. The Gaussian eigenspaces in H^(1,0)(X) both have dimension3. Choose adapted E-unitary one-form coframes and let Omega_+,Omega_- be their determinant holomorphic three-forms. The convention for a unitary coframe z_j is E=(i/2)sum z_j wedge conjugate(z_j).

The native determinant line is spanned by Omega_+ wedge conjugate(Omega_-). Its normalization can be fixed so that

    U=(1/sqrt(3)) Omega_+ wedge conjugate(Omega_-).

Indeed integral U wedge conjugate(U)=-64 by the retained cup matrix. For E-unitary determinants, integral (Omega_+ wedge conjugate(Omega_-)) wedge its conjugate is -192: the polarized volume integral E^6/6! is3. Thus the coefficient has modulus1/sqrt(3), and a determinant-frame phase fixes it to the stated positive value. This is a normalization of complex forms, not a rational change of the marked R,I.

At the chart origin it is explicit: Omega_+=u1 u2 u3 and Omega_-=sqrt(3) conjugate(u4 u5 u6), with u_j=dx_j+i dy_j.

For any smooth projective threefold map f:Y->X, put s_+=f*Omega_+, s_-=f*Omega_- in H^0(Y,K_Y). The positive Hermitian pairing of canonical forms, linear in the first argument, is

    h(s,t)=i integral_Y s wedge conjugate(t).

The factor i=i^(3^2) fixes the positivity convention. Consequently

    integral_Y f*U=-(i/sqrt(3)) h(s_+,s_-).

Thus the cross pairing is exactly the old Weil reader in canonical-form coordinates. Its vanishing has not acquired a new proof from this identification.

## A sharper effective-class inequality on the FIXED source

Write f_*[Y]=aE^3+bR+cI, using the fixed three-dimensional rational Hodge space. The Gaussian automorphism acts by -1 on U and by +1 on each Omega_+ wedge conjugate(Omega_+) and Omega_- wedge conjugate(Omega_-). Invariance of integration therefore makes their pairings with R,I zero. Unitary exterior algebra gives

    i integral_X E^3 Omega_+ conjugate(Omega_+)
      =i integral_X E^3 Omega_- conjugate(Omega_-)=144.

The exact Gram matrix is consequently

    G = [[144a, 32 sqrt(3)(c-i b)],
         [32 sqrt(3)(c+i b), 144a]].

Here the off-diagonal entry follows from integral_Y f*U=-32(b+i c). Positivity of h implies

    a>=0,   b^2+c^2 <= (27/4)a^2.

If the image has dimension3, ampleness gives a>0; if it has smaller dimension all the displayed classes and pullbacks of top forms vanish. The same inequality holds for effective rational combinations by adding their positive Gram matrices.

This improves the translation/self-intersection bound b^2+c^2<=(135/2)a^2, but is still a POSITIVITY bound, not b=c=0. It does not hold for arbitrary signed combinations. In particular the two numerical classes E^3+R and E^3-R both have positive definite G, with determinant17664, and their half-difference is R. No existence of effective representatives of these two numerical classes is asserted.

The cone permitted by this test spans the whole Hodge space. Therefore this bound alone cannot establish annihilation of the rational algebraic-cycle image.

## What the Gauss map actually says

On the rank-three locus of df, a tangent plane in T_0 X defines a point of Gr(3,6). In local coordinates on Y, the coefficients of s_+ and s_- are the two complementary Plucker minors of its differential matrix. The cross pairing integrates their product, one conjugated, against the local positive volume convention.

The Plucker equations do NOT force this product to vanish. The plane with differential matrix [I_3; I_3] has both complementary minors equal to1. It is a genuine decomposable plane, not a formal vector violating the Grassmannian equations. Such a plane is also realized by a local analytic immersion into the fixed torus. This local statement does not construct a compact algebraic threefold with that Gauss image on the fixed simple X.

Hence a viable new theorem would have to constrain GLOBAL Gauss images of projective subvarieties of this particular X. The ordinary local rank and Plucker equations do not do that. Nor does the action on X automatically induce a Gaussian action on Y or an orthogonality theorem on H^0(Y,K_Y).

## Actual algebraic nonorthogonality control on the product fiber

At the chart origin, the underlying product has positive complex coordinates u1,u2,u3 and negative coordinates conjugate(u4),conjugate(u5),conjugate(u6). There is an algebraic embedding of a product of three Gaussian elliptic curves given in native coordinates by

    f(z1,z2,z3)=(z1,z2,z3,conjugate(z1),conjugate(z2),conjugate(z3)).

The conjugations are holomorphic into the factors with reversed complex structure and preserve their lattices. This is a homomorphism of projective abelian varieties. On this Y,

    s_+=dz1 dz2 dz3,
    s_-=sqrt(3) s_+,
    h(s_+,s_+)=8,  h(s_-,s_-)=24,
    h(s_+,s_-)=8 sqrt(3),
    integral_Y f*U=-8i.

Thus the old normalized reader is (0,1/4), genuinely nonzero on an algebraic source. The Gram determinant is zero, saturating Cauchy-Schwarz without giving orthogonality. The Gaussian action of the ambient product does not preserve this graph, illustrating the missing source action.

This fiber has additional rational Hodge classes. Its cycle must NOT be forced into the fixed-X basis (E^3,R,I), and the fixed-X diagonal formula144a must not be applied there. Only the canonical-form identity and Hermitian positivity are shared across the two controls.

On the actual fixed-source complete intersection of class k^3 E^3, the Gram matrix is instead144 k^3 times I_2, so the integrated cross pairing is zero. This checks the known zero-readout control without asserting pointwise orthogonality of its Gauss minors.

## Outcome and stopping rule

Constructed: the marked canonical-form expression, its exact Gram matrix on the fixed Hodge space, the sharper necessary effective-class bound, and a local Plucker counterexample to automatic orthogonality, checked against an actual algebraic product-fiber graph.

Not constructed: any global restriction on Gauss images that forces zero cross pairing for every projective threefold map into the fixed X. In particular neither simplicity nor rational Picard rank one has been converted into such a restriction.

The bounded test therefore stops here. It yields a sharper positivity control but no independent universal necessity theorem. The fixed-candidate nonalgebraicity hypothesis remains open. Do not turn the new constant27/4 or the cross-pairing notation into another automatic sequence of obstruction nodes.

The queued polystable control is not executed by this task. Further work requires a separately justified global-geometric proposal or independent review; this note does not announce a new executable vanishing argument.

Verification separates exact Gaussian exterior algebra, Plucker minors and numerical Gram identities from the written canonical-form/Grassmannian interpretation and projective-source geometry. No proof-assistant certification or Hodge verdict is claimed.
