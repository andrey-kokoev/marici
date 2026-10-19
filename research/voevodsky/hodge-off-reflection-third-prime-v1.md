# Global iteration50, fifth series9/10: prime37 and a geometric-generic Hom bound

## Result

The remaining literal source(lambda,a,b)=(2,-7,2) FAILS at good split prime37: its sevenfold complement has no geometric E_i factor. The earlier positive opposite-type reductions at13 and17 did not lift a complex second axis. The actual source construction and primitive theta-four axis remain valid, but it cannot be isogenous to the fixed Y3.

There is also a FAMILY-LEVEL consequence, not just another finite sieve. On the fixed lambda2,b2 line, the geometric generic source has exactly one E_i factor. By invariance of Hom under algebraically closed field extension, EVERY transcendental a on this line has exactly one. The same argument on the full smooth three-parameter scalar family excludes ALL algebraically independent triples(lambda,a,b). It does not exclude all algebraically dependent or all transcendental triples. No equation for the exceptional CM-jump loci is constructed.

## 1. The prime37 model and oriented elliptic factor

The source is W:y^2=x(x-1)(x-2), g=(y+2(x^2-2))/(x^2+7x+2), V:w^2=g^3-g, with the retained cyclic-four lift and principal signature(4,4) Prym P8. At37 the denominator parameter a=-7 reduces to30. The extended branch checker verifies distinct genuine simple poles, squarefree degree4 special-fibre polynomials and all good-reduction units. The displayed29-model failed its genuine-pole condition; that failure was NOT used as an exclusion.

Take i=6 in F37 and beta=-1-6i, with Norm(beta)=37 and trace-2. The actual E_i and W point counts are40; beta reduces to0 in the chosen CM orientation. The pole identity P-(a-3)x^2=xD gives four rational poles in EVERY extension here: a^2-8 and a-3 are both nonzero squares at37. Infinity contributes the square-root count of6, namely0 in odd degrees and2 in even degrees. Neither pole nor infinity normalization is copied from the earlier nonrational-pole controls.

The primitive field moduli ascending through degree5 are

    [2,1], [5,1,1], [13,1,0,1], [2,1,0,0,1], [5,1,0,0,0,1].

The Rust counter freshly verifies full multiplicative generator cycles in all fields, including the69343957-element degree5 field. Historical generic arithmetic is included unchanged. At degrees1-4 the generalized a4 routines are cross-checked against the old denominator routines. The new a30 counts use the actual denominator, not that baseline.

## 2. Exact orbit-weighted fifth count, with direct controls

For ordinary counts the program enumerates Frobenius orbits of x in F_(37^n). Every W/E contribution and the SUM over the two possible y values in a V fibre is constant on an x-orbit, because all coefficients are in F37. Thus one representative weighted by its orbit length gives the exact full sum, independently of which square root was selected. At a genuine pole that contribution is one normalized V point per W point. Infinity is added separately.

Every x is visited exactly once. Orbit lengths must divide n; both total orbit coverage and the weighted element count are checked. For n=5 there are37 singleton orbits and13868784 length-five orbits, with total weight69343957. The checker independently verifies all orbit counts by the subfield recursion

    d*N_d = 37^d - sum_(e|d,e<d) e*N_e.

The orbit-weighted ordinary routine is compared with DIRECT enumeration in every degree1-4. The degree5 count is orbit-weighted, NOT claimed to be a second direct enumeration. It is still a fresh exhaustive count; no fifth trace is predicted and written into the data. Direct rho-Frobenius torsor enumeration supplies twisted counts through degree4, including discriminant-zero fibres.

Independent digitwise Python fields directly verify ordinary degrees1,2 and rho Frob37 fixed points inside F_(37^4), without reusing Rust chunk tables, orbit weights or the torsor parametrization.

The resulting ordinary(W,V,E) counts are

    n1: (40,50,40)
    n2: (1440,1478,1440)
    n3: (50440,50456,50440)
    n4: (1872000,1869750,1872000)
    n5: (69356200,69324890,69356200).

All have4 rational poles. The W/E moments also agree with independent powers of the known beta.

## 3. Full polynomial and geometric CM exclusion

Subtracting the known first axis, the four Gaussian moments are

    -4-6i, 16+4i, -115-306i, 44+808i.

Newton identities give a3=-43+58i, nonzero. Unitary reciprocity determines the remaining coefficients; all integrality and reciprocity identities are checked. The sevenfold Gaussian coefficients descending are

    [(1,0),(4,6),(-18,22),(-43,58),(-391,200),
     (-5550,3182),(-43808,-41070),(50653,-303918)].

The rational degree14 coefficients descending are

    [1,8,16,34,378,-7728,-65743,-345364,-2432491,-10579632,
     19146834,63721474,1109503312,20525811272,94931877133].

The rational power traces through degree5 are-8,32,-230,88,43552. The fifth is UNUSED in reconstruction and agrees with the fresh orbit-weighted ordinary count.

The exact norm F(beta U)F(conjugate(beta)U), degree28, is tested against all55 possible cyclotomic orders including1. The same proved exhaustive bound and exact division/residual modular witnesses are used as before. There are NO positive factors. Thus the complement contains no geometric E_i, even after any finite residue extension; the source has exactly the one known E_i factor.

Faithful good-reduction Hom specialization excludes a second complex E_i for the literal a=-7 control. More generally algebraic integral(lambda,a,b) reducing at a place over37 to(2,30,2) or(2,30,35=-2) have the same exclusion. The sign-pair isomorphism(p,w)->(-p,i*w) is actual and native-equivariant. These algebraic residue assertions alone do not cover arbitrary transcendental coefficients. The additional generic argument below has a different domain and proof.

## 4. Generic rank: an exclusion beyond algebraic residue boxes

### Family and specialization

Let U be the nonempty smooth scalar-source open in the three-parameter space over Q(i), with the retained T_lambda, anti-kappa function g, free cyclic-four cover and its principal Prym P->U. This is an algebraic family; normalizations can equivalently be described as the smooth double covers with the simple branch divisors used in the model certificate. Remove the finitely specified discriminant/pole/infinity boundaries, not any conjectural target locus. The point(2,-7,2) lies in U. The parameter space, and this dense open, are irreducible.

The actual curve maps to the constant E_i give a nonzero homomorphism E_i->P throughout this family (up to the already licensed isogeny). Consequently geometric Hom(E_i,P) has Z-rank AT LEAST2, from End(E_i)=Z[i]. Primitivity is not needed for this lower bound.

For abelian schemes with good reduction, a geometric generic Hom specializes INJECTIVELY, after the finite field extension needed to define it. This is the same rigidity/prime-to-residue-characteristic Tate-module fact used for earlier vetoes. In characteristic zero, apply it along the smooth specialization flag

    lambda=2, then b=2, then a=-7.

The generic points of this flag lie in U, since its final point does. Finite extensions can be followed by extensions of the corresponding DVRs; good reduction persists. Finally specialize the literal fibre at its good place37. The special fibre has precisely one E_i isogeny factor by the complete certificate above, so Hom from E_i has Z-rank2 (its ordinary endomorphism field is Q(i)). Therefore

    2 <= rank Hom(E_i,P_geometric_generic) <=2.

The same squeeze applies to the geometric generic a-line at fixed lambda2,b2 and to the literal characteristic-zero a=-7 fibre. Each has CM multiplicity exactly1. No positive finite-field factor is lifted: the argument is a lower bound from an ACTUAL global axis plus an upper bound from injective specialization.

### Why every transcendental a on the fixed line is covered

For abelian varieties over an algebraically closed field k, extension to another algebraically closed field adds no new Hom. This standard rigidity/basechange theorem is essential here.

If a is transcendental over Qbar, substitution t->a identifies Qbar(t) with Qbar(a). The fibre at a is the geometric generic a-line fibre after such a field identification and algebraically closed extension to C. Its Hom rank is thus2, not4. All transcendental a automatically avoid the algebraic boundary polynomials on this fixed line. Hence EVERY such source has only one E_i and cannot be isogenous to Y3, which has two. This is not merely an assertion outside an unspecified countable analytic exceptional set.

Likewise an algebraically independent triple(lambda,a,b) over Qbar identifies the universal rational function field with the coefficient field of that tuple. The same geometric-generic rank2 persists on extending to C. Such triples automatically lie in the algebraic smooth open. They are all excluded from the fixed target isogeny class.

This DOES NOT cover every tuple with a transcendental coordinate: algebraically dependent tuples may lie on special subfamilies with extra Hom, even when some coordinates are transcendental. Nor does generic Hom rank2 prove simplicity or compute the End algebra of the sevenfold complement. On the fixed line, any extra-CM source must have ALGEBRAIC a, but this supplies no equation or exhaustive list of those special a values. For the full family an extra axis requires an algebraic parameter relation; it is not proved to lie on one single globally constructed hypersurface. Compactified or different source families are outside U.

## 5. Scoped CRT update and next actual source

Lift the iteration49 partition mod221 to mod8177=221*37. A class is excluded if its old residue is excluded OR its residue mod37 is30. This is not a full third-prime census. The resulting complete rule classifies

    7457 excluded classes;
      36 previous two-prime survivor lifts NOT counted at37;
     684 previously uncertified classes not excluded by the new rule.

There are20 new exclusions beyond the lifted old rule,19 from the old uncertified set and one from the old survivor214. The latter is8170=-7 mod8177. Arrays of the newly excluded and remaining two-prime classes, an explicit reconstruction rule and the full classification hash are retained. Untested classes are not declared to pass prime37.

Among centered representatives of the36 previous-screened classes, the least absolute one is a=214. Exact Q-branch checks construct the actual source(2,214,2), with smooth C17/D9/B5, native signature(4,4) and primitive theta-four axis, outside the known reflection loci. It has residues6 and10 at13 and17, hence inherits their opposite-type necessary screens. Its37 branch chart passes at residue29, but its37 Frobenius/CM profile is UNCOMPUTED. This is a height choice only in the already screened domain, not a global minimum or a target match.

The family-level result argues against searching for a universal generic second axis. A useful continuation is to determine the SPECIAL algebraic Hom/equivariant-map locus or compute remaining37 profiles, starting with a214 if pursuing the arithmetic sieve. Any actual opposite-action map still needs primitive theta degree/joint kernel, residual-sixfold End/simplicity and fixed-X6 periods/correspondences. Target denominator768/four-channel transfer, other dependent parameter families, uncertified/compactified sources, birational genus-five-image and direct-cycle routes remain open.

Contract: `research/conjecture_net/contracts/hodge-off-reflection-third-prime.v1.json`.
Checker/counter: `research/voevodsky/checkers/check_hodge_off_reflection_third_prime.py`, `count_hodge_off_reflection_third_prime.rs`.
Counts: `research/voevodsky/inputs/hodge-off-reflection-third-prime-v1/counts.json`.

Trust: fresh exhaustive field/orbit counts, direct small controls and exact polynomial/CM certificates; written specialization over regular flags, invariance of Hom under algebraically closed field extension, retained universal algebraic source and actual first-axis constructions. Not proof-assistant certification or independent review. Iteration49 and pins v1-v52 remain immutable. No positive Hom lift, special-Hom-locus classification, generic simplicity theorem, target cycle or Hodge verdict is supplied.
