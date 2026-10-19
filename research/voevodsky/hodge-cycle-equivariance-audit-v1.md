# Cycle equivariance: the first necessity audit

## Question and claim boundary

Can the native finite-order symmetry and the cycle-supplied coherence dictionary supply the missing all-algebraic-cycles invariance theorem? This audit addresses `all-algebraic-cycles-annihilation` in the refutation-directed iteration52 net, with its fixed sixfold X, p3 and alpha unchanged. The SCC obligation is **route/coherence compatibility**, not an identification of a transported cycle with its source.

Two scoped shortcuts fail:

1. Centrality and functorial transport do not make every algebraic cycle OBJECT equivariant under tau=i, even on the selected X.
2. Positive-degree ordinary group cohomology of C4 with rational vector-space coefficients is zero, so it cannot supply the proposed nonzero additive higher-coherence detector.

Neither result refutes the desired CLASS-level invariance theorem on X. They do not refute every possible higher-coherence attack or decide alpha's algebraicity. They are applications of standard geometric/cohomological facts, not new general theorems. The first is a fixed-source geometric control; the second identifies a rational finite-action limitation rather than a bounded-sample pattern.

Contract and issue-boundary conjecture/rivals/falsifiers: `inputs/hodge-cycle-equivariance-audit-v1/contract.json`. Checker and result: `checkers/check_hodge_cycle_equivariance_audit.py`, `results/hodge-cycle-equivariance-audit-v1.json`.

## 1. What functoriality actually gives

For every actual algebraic cycle Z on X,

    cl(tau^* Z)=tau^* cl(Z).

Transporting a fundamental-chain packet gives the corresponding transported chain. Subdivision comparisons preserve the class of a given cycle. These are the existing dictionary's legitimate naturality statements. They do NOT supply

    tau^* Z=Z,
    tau^* O_Z isomorphic to O_Z,
    or tau^* cl(Z)=cl(Z).

The last assertion is precisely the remaining fixed-X theorem. Centrality of tau in End^0(X)=Q(i) means it commutes with algebraic ENDOMORPHISMS of X. It does not mean every subvariety or coherent sheaf carries a tau-equivariant structure.

The previous product-fiber control already refutes uniform Weil-projector annihilation across the family. It is not a counterexample to a statement restricted to our fixed X: its endomorphism/Picard algebra is larger. This audit does not recycle that different fiber as a fixed-source refutation.

## 2. A non-equivariant cycle object on the actual X

The marked lattice is Z^12; native tau sends each coordinate pair(x_j,y_j) to(-y_j,x_j). Choose

    p=(1/3,0,...,0) mod Z^12,
    q=tau(p)=(0,1/3,0,...,0).

Its four orbit points are distinct. This uses the ACTUAL fixed marked torus, not a different period point. Since X is projective, these are algebraic C-points; no field-of-definition-over-Q assertion is required.

Let M be an ample line bundle on X, and choose r so M^r is very ample. Define its norm line bundle

    L=tensor_(k=0)^3 (tau^k)^*(M^r).

L is very ample. Cyclically permuting its four factors gives tau^*L isomorphic to L, compatibly with the order-four action. Thus the line bundle itself has the finite-action coherence one might hope to use.

Choose three general sections of L vanishing at p but not at q. These conditions are compatible because very ampleness separates the two points. Their differentials at p can be chosen independent because the embedding is immersive. Bertini for the linear system through p gives smooth successive intersections away from p; independence gives smoothness at p. Consequently their intersection Y is a smooth codimension-three algebraic complete intersection with

    p in Y,  q not in Y.

At p the structure sheaf O_Y has a nonzero stalk, but tau^*O_Y has zero stalk, since its support is tau^(-1)Y and tau(p)=q is not in Y. Hence these sheaves are NOT isomorphic, and Y cannot carry a tau-equivariant embedded-cycle structure.

Nevertheless, in the rational Chow ring (indeed integrally),

    [Y]=c1(L)^3=[tau^*Y],

because tau^*L isomorphic to L and complete intersections compute the intersection product. Its cohomology class is therefore tau-invariant. On the fixed source NS_Q=QE, so it is a multiple of E^3 and the candidate Weil projector kills it.

This rejects strict object-equivariance as a necessity for algebraicity ON THE FIXED X, even with its central endomorphism. It does not exhibit a noninvariant algebraic COHOMOLOGY class there. Nor does it show absence of a homology comparison: rational equivalence supplies equality of cycle classes, and hence a comparison of fundamental cycles in homology. Requiring an isomorphism of supports/sheaves would impose an unjustified stronger condition.

The geometric assertion uses standard imported very-ampleness, Bertini, cycle-intersection and support facts. The checker verifies the marked point orbit, not explicit projective equations for Y or a formal proof of Bertini.

## 3. Rational equivariantization is the same class-level gap

For an algebraic cycle Z define the rational orbit average

    Av(Z)=(Z+tau^*Z+(tau^2)^*Z+(tau^3)^*Z)/4.

This is an invariant rational algebraic cycle. But it represents cl(Z) only if cl(Z) was invariant to begin with. Conversely, any invariant representative has invariant class. Thus, for an algebraic class beta,

    beta has a tau-invariant rational algebraic representative
      iff tau^*beta=beta.

Averaging is not a proof of the right-hand condition. On the fixed Hodge space QE^3 plus W, tau is diag(1,-1,-1), so Av is diag(1,0,0). Its complement is exactly the retained candidate O on Hodge classes. In particular Av(alpha)=0 while alpha is nonzero: averaging changes that class rather than proving it vanishes.

The checker also retains two FORMAL rational subspace models, QE^3 and the full QE^3 plus W. Both satisfy the extracted tau/(2+i)/projector stability constraints, but one has zero projected part and the other does not. They are NOT asserted to be constructed geometric cycle images on X. This is a logical underdetermination control, not a substitute source or an algebraicity witness.

## 4. Additive positive-degree C4 coherence over Q vanishes

Let V be ANY rational representation of C4 with action T and T^4=I. Its ordinary cyclic-group cochain resolution has alternating differentials

    D=T-I,  N=I+T+T^2+T^3.

Put

    A=N/4,
    B=(T+2T^2+3T^3)/4.

Direct polynomial multiplication gives

    DN=ND=0,
    DB=BD=I-A,
    N*(I/4)=(I/4)*N=A.

Define h_n=B for positive odd n and h_n=I/4 for positive even n. Then

    d_(n-1) h_n + h_(n+1) d_n = I, for EVERY n>=1.

This is an explicit all-degrees cochain contraction. Therefore H^n(C4,V)=0 for every n>0. At degree zero the surviving term is V^C4, not all of V. In particular the nonzero Weil space W is not annihilated as a vector space merely because its positive-degree group cohomology vanishes.

The result also follows from exactness of rational invariants by Reynolds averaging. The periodic-resolution identity supplies the stated constructive proof. Four exact module controls cover the actual rational Hodge representation, the Weil sign representation, a faithful order-four rotation and a trivial representation. Their number does not establish the theorem; the polynomial identities do.

The degree here is GROUP-cohomological degree, not total degree in an equivariant geometric complex. A trivial Q coefficient complex concentrated in geometric degree2 still has invariant Q in total equivariant degree2. On the actual X, the invariant polarization also supplies such a warning: the norm line bundle has an equivariant first Chern class restricting to its nonzero ordinary Chern class. Thus positive total-degree Borel/equivariant cohomology is NOT declared zero.

This rules out a nonzero detector valued ONLY in ordinary positive-GROUP-degree additive C4 cohomology over Q. It does not rule out degree-zero projectors (our O already exists), nonadditive geometric obstruction objects, infinite-group data, or a separately specified algebraic-specific coherence invariant. Those need their own construction and all-cycle necessity theorem.

## 5. Integral torsion is not a workaround

For the abstract integral sign module Z^2, D=-2I and N=0, giving H^odd(C4,Z^2_sign)=(Z/2)^2. A class represented by e1 becomes D(-e1/2) over Q. For the abstract trivial module Z, positive even cohomology is Z/4, and e1 becomes N(e1/4) over Q.

These are test lattices, not an asserted identification of the actual integral Hodge lattice. Their torsion demonstrates why an integral finite-action defect cannot simply be presented as a surviving rational Hodge obstruction. The rational contracting homotopy removes it.

## Disposition and next proof obligation

The candidate shortcuts are rejected at the scopes stated above. Main net iteration52/pins v55 and its mathematical verdicts are unchanged. In particular `all-algebraic-cycles-annihilation`, fixed-alpha nonalgebraicity and the general higher-coherence existence conjecture remain OPEN.

The remaining necessity theorem must concern rational COHOMOLOGY CLASSES of arbitrary codimension-three algebraic cycles on the fixed X. It must use additional source-specific algebraic information, not object-level equivariance, formal functoriality, averaging, or positive-degree rational finite-group cohomology alone. No complete cycle-library theorem or such additional invariant is supplied by this audit. Known algebraic cycles remain falsifiers, not a resumed confirmation programme.
