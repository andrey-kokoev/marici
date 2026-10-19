# Global iteration 42 (fifth series 1/10): an actual scalar source with a primitive theta-four axis

## Result

Fresh iteration41 leaves a scalar elliptic-isogeny branch for the exact principal Y3 problem. This turn constructs an **actual** smooth source in that shape, not just local Kummer profiles. It has:

- a free cyclic-four tower C17->D9->B5;
- a canonical principally polarized Gaussian Prym P of dimension8 and signature(4,4);
- a primitive embedded square-lattice elliptic curve in P of **theta degree4**;
- an actual ramified auxiliary V9/W1, branched at16, with induced polarization type(1^7,2), and a degree-two polarized isogeny P(V/W)->P;
- algebraicity of its auxiliary determinant-character classes by the retained Schoen theorem.

**P is not identified with Y3.** No opposite-character theta-degree-six axis, joint CM elliptic surface, complementary End calculation, target isogeny/period match or exceptional target cycle is supplied. In particular the degree-two joint map to TWO CM elliptic targets from iteration41 has not been constructed. This source realizes the scalar square, ramified diagram and first primitive axis, not every condition of that branch.

X, alpha and Y3's degree256/phase768i/denominator768/four-channel maps are unchanged. No Y2 polarized exclusion is transported to this source.

## 1. Explicit elliptic curves, the degree-two map and a cyclic-four translation

Work over C, with equations and maps over Q(i):

    W: y^2=x(x-1)(x-2),
    T: v^2=t^3+4t,
    tau:T->W,
      x=(t+2)^2/(4t),
      y=v(t^2-4)/(8t^2).

This is the dual degree-two isogeny obtained by quotienting W at its two-torsion point(1,0). Direct substitution verifies the equation; tau extends across poles as a morphism of projective elliptic curves. Its kernel is {O,(0,0)} on T, so it is unramified.

Let k=(0,0) on W, and kappa=(-2,4i) on T. Then tau(kappa)=k. On T the tangent slope at kappa is -2i and doubling gives2kappa=(0,0), so kappa has exact order4. Consequently

    Z=W/<k>=T/<kappa>

is elliptic, and T->Z is an etale cyclic-four isogeny. This is not multiplication-by-two with a noncyclic kernel. No identification of Z or T with a target axis is required.

Translation by k on W is

    x -> 2/x, y -> -2y/x^2.

Put

    D=x^2-4x+2, N=2(x^2-2),
    g=(y+N)/D.

Then x^2 D(2/x)=2D(x), x^2 N(2/x)=-2N(x), and the y transformation gives **g(p+k)=-g(p)**. This anti-translation identity is what permits the order-four lift below; a generic unrelated elliptic rational function would not do so.

## 2. Complete smoothness check at the four special values

The poles of g are the four points over D=0. D is squarefree, gcd(D,x(x-1)(x-2))=1, and gcd(D,P-N^2)=1, so all four poles are simple and genuine; no numerator cancellation is hidden. At the point at infinity of W, g has value2, not0,1,-1 or infinity.

For c=0,1,-1, imposing g=c gives y=cD-N. The x-coordinates satisfy F_c=P-(cD-N)^2, with P=x(x-1)(x-2):

    F0 = -4x^4+x^3+13x^2+2x-16,
    F1 = -x^4-7x^3-7x^2+50x-36,
    F-1 = -9x^4+25x^3-7x^2-14x-4.

Each is degree4 and squarefree over Q, and coprime to P. Each root thus selects one non-two-torsion W-point with the displayed y, and all four intersections with g=c are simple. The checker computes the exact Euclidean gcd certificates, not sampled numerical roots. These checks exhaust all special fibres, including infinity.

Hence g:W->P1 has degree4 and is unramified over the four branch values of

    E_i: w^2=z^3-z -> P1_z.

The fibre product

    V: w^2=g^3-g over W

is therefore a smooth connected projective curve of genus9. The affine equation is understood through its smooth projective fibre product/normalization, not as a claim that clearing denominators gives a nonsingular plane curve. V/W is double, branched at the twelve zeros over g=0,1,-1 and the four simple poles of g (where g^3-g has odd pole order3). Riemann-Hurwitz gives2g(V)-2=16.

## 3. The actual scalar tower, not a torsion-label placeholder

Set C=T times_W V. Pulling back an etale isogeny doubles the16 branch points, so C->T is a smooth connected double cover branched at32 and g(C)=17. Connectedness follows already from its nonempty simple branch divisor. On C define

    rho(p,w)=(p+kappa, i*w),
    beta(p,w)=(p,-w),
    sigma(p,w)=(p+2kappa,w).

The anti-translation identity verifies the equation under rho. We have rho^4=1, rho^2=h=(p+2kappa,-w), sigma=h beta, and rho commutes with beta. Every nontrivial rho-power translates T by a nonzero torsion point, so rho acts freely. In particular C/h=D has genus9, C/rho=B has genus5, and C->D->B is a smooth etale cyclic-four tower.

The group <rho,beta> is C4 x C2, with beta not contained in <rho>. Quotients give the actual scalar square

    C = B x_Z T,
    B5->Z1 double branched at8,
    T1->Z1 etale cyclic-four.

Thus no unsolved Picard root is being presented as a cover: C,T,V and the deck maps have just been specified. B,D can equivalently be taken as their finite algebraic quotients; explicit plane equations for those quotients are not needed for their existence or genera.

This gives P=P(C/D) its canonical principal polarization Xi, native rho action satisfying rho_P^2=-Id, and signature(4,4), by the usual primitive-character Riemann-Roch calculation for an etale C4 cover of B5.

## 4. The theta-four axis is primitive, not a degree inferred before dividing by a kernel

The actual map

    phi:C->E_i, (p,w)->(g(tau(p)),w)

has degree8: V->E_i has degree4 and C->V degree2. It satisfies phi rho=i phi and phi h=-phi. Its pullback homomorphism E_i->J(C) lands in P. We must show this homomorphism is an embedding before assigning an actual theta degree.

Suppose phi factors through a nontrivial elliptic isogeny E'->E_i of degree k, with psi:C->E' of degree d=8/k. This is exactly the possibility detected by a finite kernel of phi*:E_i->J(C). Necessarily k=2,4 or8, so d=4,2 or1. Since phi h=-phi, continuity into the finite isogeny kernel gives

    psi h=c-psi

for a constant c. Compare psi with the bielliptic q:C->T of degree2. The joint degree divides2. If it were2, psi would factor through q and hence through an elliptic isogeny T->E'. But h acts on T by translation2kappa, so this would give psi h=psi+c', contradicting the displayed anti-action for a nonconstant psi.

The joint map is therefore birational. Castelnuovo-Severi/adjunction for two elliptic maps of degrees2,d gives

    g(C)<=1+2d<=9,

contradicting17. Thus phi* is injective. Jacobian norm-pullback gives its theta degree8 in J(C). Since Theta_C restricted to the etale Prym P is2Xi, its **actual theta degree in P is4**. No finite collection of slopes or cohomological inverse matrix substitutes for this primitivity argument.

Consequently P is isogenous to E_i times a complementary sevenfold. Neither that sevenfold's End nor its simplicity nor an additional opposite-character CM elliptic factor is computed here. The latter is the next genuine requirement toward the Y3 elliptic surface of degrees4,6.

## 5. Actual ramified-to-principal source isogeny

The quotient C/sigma is precisely the explicit V9 above; a:C->V is etale of degree2. The involution h descends to (p,w)->(p,-w) on V, with quotient W1 and16 branch points. Let L=Theta_V restricted to P(V/W). Since the elliptic pullback q_V*:J(W)->J(V) is injective for this ramified double cover, the complementary polarization has kernel q_V*J(W)[2] of size4. Thus L has type(1^7,2), not a principal-half normalization.

The induced map b=a*:P(V/W)->P(C/D) has finite kernel and is surjective by dimension. Indeed h intertwines the anti-invariant parts, each of dimension8. The polarization identity is

    2 b*Xi = 2 L, hence b*Xi=L.

Its degree is chi(L)/chi(Xi)=2. This supplies an **actual** degree-two polarized isogeny to this constructed source P, NOT to the fixed Y3. No inverse Chow map or target period identification is inferred from it.

## 6. Auxiliary cycle theorem and the remaining matching gate

The smooth etale C4 cover now exists and has even primitive multiplicity8. The unramified branch tuple is simple. Therefore Schoen Theorem2.0 and Corollary3.1, in the freshly retained eightfold source audit, supply algebraicity of the source P's determinant-character space in codimension4. This is an imported existence theorem for auxiliary cycles; explicit equations for those cycles have not been written here.

There is still no map from these source cycles to the original target alpha: a compatible target correspondence/isogeny/period match is missing. The second elliptic theta-degree-six axis of Y3 is not constructed; the joint degree of two CM maps is consequently not defined here. A single correct theta-four axis does not identify the full source Prym with Y3.

An executable next step is to compute the complementary sevenfold's Frobenius/endomorphism data for this rational control, or vary the elliptic-function parameters to seek the missing opposite-character axis. The same anti-translation formula holds for

    W_lambda:y^2=x(x-1)(x-lambda),
    g=(y+b(x^2-lambda))/(x^2-a*x+lambda),

with the analogous degree-two elliptic isogeny and cyclic-four lift. Smooth special fibres are a genuine open condition, witnessed by (lambda,a,b)=(2,4,2). No dimension, generic-End or full-family target exclusion is asserted. Any proposed match still requires joint elliptic primitivity, complementary sixfold identification and full principal Gaussian period/correspondence data before the unchanged four-channel/denominator768 tests.

Contract: `research/conjecture_net/contracts/hodge-minimal-axis-scalar-source.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_minimal_axis_scalar_source.py`.
Receipt: `research/voevodsky/results/hodge-minimal-axis-scalar-source-v1.json`.

Trust: exact rational polynomial/isogeny/translation certificates and the written projective fibre-product, Jacobian adjunction, primitivity/genus, quotient and restricted-polarization arguments. Schoen is imported from freshly validated primary receipts, not proved by the checker. No proof-assistant certification or independent review. Iteration41 and immutable pins v1-v44 are preserved; X, alpha and all unrestricted witness obligations remain fixed and open. No target exceptional cycle or Hodge verdict is supplied.
