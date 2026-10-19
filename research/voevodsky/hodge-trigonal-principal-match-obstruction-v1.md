# Global iteration 36 (fourth series 5/10): the new family's natural principal Prym cannot be the fixed Y2

## Scoped result

The auxiliary ramified-trigonal family from iteration35 exists, carries the proved cyclic action, and has algebraic determinant classes by Schoen. However its **natural principal Prym is not isomorphic as a ppav to the fixed Y2**. This is not an exclusion of an arbitrary unpolarized K-isogeny from that family to Y2. An isogeny does not preserve the elliptic theta degree used below.

The new bridge is geometric: a degree-four rational pencil on the etale genus17 top curve, together with the degree-four elliptic map required by Y2's degree-two elliptic axis, forces a unique genus-three quotient. The quotient diagrams then force the simple X6 factor to be a primitive cyclic-quartic sixfold Prym. Iteration14's independently derived discriminant obstruction excludes that presentation, including ramified ones.

No actual quotient curve is constructed in this contradiction argument; all such quotients are conditional on a hypothetical principal match.

## 1. A previously unused pencil on the top curve

Use Y17->T9->Z5 for the actual auxiliary free cyclic-quartic tower, with generator R and h=R^2. Do not confuse Y17 with the fixed abelian eightfold Y2.

Freshly reread Lange-Ortega's retained primary section2, diagram(2.2) and Lemma2.2: the symmetric-cube curve Y maps with degree4 to the orientation double cover O->P1. The latter branches exactly at the two distinct trigonal-base values in our general ramified construction. Its normalization has genus0. Since Y is smooth, its map factors through this normalization. Therefore Y has a degree-four map

    a:Y->P1.

We need the existence of this pencil, not exact gonality or uniqueness of tetragonal pencils. The natural principal ppav isomorphism P(Y/T)~P(C16/D8) was already proved K-equivariant in iteration35.

Suppose this ppav were the fixed Y2. Its actual degree-two elliptic theta axis supplies, by the retained norm-adjoint argument, a map

    phi:Y->E, deg(phi)=4, phi h=c-phi.

After translating E, write phi h=-phi. No preservation of this chosen axis by R is assumed. The source-isogeny/axis theta-degree facts are freshly consumed from the actual Y2/tetragonal gate, not inferred from a general Gaussian eightfold.

## 2. Exhaust the joint degrees: a unique low-genus double quotient

Let V be the normalization of the joint image of(a,phi). Its common field degree d divides both degrees4, hence d=1,2 or4.

- d=1: Castelnuovo-Severi (equivalently adjunction in P1 x E) bounds g(Y) by 4*0+4*1+(4-1)^2=13, contrary to17.
- d=4: V would map with degree1 both to P1 and E, impossible because their genera differ.
- d=2: V has degree-two maps to P1 and E, and g(V)<=2*0+2*1+(2-1)^2=3. Also g(V)>=1 because it maps nontrivially to E.

Thus Y->V is a double cover with deck involution kappa. It is the **unique** involution whose quotient has genus at most3. If two were distinct, their quadratic fixed subfields would generate the function field of Y. Castelnuovo-Severi would give g(Y)<=2*3+2*3+1=13. The strict inequality17>13 is essential.

Every automorphism of Y conjugates kappa to another such involution, so kappa is central in Aut(Y). In particular it commutes with R and h. Consequently R descends to V and h descends to h_V. The elliptic map factors as phi=b composed with(Y->V), where b:V->E has degree2 and b h_V=-b. The anti-h_V part of J(V) is therefore nonzero.

This proves centrality without assuming that R preserves phi or the chosen elliptic axis. Constants in the anti-involution relation disappear on Jacobians.

## 3. Freeness and cyclic monodromy force genus3, not just genus<=3

The descended R_V has order4. Otherwise h would lie in the kernel of Aut(Y)->Aut(V), namely {1,kappa}, forcing h=kappa, which contradicts g(Y/h)=9 and g(V)<=3. Moreover R_V has no fixed points: over any fixed point of V it would permute a fibre of size at most2, so R^2=h would fix points of Y, contrary to freeness.

Set U=V/<h_V> and Q=V/<R_V>. There are no inertia-four points of V->Q. Thus U->Q is an etale double cover and

    g(U)=2g(Q)-1.

Since g(V)<=3 and V->U has degree2, this forces g(Q)=g(U)=1. Let v=g(V), and let r be the number of inertia-two branch values of V->Q. Riemann-Hurwitz gives r=v-1. In a cyclic-quartic cover all these local monodromies are2; their sum must vanish modulo4. Equivalently the cyclic-cover branch divisor has degree2r divisible by4. Hence r is even.

The cases are:

    v=1: r=0, but anti-h_V dimension v-g(U)=0, contradicting b h_V=-b;
    v=2: r=1, impossible cyclic monodromy sum2 mod4;
    v=3: r=2, anti-h_V dimension2.

Therefore V3->U1->Q1 is forced. This is a universal case argument under the stated hypotheses, not an enumeration of actual low-genus curves.

## 4. The complementary factor is exactly the forbidden sixfold

Let W=Y/<kappa h>. The commuting involutions kappa,h give a Klein-four diagram with common quotient U. The quotient-genus relation is

    g(Y)+2g(U)=g(V)+g(T)+g(W).

Thus 17+2=3+9+g(W), so g(W)=7. The anti-h part splits, up to isogeny, into

    P(Y/T) ~ P(V/U) x P(W/U),
    dimensions       2             6.

These are the (kappa=+1,h=-1) and (kappa=-1,h=-1) rational character factors. Pullback from the quotient curves realizes this as an algebraic isogeny of abelian varieties.

The fixed Y2 is unpolarized-isogenous to X6 x E_+ x E_-, with X simple, End^0(X)=Q(i), and raw discriminant norm class-3. There are no nonzero homomorphisms between X and the elliptic factors. On its multiplicity-one X factor any involution is+1 or-1, because the endomorphism field has no other square roots of1. Since kappa's positive anti-h factor has dimension2, kappa must act as-1 on X. Its negative anti-h factor has dimension6, so **P(W/U) is isogenous to X**.

Centrality of kappa lets R descend to an order-four automorphism R_W of W, with R_W^2 the deck involution of W/U. The anti-involution Prym P(W/U) is therefore the primitive sixfold of this curve automorphism. W/U has twelve double-cover branch points. The further quotient U->Q is etale, so W/Q is cyclic quartic with six inertia-two branch values; no etaleness of W/Q is assumed.

Now apply the already retained iteration14 theorem/proof, not a sixfold etale theorem outside its hypotheses. For the primitive factor of **any** order-four curve automorphism, the restricted Jacobian-polarization kernel is killed by2. Integral deck action makes H1 a free Gaussian lattice. In balanced K-dimension6 the raw Hermitian determinant is -2^a, 0<=a<=6, hence norm class-1. Every repolarized/isogenous model of the fixed simple X instead retains class-3. The ratio3/2^a has odd 3-adic valuation, impossible for a Q(i)-norm. This excludes the forced P(W/U)~X.

The comparison remains valid even if the principal ppav identification did not initially match the given K marking: the induced order-four action on the simple X must be one of i or-i in End^0(X). Both give the same determinant norm class in even K-dimension6. No arbitrary deck-invariance of the chosen elliptic axis was used.

This contradiction excludes the auxiliary family's **natural principal-polarized** identification with Y2.

## 5. Scope and executable continuation

The proof also applies to any free cyclic-four genus17 tower whose top curve has a degree-four rational pencil and whose natural principal Prym is the specified Y2. It does not exclude every etale cyclic-quartic presentation: a different top curve need not have that pencil. In particular a tetragonal genus-nine intermediate alone does not supply a degree-four top pencil.

Most importantly it does not exclude arbitrary unpolarized K-isogenies from the iteration35 auxiliary family to Y2. An isogeny may pull the fixed norm-two elliptic axis to a higher-degree elliptic polarization; then phi need not have degree4. For degrees4 and6 the birational CS bound is21, not13, so the genus17 contradiction already disappears at that first step. Replacing the natural Prym polarization is a genuine change of comparison, not an automatic repair of this principal-match proof.

The source family still exists and Schoen's auxiliary algebraicity result still holds. An actual K-isogeny to the target would remain sufficient for transporting appropriate cycles, but none is supplied. The continuation is to test that isogeny/period/factor problem explicitly, seek another principal Prym source without this low-degree top pencil, or use different objects, restricted commutative deformation arguments or direct cycles. No dimensional moduli-avoidance shortcut is taken.

## Verification and trust

Contract: `research/conjecture_net/contracts/hodge-trigonal-principal-match-obstruction.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_trigonal_principal_match_obstruction.py`.
Receipt: `research/voevodsky/results/hodge-trigonal-principal-match-obstruction-v1.json`.

Fresh inputs are the auxiliary-family receipt, actual target-axis/tetragonal gate, and primitive-sixfold discriminant exclusion. Exact controls check all common degrees, strict CS bounds, low-genus RH/monodromy cases, Klein-four genus and factor dimensions, and all two-primary determinant upper types. Written imports include Castelnuovo-Severi, quotient/Jacobian character decompositions and the previously justified polarization/discriminant rigidity. The checker is not a proof assistant or an independent review. Scientific source freshness and finite controls do not alone establish the mathematical imports.

Iteration35 and immutable pins v1-v37 are preserved. Fixed X, alpha, Y2, all four transfer channels, determinant/denominator48 data and previous target censuses are unchanged. No actual theta dimension, exceptional target cycle, all-cycle annihilation, nonalgebraicity conclusion or Hodge verdict is supplied.
