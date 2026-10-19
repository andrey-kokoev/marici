# Global iteration 29 (third series 9/10): exhaust the nonlifting diagram

## Result and boundary

The512 nonlifting labels cannot realize the fixed canonically principally polarized (Y2,theta2). Together with the previous exclusions this closes the entire **conditional bielliptic-intermediate branch** of the smooth etale cyclic-quartic route, for this fixed polarization.

The conditional polarized survivor count is now **0 labels / 0 inverse pairs**. The unpolarized isogeny count remains **516 / 258**: this argument again uses the actual elliptic theta-degree-two axis and does not transport that degree unchanged across arbitrary isogenies or changes of principal polarization.

A smooth etale cyclic-quartic realization of this fixed Y2 would consequently require dim Sing(theta2)<=3. This is a conditional necessary inequality, NOT an actual theta-dimension computation or an unconditional exclusion of all cyclic-quartic or other Prym presentations. No Hodge verdict follows.

## 1. The two degree-four maps and their h-actions

Assume a nonlifting label gives a hypothetical tower C=C17 -> C9 -> C5 with canonical principal Prym Y2, and that C9 has its bielliptic double cover q9:C9->E. Let h be the free deck involution of C/C9 and b the bielliptic involution on C9. Nonlifting means **b has no lift to C**, as proved by the norm/torsion criterion in iteration20, not merely that one selected formula fails to lift it.

Put q=q9 composed with C->C9, a degree-four map. Then q h=q, so h acts as identity on its target map.

The actual elliptic theta-degree-two subcurve T of Y2, followed by the Prym inclusion in J(C), has Jacobian theta degree four because the etale Prym restriction is twice principal. Polarization adjunction and Jacobian norm/pullback functoriality give a degree-four map phi:C->T, exactly as derived in iteration28. Anti-h Prym cohomology gives, for some c in T,

    phi h = c-phi.

The translation c reflects the Abel-Jacobi basepoint choice and is harmless. The involution r(t)=c-t has four fixed values: solutions of [2]t=c. No choice c=0 is assumed.

Let B be the normalization of the joint image of (q,phi):C->E times T, and d=deg(C->B). Since d divides both map degrees,

    d in {1,2,4}.

No coprimality or birationality is assumed before analyzing these three cases.

## 2. Joint degree four: invariant/anti-invariant contradiction

If d=4, the induced B->E and B->T both have degree one. Thus B is isomorphic to E and phi factors through q. Then phi h=phi, whereas phi h=c-phi. This would make [2]phi=c constant, impossible for a nonconstant degree-four map in characteristic zero.

This case is excluded without using the genus bound or making any elliptic non-isogeny assumption.

## 3. Joint degree one: equality forces a smooth image and fixed points

If d=1, C is the normalization of an integral image curve Gamma in E times T with projection degrees(4,4). The Hodge-index/adjunction argument of iteration28, including all possible correspondence terms, gives

    17=g(C) <= p_a(Gamma) <= 1+4*4=17.

All inequalities are equalities. In particular the sum of local normalization defects is zero, so Gamma is smooth and C->Gamma is an isomorphism. This is essential: if Gamma had nodes, an involution could fix an image point while exchanging its normalization branches. Genus equality rules out that escape.

The ambient involution H(e,t)=(e,c-t) preserves Gamma and induces h on its normalization. Pick any fixed value t0 of r on T. Since the projection Gamma->T has degree four, it meets E times {t0}; the fibre is a nonempty effective divisor of degree four. Every point of this intersection is fixed by H, hence gives a fixed point of h on the smooth curve Gamma=C. This contradicts the etaleness of C->C9.

Ramification of phi does not avoid the contradiction. We require only nonempty support in a positive-degree fibre, not four distinct points over each t0, and do not claim sixteen distinct fixed points. Both equality and freeness are explicit hypotheses in the finite negative controls.

## 4. Joint degree two: a forbidden lift is constructed

If d=2, write a:C->B for the quadratic map, and q_B:B->E, phi_B:B->T for the induced degree-two maps. The latter joint image is birational by construction and gives g(B)<=5, although this genus bound is not needed to build the lift.

The relation (q,phi) h=(q,c-phi) shows that h descends to an involution tau of B. Tau is NONTRIVIAL: if it were identity, phi h=phi would again force [2]phi constant.

Let sigma be the nontrivial deck involution of the degree-two map a. It exists in characteristic zero. Since h descends to B it normalizes the deck group {1,sigma}, so h sigma=sigma h. Moreover h is not sigma, since sigma acts trivially on B whereas h induces nontrivial tau.

Therefore sigma descends to a nontrivial involution bar_sigma on C9=C/<h>. It preserves q9: the map q=q_B a is sigma-invariant. Since q9 has degree two, its only nontrivial deck automorphism is b. Hence

    bar_sigma=b.

We have explicitly obtained an involutive lift sigma of b to C, contradicting the nonlifting criterion. We did not assume a lift merely from uniqueness of b, and we did not assume sigma initially normalizes the cyclic-four generator rho. The existing criterion proves that any such b-lift is impossible in these512 labels.

A V4 permutation control on a generic four-point fibre checks the quotient/descent pattern: h and sigma are distinct commuting involutions, and sigma acts nontrivially on the h-quotient. This control illustrates the written quadratic function-field argument; it is not a replacement for its geometric proof.

## 5. Complete conditional census and the theta gate

The earlier reductions cover all root labels in the conditional branch (with hyperelliptic-bottom alternatives already excluded). Per fixed (C5,k,zeta), the partition is

    1024 = 256 norm-zero + 252 mixed commuting + 4 scalar + 512 nonlifting.

The first two classes fail even the fixed unpolarized A-isogeny comparison, the scalar class fails the fixed principal polarization by iteration28, and the nonlifting class fails it by the three cases above. Thus no labels remain for a fixed polarized Y2 realization in this branch. There is no new unpolarized exclusion; its516/258 count remains unchanged. Old receipts retain their historical scoped counts.

The retained Mumford equality theorem and the free intermediate involution had given: for a hypothetical smooth etale cyclic-quartic realization, theta dimension>4 is impossible, and dimension4 forces a bielliptic C9 because the trigonal alternative was excluded. The new branch exclusion rules out that dimension4 possibility as well. Consequently:

| Actual dim Sing(theta2), if supplied | Consequence for this fixed smooth etale cyclic-quartic presentation |
|---|---|
| unknown | no actual dimension selected |
| >=4 | excluded |
| <=3, including empty singular locus | not excluded by this theta gate |

This does not assert that theta dimension is actually<=3; the inequality is necessary only IF the realization exists. Nor does it rule out an arbitrary noncyclic smooth etale Prym presentation, other polarizations, ramified/admissible constructions or the unpolarized isogeny routes.

## 6. Next executable work and trust

Obtain a valid theta lower bound or actual dimension from the fixed degree-two elliptic axis and explicit gluing, or investigate nonbielliptic intermediates in the remaining theta<=3 branch. Other principal models/isogenies and direct non-divisor cycles on X remain available. The four exceptional channels, original X/alpha, phase48i and denominator48 are unchanged. No exceptional algebraic cycle, all-cycle theorem, independent review or Hodge verdict exists.

Contract: `research/conjecture_net/contracts/hodge-nonlifting-polarized-obstruction.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_nonlifting_polarized_obstruction.py`.
Receipt: `research/voevodsky/results/hodge-nonlifting-polarized-obstruction-v1.json`.

    python research/voevodsky/checkers/check_hodge_nonlifting_polarized_obstruction.py

Trust boundary: fresh predecessor/source/target receipts, exact map-degree/genus/group/count controls and the written normalization-defect, reflection, finite-cover and descent arguments; Mumford's previously retained conditional theorem remains an explicit import. Not proof-assistant verification or independent review. Iteration28 and immutable pins v1-v30, including intermediate v28, are preserved.
