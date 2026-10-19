# Global iteration 19 (new series 9/10): hyperelliptic bottom obstruction and bielliptic descent

## Result

A connected smooth etale cyclic-quartic cover C17->C5 with **hyperelliptic genus-five bottom C5** has primitive Prym P=Prym(C17/C9) isogenous to Q x Q for an abelian fourfold Q. It cannot be isogenous to the fixed A=X x B, because A contains the simple sixfold X.

This excludes this cover family for **every model in the fixed unpolarized A isogeny class**, including Y and Y2, not merely for one principal polarization or Gaussian marking. It does not exclude nonhyperelliptic bottoms, arbitrary Pryms, ramified/singular covers, or unrelated correspondences from larger varieties.

Separately, if a proposed Y2 cyclic-quartic realization has a **bielliptic genus-nine intermediate C9**, its free involution descends to a nonzero two-torsion translation on the elliptic quotient. Therefore the bottom C5 is bielliptic, and C9->C5 is a pullback of an elliptic two-isogeny. This is conditional; in particular the actual theta-singularity dimension remains unknown.

The preceding audit excluded hyperelliptic C9 by a different argument. It explicitly made no assertion about C5. The new proof below treats C5 directly; old receipts and source pins are not retrospectively changed.

## 1. A pointed hyperelliptic involution lift really has square one

Suppose pi:C17->C5 is a connected etale cyclic cover with deck generator rho of order four, and let iota be the hyperelliptic involution of C5. Choose a Weierstrass point w and a point wtilde above it.

The relation p+iota(p)~2w shows iota acts as minus identity on Jac(C5), hence on H1(C5,Z). A connected cyclic-four cover is given topologically by a surjective character

    chi:pi1(C5,w)->Z/4.

It factors through H1, so chi composed with iota_* equals -chi. In particular ker chi is preserved. The pointed covering-space lifting theorem gives a unique lift sigma of iota fixing wtilde. It is holomorphic because pi is an unramified holomorphic local isomorphism, hence algebraic for these projective complex curves.

Since iota^2=Id, sigma^2 is a deck transformation. It fixes wtilde; deck transformations of a connected etale cover act freely on each fibre, so sigma^2=Id. The lifted action on the deck group gives

    sigma rho sigma=rho^-1.

Thus this is the dihedral lift, not an unverified extension whose lift might square to rho^2. Equivalently, on a four-point fibre all permutations conjugating the regular four-cycle to its inverse are reflections and square to identity. The checker enumerates all four.

Etaleness and the pointed fixed Weierstrass fibre matter. We do not apply this argument to ramified covers, where a nontrivial deck element can fix a point. We do not assert a general involutive lift for arbitrary base involutions or arbitrary covering groups.

## 2. The primitive Prym is a square up to isogeny

Put h=rho^2. On the primitive Prym

    P=ker(1+h)^0=im(1-h),

h acts exactly as -Id. The lift sigma commutes with h, so preserves P. Its restriction and rho satisfy

    rho^2=-Id, sigma^2=Id, sigma rho=-rho sigma.

Let P_+=im(1+sigma), P_-=im(1-sigma), connected abelian subvarieties of P. Their sum is P because the sum of the two endomorphisms is [2], which is surjective. Their intersection is killed by two. Addition P_+ x P_-->P is therefore an isogeny, not an asserted isomorphism of principal polarizations.

The relation rho(1+sigma)=(1-sigma)rho shows rho maps P_+ isomorphically onto P_-. As dim P=8, each has dimension four. With Q=P_+, P is isogenous to Q x Q.

The rational idempotents (1+sigma)/2 and (1-sigma)/2 give the same decomposition. The finite matrix control verifies both idempotent identities and rho-intertwining, with H1 ranks eight and eight. It is a representation control, not an actually supplied fourfold Q or a target curve tower.

## 3. Why no compatible polarization or isogeny can repair this family

The retained fixed-point proof gives End^0(X)=Q(i), so X is simple of dimension six. Any homomorphism from X to a fourfold is zero: a nonzero image of a simple abelian variety would have dimension six, exceeding four.

Thus Hom(X,Q x Q)=0. But if P were isogenous to A=X x B, there would be a nonzero homomorphism X->P by composing the inclusion with an isogeny. Contradiction.

This obstruction is independent of the Prym principal polarization and of how Q(i) is embedded. It excludes the primitive Prym of the stated hyperelliptic-bottom cover family throughout the fixed A isogeny class. It does not assert that the entire A isogeny class avoids all Pryms. Nor does it rule out arbitrary cycle correspondences from such Pryms or from higher-dimensional sources.

## 4. If C9 is bielliptic, its involution is unique

Now suppose a smooth cyclic-quartic realization in the fixed class has a bielliptic intermediate C9. Write kappa:C9->E for its degree-two elliptic quotient, with deck involution b. Let eta be the free involution defining C9->C5.

A genus-nine curve cannot have two different bielliptic involutions. If the associated degree-two maps to E1 and E2 were distinct, their joint image would be birational: a common degree-two factor would identify the two function subfields and hence the involutions.

For a curve image D in E1 x E2 with projection degrees (2,2), surface adjunction and **Hodge index** give genus at most five. Here is the necessary numerical detail. Let F1,F2 be fibre classes and D0=2F1+2F2. D-D0 is orthogonal to both fibres, hence to the ample class F1+F2, so (D-D0)^2<=0. Therefore D^2<=D0^2=8. The canonical class of the product is zero, and p_a(D)=1+D^2/2<=5. Its normalization has genus at most five, contradicting nine.

It would be wrong to assert that every product of elliptic curves has Neron--Severi rank two or that D^2 always equals eight; the Hodge-index inequality handles possible mixed classes. This uniqueness argument only applies above genus five; it does not claim uniqueness of a bielliptic involution on the bottom C5.

Uniqueness implies eta commutes with b, since conjugating b by eta gives another bielliptic involution. Thus eta descends to an involution eta_E on E.

## 5. Elliptic descent is necessarily a translation

The induced eta_E is nontrivial. Otherwise eta would be a deck automorphism of kappa, hence equal to b; but b has sixteen fixed points by Riemann--Hurwitz, whereas eta is free.

A nontrivial involution of a complex elliptic curve is either a translation by nonzero two-torsion, or minus identity followed by a translation. The latter has four fixed points and quotient P1. In that case the commuting involution square induces a degree-two map

    C5=C9/<eta> -> E/<eta_E>=P1,

making C5 hyperelliptic. Section 3 excludes that case for a realization in the fixed A isogeny class.

Consequently eta_E is a nonzero two-torsion translation. Its quotient is an elliptic two-isogeny E->Eprime, and there is a cartesian square

    C9 --kappa--> E
     |            |
     v            v  etale degree two
    C5 --kappa0-> Eprime.

The lower map has degree two, so C5 is bielliptic, with eight branch points. The square is cartesian: E is not a subfield of C(C5) over Eprime, since that would factor the degree-two kappa0 through a two-isogeny and force a degree-one map C5->E. Therefore the combined function field is C(C9). The elliptic isogeny is etale, so the fibre product is smooth; its connected normalization is C9.

This conclusion follows whenever the intermediate is bielliptic. In particular it is necessary in the previously identified **conditional** case dim Sing theta2=4. Neither biellipticity nor that actual dimension has been established for a supplied realization.

## 6. A precise conditional cover family and finite level data

The remaining bielliptic-intermediate case can be searched using the following data:

1. an elliptic curve Eprime and a smooth degree-two cover kappa0:C5->Eprime, branched at eight points; equivalently a degree-four line bundle M and a section of M^2 with simple zeros;
2. nonzero zeta in Pic0(Eprime)[2], defining E->Eprime;
3. eta=kappa0* zeta in Pic0(C5)[2], and an exact-order-four line bundle L with L^2=eta.

Eta is nonzero: a trivial pullback would lift kappa0 through the two-isogeny, forcing a degree-one map from the genus-five curve to an elliptic curve. Set C9=C5 x_Eprime E. A trivialization of L^4 defines the connected etale cyclic-quartic cover C17 with intermediate C9; Riemann--Hurwitz gives genera 17,9,5. This is a geometric construction **given the data**, not a cover matched to Y2.

Over a marked abstract group Pic0(C5)[4]~(Z/4)^10, fix eta=(2,0,...,0). The equation 2L=eta has 2^10=1024 roots, all exact order four. Inversion L->L^-1 has no fixed roots and gives 512 pairs. The checker enumerates the complete marked root set.

These are abstract level labels, not actual algebraic torsion coordinates on a supplied C5. The 512 pairs are not an unmarked cover-moduli count: automorphisms of a base curve can give further identifications. No dimension-of-moduli shortcut excludes the specific exponential-period target. The elliptic quotient Eprime has not been forced to be the CM elliptic curve of the target factors.

## 7. Frontier and verification boundary

The hyperelliptic **bottom** route is now closed even up to isogeny. Nonhyperelliptic-bottom cyclic covers and other Prym geometries remain open. The conditional bielliptic branch has a concrete elliptic-pullback and torsion-root description, but no theta dimension, actual curve matching Y2, algebraic exceptional cycle, all-cycle theorem or Hodge verdict has been supplied. The four f-pullback channels remain the acceptance test for any proposed eightfold cycle.

The old genus-nine low-gonality exclusions and the new genus-five argument are distinct; neither is silently substituted for the other. All three unrestricted research obligations and independent review remain open.

Contract: `research/conjecture_net/contracts/hodge-hyperelliptic-bottom-audit.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_hyperelliptic_bottom_audit.py`.
Receipt: `research/voevodsky/results/hodge-hyperelliptic-bottom-audit-v1.json`.

    python research/voevodsky/checkers/check_hodge_hyperelliptic_bottom_audit.py

This is an original written complex-cover argument using standard covering-space lifting, Jacobian functoriality, abelian image/isogeny decomposition, Poincare complete reducibility, surface adjunction and Hodge index. It does not claim a new exhaustive literature audit. The exact finite group, matrix, genus and marked-level controls do not formally prove those imports or constitute independent review. The iteration-18 predecessor and pins v1-v19 are retained unchanged.
