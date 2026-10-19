# Iteration 7: the entire middle Hodge space and an honest Chow projector

## Fixed-point result

For exactly the sixfold X, polarization E and alpha=R already selected, we prove

    Hdg^3(X,Q)=Q E^3 direct-sum W,    W=Q R + Q I.

Its rational dimension is three. This computes Hodge classes, **not** which ones are algebraic. The explicit candidate projector O from iteration 5 now has the simpler description

    O(v)=(v-tau*v)/2 on Hdg^3(X,Q),    tau=i.

It does not have that description on all of H^6: the right side has rank 452 there, while O has rank two. No earlier full-cohomology hostile is erased.

We also construct a genuine rational Chow idempotent

    e_CH=(Id-tau*+(tau^2)*-(tau^3)*)/4.

This is not a rank-two Weil Chow projector: its full H^6 image has dimension 452. On codimension-three **algebraic cycle classes**, it agrees with O because those classes are Hodge. Neither a nonzero homological image of e_CH nor algebraicity/nonalgebraicity of R has been established.

## 1. Lie-J constraints, not the wrong finite J-invariance test

On H^1(X,C), the complex structure J has eigenvalues i and -i. Its induced derivation L_J on H^(p,q) is multiplication by i(p-q). Thus the degree-six rational class v is of type (3,3) precisely when

    L_J v=0.

This differs from wedge^6(J*)v=v, which also admits (5,1) and (1,5). The previous hostile remains relevant.

In the ordered basis indexed by six-element subsets of {0,...,11}, dim Lambda^6 Q^12=924. For each of the same 19 rational samples of J(Z), construct the 924 scalar linear equations for L_J. Stack them to obtain a rational 17556-by-924 matrix M. The checker builds its columns directly using the exterior derivation, including antisymmetric signs.

## 2. Exact modular rank certificate

Reduce every rational entry modulo the prime p=1000003, checking that every denominator is invertible. Sparse elimination gives rank 921. The receipt records the 921 selected row indices and 921 selected column indices.

Independently form the transpose of that selected square minor and re-eliminate it. Its rank is 921 and its determinant modulo p is **960186**, nonzero. The determinant is computed from the normalization factors and the pivot-row sorting sign. These data constitute a reproducible finite-field minor certificate, not floating-point evidence.

The rational minor must therefore have nonzero determinant. If its determinant over Q were zero, reduction in Z localized away from p would give determinant zero in F_p. Hence rank_Q(M)>=921.

The three rational forms E^3,R,I lie in every sample kernel, checked exactly before modular reduction. They are independent: E^3 has a nonzero coordinate with three complete dx_j,dy_j pairs; R and I have only one coordinate from each pair, with respectively unit all-x and one-y periods. Thus rank_Q(M)<=921 as well.

Only a lower bound from modular rank is generally justified. For example, a rationally nonzero entry divisible by p may disappear modulo p. The matching rational kernel and the fixed-point genericity argument are essential here.

## 3. Why this is the kernel at the actual X

The actual X is not one of the rational samples. Its 18 real period coordinates are algebraically independent over Q by the earlier exponential-prime/Lindemann–Weierstrass proof. J(Z) has rational-function entries with rational coefficients.

For rational v, if L_J(Z)v=0 at this point, clearing denominators gives rational polynomial identities vanishing at an algebraically independent tuple. They must be identically zero, so in particular vanish at every valid rational sample. Thus

    Hdg^3(X,Q) subset ker_Q(M),
    dim_Q Hdg^3(X,Q)<=3.

Conversely E is a polarization class throughout this chart and R,I are universal balanced Weil (3,3) classes, as proved previously. Therefore their span lies in the actual Hodge space. Independence gives equality.

This does not assert the same Hodge dimension at the elliptic-product control or at every member of the family. Such points have extra rational Hodge classes. The proof uses all rational classes at the specified algebraically independent point, not only the three class candidates that were initially supplied.

## 4. Anti-i symmetry is now a complete criterion on Hodge classes

Tau fixes E^3 and negates R,I. Thus (Id-tau*)/2 and O agree on the three generators and hence on all of Hdg^3(X,Q). The full-cohomology rank of the anti-i projector is instead

    1+225+225+1=452.

The coarser 1+i spectral reader rejected in iteration 5 selects precisely this larger sector. It can now be used on **known Hodge classes** because we proved that the anti-i Hodge sector is exactly W. It remains the wrong rank-two projector on full cohomology. Domain information cannot be dropped.

For an actual codimension-three cycle beta, define its anti-invariant cycle class

    z=(cl(beta)-tau*cl(beta))/2.

It is automatically in W. If z is nonzero, it is algebraic, and iteration 5's explicit 2x2 inverse using (2+i)* produces an algebraic representative of R. Conversely, if R is algebraic, its representative supplies such a beta. Therefore

    R algebraic
      iff some algebraic cycle class is not tau-invariant
      iff some actual algebraic bundle has nonzero anti-i part of kappa_3.

The bundle equivalence uses iteration 6's resolution and normalized-Chern argument, not a claim that arbitrary bundles have exponential Chern character. Their higher components are precisely what remains unconstructed.

The negative route is equivalently to prove every codimension-three algebraic cycle class tau-invariant. The divisor/power library theorem supplies this only for its specified source expressions. It is not a theorem about arbitrary cycles.

Tau is not a translation or a map homotopic to the identity: already its action on H^1 is nontrivial. A continuous scalar path in the real vector space does not generally preserve the lattice and therefore does not give a homotopy of torus endomorphisms proving cycle invariance.

## 5. Genuine Chow idempotence: four terms, with the correct scope

Tau is an algebraic automorphism with tau^4=Id on X. All its pullbacks are defined on CH^3(X)_Q. In Q[t]/(t^4-1),

    e=(1-t+t^2-t^3)/4,
    e^2=e,    t e=-e.

The checker verifies these identities by exact cyclic convolution. Substituting the actual automorphism pullbacks proves e_CH^2=e_CH on Chow groups, without assuming cohomological faithfulness.

On H^6, (tau^2)*=[-1]*=Id, so e reduces to (Id-tau*)/2. It therefore has the correct class-level restriction to W for cycle classes at our X.

The two-term polynomial h=(1-t)/2 instead satisfies

    h^2-h=(t^2-1)/4 !=0 in Q[t]/(t^4-1).

Thus finite order alone does not prove the two-term operator is Chow-idempotent. One would additionally need inversion to act trivially on the relevant Chow group; no such assertion is made. The calculation is a failure of a formal justification, not a proof that the resulting operator is nonidempotent on this particular Chow group.

Nor do we identify e_CH with the old P_CH on Chow. Their cycle classes agree in codimension three at the fixed X, but their difference could be homologically trivial, and their full-cohomology actions already differ. In particular, a nonzero element e_CH(beta) in Chow may have zero cycle class and is **not** by itself a Hodge witness.

## 6. The remaining algebraic-image dichotomy

Let A be the image of CH^3(X)_Q in H^6(X,Q). It contains the nonzero divisor cube. Since O preserves algebraic classes and the rational Weil plane is irreducible under (2+i)*, as proved by the previous determinant argument,

    A=Q E^3 direct-sum (A intersect W),
    A intersect W is either 0 or W.

Consequently dim_Q A is either **one or three**, never two. The latter case is equivalent to the Hodge conjecture in this codimension on this X; the former would make R a counterexample. Which case holds is not established. This local dichotomy neither proves nor refutes the general Hodge conjecture.

## 7. Artifacts, next action and trust

Contract: `research/conjecture_net/contracts/hodge-middle-hodge-kernel.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_middle_hodge_kernel.py`.
Receipt: `research/voevodsky/results/hodge-middle-hodge-kernel-v1.json`.

    python research/voevodsky/checkers/check_hodge_middle_hodge_kernel.py

Next: examine actual non-tautological cycle or higher-Chern/sheaf constructions, checking the fixed sixfold's nonsplit hypotheses, and compute their anti-i cohomological component. A nonzero result in Chow alone, a changed fiber, or a freely specified cohomology tensor is insufficient.

The rational/minor/group-algebra checks are exact regressions for the written arguments. Algebraic independence, torus Hodge decomposition and cycle functoriality are imported standard mathematics. This is not proof-assistant certification. The global witness, all-cycle annihilation and independently reviewed counterexample assembly remain open; no classical or foundational outcome is imported.
