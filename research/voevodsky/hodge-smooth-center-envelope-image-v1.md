# General smooth centers: the envelope retains the center's primitive class

## Fresh task and hypotheses

Execute smooth-center-envelope-image. Let Z be ANY supplied smooth connected closed algebraic threefold in the fixed smooth projective sixfold X. No complete-intersection or polarization-class hypothesis is made about Z. Fix H with c1(H)=E and let N=N_(Z/X), a rank-three bundle. The smooth-center hypothesis is essential throughout; no smoothability of arbitrary cycles is assumed.

For a general sufficiently high-degree D in |I_Z tensor H^m| we prove

    im(H_D^6(X,Q)->H^6(X,Q))
      = E cup H^4(X,Q) + Q cl_X(Z).

This is a source-specific formula. It is NOT universal annihilation of the second summand.

## Normal generation and generic nodes still work

Smoothness of Z makes I/I^2=N*. The sequence

    0 -> I^2 tensor H^m -> I tensor H^m -> N* tensor H^m|Z -> 0

and Serre vanishing supply surjectivity on global sections for m sufficiently large. The last bundle and I tensor H^m are globally generated for large m. The same generic-smoothness and Bertini arguments as in the complete-intersection control give isolated transverse normal zeros on Z and smoothness of D away from Z.

Write e=E|Z. The node count is now

    n(m)=integral_Z [m^3 e^3 - m^2 e^2 c1(N)
                          + m e c2(N) - c3(N)].

This is c3(N* tensor H^m|Z), obtained by multiplying (m e-n_i) for the formal Chern roots n_i of N. Its leading coefficient integral_Z e^3 is strictly positive by ampleness, so n(m)>0 for sufficiently large m. Neither the lower coefficients nor a numerical threshold are assumed known.

At each transverse normal zero the coordinate change (x,y)->(g(x,y),y) still puts the pair in the form sum x_i y_i=0, Z:y=0. Thus the singularities are ordinary double points, and the local ruling-plane residue of Z is nonzero at every node. This uses no splitting of N into line bundles.

## Both blowup comparisons, with b2(Z) left unknown

Blow up X along Z. For sufficiently large m the strict transform Dtilde is a smooth ample divisor in this smooth blowup. Its degree-four cohomology is

    H^4(Dtilde)=H^4(X) plus H^2(Z)(-1) plus H^0(Z)(-2).

The connected center gives b0(Z)=1; b2(Z) is NOT replaced by b2(X). The node fibers are P^2 of codimension three in Dtilde. Removing them preserves H^4 by smooth purity. The remaining space is the blowup of U=D minus Sing(D) along Z minus Sing(D), a smooth codimension-two center, and has cohomology

    H^4(V)=H^4(U) plus H^2(Z minus Sing(D))(-1).

Removing finitely many points from the smooth threefold Z preserves H^2. Consequently the unknown b2(Z) cancels:

    b4(U)=[b4(X)+b2(Z)+1]-b2(Z)=b4(X)+1=496.

The affine-complement weak-Lefschetz argument still gives H^4(D)=H^4(X), hence dim K_D=1. The actual nonzero residue r_Z spans K_D. None of these facts depended on Z being a complete intersection.

## The global map is the center class, not automatically zero

Let h_Z in H^4(U) be the class of the supplied Z minus Sing(D). Naturality gives

    res(h_Z)=r_Z,
    Phi_D(h_Z)=cl_X(Z).

With P=H^6(X)/(E cup H^4(X)), the well-defined quotient map therefore satisfies

    psi_D(r_Z)=cl_X(Z) modulo E cup H^4(X).

Since r_Z spans K_D, this proves the advertised FULL image formula. Let epsilon be 0 if this quotient class is zero, and 1 otherwise. On the fixed sixfold:

    dim source H_D^6(X)=496,
    rank support image=495+epsilon,
    dim support kernel=1-epsilon.

The complete-intersection control had epsilon=0 precisely because its center class was k^3 E^3. Setting epsilon=0 for arbitrary smooth algebraic centers would be an additional unproved theorem, not a consequence of nodality or blowup coherence.

For clarity a genuine primitive representative of the quotient can be defined using hard Lefschetz:

    P_prim(v)=v-L (L^2|H^4)^(-1)(L v),  L=E cup -.

This has L P_prim(v)=0 and kernel L H^4. On the fixed rational Hodge space it is the already retained projection to QR plus QI. If cl(Z)=aE^3+bR+cI, the envelope's extra direction is precisely Q(bR+cI). Effectivity gives a>0, but does not force b=c=0. In particular the envelope construction has not evaluated those two coefficients for a new center.

## Controls and scope

For the actual complete intersection, N=(H^k|Z)^3, the general count reduces to 2160 k^3(m-k)^3, and the primitive image is zero, recovering the prior theorem. In the finite linear checker a formal vector E^3+R instead gives a nonzero extra direction: this is a hostile against silently setting every center's primitive component to zero, NOT an assertion that such a smooth center exists on the fixed X.

The general formula shows that the constructed envelope does not create a new independent obstruction to the supplied center's class. It transfers that class's existing primitive part through a one-dimensional residue source. A nonzero psi value would be compatible with the center already being algebraic, not evidence against its algebraicity.

## Next executable source interface: singular cycles via proper maps

The classical cycle domain also contains singular irreducible threefolds and signed unions. They cannot be replaced by smooth embedded centers without proof. The next bounded task is instead to use a projective resolution f:Y->Z followed by Z->X and type the proper pushforward of the smooth source fundamental class. Check exceptional contributions and compare this map with the embedded-center construction on an explicit singular algebraic control. Resolution gives a smooth source mapping to X, not automatically a smooth subvariety of X; the distinction must remain visible.

Verification combines the written normal-generation, blowup and cycle-map arguments with exact Chern-root polynomial expansion and two-branch image/kernel arithmetic. Standard resolution is only proposed for the next task. No universal smoothability, all-cycle annihilation, proof-assistant certification or Hodge verdict is claimed.
