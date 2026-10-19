# Global iteration 46, fifth series 5/10: actual reflection quotients exclude the symmetric loci

## Result and domain

There is a stronger geometric obstruction than the preceding prime screens. For

    W_lambda: y^2=x(x-1)(x-lambda),
    g=(y+b(x^2-lambda))/(x^2-a*x+lambda),
    V/W: w^2=g^3-g,

assume lambda is complex, not0 or1, g has degree4, and is unramified over0,1,-1,infinity. These are the smooth genus9/1, sixteen-branch-point sources under discussion. On EACH of the loci

    a=2*lambda,   a=2,   b=0,

an actual elliptic reflection preserves g. The principal source Prym P8 is isogenous to a product of Jacobians of genera3 and5. The isogeny has degree256 and pulls the principal source polarization back to twice the product principal polarization.

**No such P8 can be isogenous to Y3**, since Y3 contains the fixed simple sixfold X as an isogeny factor. A product of abelian varieties of dimensions3 and5 cannot have a simple factor of dimension6. This excludes the remaining literal b=3 control and indeed the entire admissible lambda2,a4 line, including admissible infinity-branch cases. It applies directly over C, not only to algebraic parameters or congruence classes.

This is an actual quotient construction, NOT a lift of the degree4+10 Frobenius factorization seen earlier. No full-family exclusion is asserted off these three loci. Actual source constructions and auxiliary classes remain valid.

## 1. Exact reflections

The checker works in Q[lambda,a,b,x,s] with exact rational coefficients. Put D=x^2-a*x+lambda, N=b(x^2-lambda). The three involutions are

| locus | reflection on W | invariant coordinate |
|---|---|---|
|a=2lambda|sigma_1=(-p)+(1,0): x'=(x-lambda)/(x-1), y'=(1-lambda)y/(x-1)^2|s=y/(x-1)|
|a=2|sigma_lambda=(-p)+(lambda,0): x'=lambda(x-1)/(x-lambda), y'=lambda(lambda-1)y/(x-lambda)^2|s=y/(x-lambda)|
|b=0|sigma_0=(-p)+(0,0): x'=lambda/x, y'=lambda*y/x^2|s=y/x|

After clearing denominators, the elliptic equation, matrix-square identity, differential action sigma*(dx/y)=-dx/y and g*sigma=g are checked symbolically. Each reflection has four fixed points and quotient P1_s. For the first two, the exact denominator-invariance defects are

    (2lambda-a)*(x^2-2x+lambda),
    lambda*(2-a)*(x^2-2lambda*x+lambda),

respectively. Thus these identities do not silently extend to arbitrary a. On the third locus the reflected numerator changes the sign of N, which vanishes when b=0. Other possible symmetries are not classified.

## 2. Explicit projective quotient models

Let W have function field C(s,eta), eta^2=R(s), and write g=h(s)=n(s)/d(s). The models are

| locus | d | n | R |
|---|---|---|---|
|a=2lambda|s^2-lambda|s+b(s^2+lambda)|(s^2+lambda)^2-4s^2|
|a=2|s^2-1|s+b(s^2+1)|(s^2+1)^2-4lambda*s^2|
|b=0|s^2+1+lambda-a|s|(s^2+1+lambda)^2-4lambda|

In the three cases eta is2x-(s^2+lambda),2x-(s^2+1),2x-(s^2+1+lambda), respectively. Substitution into W and D,N gives these identities; the checker verifies the invariant-coordinate quadratic relations and discriminants exactly.

Put

    F=d*n*(n-d)*(n+d),    U=w*d^2,    Z=eta*U.

Then the quotient curves and maps are ACTUAL rational formulas extending to the smooth projective normalizations:

    H3: U^2=F(s),               V -> H3: (s,U),
    H5: Z^2=R(s)*F(s),          V -> H5: (s,eta*U).

Both maps have degree2. On V, beta negates w and the lifted reflection sigma negates eta but fixes w. They commute, generating C2 x C2; H3=V/sigma, W=V/beta, H5=V/(sigma*beta).

The assumed special-fibre transversality means h is degree2, unramified over the four elliptic branch values. It also means those eight branch points on P1_s are disjoint from W's four branch points: a fixed point of sigma is a ramification point of W->P1_s and would force ramification of g if it lay over a special value. Thus the biquadratic branch divisors have sizes8 and4, disjoint. This gives genera3 and5. Equivalently sigma has eight fixed points on V, while sigma*beta has none.

Infinity is included. In the explicit polynomial chart, F is squarefree of degree8 or7; the latter has an additional branch point at infinity. R is squarefree of degree4 and coprime to F. Thus F has eight projective branch points, RF twelve, giving the same genera. For lambda2,a4, the literal b=0,+1,-1 cases have degree7, not a missing branch point. Separate exact gcd witnesses cover all three loci, lambda3 examples, and b=0,+1,-1,2,3,6 on the old line. This is not a claim that every parameter on a locus is admissible; degenerate or lower-degree maps and compactified limits are outside the stated domain.

## 3. The actual scalar principal source for general lambda

The earlier elliptic cyclic-four lift has the explicit generalization

    T_lambda: v^2=t^3+(2lambda-4)t^2+lambda^2*t,
    tau: x=(t+lambda)^2/(4t), y=v(t^2-lambda^2)/(8t^2),
    kappa=(-lambda,2i*lambda).

The equation is checked symbolically. The point lies on T, its tangent slope is-2i, and doubling gives(0,0), so it has exact order4. Its image on W is k=(0,0). Tau is the unramified dual two-isogeny associated to W's point(1,0); its kernel is{O,(0,0)}. The curves are nonsingular for lambda not0,1.

Translation by k gives x->lambda/x,y->-lambda*y/x^2 and g(p+k)=-g(p) for all a,b. Consequently C=T times_W V is smooth connected of genus17, and rho(t,w)=(t+kappa,i*w) acts freely. Its quotients have genera9 and5, yielding the principal Prym P=P(C/(rho^2)) of dimension8 and native signature(4,4). The quotient a_C:C->V is etale of degree2. As in iteration42, its actual pullback b_V:P(V/W)->P is a degree-two polarized isogeny, b_V*Xi=L, where L=Theta_V restricted to the ramified Prym has type(1^7,2).

No unsolved torsion root or cohomological inverse is substituted for these maps. The first degree-eight elliptic map and primitive theta-four argument are unchanged, but they are not enough for a target match.

## 4. Quotient Jacobians really give an isogeny, with degree256

Let q3,q5 be the quotient maps V->H3,H5. Their pullbacks have finite kernels since norm composed with pullback is multiplication by2. On their images, beta acts as-1. Sigma acts as+1 on q3*J(H3) and-1 on q5*J(H5), since its action on H5 is the hyperelliptic involution. Their intersection is therefore contained in two-torsion. The ACTUAL homomorphism

    f=q3*+q5*: J(H3) x J(H5) -> P(V/W)

has finite kernel, and is surjective by dimension3+5=8. This is not just an isomorphism of cohomological vector spaces. In particular the etale q5 pullback is not assumed to be an embedding.

The quotient pullback identities give qj*Theta_V=2Theta_Hj as polarizations. Opposite sigma eigencharacters make cross terms zero: they are negated by sigma, and Hom groups are torsion-free. Hence

    f*L = 2Theta_H3 boxplus 2Theta_H5.

The Euler characteristic on the product is2^8=256, whereas chi(L)=2. Thus deg(f)=128. Composing with b_V gives an actual isogeny

    Phi:J(H3) x J(H5) -> P,
    Phi*Xi=2(Theta_H3 boxplus Theta_H5),    deg(Phi)=256.

This does NOT make P a product as a principally polarized variety: finite gluing can preserve indecomposability. The degree256 is a SOURCE computation, not an identification with Y3's different degree256 presentation. No inverse Chow map or target correspondence is inferred.

## 5. Exclusion by the simple sixfold, not by CM multiplicities

The retained target has X simple of dimension6 and Y3 isogenous to X x E_i^2. If a P above were isogenous to Y3, composing Phi and an actual isogeny-category projection to X would give a surjection J(H3) x J(H5)->X. Each summand's image is an abelian subvariety of the simple X. Since its dimension is at most3 or5, it must be zero. The whole map would be zero, a contradiction.

Thus every admissible source in the stated reflection loci is excluded even up to unpolarized complex isogeny. This includes all admissible lambda2,a4,b, not just the algebraic congruence classes previously pruned. The finite-field CM factors of b=3 never needed to lift. The old prime results and actual source constructions remain correct; the new geometric obstruction supersedes further prime screening on this line.

## Next executable frontier and trust

Move OFF the known reflection loci. The checker supplies the actual new control(lambda,a,b)=(2,0,2): D=x^2+2, the three finite special-fibre quartics are squarefree and coprime to W's cubic, poles are genuine and simple, and infinity has g=2. The same cyclic-four construction and primitivity argument give an actual C17/D9/B5 source with a primitive theta-four axis. It escapes all three specified reflection conditions, but no second CM axis, simple complement or target compatibility is established. Its good-prime CM screen or a search for further automorphisms/elliptic maps is the next executable test. More generally choose b nonzero and a different from2 and2lambda, verify all projective branch conditions, then attempt target matching. Escaping these reflections is not proof of simplicity or compatibility. Other symmetries, other scalar sources, the birational genus-five-image branch, direct cycles and broader constructions remain open. X/alpha and denominator768/four-channel target transfers remain fixed.

Contract: `research/conjecture_net/contracts/hodge-scalar-reflection-decomposition.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_scalar_reflection_decomposition.py`.

Trust: exact generic polynomial/isogeny identities and projective branch witnesses, plus written quotient-Jacobian, polarization and simple-factor arguments using standard abelian-variety facts. No proof-assistant certification or independent review. Iteration45 and pins v1-v48 remain immutable. No End computation, ppav product isomorphism, whole scalar-family exclusion, target cycle or Hodge verdict is supplied.
