# Hodge iteration 4: an explicit marked sixfold and integral Weil class

## Bound result

We select a particular smooth projective abelian sixfold X, not merely a family, and the class

    alpha = Re wedge_(j=1..6)(dx_j+i dy_j) in H^6(X,Z).

We prove that alpha is nonzero and of Hodge type (3,3). The selection does not assume nonalgebraicity. A further exact certificate proves NS(X)_Q=Q E and alpha not in Q E^3. This excludes divisor-product witnesses, **not all algebraic witnesses**. Algebraicity of alpha remains unresolved here.

The construction uses classical Riemann projectivity, torus Hodge theory and Lindemann-Weierstrass as explicitly imported theorems. It does not construct algebraic equations for X or prove the foundational source-generated higher-identity conjecture.

## 1. One actual period, specified without a generic-point oracle

Let L=Z[i]^6 in V=C^6, considered initially as a real vector space. Order coordinates (x1,y1,...,x6,y6) and use the Hermitian form

    h(v,w)=conjugate(v)^t diag(1,1,1,-1,-1,-3) w,
    E(v,w)=Im h(v,w).

The distinct primes are

    (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61).

For l=1,...,18 put t_l=exp(sqrt(prime_l))/2^20. Define the 3x3 complex matrix in row-major order by

    Z_(a,b)=t_(2k+1)+i t_(2k+2),  k=3a+b,  a,b=0,1,2.

These are exact named real constants, not numerically fitted periods and not a selection from an unspecified generic locus.

Write D=diag(1,1,3). Since every prime is less than 64, sqrt(prime)<8. The elementary series bound e<3 gives

    0<t_l<3^8/2^20<1/64,
    ||D^(1/2) Z||_F^2 < 30/64^2 = 15/2048 < 1.

The factor 30 is 2 times the three columns times sum(1,1,3). Therefore G=I-Z*DZ is positive definite. Here * denotes conjugate transpose, not a topological duality operation.

In V split into two C^3 blocks, set

    W={(v,Zv)},
    W_perp={(Z*Dw,w)}.

They are h-orthogonal, W is positive definite and W_perp is negative definite. They are complementary because W is nondegenerate. Define the real complex structure J by multiplication by i on W and by -i on W_perp. Equivalently, with

    A=[[I,Z*D],[Z,I]],
    J=A diag(iI,-iI) A^-1.

The selected variety is the analytic torus

    X=(V_R,J)/L.

This is an unambiguous marked object, depending on the fixed ordered prime list and no unknown algebraic-cycle space.

## 2. Smoothness, projectivity and the Weil structure

The quotient of a complex vector space by this full lattice is a smooth compact complex torus of complex dimension six. The original scalar multiplication T=i on V preserves L and commutes with J, so it supplies the Q(i) action.

The form E is integral on L. Orthogonality of the two planes shows E(Jv,Jw)=E(v,w). Writing v=v_++v_- gives

    E(v,Jv)=h(v_+,v_+)-h(v_-,v_-)>0 for v nonzero.

Thus E is a positive integral Riemann form. The imported Riemann criterion algebraizes X as a polarized projective abelian variety. Its alternating form has elementary divisors (1,1,1,1,1,3) and determinant 9. No equations or finite algebraic-cycle generation algorithm are inferred from that algebraization theorem.

The tangent action of Q(i) has three directions with its first complex embedding and three with its conjugate. This is the balanced Weil condition. The Hermitian discriminant is the class of -3 in Q*/Nm(Q(i)*), different from split -1 by the previous iteration's norm proof. Passing between homology and its dual changes the determinant by inversion, which gives the same norm class; normalization scalars in this even K-dimension likewise do not change that class.

## 3. The selected class and its exact Hodge type

The marking identifies H^*(X,Z) with the exterior algebra on the integral one-forms dx_j,dy_j. Let u_j=dx_j+i dy_j and U=u1 wedge ... wedge u6. The T* eigenvalue of each u_j is i. On the six-dimensional complex space spanned by the u_j, the J* holomorphic and antiholomorphic dimensions are three and three. Hence its determinant U has type (3,3); the conjugate determinant has the same type. Translation-invariant forms are harmonic for an invariant flat Hermitian metric, so this statement concerns the cohomology classes, not just chosen representatives.

Set alpha=Re U. In the expansion, precisely the 32 terms containing an even number of dy_j survive, with coefficient (-1)^(number_of_dy/2). Thus alpha is integral and rational. On the real x-coordinate six-torus in V_R/L its period is exactly one: only dx1 wedge ... wedge dx6 contributes. In particular alpha is nonzero, with no rescaling chosen to force a detector value.

**A degree-six hostile.** Checking wedge^6 J* alpha=alpha alone is insufficient: types (5,1) and (1,5) also have eigenvalue +1. The checker instead tests the infinitesimal action

    D_J(eta1 wedge ... wedge etar)
      = sum_a eta1 wedge ... wedge (J*eta_a) wedge ... wedge etar.

Its eigenvalue on type (p,q) is i(p-q), so its degree-six kernel is exactly type (3,3). A rational real part of u1 u2 u3 conjugate(u4) conjugate(u5) u6 at Z=0 passes full J* invariance but fails D_J. This prevents a false Hodge-membership shortcut. Membership at our actual transcendental period is the general determinant proof above, not inference from finite sample agreement.

## 4. Why this point has no accidental rational Hodge conditions

The square roots of the 18 distinct primes are Q-linearly independent. Indeed their prime square classes are independent, and the sign automorphisms of the associated multiquadratic extension isolate each square root in a linear relation.

The imported Lindemann-Weierstrass theorem now implies algebraic independence of their exponentials. To see the implication precisely, a polynomial relation among those exponentials would be a linear relation with algebraic coefficients among exp(sum m_l sqrt(prime_l)). Distinct exponent vectors give distinct algebraic exponents, contradicting the linear-independence form of Lindemann-Weierstrass. Rational scaling by 2^20 preserves algebraic independence. No unproved form of Schanuel's conjecture is used.

In real coordinates the displayed formula for J is rational in the 18 parameters, with rational coefficients. Its denominators are nonzero throughout the positive-plane domain. For any rational two-form v, the condition

    (wedge^2 J*)v=v

is a finite list of rational-function equations over Q. If it holds at our algebraically independent parameter tuple, clearing denominators makes each numerator polynomial identically zero. It therefore holds at every rational period sample in that domain. This is the only genericity claim needed below; we do not assume a full Mumford-Tate computation or that all Hodge loci have already been classified.

## 5. Exact Picard certificate and the divisor-product boundary

Take 19 samples: Z=0, and each matrix with just one entry equal to 1/8 or i/8. All satisfy the positive-plane inequality. Use the 66-element basis of two-forms in 12 variables, ordered lexicographically. Stack the exact rational matrices

    wedge^2 J_sample* - I.

The checker computes rank 65 by sparse rational elimination. It records 65 independent row indices and independently verifies their rank by dense rational RREF, whose one-dimensional kernel is the vector of E. It also verifies that every stacked row annihilates E.

Any rational (1,1) class at our chosen X must be in this common kernel by the algebraic-independence argument. Conversely E is a (1,1) class on every member by its Riemann form. Consequently

    H^2(X,Q) intersect H^{1,1}(X)=Q E,
    NS(X)_Q=Q E

by the imported Lefschetz (1,1) theorem. This also distinguishes the actual point from the elliptic-product control, which has multiple independent divisor classes.

Every degree-six product of divisor classes is therefore in Q E^3. But E=sum d_j dx_j wedge dy_j, so E^3 restricts to zero on the real x-coordinate six-torus, while alpha has period one there. It follows that

    alpha not in the rational span of products of three divisor classes.

This is not a counterexample to Hodge: codimension-three cycles need not be divisor intersections. The old Q4 controls and the special product-point construction already demonstrate precisely why that stronger inference would be invalid. The full algebraic-witness-search node remains open.

## 6. Literature and trust limits

The source-specific status was renewed with `pnpm pdf:search` against the retained Markman 2509.23403v2 p3 theorem and Brosnan 2609.14169v1 Proposition 4 in the same-day audit snapshot. The nonsplit sixfold is not covered by the cited split-sixfold Weil-class theorem. Neither this bounded review nor failure of maximal degeneration proves its class nonalgebraic.

Imported background, not formalized here: multiquadratic Galois theory; Lindemann-Weierstrass; the Riemann projectivity criterion (standard complex-abelian-variety theory); marked torus cohomology/Hodge theory; Lefschetz (1,1). The exponential formula is not a numerical independence test. The finite sample matrix calculations prove the stated rank and, together with the written genericity argument, the Picard conclusion; they do not enumerate all algebraic cycles.

The foundational net remains a methodological reference. An explicit classical transcendental-period construction is not automatically a construction by its licensed finite packet operations.

## 7. Net disposition and reproduction

Resolved with the same fixed source:

- `candidate-variety-and-class`: explicit marked polarized torus and integral alpha;
- `candidate-hodge-membership`: balanced-determinant proof of rational type (3,3).

Ready next: `obstruction-construction` and `algebraic-witness-search`. The first must do more than detect non-divisor-generation or the nonsplit discriminant. The second may seek non-divisor codimension-three cycles; no such representative has been constructed here.

    python research/voevodsky/checkers/check_hodge_explicit_sixfold_candidate.py

Contract: `research/conjecture_net/contracts/hodge-explicit-sixfold-candidate.v1.json`.
Receipt: `research/voevodsky/results/hodge-explicit-sixfold-candidate-v1.json`.

Nine checks, written proofs and declared imported theorems support these scoped resolutions. No class-level all-cycle obstruction, nonalgebraicity proof, Hodge proof/refutation or proof-assistant certificate is claimed.
