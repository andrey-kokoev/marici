# Global iteration 18 (new series 8/10): Jacobian exclusion and low-gonality constraints on Y2

## Result and scope

The specified indecomposable principally polarized eightfold (Y2,theta2) **is not the canonically polarized Jacobian of a smooth curve**. Its native Gaussian automorphism squares to minus identity, so strong polarized Torelli would force such a curve to be hyperelliptic. The actual elliptic subcurve of polarization degree two would then give an elliptic double cover, contradicting genus eight.

Consequences for a hypothetical smooth etale cyclic-quartic tower

    C17 -> C9 -> C5, Prym(C17/C9)=(Y2,theta2):

- C9 cannot be hyperelliptic, by Mumford's hyperelliptic Prym theorem and Y2's indecomposability/non-Jacobian property.
- C9 cannot be trigonal: any trigonal genus-nine curve has a unique degree-three pencil, incompatible with its required fixed-point-free involution C9->C5.
- Therefore the intermediate C9 has gonality at least four.
- If dim Sing theta2 >4, smooth etale Prym membership is excluded. If dim Sing theta2=4, the cyclic-quartic realization requires **C9 bielliptic**. This is conditional: the actual dimension is not computed here. At smaller dimension this theorem gives no further base classification.

The genus-nine intermediate, not the genus-five bottom curve, is the base of the double cover to which Mumford's theorem applies. No claim is made about all genus-five bases, all smooth Pryms, ramified/singular Pryms, other polarizations or arbitrary isogenous Jacobians. The original X, alpha=R6, the actual Y2, its phase 48i and four cycle channels are unchanged.

## 1. A fresh precise Torelli import

J.S. Milne, *Jacobian Varieties*, June 12, 2021 revision of the Arithmetic Geometry chapter (1986), Theorem 12.1(a,b), PDF page 38:

https://www.jmilne.org/math/xnotes/JVs.pdf

For smooth curves over an algebraically closed field, a canonical-polarization-preserving Jacobian isomorphism is induced by a curve isomorphism up to sign (and a harmless Abel--Jacobi translation). In the nonhyperelliptic case, the curve isomorphism and sign are unique.

The full author-hosted PDF and Unicode extraction, PDF pages 37-38 as text and images, and bounded search provenance are retained and hashed under `inputs/hodge-y2-curve-audit-v1/`. The sign statement and canonical-polarization requirement were checked in the rendered page 38. The local `pnpm pdf:search Torelli` had no matches in its bounded index; this is not a literature absence claim.

Mumford's *Prym Varieties I* section 7(a,d), printed p.344, is the previously retained primary theorem, freshly reread for this application. Its upper bound and equality implication are not strengthened to an equivalence.

## 2. Why a hypothetical Jacobian would be hyperelliptic

Let rho be the actual native Gaussian automorphism of Y2. It preserves theta2 and satisfies rho^2=-Id as a group morphism. The preceding Gaussian lattice construction proves this on the actual variety, not just on its middle Weil plane.

Suppose (Y2,theta2)=J(D) canonically, with D smooth of genus eight. Strong Torelli writes rho=epsilon*sigma_J for a curve automorphism sigma and a sign epsilon. The Abel--Jacobi translation disappears on the induced group homomorphism. Thus

    (sigma^2)_J=rho^2=-Id.

If D were nonhyperelliptic, this would give two different signs for the polarized Jacobian automorphism -Id: plus the automorphism sigma^2, or minus the identity curve automorphism. This contradicts the sign uniqueness in Milne 12.1(b). Therefore D is hyperelliptic. No claim that arbitrary unitary lattice isometries lift to curve automorphisms is used; rho is an actual polarized automorphism.

## 3. The degree-two elliptic map gives genus at most three

The preceding construction embeds an elliptic curve j:E->Y2 with deg j*theta2=2. Were Y2=J(D) canonically, its polarization adjoint f:J(D)->E would satisfy

    f j=[2].

Composing f with an Abel--Jacobi map gives a nonconstant curve map phi:D->E. Standard Jacobian functoriality identifies phi_*=f, phi*=j; norm-pullback is multiplication by deg phi. Hence phi has degree two, not four (the elliptic polarization-homomorphism degree), 256 or 2304.

Hyperellipticity gives another degree-two map psi:D->P1. The maps have **equal degrees, not coprime degrees**, so independence needs proof. Let B be the normalization of their joint image. The degree D->B divides two. If it were two, B->P1 would have degree one, so B=P1 and the elliptic map would factor through a nonconstant morphism P1->E. Such a morphism is impossible in characteristic zero by Riemann--Hurwitz. Thus the joint map is birational.

Its image in P1 x E has projection degrees (2,2), self-intersection eight and canonical intersection minus four. Adjunction gives arithmetic genus

    1+(8-4)/2=3.

The normalization has genus at most three, contradicting genus(D)=8. More generally the same independence proof works for a degree-d elliptic map from a hyperelliptic curve, giving g<=2d-1 even when d is even. The previous coprime-only helper is not silently relaxed: this turn supplies the additional rational-to-elliptic impossibility argument.

This excludes the **fixed canonical principal Jacobian presentation**, not unpolarized isomorphism or arbitrary isogeny to a Jacobian. Quotients of high-genus Jacobians or correspondences from them are not excluded.

## 4. The actual elliptic reflection and a necessary caution

There is also an actual involution sigma2 of Y2. On the new Gaussian coordinates it swaps the first and seventh coordinates and fixes the rest. This is not declared holomorphic merely because it preserves a Hermitian matrix: the composite isogeny matrix Tf satisfies

    sigma2_new Tf = Tf sigma_A,

where sigma_A is minus identity on the actual old E_+ factor and identity on X x E_-. Thus sigma2 descends from an actual holomorphic old automorphism. Its new matrix is integral, preserves the principal form and squares to identity. Equivalently sigma2=Id-j j^dagger for the degree-two elliptic embedding; j^dagger j=[2].

Its H1 minus eigenspace has rational dimension two; on full H8 its anti-invariant dimension is

    2*binomial(14,7)=6864.

It negates both native Weil generators. However it also negates an explicit nonzero algebraic divisor-sector class:

    Gamma=f_*(E_X^3 external r_B),

where r_B is the retained actual graph divisor. This class is nonzero in cohomology, anti-invariant under sigma2, and all four exceptional channels vanish. Its source is algebraic; pushforward through the actual isogeny preserves this status.

The finite-order anti-projector is a legitimate group-algebra Chow idempotent, but anti-invariance is not an exceptional-cycle test or all-cycle annihilation theorem. This reflection is not the original i-on-X obstruction. It does not supply alpha, and its nonzero algebraic anti-control prevents that shortcut.

## 5. Necessary restrictions on the genus-nine intermediate

### Hyperelliptic C9

Mumford 7(a) says the canonical principal Prym of a smooth unramified double cover of a hyperelliptic curve is a hyperelliptic Jacobian or a product of two such Jacobians. Y2 is indecomposable, so the product alternative is impossible; the remaining Jacobian alternative is excluded above. Thus a smooth etale double-cover presentation of this fixed Y2 cannot have hyperelliptic base C9. No calculation of dim Sing theta2 is needed for this conclusion.

### Trigonal C9 in a cyclic-quartic tower

First, a genus-nine trigonal curve has a unique degree-three pencil up to PGL2. If two pencils were distinct, the degree to the normalization of their joint image in P1 x P1 would divide three. The degree-three alternative would mean the same function subfield, hence the same pencil. For distinct pencils the image is birational, has bidegree (3,3), and arithmetic genus (3-1)^2=4. This contradicts genus nine.

Now the free involution eta giving C9->C5 must preserve that unique pencil, inducing an involution on P1 (possibly the identity). It has a fixed point; choose a fibre over such a point. This is an eta-invariant effective divisor of odd degree three. If eta had no fixed point on its support, all points would come in pairs of equal multiplicity, giving even degree. Hence eta fixes a point of C9, contradicting etaleness.

This proof includes ramified fibres of the trigonal map: the multiplicity partitions (3), (2,1) and (1,1,1) all give the same odd-degree contradiction. The checker enumerates the weight-preserving involutions for these partitions. It does not infer unique trigonal pencils at genus four or below, where the genus bound does not exclude two distinct pencils.

The free involution on C9 is essential to this proof. We do not use Recillas's theorem or claim a trigonal exclusion for every arbitrary etale double-Prym presentation without this extra cyclic-tower structure. The conclusion here is exactly gonality(C9)>=4 for a proposed cyclic-quartic realization of Y2.

## 6. Conditional theta-singularity decision table, not an actual dimension

For a smooth etale Prym realization, C9 is now nonhyperelliptic. Mumford 7(d) implies

    dim Sing theta2 <=9-5=4.

At equality, his theorem forces a trigonal or bielliptic base, except for listed genus-five/six cases that do not apply to genus nine. In a cyclic-quartic tower the trigonal alternative is excluded by the free involution. Therefore:

- dimension >4: no such smooth etale Prym;
- dimension =4: a cyclic-quartic realization requires a bielliptic C9;
- dimension <=3 (including an empty singular locus): no further base classification follows from this theorem;
- dimension unknown: no branch is selected.

The actual dimension is **unknown in this receipt**. Conditional biellipticity is not promoted to an actual elliptic quotient of a supplied curve. In particular it concerns C9, not C5. The old reducible-theta crossing argument for Y is not reused for indecomposable Y2.

## 7. Live consequence and remaining geometry

Close the bounded Jacobian/hyperelliptic-intermediate/trigonal-cyclic-intermediate transplant attempt. Retain Y2 and its exact cycle transfers; its general smooth-etale-Prym membership remains open. Next compute actual theta/cover invariants, investigate a nonhyperelliptic nontrigonal genus-nine intermediate (bielliptic only under the stated dimension condition), or supply other valid cycle geometry on Y2 or directly on X.

No curve tower, nonzero exceptional algebraic cycle, all-cycle theorem, alpha algebraicity/nonalgebraicity or Hodge verdict is supplied. A proposed Y2-cycle still requires all four f-pullback channels. The three unrestricted research obligations and independent review remain open.

Contract: `research/conjecture_net/contracts/hodge-y2-curve-audit.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_y2_curve_audit.py`.
Receipt: `research/voevodsky/results/hodge-y2-curve-audit-v1.json`.

    python research/voevodsky/checkers/check_hodge_y2_curve_audit.py

Matrix, sign, genus, weighted-fibre and algebraic control computations are exact finite controls. Strong Torelli, Mumford, Jacobian norm-adjoint functoriality and surface adjunction remain explicit mathematical imports in the written proof, not proof-assistant verification or independent review. The iteration-17 predecessor and pins v1-v18 are retained unchanged.
