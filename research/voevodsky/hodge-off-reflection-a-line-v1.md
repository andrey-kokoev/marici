# Global iteration 47, fifth series 6/10: denominator-line CM screening beyond the reflections

## Result

The new literal off-reflection source(lambda,a,b)=(2,0,2) is excluded from Y3 even up to complex isogeny. At good prime13 its sevenfold complement has no geometric E_i factor, so faithful Hom specialization forbids the missing second CM factor over C. Its actual smooth source and primitive theta-four axis remain valid.

A complete regular-chart census of the a-line at lambda2,b2 gives:

| a mod13 | conclusion |
|---|---|
|0,7,8,10,11,12|no extra geometric E_i; negative congruence veto|
|2,6|exactly one extra E_i in reduction, of conjugate-beta unit type; necessary screen survives only|
|1,3,4,5,9|the displayed good-reduction certificate fails; no complex-source exclusion follows|

The literal a=2 source is already excluded by the exact reflection theorem. This DOES NOT exclude the entire residue class a=2 mod13: a different lift such as a=15 need not satisfy a=2 or2lambda over C. Conversely literal a=6 is a new actual off-reflection source, with exactly the desired single opposite-type CM factor in reduction. It is not identified with Y3 and no complex theta-six axis is lifted.

## 1. Full chart and projective counts

Work with W:y^2=x(x-1)(x-2), D_a=x^2-a*x+2, N=2(x^2-2) and g=(y+N)/D_a. For every a in F13 the checker tests D_a squarefree and coprime to W's cubic, each special-fibre quartic P-(cD_a-N)^2 for c=0,+1,-1 squarefree and coprime to P, and genuine poles via gcd(D_a,P-N^2)=1. The eight regular and five uncertified residues above exhaust F13. Here g(infinity)=2, not a special branch value; the unhandled infinity charts from the earlier b-line do not occur on this line at13.

The new Rust counter reuses the checked generic field kernel, but generalizes BOTH the ordinary and twisted denominator coefficient. For every field it also cross-checks its a=4,b=3 specialization against the old counter's actual arithmetic. It freshly enumerates all40 ordinary rows (eight cases through degree5) and32 rho-Frobenius rows (through degree4). Full primitive-generator cycles certify the fields. The nonsplit elliptic two-isogeny torsor, including discriminant-zero fibres, is counted with the new g, not an a=4 substitute.

Pole rationality depends on a. There is the exact generic identity

    x(x-1)(x-lambda)-(a-lambda-1)*x^2
       = x*(x^2-a*x+lambda).

Thus at a denominator root for lambda2, y^2=x^2*(a-3). The four geometric poles are all defined over F13^2. They are rational over F13 precisely when both a^2-8 and a-3 are nonzero squares. Of the regular cases only a=2 has four rational poles in odd degrees; every other regular case has none in odd degrees. All have four in even degrees. This is checked rather than copying a constant-pole assumption. Each genuine simple pole contributes one normalized V point. Infinity contributes the square-root count of6, namely0 in odd degrees and2 in even degrees.

Independent digitwise Python arithmetic directly enumerates ordinary degree1,2 counts for all eight cases and directly tests rho Frob13 fixed points inside F13^4. It does not reuse the Rust digit-block tables or torsor parametrization. The counts agree.

## 2. Complete polynomials and exhaustive CM certificates

The native elliptic Frobenius remains beta=3+2i at i=5, norm13 and trace6. Four ordinary/twisted Gaussian moments determine a1,...,a4; a3 is nonzero in all eight cases. Unitary reciprocity gives a7=13^3*a4/conjugate(a3) and then a5,a6. All Gaussian integrality and reciprocal identities are checked. The unused fifth ordinary count verifies the full rational degree14 polynomial in every case. Where the pole profile agrees, the result is also compared with the preceding generic reconstruction routine using the UNMODIFIED counts.

For each rational polynomial F, the exact degree28 norm F(beta U)F(conjugate(beta)U) is tested against all55 possible cyclotomic orders, including1. The degree bound28 and phi(m)^2>=m/2 make the exhaustive order bound1568. Positive factors require exact integer monic division; modular residual-gcd certificates prove completeness. The six excluded cases have empty cyclotomic parts. For a=2 the complete part is Phi_4; for a=6 it is Phi_1^2. Exact Gaussian linear division accounts for each positive factor:

    a=2: -i*conjugate(beta), once;
    a=6: conjugate(beta), once.

The source's known first axis contributes beta. Thus the a=6 SPECIAL FIBRE has total E_i multiplicity2 with both arithmetic types, a closer necessary profile than the earlier b3 controls. No lower-bound lifting of Hom to characteristic zero is inferred.

For the excluded a=0 control the Gaussian coefficients descending are

    [(1,0),(2,0),(6,4),(-13,14),(67,16),
     (-130,312),(-1014,676),(-6591,4394)].

Its rational coefficients descending are

    [1,4,16,-2,134,-36,-1251,-17596,-16263,-6084,
     294398,-57122,5940688,19307236,62748517].

Its power traces through degree5 are-4,-16,134,-824,1836. All other Gaussian and rational polynomials, norm polynomials, cyclotomic divisions and modular witnesses are retained in the receipt. For a=6 the rational polynomial divides exactly by T^2-6T+13, leaving a finite-field factor of degree12. That factor is NOT identified with the fixed X6; its simplicity and characteristic-zero lift are uncomputed.

## 3. Negative evidence extends to algebraic congruence boxes

Let lambda,a,b be algebraic and integral at a place over13, reducing to lambda=2, a in{0,7,8,10,11,12}, b=2 or11. All chart conditions are units at that place, so the general scalar curves and the explicit T_lambda cyclic-four lift of iteration46 have good reduction there. Their special fibres are the excluded controls, possibly after extending the residue field. For b=11=-2, the actual V isomorphism(p,w)->(-p,i*w) identifies the sign pair, independently of a. Good-model checks are also performed at b=11.

A hypothetical extra complex E_i homomorphism descends to a number field and specializes faithfully. Over any finite residue extension it would force a Frobenius root to differ from beta or its conjugate by a root of unity. The exhaustive certificate forbids that. Each source therefore has exactly one E_i isogeny factor, versus the fixed Y3's2. All twelve residue boxes are excluded even up to complex Y3 isogeny. No model or reduction of the fixed transcendental-period sixfold X is required. This arithmetic statement does not cover arbitrary transcendental parameters.

This is not an exclusion of all denominator parameters, all failed-chart cases or all sources outside the reflection loci. In particular the exact a=2 reflection is not applied merely from congruence. Positive finite-field factors and their arithmetic character do not construct a complex elliptic axis or give a theta degree.

## 4. The next actual source

For the literal lift(lambda,a,b)=(2,6,2), exact Q-gcd tests verify genuine simple poles and the twelve simple finite special-value points; infinity has g=2. The same explicit T and kappa, scalar tower, ramified-to-principal degree-two isogeny and genus/primitivity proof yield a smooth C17/D9/B5 and a primitive theta-four E_i axis. It is outside a=2lambda, a=2 and b=0. Other symmetries or decompositions are NOT excluded by this observation.

Next test this source at another certified good split prime, or construct an actual opposite-character map and compute its primitive theta degree and joint kernel. The residual sixfold's End, simplicity and X6/Y3 periods/correspondences still require proof before the unchanged denominator768/four-channel target transfer. Alternative lifts of surviving a residues, other lambda/b values, compactified sources, the birational genus-five-image route and direct cycles remain open.

Contract: `research/conjecture_net/contracts/hodge-off-reflection-a-line.v1.json`.
Checker/counter: `research/voevodsky/checkers/check_hodge_off_reflection_a_line.py`, `count_hodge_off_reflection_control.rs`.
Counts: `research/voevodsky/inputs/hodge-off-reflection-a-line-v1/counts.json`.

Trust: fresh finite-field enumeration with independent small counts, exact coefficient and exhaustive cyclotomic certificates, written projective-family and faithful-Hom specialization arguments, and the retained scalar-source primitivity proof. Finite-field isogeny interpretation uses standard Tate semisimplicity. Not proof-assistant certification or independent review. Iteration46 and pins v1-v49 remain immutable. No complex CM-factor lift, End calculation, whole-family exclusion, target cycle or Hodge verdict is supplied.
