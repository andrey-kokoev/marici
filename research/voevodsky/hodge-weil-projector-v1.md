# Hodge iteration 5: a canonical Weil projector and the actual remaining gap

## Result and limit

Keep exactly the sixfold X and alpha of iteration 4. We construct a rational class-level candidate map

    O:Hdg^3(X,Q)->W,

where W is its two-dimensional rational Weil determinant space. The map is noncircular, descends to cohomology, survives rationalization, and satisfies O(alpha)=alpha !=0. It is independent of charts, representatives and markings, relative to the supplied Q(i) action.

**It is not a validated Hodge obstruction.** Its crucial feature is that it **preserves** algebraic cycle classes. There is no proof that it annihilates them. In fact, proving all-cycle annihilation for this map is equivalent to proving alpha nonalgebraic. The map isolates the exact missing geometric theorem, rather than solving it.

A uniform-in-family annihilation claim is refuted by the earlier elliptic-product control and retained as a scoped rejected node. Neither the fixed X nor alpha is replaced by that control fiber.

## 1. A separating algebraic endomorphism

The Q(i) action on X gives the holomorphic endomorphism f=2+i. Homomorphisms of projective abelian varieties are algebraic (the standard algebraization/GAGA fact). This is a finite etale isogeny. Let F=f* on H^6(X,Q).

Over Q(i), split H^1 into six-dimensional eigenspaces U and conjugate(U). Its degree-six exterior algebra splits by the number a of factors from U, for a=0,...,6. The eigenvalue and multiplicity of F on that summand are

    lambda_a=(2+i)^a(2-i)^(6-a),
    multiplicity=binomial(6,a)^2.

The seven eigenvalues are distinct. Their conjugate-pair minimal polynomials are

    m0(t)=t^2+234t+15625,     a=0,6; eigenvalues -117 +/-44i,
    m1(t)=t^2+70t+15625,      a=1,5; eigenvalues -35 +/-120i,
    m2(t)=t^2-150t+15625,     a=2,4; eigenvalues 75 +/-100i,
    m3(t)=t-125,             a=3.

The multiplicities (1,36,225,400,225,36,1) sum to 924. The endpoint pair is precisely the rational Weil space W; its dimension over Q is two. This uses the exterior description of torus cohomology, not an assumed dimension of the entire Hodge-class space. No full generic Hdg^3 computation is claimed.

## 2. Explicit CRT projector

Put q=m1*m2*m3 and

    D=930187500000000000,
    P(t)=-(68381t+10391779)q(t)/D.

Exact polynomial division verifies

    P=1 mod m0,
    P=0 mod m1,m2,m3,
    P^2=P mod (m0*m1*m2*m3).

Thus P(F) is identity on W and zero on all the other character summands. Define O as its restriction to Hdg^3(X,Q), with codomain W. The image is of type (3,3) because the selected X has the balanced Weil structure proved previously.

The construction uses the known K action, never Hdg/image(cl), a presumed nonalgebraic complement, or a fitted scalar reader. It is an explicit rational polynomial in a geometric pullback.

**Coarse-generator hostile.** With 1+i instead, the endpoints collide spectrally with a=2,4. If B=(1+i)* on H^6, the naive projector (64-B^2)/128 selects every even a, of total rank 452 rather than two. It is not the full-cohomology Weil projector. Testing only its value on alpha and a divisor cube would miss this failure. The exact checker verifies the complete character census.

## 3. Descent, auxiliary choices and rational survival

Pullback by f is defined functorially on rational cohomology. At the cochain level it preserves coboundaries; every rational polynomial in it therefore preserves coboundaries too. Consequently O is Q-linear on classes, not a reader of selected histories, covers or cocycles. This is the concrete descent theorem for the map at hand, distinct from iteration 1's general kernel criterion.

Its intrinsic description is the identity on the two determinant characters and zero on the other K-character summands. A different marking conjugates F and P(F), hence gives the same geometric map. Swapping the two embeddings of K merely swaps the endpoint lines. Any other endomorphism that separates the same seven characters gives the same idempotent. The chosen K action is part of the fixed input, not an auxiliary choice being silently forgotten. No independence under changing that input is asserted.

Write R=Re wedge_j(dx_j+i dy_j)=alpha and I=Im wedge_j(dx_j+i dy_j). Direct exterior computation gives

    F(R)=-117R-44I,
    F(I)=44R-117I,
    P(F)R=R,  P(F)I=I.

Thus O(alpha)=alpha is nonzero in a genuine rational vector space. The large denominator D is not torsion: clearing it gives D alpha, whose x-coordinate six-torus period is D, not zero. Every nonzero rational multiple remains nonzero. This closes rational survival and candidate detection for the **candidate map**, without asserting its all-cycle vanishing.

As a positive check, f*E=5E, so F(E^3)=125E^3 and P(F)E^3=0. By the selected point's previous Picard certificate, this covers all degree-six divisor products on this X. It does not cover arbitrary codimension-three cycles.

## 4. Algebraic correspondence: preservation is not annihilation

Expand P(t)=sum p_k t^k. Since every f^k is finite etale, its flat pullback is defined on codimension-three algebraic cycles and on CH^3(X)_Q. Therefore

    P_CH = sum p_k (f^k)*

is an actual rational algebraic correspondence. This successor explicitly licenses flat pullbacks CH^3(X)_Q->CH^3(X)_Q by these particular finite etale isogenies, with no degree shift; it does not silently assume a general pullback library or change iteration 1's frozen scope contract. Standard cycle-class functoriality gives

    cl(P_CH beta)=P(F)cl(beta).

In particular O takes algebraic cohomology classes to algebraic cohomology classes lying in W. Negative coefficients and denominators are allowed in rational cycles.

Cohomological idempotence does **not** prove P_CH^2=P_CH on Chow groups: the polynomial identity used here was proved on cohomology, where homologically trivial information is forgotten. No Chow idempotence is asserted.

This preservation result is a useful positive-witness mechanism. It is not an annihilation theorem. The latter is the difficult condition still open in the net.

## 5. A single nonzero projected algebraic cycle would settle the positive route

Let A^3_Q denote the image of all rational codimension-three cycle classes on our fixed X. The subspace A^3_Q intersect W is stable under F. For z=aR+bI nonzero,

    Fz=(-117a+44b)R+(-44a-117b)I,
    det[z,Fz]=-44(a^2+b^2) !=0.

Thus any nonzero algebraic z in W spans all of W together with Fz; both vectors are algebraic. This is the elementary irreducibility of the rational Weil plane, proved by a determinant rather than an assumption about the unknown cycle image.

More explicitly,

    alpha=c z+d Fz,
    c=(44a+117b)/(44(a^2+b^2)),
    d=b/(44(a^2+b^2)).

The checker verifies this formula on 48 signed rational pairs; the displayed 2x2 inverse proves it for every rational nonzero pair.

If an actual cycle beta is found with O(cl(beta))=z nonzero, set zeta=P_CH beta. Then c zeta+d f*zeta is an actual rational cycle with class alpha. The coefficients a,b can be read as periods against the x1...x6 torus and the y1,x2,...,x6 torus. No algebraic representative has been found by this conversion rule alone.

Conversely, if alpha is algebraic, O(alpha)=alpha is already a nonzero algebraic image. These implications establish the exact equivalence

    O(A^3_Q)=0
      iff A^3_Q intersect W=0
      iff alpha is nonalgebraic.

This equivalence does not construct O from the unknown quotient: O was already constructed independently from f. It explains why the still-missing annihilation theorem is just as strong as the selected Weil-class nonalgebraicity problem. Passing the other gates cannot substitute for it.

## 6. Uniform vanishing is actually false

At the earlier Z=0 elliptic-product fiber of the same discriminant family, put u_j=dx_j+i dy_j and

    b_j=u_j wedge u_(j+3)=r_j+i s_j, j=1,2,3.

The real and imaginary parts are rational (1,1) classes there, hence divisor classes by Lefschetz (1,1). The identity U=-b1*b2*b3 expresses R and I as rational divisor polynomials. The same projector has P(R)=R and P(I)=I, so it does not annihilate those algebraic classes.

The node `uniform-weil-projector-annihilation` is therefore rejected only for the uniform family claim. At the selected transcendental-period X, the r_j,s_j are not all rational Hodge divisor classes: its Picard rank is one. We cannot move their algebraic witnesses to X merely because their determinant combination remains a flat Hodge class. Such a deformation claim would require new geometry, not face cancellation or flatness alone.

This control also explains the scope of the older P4/Q4 tests: the specific K-endomorphism formula is not defined on those unrelated varieties. One may not apply it there without typed K data. The in-family algebraic control is the relevant direct test, and it falsifies the tempting uniform necessity claim.

## 7. Net and trust disposition

Constructed at explicitly bounded scope:

- `obstruction-construction`: the candidate Weil projector, **not** a validated obstruction;
- `cohomology-descent`: its functorial class-invariance theorem;
- `rational-survival`: rank-two rational target with nonzero value;
- `candidate-obstruction-nonzero`: the exact equality O(alpha)=alpha.

Retained rejection: `uniform-weil-projector-annihilation`.

Still open: all-cycle annihilation on the selected X, actual algebraic-witness search, and reviewed counterexample assembly. The independent review port remains unfilled. No Hodge or foundational verdict follows.

The proofs use the prior torus geometry and standard functoriality of algebraic cycles under finite flat maps. Exact polynomial, exterior-algebra and rational witness controls are regressions for the written arguments, not proof-assistant certification or a complete cycle enumeration.

    python research/voevodsky/checkers/check_hodge_weil_projector.py

Contract: `research/conjecture_net/contracts/hodge-weil-projector.v1.json`.
Receipt: `research/voevodsky/results/hodge-weil-projector-v1.json`.
