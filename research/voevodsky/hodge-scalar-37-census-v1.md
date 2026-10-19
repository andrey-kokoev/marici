# Global iteration51, fifth series10/10: complete regular37 screen with CM type and polarization

## Result

The entire regular denominator chart at37 is now screened, not just the next literal lift. For lambda2,b2,34 residues have certified smooth models and full degree14 Frobenius polynomials. The result is

| a mod37 | outcome |
|---|---|
|1,4,5,6,7,9,10,12,14,15,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36|no extra geometric CM factor|
|21|extra CM, but no opposite native type|
|2,8,13|opposite CM line, but3-integral complement projector contradicts fixed target norm parity|
|0,16|necessary tests survive only|
|3,11,17|displayed model uncertified, not excluded for that reason|

In particular the actual source(2,214,2), residue29, is excluded from Y3 EVEN UP TO UNPOLARIZED complex isogeny. Its source and first theta-four axis remain valid. No positive factor lifts to C.

Combining the earlier rules,8077 integral a classes mod8177 are excluded, two jointly certified necessary classes remain(3087,6623), and98 uncertified classes remain unexcluded. This replaces the previous state of36 classes not counted at37. The least-absolute lift in the JOINTLY CERTIFIED domain is now a=-1554, a new actual theta-four source passing all three necessary screens. This is not a classification of complex sources or a proof that its extra axis exists.

## 1. Full branch chart and shared exhaustive counts

For each a in F37 use W:y^2=P=x(x-1)(x-2), D=x^2-a*x+2, N=2(x^2-2), g=(y+N)/D. The checker exhausts all37 residues, testing D squarefree and coprime to P, genuine poles via gcd(D,P-N^2)=1, and degree4/squarefree special fibres P-(cD-N)^2 for c=0,+1,-1. The transverse-Weierstrass chart of iteration48 is retained; intersections with P=0 are not incorrectly labelled double branch points. Exactly a3,11,17 fail the displayed sufficient model certificate. Failure of this certificate alone is not a complex exclusion.

The new counter freshly enumerates170 ordinary rows (34 cases through degree5) and136 rho-Frobenius rows (through degree4), with the same proven primitive field moduli as iteration50. Complete multiplicative generator cycles and every Frobenius x-orbit are verified. Infinity contributes the root count of6. Poles are checked separately for EVERY a: all four are defined over F_(37^2), and in odd degrees all four are rational iff both a^2-8 and a-3 are nonzero squares. It is not a constant-pole assumption.

### Shared ordinary character identity

One orbit pass is shared across all a, avoiding34 redundant degree5 field scans. At a finite nonpole point let u=y+N and d=D. Then

    chi(g^3-g)=chi(u)*chi(d)*chi(u-d)*chi(u+d).

This follows from g^3-g=u(u-d)(u+d)/d^3 and chi(d)^(-3)=chi(d). Because-1 is a square here, chi(u-d)=chi(d-u), allowing additions with a precomputed-u. The a denominators are stepped exactly by d_(a+1)=d_a-x. Zero factors correctly give the single branch point; genuine poles are handled before the character product.

The sum over BOTH y roots is constant on each x-Frobenius orbit, even if the selected square root itself moves. Weighting by orbit length is exact. The full orbit histogram is checked by the subfield recursion, including the69343957 total elements in degree5. Every case is compared with the ORIGINAL direct g-division ordinary routine in degrees1-4. No direct degree5 enumeration is claimed; its fresh exhaustive orbit count is UNUSED in reconstruction and checks the fifth trace in ALL34 cases.

### Fast twisted character identity

The original nonsplit Lang torsor parametrizes pairs of W points with Frob_q(p)=p+kappa. For each pair, g^q=-g. In K=Fq(sqrt(nu)), nu nonsquare, write g=z*sqrt(nu), and

    g^3-g=c*sqrt(nu), c=z*(nu*z^2-1) in Fq.

For nonzero c and q=1 mod4,

    (g^3-g)^((q-1)/2)=chi(c)*nu^((q-1)/4).

Thus the fixed-lift sign is the precomputed constant i*nu^((q-1)/4), equal to+1 or-1, times chi(c). This replaces repeated quadratic-field powers; it does NOT change their criterion. If c=0, nonsquareness of nu forces z=0, and the original branch count is used. Poles and discriminant-zero torsor fibres are handled exactly as before.

The fast sign is compared against the original quadratic-field POWER at EVERY evaluated pair for every a in degrees1,2. The a4 baseline is compared against the unchanged historical twisted kernel in every degree1-4. All ordinary/twisted rows for a30 recover the preceding independent slow37 counter, which is itself freshly rerun. The checker independently enumerates ordinary degrees1,2 and direct rho Frob37 fixed points inside F_(37^4) for ALL34 cases, using digitwise Python fields, direct roots and the original g; it uses neither character acceleration nor the torsor parametrization.

## 2. Complete polynomials and native CM factors

The known first axis has beta=-1-6i at i=6, norm37, trace-2. Four Gaussian moments give a1,...,a4 with a3 nonzero in every case. Integral Gaussian reciprocity determines the remaining coefficients, and all34 unused fifth traces agree. The rational reciprocal polynomials, Gaussian coefficients and full moment data are retained.

For the now-excluded literal a214 (residue29) the Gaussian coefficients descending are

    [(1,0),(2,4),(18,30),(-125,148),(-1013,602),
     (-5994,-5106),(-30118,-21904),(50653,-303918)].

Its rational coefficients descending are

    [1,4,56,62,-118,-6844,-87879,-285100,-3251523,-9369436,
     -5977054,116197982,3883261592,10262905636,94931877133].

Power traces through degree5 are-4,-96,422,4408,-1564. Its cyclotomic part is empty, so faithful Hom specialization excludes a second complex E_i.

Each full rational polynomial receives the complete55-order cyclotomic-ratio certificate, with exact positive divisions and modular residual exclusions. For the positive cases, native type is NOT guessed from rational multiplicity. The checker substitutes beta*U and conjugate(beta)*U into the Gaussian f7 and computes exact MONIC GCDs with the positive cyclotomic factors over Q(i), repeatedly dividing all multiplicities. The full norm certificate excludes every other possible order. The sum of the two Gaussian extracted degrees must equal the complete geometric CM multiplicity. The families are disjoint because beta/conjugate(beta) is not a root of unity.

This algorithm handles factors of degree larger than one over K; it is not limited to testing four Gaussian unit roots. In this particular census the positive data are:

|a|extra same-type rank|extra opposite-type rank|opposite eigenvalue|
|---|---|---|---|
|0|0|1|-6-i|
|2|0|1|1-6i|
|8|0|1|-1+6i|
|13|0|1|6+i|
|16|1|1|-1+6i|
|21|1|0|none|

Case16 has THREE E_i factors in the SPECIAL source including the known first axis. This alone is NOT a complex exclusion: an extra special-fibre factor may come from a reduction jump in the simple sixfold. A finite upper bound of three does not contradict a complex multiplicity of two.

## 3. Typed and polarized vetoes, and conditional degree bounds

CM-absent cases exclude Y3 by the same faithful-Hom argument. For a21, equivariant Hom specialization excludes any opposite-action complex elliptic subvariety. Under an assumed unpolarized Y3 isogeny, the fixed End^0(X6)=Q(i) and signature(3,3), together with source signature(4,4), force a balanced elliptic-isotypic surface. Thus a21 is excluded even WITHOUT assuming the isogeny is K-linear. Its positive same-type CM factor is not called absent.

There is a useful improvement over using the full f8 Frobenius polynomial alone. Let u:E_i->P8 be the ACTUAL known first axis and u^dagger its polarization adjoint. Its primitive theta degree4 gives u^dagger*u=[4]. Thus e_plus=u*(1/4)*u^dagger is an integral self-adjoint projector at3. It commutes with the native action and Frobenius. The principal Tate lattice splits orthogonally into this rank-one lattice and a3-SELF-DUAL rank-seven complement L7. The complement has characteristic polynomial f7. This uses the actual first map, not an assumed polynomial projector for the known eigenvalue.

For each unique opposite line write f7=(T-gamma)*r7 and use e_minus=r7/r7(gamma) ON L7. Exact idempotent, Frobenius eigenvalue, rank-one and Rosati self-adjoint identities are checked there, with T^dagger=37/T. The earlier full-f8 projector is also retained as a control. For a2,a8,a13 the COMPLEMENT projector is3-integral. In particular a8 has a NONintegral full-f8 projector, but a UNIT complement derivative

    f7'(gamma)=-31672+58608i, gamma=-1+6i.

The full derivative unnecessarily includes gamma-beta=12i, divisible by3; splitting the known degree-four axis removes that factor. A nonunit full projector alone was inconclusive, not proof that this improvement was impossible. The same correction sharpens a16's coefficient bound from2 to1.

The self-dual lattice argument forces any primitive complex opposite axis in these three cases to have3-unit degree. It lies in L7 because opposite native actions are orthogonal. Principal determinant parity with the known degree4 axis then forces an even3-valuation on the sixfold factor, contradicting the fixed class-3. The contradiction remains valid for an arbitrary unpolarized isogeny: End(X6)=Q(i) makes its polarization space one-dimensional, rescaling changes its determinant by a SIXTH power, a K-basis change by a norm, and either K embedding preserves the parity. These are precisely the retained iteration49 hypotheses, not an implicit transfer of a principal polarization through an isogeny.

For surviving a0,16 the COMPLEMENT polynomial projectors both have coefficient denominator bound3^k with k=1. Multiplying every coefficient by3^k is checked to be integral. There is a further conditional necessary constraint, not an equality inferred from a denominator:

If a primitive opposite complex axis E exists, its saturated Tate module M specializes into the unique opposite line. In a perfect ambient lattice L, restriction L->M^* is surjective. The orthogonal projector then has image eL=(1/d)M up to a unit, where d is the restricted elliptic theta degree. If3^k e is integral, primitiveness L intersect M_Q=M gives

    0 <= v3(d) <= k.

The coefficient bound need not be sharp on the ACTUAL lattice, so it does not by itself compute d. But under the additional hypothesis of a Y3 isogeny, the same determinant argument requires v3(d) ODD. For k=1, the only possibility is

    v3(d)=1.

This conditional statement is proved for both necessary survivors. It does not construct an axis, prove degree6, determine the joint kernel or identify the residual sixfold. Without the TARGET norm hypothesis a nonunit projector proves no odd degree. The data retain both the upper bound and the conditional target values, with scope guards against conflating them.

## 4. Algebraic boxes and full scoped CRT

All32 negative a residues give algebraic integral residue-box exclusions at37 for(lambda,a,b)=(2,a,2) or(2,a,35=-2):64 boxes in total. The b sign-pair V isomorphism(p,w)->(-p,i*w) commutes with the native action. The corresponding principal source has the same Gaussian characteristic polynomial, principal3-adic lattice and actual first theta-four axis, so both type and norm arguments apply. No arithmetic reduction assertion is made for arbitrary transcendental coefficients.

Retain iteration49's201 excluded mod221 classes, joint survivor214 and19 uncertified classes. A residue mod8177 is excluded if either the old rule or a negative37 certificate applies. It survives the JOINT necessary screen only if both models/screens are certified. Otherwise it remains uncertified. The resulting disjoint partition is

    8077 excluded;
       2 jointly certified survivors:3087,6623;
      98 uncertified classes not excluded by another rule.

The98 classes include old uncertified parameters and lifts with37 model residues3,11,17. They are NOT folded into the exclusion count. A reconstruction rule, all survivor/uncertified residues and the full classification hash are retained. This is a complete finite-domain necessary screen, not sufficiency for the complex target.

The preceding generic Hom theorem remains valid: all transcendental a on the fixed lambda2,b2 line and algebraically independent scalar triples are excluded. It does not classify special algebraic a or dependent higher-parameter families. The new finite screen does not supply an equation for those exceptional Hom loci.

## 5. Next executable frontier

The centered joint survivor lifts are3087,-1554. The least absolute one is a=-1554. Exact rational branch tests give an actual source(2,-1554,2), with smooth C17/D9/B5 and primitive theta-four axis. Its residues at13,17,37 are6,10,0, all passing the necessary opposite-type screens. Its37 opposite projector bound is k=1; a hypothetical target-compatible complex axis must have v3 of its theta degree1. This does not give the axis or its full degree.

One substantive next route is a higher good-prime test of these TWO joint classes/actual lifts, or determination of the SPECIAL equivariant-map/Hom locus rather than a generic second-axis formula. For the actual source seek an opposite-action map, primitive theta-six degree and joint kernel, then prove the residual sixfold's End/simplicity and fixed-X6 period/correspondence matching before denominator768/four-channel target transfer. The98 uncertified classes, dependent parameter subfamilies, compactified sources, birational genus-five-image and direct-cycle routes remain executable. The ten-turn series ends with these gates open, not with the Hodge objective complete.

Contract: `research/conjecture_net/contracts/hodge-scalar-37-census.v1.json`.
Checker/counter: `research/voevodsky/checkers/check_hodge_scalar_37_census.py`, `count_hodge_scalar_37_census.rs`.
Counts: `research/voevodsky/inputs/hodge-scalar-37-census-v1/counts.json`.

Trust: fresh exhaustive field/orbit counts with direct, power and independent small controls; exact full polynomial, CM/native-GCD and projector certificates; written character identities and inherited faithful-Hom, saturated Tate-lattice, target End/signature/norm arguments. Not proof-assistant certification or independent review. Iteration50 and pins v1-v53 remain immutable. No positive Hom lift, complete special-locus equation, source End/simplicity computation, target cycle or Hodge verdict is supplied.
