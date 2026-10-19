# Global iteration 34 (fourth series 3/10): the full-Hochschild criterion failure persists to the standard eightfold construction

## Result and scope

Under iterations32-33's explicit transverse-incidence hypotheses, let E be the corrected d=9 source perfect complex on the auxiliary abelian fourfold A0. Set

    P=E external_product E_dual on A0 x A0.

The kernel of the trace/semiregularity map on the image of Hochschild evaluation for P has dimension **at least four**. This failure persists through Fourier-Mukai equivalence, shifts, line-bundle twists and derived duality. It also persists under an actual finite etale abelian-isogeny descent, if a descended object and its pullback identification are supplied, and under finite etale isogeny pushforward.

Consequently these standard operations cannot make this corrected pair satisfy the full-HH2 weaker criterion. This closes a bounded repair strategy, not every secant construction, every deformation theorem or any Hodge-class question. In particular, we have not constructed a matching target or shown that every ordinary complex-structure deformation is obstructed.

## 1. What the retained primary text actually constructs

Freshly inspected Markman arXiv:2509.23403v2, PDF p16, section9/Corollary9.2, uses an Orlov equivalence from D(A0 x A0) to D(A0 x dual(A0)) applied to an external product of two secant sheaves. Section11.2, PDF p18, uses a factor and a derived-dual factor, a shift and then further sheaf/equivariance arguments in the proved genus-three case. These pages are available in the already pinned full survey PDF; the source's genus-three sheaf/concentration theorem is not applied in dimension four.

Our theorem below does not need the equivalence's cohomological matrix. It applies to **any** such Fourier-Mukai equivalence and any shift or line twist, whether or not the transformed corrected pair has been shown concentrated in one degree or of nonzero rank. If a proposed transform does become a sheaf, the same criterion failure still applies.

## 2. External products preserve, and here double, the kernel

For a perfect complex F on a smooth proper variety, use

    ev_F:HH2 -> Ext2(F,F),
    sigma_F composed with ev_F = action_on_ch(F).

Suppose xi annihilates ch(F), but w=ev_F(xi) is nonzero. For any nonzero perfect G, pull xi to the first factor. On F external G its evaluation is w external id_G, while its Chern-character action is zero. The Kunneth isomorphism

    Ext*(F external G,F external G)
      = Ext*(F,F) tensor Ext*(G,G)

makes w external id_G nonzero and preserves independence of a family of w's. The identity of a nonzero object is nonzero. This assertion does not assume its Chern character is nonzero.

Iteration33 supplies two independent w's for E. It also applies to E_dual. Explicitly,

    ch(E_dual)=1-3t-(9/2)t^2+(9/2)t^3+(27/8)t^4

has the same recurrence c_(q+2)(q+2)(q+1)=-9c_q. The compensated bivectors (9 gamma_beta,0,beta) still annihilate it. Dualizing the normalized-node model transposes the differential with the usual Hom-complex signs; the antisymmetrized derivative compositions are the same nonzero columns [2,0]^t and [0,-2]^t, up to the universal HKR scalar. Thus there are two independent evaluated trace-kernel classes in each factor.

For P, the first two classes lie in Kunneth bidegree(2,0), and the other two in bidegree(0,2). These are distinct direct summands even if other Ext degrees are nonzero. Therefore they are independent, proving the lower bound four. We do not infer an exact dimension of global Ext2 or of the whole trace kernel.

The checker verifies both dual character compensation and local derivative matrices, plus a four-column Kunneth independence control. That finite coordinate control illustrates the direct-summand argument; it does not replace Kunneth or compute an unknown global Ext algebra.

## 3. Equivalences and elementary autoequivalences cannot repair the full criterion

A Fourier-Mukai equivalence transports Hochschild cohomology, its action on objects, categorical Chern characters in Hochschild homology, and the evaluation maps. These are isomorphisms. On abelian varieties Todd=1, so HKR identifies the action/trace diagram with the ordinary Hodge-cohomology diagram used here. The transported xi still has zero character action and nonzero evaluation. Independence and hence the lower bound four survive.

Tensoring by a line bundle and shifting are equivalences; the Hochschild directions themselves must be transported, not held fixed in an unrelated HKR marking. Derived duality is the corresponding contravariant equivalence: the Atiyah/trace duality signs are invertible and preserve the failure. The explicit dual calculation above independently checks the source pair.

For any Fourier-Mukai equivalence Phi between the relevant abelian eightfolds, any line bundle L and integer r,

    K=Phi(P)[r] tensor L

therefore fails the full-HH2 weaker criterion. This is a categorical assertion about K, not proof that K is a sheaf, a Weil-cycle source deforming to Y2, or an object with the source paper's other hypotheses.

## 4. Finite etale abelian isogenies: both genuine descent and pushforward

Let p:B->C be a finite etale isogeny of complex abelian varieties. Pullback on each Hodge-cohomology group is an isomorphism over C. The etale tangent identification likewise makes

    p*:HH2(C) -> HH2(B)

an isomorphism. This follows from translation-invariant forms/tangent fields and invertibility of the isogeny differential, not from a claimed functorial Hochschild pullback for arbitrary morphisms. The checker tests diagonal isogenies on elliptic products as positive controls; they are not an enumeration of all isogenies. For eightfolds dim HH2=28+64+28=120.

**Actual descent:** suppose K=p*D has been supplied, with an actual object D and an isomorphism p*D~K. For every kernel witness xi for K choose eta=(p*)^-1 xi. Naturality gives

    p*(ev_D(eta))=ev_K(xi).

Nonzero and independent evaluations on K imply nonzero and independent evaluations on D. The character action for D vanishes since its pullback is zero and Hodge pullback is injective. Thus D still fails the criterion, with the same lower bound. A declaration that a quotient exists or a group acts is not a supplied descent; no new descent existence is asserted.

**Pushforward:** for any K on B, the finite etale base-change identity gives

    p*p_*K = direct_sum_{g in ker(p)} t_g* K.

Translations act trivially on Hochschild and Hodge cohomology. Hence a witness xi for K annihilates the character of every translate, and evaluates block-diagonally on the sum, nontrivially on the identity translate. The witnesses stay independent there. Lift xi back to eta on C as above. Pullback of ev_(p_*K)(eta) is the displayed nonzero block action, while character vanishing descends by injectivity. Therefore p_*K also fails the criterion. This argument does not assume K is equivariant.

This covers genuine finite etale abelian-isogeny descent/direct image of the specified object. It does not admit arbitrary quotients, ramified maps, unrelated equivariant categories or arbitrary direct summands. Such changes may require different data and separate proofs.

## 5. Research consequence and continuation

The repaired character alone was insufficient at iteration31. The local source criterion fails at iteration33. We can now reject the attempt to fix that failure merely by the standard external-product/Orlov/shift/dual/line-twist construction, or genuine finite etale isogeny descent/pushforward. This includes a pair of translates or Picard-zero twists of the same corrected source, by functoriality.

This does **not** refute Question11.4: its conditional theorem could still be true for objects satisfying its hypothesis. Nor does this test rule out algebraicity by a deformation theorem restricted to a smaller commutative locus; the exhibited source witnesses involve bivectors and B-fields, not just ordinary complex-structure directions. A different object or a different theorem remains a real research task, not an automatic rescue.

Prioritize a genuinely different source, a justified restricted-deformation argument, or the parallel ramified generalized-Prym route. In the latter route the pending Lange-Ortega/addendum/action hypotheses and actual period/isogeny matching remain executable. Direct cycles and actual theta data remain available. The original X, alpha, Y2, determinant48i, all four transfer channels and prior target censuses are unchanged.

## Verification and boundaries

Contract: `research/conjecture_net/contracts/hodge-secant-criterion-persistence.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_secant_criterion_persistence.py`.
Receipt: `research/voevodsky/results/hodge-secant-criterion-persistence-v1.json`.

Written mathematical imports: Kunneth for perfect complexes on smooth proper varieties; categorical Chern/action naturality for Fourier-Mukai equivalences; derived duality; finite etale base change and translation-invariant cohomology on abelian varieties. Exact arithmetic and proof-hypothesis controls are not proof-assistant certification or independent review. Product Euler pairing1679616 is a numerical control, not an Ext dimension. The prior source-failure receipt is consumed freshly. Iteration33 and pins v1-v35 are preserved. No target object/isogeny, exceptional algebraic cycle, actual geometric obstruction value, all-cycle theorem or Hodge verdict is supplied.
