# Traversal step 1: fixed volume dictionary and a nonsingular test

Fresh input: the versioned-source conflict in `triangle-primary-reconciliation.md`. Fix ordinary Euclidean volumes rather than treating every displayed source equality as a definition simultaneously.

For a base triangle and its tetrahedron, let G2,G3 be Gram determinants, D the squared Euclidean triangle area and K the squared Euclidean tetrahedral volume. For raw distance-matrix Cayley–Menger determinants:

    G2=4D; signed_CM2=-CM2=4G2=16D;
    G3=36K; CM3=8G3=288K.

These are exact determinant identities. Source formulas omitting these factors cannot be read as literal equalities in this dictionary without an explicit conversion.

## Compact nonsingular control

Take base points(0,0,0),(2,0,0),(1,3,0). Use the two Cartesian boxes X,Y in[0,1], Z in[1,2] or[-2,-1]. They have total volume2. On the positive sheet D=9,K=Z^2, and the pullback of r dr s ds t dt is6Z dX dY dZ. The Euclidean distance density, including both sheets, is1/(3Z), so its pullback is exactly2. Its integral over the positive unit box is therefore2, matching Cartesian volume with no quadrature or boundary limit.

This patch stays away from K0. Choose positive external energies if attaching rational source denominators; no singularity is needed to distinguish the measures.

Under an ordinary-volume interpretation of v3's specific eq3.11, its density is16/sqrt(pi) times Euclidean density, and its patch integral at d3 is32/sqrt(pi), not2. Multiplication by sqrt(pi)/16 explicitly converts that convention to the Cartesian benchmark. This is a declared normalization map, not a correction silently imposed on the source.

The old printed measure and the literal raw-CM appendix(A.12) both tend to zero on this compact patch as epsilon→0. They therefore cannot be reconciled with the Cartesian benchmark by a factor regular and nonzero at epsilon0. No endpoint divergence or continuation prescription can account for the discrepancy on this test.

## Appendix conversion kept distinct

Retaining its raw CM symbols and its product d(y_e^2), appendix(A.12) gives, relative to the Cartesian density,

    mu_appendix/mu_geom
      = [2sqrt(2)/sqrt(pi)] * 2^epsilon
           * Gamma(epsilon+1/2)/Gamma(epsilon).

The factor8 from product d(y_e^2)=8 product(y_e dy_e) is essential. The ratio still vanishes linearly at epsilon0; converting raw CM to ordinary volumes does not remove its shifted Gamma denominator.

Thus the geometric dictionary is now fixed, and the primary formulas have distinguishable normalized meanings. The author's intended common formula and physical continued cycle remain unsettled. We can proceed with a transparently defined Euclidean benchmark, but cannot label it the frozen printed period without its conversion factor.

## Verification and next step

`check_triangle_volume_dictionary.py` passes27 exact determinant/Jacobian fixtures and checks the constant pullback density underlying the exact volume2 test. Gamma limits and printed-formula conversions are written analysis. Receipt: `triangle-volume-dictionary.json`.

Next: transport the existing conditional local period through the explicit old-to-Euclidean measure ratio and reassess its regulator boundary. Do not carry over its finite coefficient unchanged.
