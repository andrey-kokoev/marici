# Global iteration 27 (third series 7/10): localize the scalar family

## Result and scope

Fix the preceding rational cyclic-four elliptic isogeny psi:E->E' and E':y^2=h(x)=x(x-1)(x-25). There is an explicit seven-dimensional scalar branch chart with:

- an immersive Prym period map, hence a quasi-finite algebraic map to principally polarized eightfold moduli;
- a geometrically simple generic Prym, and simple very general complex fibres;
- at most countably many parameters realizing the fixed nonsimple A/Y2 isogeny class;
- an entire seven-adic residue class whose rational fibres are absolutely simple and thus cannot realize A/Y2.

None of these statements makes the target parameter set empty or finite. Other level isogenies, the four marked scalar labels, the 512 nonlifting labels, target theta dimension, and the cycle/Hodge gates remain open. No Zariski-open locus of all simple fibres is asserted.

## 1. Explicit chart and a deliberately sufficient discriminant

Put L=O_E'(4O), and let M have exact order four with M^2=zeta nonzero in Pic^0(E')[2], the character line bundle of psi. Sections of L^2 have the eight-element pole-order basis

    1,x,y,x^2,xy,x^3,x^2*y,x^4.

Their pole orders at O are 0,2,3,4,5,6,7,8. Riemann-Roch gives h0(L^2)=8, so these are a basis. Normalize the x^4 coefficient to one and write

    s=x^4+a3*x^3+a2*x^2+a1*x+a0 + y*(b2*x^2+b1*x+b0).

Coordinates are (a0,a1,a2,a3,b0,b1,b2) in A^7. For A(x)=x^4+...+a0 and B(x)=b2*x^2+b1*x+b0, define the monic degree-eight norm

    N_s(x)=A(x)^2-h(x)*B(x)^2.

Use the principal open S where Disc_x(N_s) is nonzero. Squarefree norm is SUFFICIENT for the eight branch zeros on E' to be simple: a multiple zero on E' would force a repeated norm root. It is not necessary. In particular B=0 and A=x^4-2 has eight simple branch zeros on E', although N_s=A^2 has repeated x roots. The checker retains this negative control to prevent conflating this convenient chart with the whole smooth scalar family.

At s0=x^4+y-2, coordinates (-2,0,0,0,1,0,0),

    N_s0=x^8-4x^4-x^3+26x^2-25x+4.

Its reduction modulo seven is squarefree. Thus S is nonempty, geometrically integral and dense in the seven-dimensional normalized chart. The elliptic isogeny pullbacks give smooth connected curves of genera5,9,17 and an etale C17->C9 Prym P_s of dimension eight. Branching also proves the double covers connected. The fixed x^4 leading coefficient excludes a branch zero at infinity and preserves the preceding normalized pole convention.

## 2. Prym eigenspaces and a pencil isomorphism

Let delta generate the cyclic-four deck group and epsilon be the square-root sheet involution. The anti-delta^2 holomorphic forms are the delta eigenvalues i and -i, each of dimension four. The elliptic character decomposition identifies these spaces, up to swapping signs, as

    V_i=H0(E',L tensor M),
    V_-i=H0(E',L tensor M^-1).

Write A_bundle=L tensor M and B_bundle=L tensor M^-1. Both have degree four and h0=4. Choose a base-point-free pencil U in H0(A_bundle). Such pencils exist: the bad pencils contained in H0(A_bundle(-p)) have Grassmannian dimension two for each p, hence their union has dimension at most three in Gr(2,4), of dimension four.

The pencil sequence tensored with B_bundle is

    0 -> M^-2 -> U tensor B_bundle -> L^2 -> 0.

M^-2=zeta is a NONTRIVIAL degree-zero line bundle. On an elliptic curve h0(zeta)=h1(zeta)=0. Therefore multiplication is an isomorphism

    U tensor H0(B_bundle) -> H0(L^2), dimensions 8 -> 8.

The full multiplication V_i tensor V_-i ->H0(L^2) consequently has rank eight, domain dimension sixteen, and kernel dimension eight. This is a cohomological pencil argument, not a claimed computed 16-by-8 coordinate matrix or an eight-dimensional Hodge kernel on X.

## 3. Differential and finite polarized fibres

The standard Prym period differential is dual to multiplication of anti-involution holomorphic forms. Restricting to deck-invariant scalar deformations picks precisely the cross product above. On E' the product is viewed as a quadratic differential with simple poles on D=(s=0), by division by s. Thus the codifferential lands in

    H0(E',K_E'^2(D)) = H0(L^2), dimension eight.

This formula follows from the Kodaira-Spencer/Serre-duality pairing: the derivative of H1 is cup product with the deformation class, whose dual pairs two holomorphic one-forms by multiplication. Nonzero descent constants do not change rank.

For fixed E', branch points modulo translations have dimension seven. More explicitly the pointed-elliptic deformation sequence has the branch-motion subspace of dimension 8-1=7, with the remaining direction varying E'. Fixing O(D)=L^2 removes translations infinitesimally: translating a degree-eight divisor changes its Picard class by multiplication by eight, nonzero in characteristic zero. Therefore our seven-parameter chart has injective Kodaira-Spencer map into that eight-dimensional deformation space.

Surjectivity of the full eight-dimensional codifferential restricts to a surjective map onto the seven-dimensional chart cotangent. The scalar Prym period map is immersive at every point of S. After a finite level cover to remove moduli automorphisms it is an algebraic map to fine ppav moduli with zero-dimensional fibres. Finite type then gives finite fibres; forgetting level preserves quasi-finiteness. The compatible unitary period domain has dimension 4*4=16, not seven or eight.

A fixed complex abelian variety has only countably many isogeny targets: every target is a quotient by a finite subgroup after choosing an isogeny in the appropriate direction, and torsion is countable. Each quotient has at most countably many principal polarizations (the Neron-Severi group is finitely generated). Since each polarized isomorphism class has finite inverse image in S, the fixed A/Y2 isogeny class has at most COUNTABLY many parameters in S. It need not be finite, empty, or Zariski closed; countability does not prevent Zariski density.

## 4. Generic simplicity, not all-fibre simplicity

The preceding absolute-simplicity receipt supplies a geometrically simple fibre at s0. For an abelian scheme over a smooth integral characteristic-zero base, rational endomorphisms of the geometric generic fibre inject under specialization into a geometric fibre, after extending the definition field as needed. This is the usual good-reduction Hom/endomorphism rigidity statement; a nontrivial idempotent cannot disappear at a smooth fibre. Hence a nontrivial generic abelian factor would contradict simplicity of P_s0. The geometric generic Prym is simple.

This also yields very general simplicity without a claimed effective discriminant for decompositions: all seven coordinates algebraically independent over Qbar realize the geometric generic family after embedding its field into C. Such coordinates lie outside a countable union of proper Qbar-polynomial zero loci. It does NOT follow that every smooth fibre is simple, or that the simple locus is Zariski open. The previous even section is a smooth nonsimple square-of-fourfolds control in the full scalar family.

## 5. A complete arithmetic residue class

For rational parameters integral at seven with

    (a0,a1,a2,a3,b0,b1,b2) = (5,0,0,0,1,0,0) mod7,

the normalized section, elliptic curves and fixed level isogeny reduce to exactly the preceding model. N_s reduces to N_s0, so its discriminant is a seven-adic unit. The smooth double covers, etale quotient and Prym have the same good special fibre as s0. The established absolutely simple reduction therefore proves absolute simplicity of every such rational fibre and excludes its isogeny to A/Y2.

This includes infinitely many native parameter choices, for example a0=-2+7t for integer t. It is not a claim about distinct unmarked moduli or isogeny counts. Rational denominators prime to seven are allowed and reduced by modular inversion, NOT integer truncation; the checker includes a0=-2+7/2 as a control. Seven-divisible denominators lie outside this sieve's stated domain. Parameters outside the residue vector are UNKNOWN to this sieve, never admitted targets.

There is no transfer of algebraic cycles from characteristic seven to the fixed X. Simple good reduction is used only in the licensed endomorphism/idempotent specialization direction.

## 6. Next work and verification boundary

Seek special 6+2 correspondences outside the excluded residue class, vary the scalar level/isogeny data, study the 512 nonlifting labels, or obtain actual target theta information and direct non-divisor cycles. Blindly matching a generic member of this fixed seven-parameter chart cannot realize the nonsimple target. All four exceptional transfer channels and the unchanged516-label conditional census remain necessary.

Contract: `research/conjecture_net/contracts/hodge-scalar-family-localization.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_scalar_family_localization.py`.
Receipt: `research/voevodsky/results/hodge-scalar-family-localization-v1.json`.

    python research/voevodsky/checkers/check_hodge_scalar_family_localization.py

The checker recomputes rational norms, modular controls and the fresh absolute-simplicity predecessor. Rank and genericity conclusions use the written elliptic Riemann-Roch, pencil, Prym differential, algebraicity and specialization lemmas; they are not numerical period inversion or proof-assistant verification. Independent review and all Hodge research gates remain open. Preserve iteration26 and immutable pins v1-v27. Intermediate pin v28 is also retained: a regression exposed a timeout while refusing an existing pin after expensive verification. The successor v29 checks refusal first and uses exclusive file creation; it does not skip fresh verification when creating a new pin or checking an existing one.
