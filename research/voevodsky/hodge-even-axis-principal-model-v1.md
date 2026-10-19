# Global iteration 39 (fourth series 8/10): an actual even-axis principal model Y3 with cycle transfers

## Result

Keep the fixed X, alpha=R6 and Y2 unchanged. Construct a **new auxiliary** principally polarized Gaussian eightfold Y3, with an actual isogeny

    q:Y2->Y3, deg(q)=256, q*theta3=2theta2.

The elliptic isotypic surface remains an actual product, but its physical CM polarization degrees are now **4 and6**. More strongly every connected elliptic subvariety of Y3 has even theta degree at least4. Y3 is indecomposable as a ppav. Thus the particular odd-axis and degree-two-axis obstructions used for Y2 do not apply to Y3.

This is not a Prym-membership proof. Even degrees are necessary controls, not sufficient geometry. No matched cover, exceptional cycle or theta-singularity dimension is supplied.

The composite F3=q f2 from A=X x B has Gaussian determinant768i and degree589824. The phase-correct cycle transfers have denominator768, and all four exceptional reverse channels are transported explicitly. This makes testing cycle constructions on Y3 a licensed continuation, rather than an untracked change of the fixed candidate.

## 1. Four same-sign Hadamard lattice blocks

Use Y2's existing Gaussian marking, with

    d=(1,1,1,-1,-1,-1,1,-1).

Pair the coordinates, in one-based labels, as

    (1,2), (3,7), (4,5), (6,8).

Every pair has the same Hermitian sign. On each put H=[[1,1],[1,-1]], and let Q be the direct sum of these four blocks, with the indicated coordinate interleavings. Set the new lattice basis relative to the old one to H/2 on each pair. Since H^2=2Id, the old lattice lies in the new lattice, the quotient is killed by2, and

    det_K(Q)=(-2)^4=16, index_Z=Norm(16)=256.

Keep the **same underlying physical complex structure**, and scale the old Riemann form by2. In each new basis block,

    (H/2)^t (2 sign*Id) (H/2)=sign*Id.

Thus the new alternating form is integral and unimodular, of type(1,1) and positive. Riemann's theorem supplies a ppav Y3. The identity of the physical vector space induces the holomorphic, hence algebraic, isogeny q, represented by Q in the new markings. It has q*theta3=2theta2. Native multiplication by i remains holomorphic, lattice-preserving and polarization-preserving, with signature(4,4).

Q is **not** asserted to be an endomorphism of Y2. It need not commute with its old marked complex structure. The complex structure in the new marking is Q J2 Q^-1. This lattice change does not invent a forbidden homomorphism from X to an elliptic factor.

## 2. No hidden elliptic gluing; both axes get even degrees

Iteration37 saturated the entire elliptic-isotypic lattice of Y2, with Gaussian generators

    b_plus=e1-e7,
    b_minus=(1-i)e6+e8.

The new isogeny sends them to

    Q b_plus=e1+e2-e3+e7,
    Q b_minus=(2-i)e6-i e8.

Their supports are disjoint and each column contains a Gaussian unit. Consequently integrality forces each parameter separately to lie in Z[i]; the full joint lattice is saturated, with no mixed cancellation. The quotient kernel meets this elliptic surface trivially, not just its two axes separately. Hence q restricts to an isomorphism on the actual elliptic product.

The old theta degrees2,3 therefore double to4,6. The native Gaussian Hermitian restriction is diag(4,-6); in physical holomorphic CM coordinates the positive form is diag(4,6). The two axes are still square-lattice elliptic curves. Relative to the original E_+,E_- in A, their composite isogeny degrees remain1,2; equivalently 4*1/1=4 and4*3/2=6 from F3*theta3=4E_A.

The explicit half-Gaussian residue controls give axis kernel orders(1,1) at this step. They are complete since ker(q) is killed by2. The disjoint unit-column argument additionally proves saturation of the whole surface, not an assumption from separate axis counts.

The choice of pairings matters. Pairing coordinates(1,7) together instead would send b_plus to a column divisible by2, giving step axis kernel order4 and a degree-one elliptic curve. The checker retains this bad-pairing control; not every two-primary quotient fixes the earlier problem.

## 3. Every elliptic theta degree is even and at least4

The fixed X is simple of dimension6 and has no elliptic factor. Thus every connected elliptic subvariety of Y3 lies in its intrinsic elliptic-isotypic surface, now the actual product E_i x E_i just computed.

A rational complex line defining an elliptic subvariety of this product is a K-line. Its saturated intersection with Z[i]^2 is a rank-one Gaussian module. Since Z[i] is a PID, choose a primitive vector(a,b) in Z[i]^2. The resulting map E_i->E_i^2 is an embedding: Bezout for a,b proves its parameter lattice is exactly Z[i]. Conversely this describes every connected elliptic subvariety. Its theta degree is

    d(a,b)=4 Norm(a)+6 Norm(b).

For any nonzero vector this is even and at least4. In particular there is no degree-one, degree-two or odd-degree elliptic subvariety, whether or not it is invariant under the native Gaussian action. This is a universal lattice/PID argument, not a finite enumeration of all elliptic curves. The finite coefficient controls test the quadratic expression only; nonprimitive vectors are not counted as distinct embedded curves.

The standard physical unitary restriction with weights(4,6) again preserves the two axes, but there is now no odd degree to contradict the cyclic action. In the standard zero/two-branch cyclic-quartic cases the selected axis maps would have degrees8 and12. They pass the earlier orbit-divisibility and local tangent residue tests. Passing these tests supplies no actual maps or covers.

The old degree-two-axis proof is also unavailable: for a top rational pencil of degree4 and an elliptic map of degree8, the birational Castelnuovo-Severi bound is29, not13. We do not infer a low-genus quotient or membership from this change.

## 4. Principal indecomposability

As an unpolarized isogeny object Y3 is still X6 x E^2. The possible nontrivial indecomposable ppav-factor dimension patterns are(6,2), (6,1,1) or(7,1).

In the first two, the unique sixfold principal factor is preserved by native i, since polarized automorphisms permute the indecomposable principal factors. It would be a Gaussian principally polarized sixfold isogenous to X. Its unimodular raw discriminant class would be-1, contradicting the fixed isogeny/repolarization class-3, as retained in the earlier rigidity proof.

The last pattern would give a degree-one elliptic subvariety, excluded by the complete lower bound just proved. Therefore Y3 is indecomposable. This is not a theta-dimension calculation or a Prym criterion.

## 5. Phase-correct licensed cycle maps

The actual old f2:A->Y2 had det_K(f2)=48i. Thus

    F3=q f2, det_K(F3)=16*48i=768i,
    deg(F3)=2304*256=589824=768^2,
    F3*theta3=4E_A.

Write U_j=R_j+iI_j for the native Weil generators. The new step has real positive Gaussian determinant16, so

    q*U3=16 U2, q_*U2=16 U3.

It adds no extra phase to the existing quarter-turn. With the old actual rational algebraic correspondences S2,D2 define

    S3=(1/16) q_* S2,   D3=(1/16) D2 q*.

Equivalently S3=F3_* S_A/768 and D3=D_A F3*/768. These are licensed rational Chow operations, not merely cohomology inverses. On the Weil planes,

    S3(R6)=I3, S3(I6)=-R3,
    D3(I3)=R6, D3(R3)=-I6,
    D3 S3=Id on cohomology.

The inverse identity uses q* q_*=256Id on cohomology. We do not claim a Chow retraction: on Chow the other composite order is a sum of torsion translations, and no extra Chow theorem is silently imported.

For an arbitrary Y3 cycle all four exceptional reverse channels are

    P6 C_j f2* q* = P6 C_j F3*.

The full exceptional cohomological projector is Pi3=q_*Pi2 q*/256. Its rank8, the full middle Hodge rank14 and divisor-sector rank6 are unchanged by isogeny. The rank-two Weil projector is not substituted for these four channels. A supplied exceptional Y3 cycle could be tested and transferred back to alpha, but none has been supplied. The actual divisor-cube control stays algebraic and has zero exceptional channels.

## 6. Exact exterior certificate and continuation

The real Q is a direct sum of four dimension-four blocks. Both local exterior inverse orders are checked on every local basis column,64 in total. The exterior algebra of a direct sum is the graded tensor product, so these block identities give the full inverse, including the12870-dimensional H8. Four global H8 columns are independently cross-checked against the full native matrix to guard interleaving/Koszul signs. They are not misreported as an exhaustive global enumeration.

This turn reopens a valid model-specific search: investigate actual Prym or K-isogeny/period/factor matching on **Y3** and test all four cycle channels there. The exclusions for the exact polarization of Y2 remain true and immutable. They cannot be transported through q as ppav exclusions, since q*theta3=2theta2 rather than theta2. No generic even-axis sufficiency theorem is asserted. Direct cycles, differently polarized/generalized sources and justified deformation methods remain alternatives.

Contract: `research/conjecture_net/contracts/hodge-even-axis-principal-model.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_even_axis_principal_model.py`.
Receipt: `research/voevodsky/results/hodge-even-axis-principal-model-v1.json`.

Fresh inputs are the actual Y2 construction and its etale/two-branch odd-axis exclusions. Written imports include Riemann projectivity, isotypic decomposition, Gaussian PID lattice theory, principal-factor uniqueness, the earlier sixfold norm-class rigidity, and standard Chow/isogeny functoriality. Exact arithmetic and source freshness do not replace mathematical review or proof-assistant certification. Iteration38 and immutable pins v1-v40 are preserved. No matched Prym, target exceptional cycle, all-cycle theorem, alpha nonalgebraicity or Hodge verdict is supplied.
