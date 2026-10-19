# Blowup closes the complete-intersection nodal-envelope control

## Fresh task and exact family

Execute complete-intersection-envelope-blowup. Retain the fixed polarized sixfold X, the connected smooth complete intersection Z=CI(kE,kE,kE), and a general sufficiently high-degree divisor D of class mE containing Z. The prior normal-jet proof gives N nodes Sigma, all on Z, and U=D minus Sigma. The known-cycle calculation gives a nonzero r_Z in K_D=ker(gamma:Q^N->H^5(D)), with psi_D(r_Z)=0.

We now compute ALL of K_D and the support image of this D, not merely one vector. Sufficiently high degree is increased if necessary to satisfy ampleness on the blowup as well as the earlier generation and transversality hypotheses.

## Smooth ample strict transform and the exceptional fibers

Let pi:B=Bl_Z(X)->X, with exceptional divisor F. The center is smooth of codimension three, so B is a smooth projective sixfold. The line bundle

    pi* H^m tensor O_B(-F)

is ample and globally generated for all sufficiently large m: O_B(-F) is relatively ample for the blowup, and an ample twist from X supplies the absolute statement. Its sections are H^0(X,I_Z tensor H^m). A general strict transform Dtilde is therefore smooth and ample in B. These generic conditions can be intersected with the prior nodal-envelope open conditions.

The fibers must be distinguished. In the retained local pair at a node,

    D: sum x_i y_i=0,  Z:y=0.

Blow up the y variables. On a chart y=t v, with v_j=1 for a chosen j, the STRICT transform is

    sum x_i v_i=0,

not t times this equation. Its derivative with respect to x_j is 1, so it is smooth there. Above a node, all x_i vanish and the fiber is the entire P^2 of v-directions. Above a smooth point of Z on D, the nonzero normal derivative cuts a hyperplane in this P^2, giving P^1. Away from Z the map is an isomorphism.

Let T be the disjoint union of the N exceptional P^2 fibers over Sigma, and put V=Dtilde minus T. Each component of T has complex codimension THREE in the smooth fivefold Dtilde. Over U there is instead the ordinary smooth-center blowup

    V = Bl_(Z minus Sigma)(U),

whose center has codimension TWO in U. This is the source of the different cohomological shifts below.

## First comparison: ambient blowup and ample weak Lefschetz

The smooth-center blowup formula in degree four gives

    H^4(B,Q) = H^4(X,Q) plus H^2(Z,Q)(-1) plus H^0(Z,Q)(-2).

Weak Lefschetz for the smooth ample fivefold Dtilde gives H^4(B)=H^4(Dtilde). The successive complete-intersection weak-Lefschetz isomorphisms give H^2(Z)=H^2(X), and Z is connected. On the abelian sixfold,

    b4(X)=495, b2(Z)=66, b0(Z)=1,
    b4(Dtilde)=495+66+1=562.

The direct sum is the standard rational blowup decomposition; it is not an assertion that a numerical rank alone determines the maps.

## Second comparison: remove the exceptional node fibers

Purity for the closed smooth codimension-three submanifold T in Dtilde identifies

    H_T^j(Dtilde,Q)=H^(j-6)(T,Q)(-3).

In particular the groups for j=4 and j=5 vanish. The exact localization sequence therefore gives

    H^4(Dtilde,Q) -> H^4(V,Q) is an isomorphism.

Thus b4(V)=562 independently of N. Removing N copies of P^2 does NOT add N degree-four classes. Their first possible supported contribution is in degree six, not five. Purity is applied on the smooth strict transform here, never on the singular D.

## Third comparison: blowup of the smooth locus

The rational blowup formula also holds for the smooth quasi-projective U with its closed smooth codimension-two center Z minus Sigma. It gives

    H^4(V,Q) = H^4(U,Q) plus H^2(Z minus Sigma,Q)(-1).

Removing finitely many points from the smooth threefold Z changes no degree-two cohomology: the supported groups in degrees two and three vanish by codimension-three purity. Therefore H^2(Z minus Sigma)=H^2(Z), and

    b4(U)=562-66=496.

The subtraction is licensed by this actual blowup decomposition, not by an informal count of exceptional fibers.

## Full residue rank and ambient support image

The previously constructed localization sequence is

    0 -> H^4(D,Q) -> H^4(U,Q) -> K_D -> 0,

with H^4(D)=H^4(X) by the affine-complement argument. Hence

    dim K_D=496-495=1,
    K_D=Q r_Z,
    rank gamma=N-1.

Since psi_D(r_Z)=0 for the supplied complete intersection, psi_D vanishes on ALL of K_D. It follows that

    im(H_D^6(X,Q)->H^6(X,Q)) = E cup H^4(X,Q).

The source has dimension496, its image dimension495 and its kernel dimension1. The prior corrected algebraic cycle Z-(k^3/(m q^2))Y supplies a nonzero generator of that kernel. Thus the whole apparent additional residue sector is killed by ambient pushforward in this family, not only one tested residue.

In particular alpha restricts nontrivially to X minus D for every D in this general high-degree family. N may grow cubically in m, but it supplies neither N global residue dimensions nor any extra ambient primitive support direction here.

## Scope and next nonredundant test

This completes the complete-intersection-envelope control. It does NOT exclude all algebraic supports of alpha. Forcing a new arbitrary support into D imposes additional conditions on the linear system, and the resulting divisor need not belong to the generic family just analyzed. Nor is every support a smooth complete intersection.

The calculation suggests a new source-level test: replace Z by an arbitrary supplied smooth codimension-three center, keeping its actual class rather than k^3 E^3. Recheck normal generation, nodality, the two blowup formulas and the residue map. Determine whether the extra ambient direction is precisely the primitive projection of the center class; do not assume it vanishes for an arbitrary algebraic center. This tests which part of the result was really due to the complete-intersection hypothesis, and must retain the unresolved singular-support case.

Verification combines explicit blowup-chart equations and exact degree/rank arithmetic with the written general geometry. Blowup cohomology, relative ampleness, weak Lefschetz and smooth purity are imported standard facts, not mechanically proved by the checker. No numerical high-degree threshold, universal support enumeration, proof-assistant certification or Hodge verdict is claimed.
