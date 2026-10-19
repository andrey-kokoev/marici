# Global iteration 30 (third series 10/10): an equivariant tetragonal search gate

## Result: necessary geometry, not a matched cover

A hypothetical smooth etale cyclic-quartic realization of the fixed principal Y2 must have an **exactly tetragonal, nonbielliptic genus-nine intermediate**, with its tetragonal pencil preserved by the free involution. This supplies two normalized quadratic base-change squares, prescribed even fibres, harmonic CM branch data, and a cyclic-lift norm condition.

This does not compute theta dimension, assert an unproved lower bound of four, construct a target curve, or exclude the remaining route. The prior conditional bielliptic polarized census remains0/0 and its unpolarized comparison remains516/258. Those counts do not parameterize the nonbielliptic diagrams here. The unrestricted Hodge/cycle gates stay open.

## 1. The actual axis gives a tetragonal pencil

Write C=C17 -> D=C9 -> B=C5, with rho generating the cyclic-four cover, h=rho^2 and eta the free involution of D/B. The previous turn excludes bielliptic D for this fixed polarized target. Earlier work excludes hyperelliptic or trigonal D, and hyperelliptic B.

The actual first elliptic axis T in Y2 has theta degree two. It is the image of the old square-lattice E_+ with source isogeny degree ONE, not merely an unspecified elliptic curve isogenous to it. Thus T is isomorphic over C to the j=1728 elliptic curve. These degree/isomorphism facts are bound to the original B=diag(i,-i) construction and the actual principal-model receipt; we do not infer j from a generic dimension-eight Weil action.

As proved in the preceding adjoint argument, the axis produces phi:C->T of degree four and

    phi h = c-phi.

The quotient pi_T:T->R=T/(t->c-t) is a double cover of R=P1. The map pi_T phi is h-invariant, so descends to g:D->R. Its degree is(4*2)/2=4. The prior gonality lower bound is four, hence gonality(D)=4. This gives no equality assertion about gonality(B).

The field phi^*C(T) is not contained in C(D), since phi is anti-h and nonconstant. Because C(C)/C(D) is quadratic, C(C)=C(D)C(T). Therefore C is the normalization of D times_R T. This is an actual necessary function-field identification, not merely a matching degree count.

## 2. Why the free involution preserves the pencil

Compare the degree-four pencils g and g eta. Let d be their joint degree to the normalization Z of their image in P1 times P1. It divides four.

- **d=1.** The image has bidegree(4,4), arithmetic genus(4-1)^2=9, and normalization D of genus nine. Equality makes the image smooth, so D is isomorphic to it. Eta exchanges the two coordinates, whose fixed diagonal has intersection degree4+4=8 with the image. A nonempty intersection gives a fixed point of eta, contradicting freeness. No assumption of eight distinct intersections is needed.
- **d=2.** Z has two degree-two maps to P1 and is birational to their joint image of arithmetic genus one. Thus g(Z)<=1. The degree-two map D->Z makes D hyperelliptic if g(Z)=0 or bielliptic if g(Z)=1; both have already been excluded for this target.
- **d=4.** Both Z->P1 maps have degree one. The pencils agree up to a projective automorphism: g eta=mu g.

Only the last case remains. Surjectivity of g and eta^2=1 give mu^2=1. Mu is NONTRIVIAL: otherwise g factors through B=D/<eta> with degree two, making the genus-five B hyperelliptic, also excluded.

This proves preservation of the selected pencil, indeed of every degree-four pencil under these hypotheses. It does NOT prove that all tetragonal pencils on D are identical. Equal-genus fixed-diagonal reasoning, not a false uniqueness theorem above the strict genus threshold, is used.

## 3. Bottom square and two even fibres

Let S=R/<mu>=P1. The composition D->R->S is eta-invariant and induces f:B->S of degree four. Since g is not eta-invariant, its field together with C(B) generates C(D). Thus

    D = normalization(B times_S R),
    R->S is the double cover branched at two values.

Etaleness of D/B forces every multiplicity in the f-fibres at these two branch values to be even. A degree-four fibre can therefore have only partition(2,2) or(4).

For clarity choose coordinates making mu(u)=-u and R->S given by t=u^2. Then

    div(f)=2D0-2Dinf, deg D0=deg Dinf=2,
    eta_class=O_B(D0-Dinf) is nonzero two-torsion.

Nonzero is essential for connectedness. Even multiplicities alone certify an unramified normalization, not that the quadratic cover is connected. Here connectivity is supplied by the actual connected D/B; in a reverse construction it must be checked. A square function gives a disconnected pullback despite even valuations (for example z^4 on P1). In this particular genus-five setting a square degree-four function would moreover give the already excluded degree-two map to P1.

The map f has degree four; B might still have a separate trigonal pencil. No exact bottom gonality is asserted.

## 4. Top square, four harmonic even fibres and ramification budgets

Translate T to center its reflection. Its quotient by minus identity is the square-lattice elliptic double cover, whose four branch values form a harmonic set. In a suitable R-coordinate it is

    T: v^2=u*(u-1)*(u+1),
    branch values {0,1,-1,infinity}.

The unordered cross-ratio values are -1,2,1/2. The exact Legendre formula

    j(lambda)=256*(1-lambda+lambda^2)^3/(lambda^2*(1-lambda)^2)

gives1728 for each. This R-coordinate need NOT simultaneously put mu in the form u->-u. We do not assume mu preserves the harmonic branch set or that rho preserves the chosen elliptic axis. These are separate questions.

Since C is the normalized pullback of T along g and C/D is etale, g has even fibre multiplicities at all four harmonic values, again partitions(2,2) or(4). Locally a quadratic cover y^2=t pulled back along t=z^e ramifies after normalization exactly when e is odd. This includes the infinity branch after using a local uniformizer.

The square class defining C/D must be nontrivial. If it were trivial, the pullback would split and D would itself map to T with degree two, giving the excluded bielliptic intermediate. A proposed reverse construction must still check this square-class/connectedness gate explicitly.

Riemann-Hurwitz gives total ramification24 for g:D9->P1 and16 for f:B5->P1. If k of the four top prescribed fibres have partition(4), their contribution is8+k, leaving16-k elsewhere. After the elliptic pullback phi:C17->T, the contribution over elliptic branch values is2k and the contribution elsewhere is32-2k, totaling32=2*17-2. For the bottom two fibres, contribution4+k and remainder12-k pull back to total24, as required for D9->P1.

The checker enumerates16 top and4 bottom local partition patterns and checks these budgets. They are local combinatorial controls, not counts of actual covers, root labels or moduli points.

## 5. Order-four lift, not just two unrelated double covers

Write the connected top extension as C(D)(v), v^2=F(g), where the rational F on R represents the elliptic double cover with harmonic branch divisor. A lift rho of eta commuting with h must have

    rho(v)=r*v, r in C(D)^*,
    r^2=F(mu(g))/F(g).

Its square on v is eta(r)*r. The CYCLIC-FOUR requirement rho^2=h is therefore

    eta(r)*r=-1.

A value+1 gives an involutive lift, not the required generator. No change v->a*v or sign of r repairs that intrinsic square without changing the relevant data.

Formal controls demonstrate the distinction: for F(u)=u^3-u, mu(u)=-u, r=i has r^2=-1 and eta(r)r=-1, giving order four. For even F(u)=u^4+1 and r=1 the same base involution has lift square+1. Neither control supplies a genus-five base, a genus-nine intermediate, or a Y2 match.

We require r in C(D), not in C(g). Assuming it rational in g would silently impose descent to the chosen elliptic axis, which has not been established. The normalized whole diagram can also be viewed as B times_S T, but T->S is not declared Galois: base change can alter monodromy.

## 6. Remaining executable frontier and trust

Solve these equivariant tetragonal, harmonic even-fibre and norm-minus-one constraints, then test actual principal periods/isogeny data and all four exceptional channels. This is a more explicit curve/function-field search than an unspecified nonbielliptic genus-nine base. Alternatively obtain a justified actual theta dimension or lower bound from the gluing, vary principal models/isogenies, or pursue non-divisor cycles on X.

The necessary theta<=3 condition from iteration29 is unchanged and conditional on a realization; the actual dimension is unknown. We do not replace that gap with an unverified assertion that every ppav containing a degree-two elliptic curve has theta-singularity dimension at least four. No target curve, exceptional cycle, all-cycle theorem, independent review or Hodge verdict is supplied.

Contract: `research/conjecture_net/contracts/hodge-equivariant-tetragonal-gate.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_equivariant_tetragonal_gate.py`.
Receipt: `research/voevodsky/results/hodge-equivariant-tetragonal-gate-v1.json`.

    python research/voevodsky/checkers/check_hodge_equivariant_tetragonal_gate.py

Trust: fresh source/target/exclusion receipts, written norm-adjoint, normalization-genus, quotient/function-field and local-ramification arguments, plus exact finite controls. Not proof-assistant verification, period inversion or independent review. Iteration29 and immutable pins v1-v31, including intermediate v28, remain unchanged.
