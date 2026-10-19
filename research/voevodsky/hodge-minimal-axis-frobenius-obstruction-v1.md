# Global iteration 43 (fifth series 2/10): the explicit theta-four source lacks the second CM elliptic factor

## Result

The actual source of iteration42 remains valid, with its primitive theta-four elliptic axis and auxiliary algebraic determinant classes. However **this particular source is not isogenous over C to the fixed Y3**. Its complementary sevenfold Q has no elliptic isogeny factor isogenous to E_i. Thus the source contains exactly one E_i up to isogeny, while Y3 contains two.

This rejects only parameters(lambda,a,b)=(2,4,2). It does not exclude the anti-translation family, compute its End, prove Q simple, or supply a target cycle. In fact the reduction polynomial of Q factors in degrees4 and10; a simple-reduction shortcut would be false.

## 1. Good reduction and counts

Use the explicit iteration42 V9/W1 and its degree-two polarized isogeny to the principal source P. Up to Q-isogeny,

    J(V) ~ J(W) x P ~ J(W) x E_i x Q7.

The elliptic maps, source, and complementary abelian subvariety are defined over Q. At17, exact gcd tests on the three special-fibre quartics and pole denominator certify good reduction. The elliptic curves and degree-two isogenies also have good reduction there. The same displayed branch model degenerates at5 and13, so those primes are NOT used as good-reduction evidence.

The crate-free Rust counter reruns ordinary counts through degree5 and rho-twisted counts through degree4. Every field representation is certified by a complete nonzero generator cycle. Infinity on W has g=2, giving1+chi(6) points on V; each genuine simple pole has one normalized V point.

| n | #W(F17^n) | #V(F17^n) | #E_i(F17^n) | #Fix(rho Frob^n) on V |
|---|---:|---:|---:|---:|
|1|16|8|16|16|
|2|320|336|320|272|
|3|5008|5000|5008|4768|
|4|83200|82096|83200|83072|
|5|1417616|1410248|1417616|not used|

Independent digitwise Python arithmetic directly enumerates the ordinary degree1,2 counts. It also checks rho Frob17 fixed points directly in F17^4, rather than reusing the Rust torsor parametrization. Both implementations agree.

## 2. How the twisted count is actually computed

On V, rho(p,w)=(p+k,i w), with k=(0,0) on W and i=4 in F17. Its base fixed-point condition is Frob^n(p)=p+k. These points form a Lang torsor with exactly #W(Fq) points, q=17^n.

Use the rational quotient

    Z:Y^2=X^3+6X^2+X,
    X=x-3+2/x, Y=y(1-2/x^2).

The nonsplit fibres over Z(Fq) parameterize the torsor. For a given X, solve x^2-(X+3)x+2=0 in Fq^2, then y=Y/(1-2/x^2). The discriminant-zero case is handled separately; its fibre may instead be nonsplit in y. Rational kernel fibres are split and omitted. The counter verifies the recovered W equation and the total Lang torsor count.

Since g(p+k)=-g(p), a=g^3-g is anti-invariant under q-Frobenius. For a nonzero finite value, a^((q-1)/2)=+i or-i. The equation rho Frob(w)=w requires w^q=-i w, so its fixed-fibre size is

    1+i*a^((q-1)/2), either0 or2.

A zero or simple pole gives one normalized point. Paired torsor points give equal counts because q=1 mod4. These formulas count genuine fixed points, not a guessed quartic character sum.

## 3. Complete sevenfold polynomial from FOUR Gaussian moments

Let beta=1+4i be the E_i Frobenius on the rho=i eigenspace. Its norm is17, its trace is2, and beta reduces to0 at the chosen i=4 prime, fixing its orientation. Lefschetz gives

    Tr(Frob^n|P) = #W-#V,
    Tr(rho Frob^n|P) = #W-#Fix(rho Frob^n,V).

If z_n is the Gaussian trace of Frob on Q's rank-seven i-character space, then

    z_n=(Tr(Frob^n|P)-i Tr(rho Frob^n|P))/2-beta^n.

The first four are

    3-4i, 7-32i, 51-68i, 391+176i.

Newton's identities yield the first four coefficients a_j of the monic Gaussian characteristic polynomial f of degree7:

    a1=-3+4i, a2=-7+4i, a3=-51-32i, a4=-77-236i.

Polarized K-linear Frobenius has the unitary reciprocity identity

    a_(7-j)=a7*conjugate(a_j)/17^j.

Because a3 is nonzero, a7=17^3*a4/conjugate(a3) is determined, followed by a5,a6. This is a full polynomial reconstruction theorem in this case, NOT an assertion that four ordinary moments determine a general sevenfold. If a3 were zero, this reconstruction would not be licensed. The Gaussian coefficients, descending, are

    1,
    -3+4i,
    -7+4i,
    -51-32i,
    -77-236i,
    391-408i,
    5491-2312i,
    -4913+19652i.

Multiplying f by its conjugate gives the complete rational characteristic polynomial

    F(T)=T^14-6T^13+11T^12-28T^11-39T^10-186T^9
         +8187T^8-47048T^7+139179T^6-53754T^5
         -191607T^4-2338588T^3+15618427T^2
         -144825414T+410338673.

The unused degree-five ordinary count predicts and verifies trace5126, after traces6,14,102,782. Full reciprocity is checked. The middle coefficient is8 mod17, so Q's reduction is ordinary. There is the exact factorization

    F=(T^4+2T^3+2T^2+34T+289)
      *(T^10-8T^9+25T^8-96T^7+86T^6+1296T^5
        +1462T^4-27744T^3+122825T^2-668168T+1419857).

This is a reduction factorization, not a lifted factorization of the complex sevenfold. No absolute-simplicity claim is made.

## 4. Exclude the SPECIFIC extra square-lattice elliptic factor

An E_i factor over F17bar would be defined, with its nonzero homomorphism, over some finite extension. A Frobenius root alpha of F would then satisfy alpha^m=beta^m or conjugate(beta)^m. Thus alpha/beta (or alpha/conjugate(beta)) would be a root of unity.

Construct the exact rational integer polynomial of degree28

    N(U)=F(beta U)*F(conjugate(beta) U).

Its roots include all these possible ratios. Such a ratio has algebraic degree at most14*2=28. Hence its order m has phi(m)<=28; the bound phi(m)^2>=m/2 makes the exhaustive search m<=1568. There are55 admissible orders INCLUDING order1, the largest being90. This is a proved finite enumeration, not a numerical cutoff.

For each cyclotomic polynomial Phi_m, a coprime modular gcd with N rules out divisibility over Q. Prime101 eliminates54 orders, leaving50; prime103 eliminates50. Both primes avoid the leading coefficient's factor17. The certificate includes all orders and the exact degree28 norm polynomial. Therefore **no root of F differs from either E_i Frobenius root by ANY root of unity**. This rules out E_i factors over every finite extension, without claiming that all roots of F have non-torsion ratios to each other or that there are no other elliptic factors.

## 5. Why this excludes the complex target match

A hypothetical complex E_i factor of Q would give a nonzero homomorphism E_i->Q. Since both abelian varieties are defined over Q, rigidity descends the homomorphism to Qbar and a finite number field. At a prime over17, faithful specialization of Hom for good-reduction abelian varieties would give a nonzero homomorphism of their geometric reductions. The preceding certificate forbids that. Thus Q has no E_i factor over C.

The constructed source P consequently has E_i isogeny multiplicity exactly1; Y3 has multiplicity2, from its actual saturated E_i^2 surface and simple sixfold complement. Hence **P is not isogenous to Y3 even over C**, independently of the principal polarization. This argument does not require reducing the fixed transcendental-period X or producing a number-field model of Y3.

The source, its theta-four axis, ramified diagram and auxiliary Schoen classes are retained. What fails is this one proposed source-to-target transplant, not the theorem or the scalar branch as a whole.

## 6. Continuation and trust

Vary the anti-translation parameters to seek the missing opposite-character E_i axis, testing good-prime CM-ratio obstructions before expensive target period comparisons. A surviving finite-field profile would still not lift a complex CM factor or identify X6/Y3. The separate birational genus-five-image route remains open, as do direct cycles and broader sources. Original X/alpha and denominator768/four-channel transfers are unchanged.

Contract: `research/conjecture_net/contracts/hodge-minimal-axis-frobenius-obstruction.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_minimal_axis_frobenius_obstruction.py`.
Counter/data: `research/voevodsky/checkers/count_hodge_minimal_axis_frobenius.rs`, `research/voevodsky/inputs/hodge-minimal-axis-frobenius-v1/counts.json`.

Trust: written Lefschetz fixed-point, K-linear polarized Frobenius reciprocity, root-of-unity/cyclotomic and Hom descent/specialization arguments; complete fresh field enumeration, independent small counts, exact coefficient identities and modular certificates. Not proof-assistant certification or independent review. Iteration42 and immutable pins v1-v45 are preserved. No End0 calculation, family exclusion, fixed-target cycle or Hodge verdict is supplied.
