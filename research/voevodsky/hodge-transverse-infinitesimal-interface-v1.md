# Embedded first-order lifting and its Hodge image

## Fresh task and the necessary source hypothesis

Execute transverse-cycle-infinitesimal-interface. Let i:Z->X be a SUPPLIED smooth closed codimension-three subvariety of a smooth projective sixfold. Then Z is a smooth threefold and N=N_(Z/X) is a rank-three normal bundle. A first-order deformation of X has Kodaira-Spencer class kappa in H^1(X,T_X).

This hypothesis does not say that alpha has a smooth representative. The imported correspondence cycles and traced Chow classes need not have supplied smooth embedded representatives. The following normal-bundle construction is not silently applied to those unspecified or singular representatives.

## Actual embedded obstruction from local lift comparisons

There is a canonical map

    ob_Z:H^1(X,T_X) -> H^1(Z,T_X|Z) -> H^1(Z,N),

given by restriction and the normal quotient. In a local trivialization of a first-order deformation, lift the defining regular sequence of Z. On overlaps the ambient gluing cocycle representing kappa changes these local lifts by its normal component. These normal components form a Cech one-cocycle representing ob_Z(kappa). Changing the local embedded lifts adds a coboundary.

Consequently ob_Z(kappa)=0 iff the given Z admits an embedded flat lift over that specified first-order deformation. This is a first-order statement; it does not assert that a choice extends to all higher orders.

For a supplied smooth projective family mathcal X->S with central fiber X, the relative Hilbert tangent sequence is exact through T_s S:

    0 -> H^0(Z,N) -> T_(Z,s) Hilb(mathcal X/S)
      -> T_s S --ob_Z composed with KS--> H^1(Z,N).

No surjectivity onto the last group is asserted. No quotient by ambient automorphisms is being taken here: this is the relative Hilbert parameter space, not a moduli space of abstract pairs.

## Semiregularity has a different target

For this smooth embedding the codimension-three semiregularity map is

    sigma_Z:H^1(Z,N) -> H^4(X,Omega_X^2).

Its source and target can be constructed without an assumed injectivity theorem. The conormal filtration gives a canonical map

    Omega_X^4|Z -> N* tensor Omega_Z^3,

since four tangent cotangent factors on a threefold vanish, and the first nonzero quotient has one conormal factor. Restriction on H^2 followed by this map gives

    H^2(X,Omega_X^4) -> H^2(Z,N* tensor K_Z).

Dualizing by Serre duality on X and Z gives sigma_Z (with the usual compatible cycle-class/sign normalization). The standard semiregularity compatibility is

    sigma_Z(ob_Z(kappa)) = kappa contracted with cl(Z)
                         in H^4(X,Omega_X^2).

Here cl(Z) is viewed as its Dolbeault type(3,3) component. Contraction by kappa of bidegree(-1,1) produces type(2,4); thus all degrees match. This compatibility is imported standard deformation/Hodge theory, not proved by a finite matrix fixture.

Therefore a zero first-order Hodge derivative only places ob_Z(kappa) in ker(sigma_Z). It implies actual first-order lifting if sigma_Z is injective, or if the particular normal obstruction is independently shown zero. Injectivity has not been supplied for the unknown cycle witnesses. Higher-order existence would require additional control even after a first-order lift.

## Actual positive control in the polarized family

Take the unchanged fixed X as a fiber of a smooth polarized abelian family with an actual relative polarization line bundle H, after the level/rigidification already allowed. Choose k sufficiently large and three transverse sections of L=H^k on X. Their zero locus Z is a smooth complete-intersection threefold, with class l^3 where l=kE.

Kodaira vanishing on each abelian fiber gives H^j(X,L)=0 for j>0, since K_X is trivial and L is ample. Cohomology and base change therefore make the relative space of sections locally free with surjective restriction to the central fiber. Extend the three chosen sections locally on S. Relative transversality and properness allow shrinking around s so their simultaneous zero locus is a smooth relative threefold.

This is an actual embedded lifting construction for every tangent direction in that polarized family. Hence

    ob_Z(KS(v))=0 for every v in T_s S.

It is not deduced merely from the fact that l^3 stays Hodge. Rather, extending the line bundle and sections explicitly supplies the lift. The argument works for the Weil-family directions as a subfamily of the polarized deformation space. It says nothing about unpolarized directions that fail to extend L.

## The control obstruction group is not zero

Even for this positive lifting control, H^1(Z,N) is large. The Koszul resolution of i_*(L|Z) has terms

    L^(-2), (L^(-1))^3, O_X^3, L

in degrees -3,-2,-1,0. Positive powers have no higher cohomology and negative powers have no cohomology below degree6, by Kodaira and Serre duality. The unique surviving term in total degree1 is H^2(X,O_X)^3; there is no incoming or outgoing nonzero spectral-sequence differential for it. Thus

    H^1(Z,L|Z) isomorphic to H^2(X,O_X)^3,
    h^1(Z,L|Z)=3 binomial(6,2)=45,
    h^1(Z,N)=3*45=135.

Meanwhile

    dim H^4(X,Omega_X^2)=binomial(6,2)binomial(6,4)=225.

The positive lift therefore is not explained by an empty obstruction group. These dimensions alone neither prove nor disprove injectivity of sigma_Z. In particular a nonzero obstruction SPACE is not an obstruction VALUE.

## Application boundary for alpha and for the retained controls

The fixed Weil class alpha remains Hodge throughout the allowed Weil family, so its class-level first-order derivative vanishes in every such direction. If a smooth embedded representative were supplied, the identity above would only show its embedded obstruction lies in the semiregularity kernel. No such representative, obstruction value or injectivity certificate for it is supplied by that identity.

For the theorem-backed signed correspondences and relative Chow classes, one must first choose actual representatives and the appropriate Hilbert or derived deformation interface. Their mere existence does not license replacing their obstruction groups by the normal group of the complete-intersection control. The complete intersection realizes k^3 E^3, not alpha.

## Next bounded calculation

Compute sigma_Z itself for the explicit complete-intersection control, not just its source/target dimensions. Track the three-dimensional space of defining sections through the Koszul identification and compare changes of its basis; determine the actual rank/kernel and how the ambient Kodaira-Spencer obstruction lands in it. This can calibrate the difference between failure of semiregularity injectivity and genuine cycle lifting on an already algebraic input, without pretending to settle the unknown correspondence representatives.

Verification retains the written Cech obstruction construction, dual semiregularity map and actual section extension, alongside exact cohomological-degree/dimension and linear-kernel controls. The standard geometric theorems are imported, not proof-assistant certified. No transverse realization of alpha or Hodge verdict is claimed.
