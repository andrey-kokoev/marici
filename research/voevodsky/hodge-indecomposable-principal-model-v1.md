# Global iteration 17 (new series 7/10): an indecomposable principal Gaussian model

## Result

Construct an actual principally polarized Gaussian eightfold Y2 in the same isogeny class as A=X x B, now **indecomposable as a principally polarized variety**. This changes the auxiliary polarization explicitly, not the original candidate X or alpha=R6.

There are actual isogenies

    A --q--> Y --u--> Y2,
    deg q=9, deg u=256, deg f=deg(u q)=2304,
    u*theta2=2 theta_Y, f*theta2=2 E_A.

The previous exact smooth-etale-Prym exclusion applied to the four principal quotients retaining E_A, and is retained unchanged. Its product crossing does not automatically apply to the new polarization. This construction does not prove Prym membership either.

The new Gaussian determinant is 48i, not 48. Consequently native Weil generators undergo a quarter-turn. The phase-correct maps Snew=f_* S_A/48 and Dnew=D_A f*/48 reverse one another on cohomology, with

    Snew(R6)=Inew, Snew(I6)=-Rnew,
    Dnew(Inew)=R6, Dnew(Rnew)=-I6.

No actual exceptional algebraic cycle is supplied.

## 1. A two-primary gluing which touches the elliptic factor

Use the native Gaussian lattice basis of the principal Y from global iteration 15; its Hermitian diagonal is

    dY=(1,1,1,-1,-1,-1,1,-1).

The old E_+ factor is its seventh Gaussian coordinate. Couple it to the first coordinate, which belongs to X before the old quotient. Set the new lattice basis to be

    e1'=(e1+e7)/2, e7'=(e1-e7)/2,
    ej'=ej/(1+i) for j not in {1,7}.

On the coupled positive pair, the marking matrix is H/2 for

    H=[1  1], H^t H=2 I2.
      [1 -1]

On the other six coordinates it is multiplication by 1/(1+i). The old lattice lies in the new one: H is integral and each remaining inverse marking coefficient is 1+i. The quotient lattice has order 4*2^6=256 and is killed by two. It is Gaussian-stable.

Keep the same underlying real vector space and **the same complex structure**, but use the alternating form 2E_Y. In the new basis the Hermitian diagonal is again dY: on the coupled pair (H/2)^t (2 I2)(H/2)=I2; on each other coordinate the factor is 2 Norm(1/(1+i))=1. Thus the new alternating form is integral and unimodular. Its positivity and type (1,1) are unchanged by scaling the old Riemann form positively.

The Riemann theorem supplies a principally polarized abelian variety Y2. The identity of the underlying vector space induces the finite holomorphic (hence algebraic) isogeny u:Y->Y2 with u*theta2=2theta_Y. Multiplication by i preserves both lattices, the complex structure and polarization; the signature is (4,4).

These are polarization-class identities. No preselected rigidified theta line bundle or linearization is asserted. Nor is the marking H/2 claimed to commute with the old marked complex structure. In particular the first native coordinate need not be a complex subtorus of X; the gluing only needs torsion points in the actual torus. Changing a lattice in the unchanged complex vector space is not inventing a homomorphism mixing the simple X with an elliptic curve inside the old A.

## 2. Explicit composite matrix and elliptic degrees

Let T9 denote the previous q matrix on the sixth/eighth Gaussian coordinates:

    T9=[ 1      1-i ], det_K T9=3.
       [ -1-i     1 ]

The composite f in new markings has mutually disjoint Gaussian blocks:

- H on coordinates (1,7);
- (1+i)T9 on coordinates (6,8);
- 1+i on each of coordinates 2,3,4,5.

Call this integral matrix Tf. Its determinant is

    (-2)*(6i)*(1+i)^4=48i,
    Norm(det_K Tf)=2304.

Its real degree is 2304=9*256. Direct exterior pullback checks f*theta2=2E_A and the same degree on H16. The new Hermitian determinant is one, with split signature (4,4); diagonal entries are all units. The actual complex structure in the new marking is Tf J_A Tf^-1, not assumed equal to J_A.

The images of the two actual CM elliptic subvarieties E_+,E_- have different polarization degrees from the old product situation:

- For E_+, the composite column has coefficients (1,-1) in the coupled pair. Lattice integrality forces its parameter to be Gaussian integral. Thus f restricted to E_+ has degree one. Its image has theta2-degree 2*1/1=2.
- For E_-, the composite column in the negative pair has coefficients (2,1+i). Its parameter lattice enlarges by 1/(1+i); hence the restricted isogeny has degree two. Its image has theta2-degree 2*3/2=3.

The checker enumerates the half-Gaussian residues and obtains kernel orders one and two. This enumeration is complete because the plus column contains a unit and the minus column contains 1+i, bounding all possible denominators by two. These are elliptic line-bundle degrees two and three, not the degrees of their polarization homomorphisms.

## 3. Why this principal polarization is indecomposable

As an unpolarized rational isogeny object Y2 is still X x E^2. The fixed X is simple, six-dimensional, End^0(X)=Q(i), with no maps to the CM elliptic factors. Every nontrivial principally polarized product decomposition must therefore have one of the following indecomposable-factor dimension patterns:

    (6,2), (6,1,1), or (7,1).

This uses Poincare complete reducibility and uniqueness of the simple isogeny factors. Uniqueness of indecomposable principally polarized factors, already used in the preceding audit, makes the actual automorphism i permute those factors.

In the first two patterns the sixfold factor is unique and preserved by i. It would be a principally polarized sixfold isogenous to X with an integral Gaussian action and signature (3,3). Its unimodular raw Hermitian determinant would be -1. This contradicts the original -3 norm class, invariant under repolarization, compatible isogeny and either field embedding: their ratio has odd valuation at the inert prime three.

In the (7,1) pattern the unique elliptic principal factor must be preserved by i. On the two-dimensional CM isogeny summand the **physical complex** CM action of the native i is diag(i,-i), since the original E_+ and E_- have opposite CM types. Its invariant one-dimensional rational CM subspaces are exactly its two eigenaxes. Indeed, a line with both components nonzero would have to have both distinct eigenvalues i and -i. Thus that elliptic factor would have to be one of the two actual connected elliptic axis subvarieties. But their restrictions have degrees two and three, not one.

All three product patterns are impossible. Therefore (Y2,theta2) is indecomposable. This does not classify all elliptic subvarieties: non-invariant CM slopes can exist. It uses invariance only for the unique elliptic factor in the (7,1) product pattern. In the two-elliptic-factor case i is allowed to exchange them; the preserved sixfold already gives the contradiction.

In particular the old proof's untouched degree-one elliptic factor is genuinely removed, not merely relabeled. Indecomposability does not assert any value for dim Sing theta2 and is not a Prym membership criterion.

## 4. A factorized exact exterior certificate, with its scope explicit

The full real Tf decomposes into blocks of dimensions 4,4,2,2,2,2 on all sixteen real coordinates. For every block, the checker verifies both exterior inverse orders in every degree. This is 16+16+4+4+4+4=48 local exterior basis columns.

The exterior algebra of a direct sum is the graded tensor product of the block exterior algebras. Those local identities therefore prove the full rational exterior inverse identity, including the 12870-dimensional H8. They are **not** an explicit enumeration of 12870 global basis columns. The implementation applies the blocks with the signs required by the intervening native coordinates and cross-checks four global H8 columns against the original full native-coordinate pullback, as well as the independent polarization and Weil identities.

The claimed full inverse follows from the block tensor factorization plus the written sign formula, not from treating four global samples as an exhaustive search. The certificate is smaller than the preceding explicit census but its factorization argument is essential and exposed in the contract and receipt.

## 5. Weil phase and the licensed cycle tests

Write U=R+iI in each native Gaussian marking. Then

    f* Unew=48i U_A,
    f* Rnew=-48 I_A, f* Inew=48 R_A,
    f_* R_A=48 Inew, f_* I_A=-48 Rnew.

The phase is not discarded by replacing a complex determinant with its norm or absolute value. Let

    Snew=f_* S_A/48, Dnew=D_A f*/48.

Both are actual rational algebraic cycle correspondences at the existing codimensions. On cohomology,

    Dnew Snew=(1/2304) D_A f* f_* S_A=D_A S_A=Id.

The phase-sensitive generator identities in the result follow. In particular the original alpha=R6 transfers to **Inew**, not Rnew. The original alpha is not changed to hide this phase. An actual algebraic nonzero native Weil class on Y2 would still give alpha by the previously licensed inverse within W6.

The standard projection formula gives f_* f*=2304 Id on Chow, but the other order is a sum of torsion translations. Without invoking additional Chow results, the displayed maps are not claimed to be a Chow retraction. Likewise the transported exceptional formula is not automatically a new Chow idempotent.

The full Hodge space remains of dimension fourteen, with six divisor directions and eight exceptional directions. NS has rank five. The full exceptional cohomological projector is

    Pi_new=f_* Pi_exc,A f*/2304.

All four actual reverse channels are P6 C_j f*. The two-plane CRT Weil projector remains rank two and is not a replacement for those four channels. A supplied algebraic Y2-cycle outside the transported divisor sector would yield alpha; the construction supplies no such cycle. The actual divisor-cube control reverses but has zero exceptional channels.

## 6. New precise continuation and boundaries

The previous four fixed-E_A models remain excluded from smooth etale Prym images. Y2 lies outside that bounded library because f*theta2=2E_A, and its principal polarization is indecomposable. Neither fact proves it is or is not the Prym of a genus-17/9/5 etale cyclic-quartic tower. The old six-dimensional cycle theorem is not applied in dimension eight.

Next investigate actual cover membership or another valid eightfold cycle construction on this specified Y2, including any needed theta-singularity constraints. Do not reuse the old product crossing or infer membership from principal splitness and indecomposability. A curve/cycle theorem and compatible correspondence are still required. Ramified/singular covering routes and direct non-divisor smooth-threefold/reflexive geometry on X remain open.

No nonzero exceptional algebraic cycle, all-cycle theorem, alpha algebraicity/nonalgebraicity or Hodge verdict is claimed. All three research obligations and independent review remain open.

## Artifacts

Contract: `research/conjecture_net/contracts/hodge-indecomposable-principal-model.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_indecomposable_principal_model.py`.
Receipt: `research/voevodsky/results/hodge-indecomposable-principal-model-v1.json`.

    python research/voevodsky/checkers/check_hodge_indecomposable_principal_model.py

The matrix, phase, kernel and exterior calculations are exact rational controls. Riemann projectivity, uniqueness of principal factors, the retained generic sixfold rigidity and standard isogeny functoriality are explicit mathematical imports in the written argument, not proof-assistant certification or independent review. The iteration-16 predecessor and immutable pins v1-v17 are retained unchanged.
