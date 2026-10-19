# Global iteration 45, fifth series 4/10: a second-prime veto and a surviving control

## Result

Fresh iteration44 leaves literal b=3 and b=6 on the lambda2,a4 line, both actual primitive theta-four sources. The new tests give:

* b=3 has good reduction at13 and still has two extra E_i factors in the reduced sevenfold. It survives the necessary screens at13 AND17. No complex CM factor, theta-six axis or target match is lifted from these reductions.
* b=6 has good reduction at29 but its reduced sevenfold has NO geometric E_i factor. Faithful specialization therefore excludes an extra E_i factor over C, and the source is not isogenous to the fixed Y3. Its genuine source construction and first primitive axis remain valid.
* The latter veto applies to every algebraic b integral at a place above29 and reducing to6 or23. Together with iteration44's classes2,15 mod17 this prunes part of the parameter line, not all of it. The b=3 control is not excluded.

## 1. Good primes and projective normalization

Continue with W:y^2=x(x-1)(x-2), D=x^2-4x+2 and g_b=(y+b(x^2-2))/D. As before C_b=T times_W V_b, V_b:w^2=g_b^3-g_b, and the principal source P_b is degree-two isogenous to P(V_b/W). Up to isogeny,

    J(V_b) ~ J(W) x E_i x Q_(b,7).

Exact modular gcd tests certify the complete regular branch chart for b=3 at13 and b=6 at29. They also certify b=23 at29. Prime13 is NOT used for b=6: its displayed branch chart fails there. Prime5 is not used for either control. The T isogeny and torsion lift retain good reduction at these odd good primes.

Both13 and29 are5 modulo8. D has discriminant8, so its four geometric poles have no rational representatives over odd extension degrees, and all four are rational over even degrees. The counter checks pole counts0,4,0,4,0; it does not copy the all-rational-poles shortcut from17. Infinity contributes the actual square-root count of b^3-b. In particular V_3(F13) is empty, a valid point count for a smooth genus-nine curve, not an omitted projective point.

## 2. Fresh finite-field evidence

A new generic-prime Rust kernel uses exact p^2-digit addition tables and full nonzero primitive-generator cycles for all ten field representations. It performs ordinary counts through degree5 and rho-Frobenius fixed-point counts through degree4. The twisted-point formula, including the nonsplit elliptic two-isogeny torsor and discriminant-zero fibres, is the prime-independent one proved in iteration43. The chosen square roots of-1 are5 at13 and12 at29.

| b | p | n | #W | #V | #E_i |
|---|---|---|---:|---:|---:|
|3|13|1|8|0|8|
|3|13|2|160|144|160|
|3|13|3|2216|2304|2216|
|3|13|4|28800|28912|28800|
|3|13|5|372488|376320|372488|
|6|29|1|40|68|40|
|6|29|2|800|800|800|
|6|29|3|24520|24068|24520|
|6|29|4|707200|713008|707200|
|6|29|5|20508200|20534548|20508200|

Independent digitwise Python arithmetic directly enumerates ordinary degree1,2 counts, and tests rho Frob_p fixed points directly in F_(p^4). It does not use the Rust block-addition tables or its torsor parametrization. The independent and fresh Rust counts agree. Weil bounds and base Lang-torsor counts are checked for every relevant row.

## 3. Full polynomials, with unused fifth-trace control

The E_i eigenvalues in the native i-character spaces are beta13=3+2i and beta29=-5-2i. Each has norm p, trace p+1-#E_i, and a+i_mod_p*b=0, which fixes the Frobenius orientation. The trace extraction and unitary coefficient identity are unchanged:

    z_n=(#W-#V+i*(#Fix(rho Frob^n,V)-#W))/2-beta^n,
    a_(7-j)=a7*conjugate(a_j)/p^j.

Four Gaussian moments determine a1,...,a4. In these cases a3=11-26i and119-2i, both nonzero, so a7=p^3*a4/conjugate(a3) and then a5,a6 reconstruct the entire polynomial. Gaussian integrality, all reciprocal identities and its rational norm are verified. The unused fifth ordinary count checks the result, not the determinant's selection.

For b=3 at13, the Gaussian coefficients descending are

    [(1,0),(-1,-2),(-3,0),(11,-26),(-85,-56),
     (117,-78),(-169,-1352),(-6591,4394)].

The rational degree14 polynomial coefficients descending are

    [1,-2,-1,28,-79,562,1047,-7096,13611,94978,
     -173563,799708,-371293,-9653618,62748517].

Its rational power traces through degree5 are2,6,-70,126,-2638. The fifth trace is independently checked against the counts. The reduction is ordinary (middle coefficient2 mod13).

For b=6 at29, the Gaussian coefficients descending are

    [(1,0),(9,0),(51,6),(119,-2),(599,-228),
     (7047,-3828),(37845,-15138),(121945,-48778)].

The rational coefficients descending are

    [1,18,183,1156,5977,36990,275063,1741432,7976827,
     31108590,145773053,817616836,3753540267,10706819778,17249876309].

The power traces are-18,-42,582,-5890,-29298. The unused fifth count agrees. This reduction is ordinary too (middle coefficient11 mod29), but ordinary reduction alone is NOT the reason for the veto. No simple-reduction or absolute-simplicity shortcut is asserted.

## 4. Complete CM-ratio certificates

For each rational characteristic polynomial F, use the exact integer polynomial

    N(U)=F(beta U)*F(conjugate(beta) U).

As in iterations43-44, every possible torsion ratio has algebraic degree at most28, hence order m with phi(m)<=28 and m<=1568. All55 admissible orders including1 are exhausted. Exact integer monic division extracts positive cyclotomic factors with multiplicity. Modular gcd certificates then exclude every admissible cyclotomic polynomial from the residual. Thus both positive and negative conclusions are complete, not searches stopped at convenient orders.

At13 for b=3, the cyclotomic part is Phi_1^2*Phi_2^2. Exact division of the Gaussian polynomial exhibits beta13 once and -conjugate(beta13) once; these account for both extra E_i factors over F13bar. The source's extra CM multiplicity at17 was also2. These stable finite-field observations are necessary evidence only: Hom can grow under specialization.

At29 for b=6 the cyclotomic part is EMPTY. There is no root alpha of F such that alpha/beta29 or alpha/conjugate(beta29) is any root of unity. This rules out E_i factors over EVERY finite extension of F29, not merely rational factors over F29. All norm polynomials, divisions, residuals and modular witnesses are retained in the receipt.

## 5. One-way specialization and the congruence veto

For the literal source b=6, a hypothetical extra E_i factor over C descends to Qbar and a finite number field. Good-reduction Hom specialization at29 is faithful, so its reduction would give a nonzero geometric E_i->Q homomorphism. The complete CM-ratio certificate forbids it. Hence P_6 has E_i isogeny multiplicity exactly1, while Y3 has2, and no complex isogeny P_6~Y3 exists. No model or reduction of the fixed transcendental-period sixfold X is used.

The same argument applies to any algebraic integral b reducing to6 modulo29: the good branch-chart conditions are units, and its special fibre is the excluded source's base change. For residue23=-6 the identity

    g_(-b)(-p)=-g_b(p),   (p,w)->(-p,i*w)

gives an isomorphism of V reductions, commuting with rho there. Thus the rational sevenfold polynomial and missing-CM conclusion agree. Even when the residue field is enlarged, absence of geometric CM factors remains true. This proves the stated algebraic congruence-class exclusion. No extension to transcendental parameters or the entire b-line is claimed.

Conversely b=3's two surviving primes do not produce a characteristic-zero homomorphism, a theta-six degree, joint primitivity, End or target period data. Its finite-field extra multiplicity3 for the full source may exceed Y3's2 without contradiction: specialization may add endomorphisms and elliptic factors. It cannot exclude the complex source in that direction either.

## Continuation and trust

The remaining executable control is b=3: test another certified good split prime, or construct an actual opposite-character elliptic map and compute its primitive theta degree and joint kernel. The beta-type extra factors also need scrutiny; no complex decomposition is inferred from either prime. Varying a/lambda, the infinity-branch strata, direct cycle constructions and the birational genus-five-image route all remain open. X/alpha and denominator768/four-channel target transfers stay fixed.

Contract: `research/conjecture_net/contracts/hodge-minimal-axis-second-prime.v1.json`.
Checker/counter: `research/voevodsky/checkers/check_hodge_minimal_axis_second_prime.py`, `count_hodge_minimal_axis_second_prime.rs`.
Counts: `research/voevodsky/inputs/hodge-minimal-axis-second-prime-v1/counts.json`.

Trust: exact fresh finite-field enumeration and independent small counts, written unitary Frobenius reconstruction, complete cyclotomic certificates and standard faithful Hom specialization. Finite-field isogeny interpretation uses the semisimple Tate category. Not proof-assistant certification or independent review. Iteration44 and pins v1-v47 are retained. No invalidation of the actual b6 source, lifting of finite-field factors, full-family exclusion, target cycle or Hodge verdict is supplied.
