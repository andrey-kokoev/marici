# Nodal links and the two global maps before an ambient support class

## Fresh source and degrees

Execute nodal-link-localization-control for a general sufficiently high-degree envelope D from the normal-jet construction. D is an ample complex five-dimensional divisor in the fixed smooth sixfold X, with N ordinary double points Sigma and no other singularities. Put U=D minus Sigma. All groups below have rational coefficients. This is ordinary topology and Borel-Moore homology; no untracked mixed-Hodge twists are used to assert algebraicity.

## The link of the actual node

The local equation is q(z)=z_1^2+...+z_6^2=0 in C^6. Writing z=x+i y and intersecting a small Euclidean sphere gives

    |x|=|y|, x dot y=0.

After rescaling, (x,y) is an ordered orthonormal two-frame in R^6. The real nine-dimensional link K is therefore V_2(R^6), the unit tangent sphere bundle of S^5:

    S^4 -> K -> S^5.

The Euler class of TS^5 is zero, since its integral is chi(S^5)=0 and H^5(S^5,Z)=Z. The oriented sphere-bundle Gysin sequence gives

    H^j(K,Q)=Q for j=0,4,5,9,
    H^j(K,Q)=0 otherwise.

A small neighborhood is a cone on K. Consequently local cohomology H^i_{p}(D,Q), or relative cohomology of this neighborhood and its puncture, is reduced H^(i-1)(K,Q). Its only nonzero degrees are

    i=5,6,10, each of rank one.

In particular the local degree-five term is nonzero. Treating the node as a smooth point of a real ten-manifold would miss it. The node link is not a rational nine-sphere.

## Local-to-global localization, without independence assumptions

Excision and the finite singular locus identify H^i_Sigma(D) with the direct sum of these local groups. The relevant exact sequence is

    0 -> H^4(D) -> H^4(U) --res--> Q^N
      --gamma--> H^5(D) -> H^5(U) -> Q^N -> H^6(D) -> ... .

The two displayed Q^N terms have different cohomological degrees: they are H^5_Sigma(D) and H^6_Sigma(D). They must not be identified merely by their dimensions. Define K_D=ker(gamma). Then

    0 -> H^4(D) -> H^4(U) -> K_D -> 0.

Thus the extra H^4 classes on the smooth locus are measured by K_D, not by the number N of nodes. No rank of gamma for the actual D is computed here.

## Why H^4(D) is still ambient, despite the singularities

The complement X minus D is smooth affine of complex dimension six: D is ample and effective. Its homology vanishes above real degree six by the affine/Stein CW-dimension theorem. Poincare duality gives H_c^j(X minus D)=0 for j<6. The relative sequence for (X,D), with H^j(X,D)=H_c^j(X minus D), therefore implies

    H^4(X) -> H^4(D) is an isomorphism.

This is the needed weak-Lefschetz statement even for singular D. It does NOT give Poincare duality on D or allow one to replace H^4(U) by H^4(D).

## Support duality uses the smooth locus, not false purity on D

Since Sigma is finite, its Borel-Moore groups in degrees six and five vanish. Borel-Moore localization and ordinary Poincare duality on the smooth real ten-manifold U yield

    H_D^6(X) = H_6(D) = H_6^BM(U) = H^4(U).

Here compactness of D identifies ordinary and Borel-Moore homology on D. The isomorphism H_6(D)->H_6^BM(U) is restriction to the open subset, not a proper pushforward from U.

Define Phi_D:H^4(U)->H^6(X) by these identifications followed by the proper pushforward D->X and ambient duality. On the subspace coming from H^4(X), the cap-product projection formula gives

    Phi_D(i* eta restricted to U)=m E cup eta.

Thus its image contains L H^4(X), where L is cup product with E. Let

    P=H^6(X)/(L H^4(X)).

For r in K_D choose a preimage h in H^4(U) and set

    psi_D(r)=Phi_D(h) modulo L H^4(X).

This is well defined: two choices differ by H^4(D)=H^4(X), whose images are m L H^4(X). It follows that

    im(Phi_D)/(L H^4(X)) = im(psi_D:K_D->P).

There are TWO filters: membership in ker(gamma), and survival under psi_D. Even a nonzero global residue relation need not produce a nonzero ambient primitive support class.

For the fixed abelian sixfold, b4=binomial(12,4)=495 and b6=binomial(12,6)=924. Hard Lefschetz makes L injective on H^4, so dim P=429. Hence the extra support rank is bounded by min(dim K_D,429), not N. This is the full rational cohomology quotient. Its fixed rational Hodge subquotient is the two-dimensional Weil plane, but no claim is made that every element of K_D gives an algebraic class or a nonzero Weil component.

## What this establishes and what it leaves open

The support image of this nodal divisor is an actual, typed map, and the local ranks and global exact sequences are determined. The rank of gamma, the values of psi_D and membership of alpha in this image remain uncomputed. Even support on a divisor is not the same condition as support on an algebraic threefold. In particular the earlier top-homology basis theorem for codimension-three supports cannot be applied to this codimension-one D.

Next bounded test: take the known algebraic threefold Z already contained in D. Compute its local residue at a node using a maximal isotropic three-plane in the quadratic cone (equivalently a ruling plane on the projective quadric). Compare the resulting global residue vector with its ambient class k^3 E^3. This can supply an actual nonzero residue relation killed by psi_D, rather than merely a formal possibility. Do not infer that all residues or all potential supports behave like this one control.

Verification: sphere-bundle Gysin ranks, cone degree shift, a finite exact-sequence fixture with both global filters, and ambient dimension counts. The geometric link identification, duality, affine CW theorem and cap-product naturality are written/imported topology, not proved by finite rank tests. No proof-assistant certification or Hodge verdict is claimed.
