# Iteration 9: explicit split-eightfold stabilization with a Chow retraction

## Result and scope

The original sixfold X, codimension three and alpha=R6 are unchanged. We construct an **auxiliary** abelian eightfold A=X x B, with a balanced Q(i) action and split Hermitian form, plus explicit algebraic correspondences

    S_CH:CH^3(X)_Q -> CH^4(A)_Q,
    D_CH:CH^4(A)_Q -> CH^3(X)_Q,
    D_CH S_CH=Id.

On the two rational Weil planes, S sends R6,I6 to R8,I8 and D reverses those assignments. Thus

    alpha algebraic on X
      iff the specified W8 on A contains a nonzero algebraic rational class
      iff all of W8 is algebraic.

This is a genuine cycle-theoretic reduction, **not** a supplied nonzero algebraic Weil class. The retained sixfold theorem still does not apply: A has dimension eight. Neither the full Hodge space of A nor the algebraicity of W8 is computed here.

## 1. The CM elliptic surface and actual divisors

Let B=R^4/Z^4, with native coordinates x7,y7,x8,y8 and complex structure diag(i,-i). Equivalently use coordinates (z,w) with z holomorphic in the native first plane and conjugate(w) holomorphic in the second. It is a product of square-lattice CM elliptic curves. Multiplication by native i on both planes is a holomorphic lattice automorphism.

Let D1={z=0}, D2={w=0}. In the marked cohomology,

    [D1]=dx7 dy7,    [D2]=-dx8 dy8,
    E_B=D1+3D2.

This is an ample product polarization of type (1,3), with Hermitian diagonal (1,-3). The negative sign of [D2] is required because the second native complex plane is conjugated.

Define actual elliptic kernel divisors

    Gamma_1={z=conjugate(w)},
    Gamma_i={z=i conjugate(w)}.

They are fibers over zero of the split surjective holomorphic homomorphisms phi_1(z,w)=z-conjugate(w) and phi_i(z,w)=z-i conjugate(w). Hence they are algebraic divisors on the projective B. The checker verifies phi J_B=J_std phi for their integral real matrices, and computes their pullbacks of the elliptic point class.

Set the following **Chow divisor classes**, not only hypothetical Hodge forms:

    r=D1+D2-Gamma_i,
    s=Gamma_1-D1-D2.

Their cohomology classes are

    r=dx7 dx8-dy7 dy8,
    s=dx7 dy8+dy7 dx8,
    r+i s=(dx7+i dy7)(dx8+i dy8).

They have type (1,1). The complex orientation on B is the negative of the ordered real lattice orientation. Thus

    integral_B r^2=-2,    integral_B r s=0,
    integral_B s^2=-2,    integral_B E_B^2/2=3.

These are intersection **degrees** of actual divisor products. We do not assert r s=0 in CH^2(B); its degree is zero, which is exactly what the projection formula below needs.

## 2. Splitness is explicit, not merely a determinant guess

On A use the product polarization and the diagonal native Q(i) action. Its Hermitian form is

    H_A=diag(1,1,1,-1,-1,-3,1,-3).

The signature is (4,4) and determinant is 9=Norm(3), so its discriminant class is +1. We additionally exhibit a maximal rational K-isotropic four-plane. In the standard K-basis e1,...,e8 take

    l1=e1+e4,
    l2=e2+e5,
    l3=e3+(1+i)e7+e6,
    l4=(-1+i)e3+e7+e8.

They are independent and pairwise Hermitian-orthogonal isotropic vectors. The identity behind the last two is

    M=[[1,-1+i],[1+i,1]],    M* M=3 Id_2.

For c=(1,1,3,3), make m_j from l_j by reversing its negative-coordinate sign and dividing by 2c_j. The ordered basis (l1,...,l4,m1,...,m4) has Gram matrix [[0,Id_4],[Id_4,0]]. Its Gaussian determinant is -1/3. This proves K-Witt index four by exact rational arithmetic, without invoking a classification theorem to infer splitness from determinant alone.

There is no contradiction with iteration 8: we changed dimension by adjoining B, not merely polarization or isogeny model of X. The higher-dimensional split form is not a new marking of the original sixfold. "Split" here refers to its Hermitian form, not an asserted product of two abelian fourfolds.

## 3. Weil classes and their Hodge type

Write U6=R6+i I6 as before, and U_B=r+i s. Then

    U8=U6 U_B,
    R8=R6 r-I6 s,
    I8=R6 s+I6 r.

The checker verifies these identities against the full exterior definitions of the two eightfold determinant generators. Each has 128 terms; R8 has unit all-x period and is nonzero. The product types are (3,3)+(1,1)=(4,4), agreeing with the balanced Weil structure of A.

All of these are cohomology classes. The formulas do not supply cycles for R6,I6 or R8,I8: the unknown sixfold Weil factor has not disappeared.

## 4. Algebraic forward and reverse correspondences

Let f=2+i on the **sixfold** X and define the rational algebraic correspondence

    J_CH=-(f*+117 Id)/44 on CH^3(X)_Q.

On W6 its cohomological action J sends R6 to I6 and I6 to -R6, by the earlier exact matrix of f*. We do not assert J_CH^2=-Id on Chow, or J^2=-Id on full H^6.

Define, using external products with the actual Chow divisors above,

    S_CH(z)=z external r-J_CH(z) external s.

This raises codimension by one. For any beta in CH^4(A)_Q put

    D_CH(beta)=-(1/2) pX_*(beta intersection pB*r).

Its degree accounting is 4+1-2=3: cup with a divisor, then proper pushforward along the two-dimensional B. All varieties are smooth projective; the projections admit flat pullbacks, and standard intersection products and proper pushforward are defined. This explicitly licenses a new object X x B and these operations, rather than silently extending iteration 6's powers-of-X library.

For every z in CH^3(X)_Q, the projection formula gives

    D_CH S_CH(z)
      =-(1/2)[deg(r^2) z-deg(sr) J_CH(z)]
      =z.

This is an actual Chow identity. It uses only intersection degrees on B, not an identification of homologically trivial zero-cycles with zero. Therefore S_CH D_CH is a genuine idempotent on CH^4(A)_Q.

However, its full H^8 image has dimension **924**, the dimension of H^6(X,Q), not two. S_CH D_CH is not identity on all of CH^4(A), and is not a rank-two Weil Chow projector. Its restriction to the selected Weil planes is the rank-two transfer we need.

## 5. Reverse transfer is an exact isomorphism on the Weil planes

Using the degree pairings,

    D(R8)=-(1/2)[-2 R6-0 I6]=R6,
    D(I8)=-(1/2)[0 R6-2 I6]=I6.

Similarly S(R6)=R8 and S(I6)=I8. The checker also tests 48 signed rational combinations, including denominators, and the nonzero target period.

If an actual algebraic cycle beta has nonzero class aR8+bI8, D_CH(beta) supplies the nonzero algebraic class aR6+bI6. Iteration 5's explicit rational combination with f* then represents R6. Conversely, if R6 is algebraic, J_CH supplies I6 and S_CH supplies both eightfold generators. This proves the equivalence in the opening section without using an unknown quotient as a construction.

The assertion is about the **specified determinant plane** of the special split eightfold X x B. It is not an equivalence with algebraicity of every Hodge class on A, and we do not compute its entire Hodge space.

## 6. Hostiles: why no witness has been manufactured

1. **Bare projection fails.** pX_*R8=0 because the B-degree is only two, not the top degree four. Without insertion it would have the wrong codimension as well.
2. **The polarization is the wrong insertion.** E_B r=E_B s=0 in cohomology, so using E_B instead of r gives zero. A correct algebraic dual divisor matters.
3. **A nonzero arbitrary algebraic source is insufficient.** The known cycle E^3 on X transfers to E^3 external (r+(11/2)s), since J(E^3)=-(11/2)E^3. Its reverse is nonzero, but it lies outside W8. This is not an alpha witness. An arbitrary A-cycle must be shown to have an appropriate Weil component; nonzero D alone is not enough.
4. **The sixfold anti-i test changes scope.** Diagonal i on all eight factors fixes R8,I8, since i^8=1. The automorphism i on X and identity on B instead negates them. One cannot reuse the old diagonal anti-i detector in a changed dimension.
5. **A genuine Chow projector is not automatically a Weil projector.** The rank-924 image above includes unknown and non-Hodge classes; it supplies no nonzero algebraic W8 class by itself.
6. **A sixfold theorem is not an eightfold theorem.** Fresh `pnpm pdf:search` confirms the retained Markman p9 says higher-genus secant objects are constructed but semiregularity is special to genus three. Its discriminant -1 theorem is six-dimensional. The bounded local search for "eightfold" has no hit and the index warns of repository additions/removals: neither fact is an exhaustive literature status claim.

Adding a CM factor changes the ambient form and makes a useful reduction, but the unknown Weil algebraicity remains in the source or target. The earlier divisor/power-library exclusion on X is not evaded by merely writing products with known B-divisors.

## 7. Artifacts and continuation

Contract: `research/conjecture_net/contracts/hodge-split-eightfold-stabilization.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_split_eightfold_stabilization.py`.
Receipt: `research/voevodsky/results/hodge-split-eightfold-stabilization-v1.json`.

    python research/voevodsky/checkers/check_hodge_split_eightfold_stabilization.py

Next: test an actual eightfold construction with verified dimension-eight hypotheses, or construct the full-cohomology Weil projector on A to filter candidate cycles correctly. The reverse correspondence is now explicit if such a nonzero algebraic Weil class is obtained. No such class is supplied here; global witness search, all-cycle annihilation and independent counterexample review remain open.

The arithmetic/exterior checks are exact regressions for written geometric arguments. Projectivity/algebraization, cycle-class functoriality and the projection formula are imported standard facts, not proof-assistant certification. No Hodge or foundational verdict follows.
