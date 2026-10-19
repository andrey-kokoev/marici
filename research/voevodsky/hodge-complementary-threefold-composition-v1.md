# Two varying threefold factors: compose correspondences over the elliptic curve

## Fresh task and larger control family

Execute complementary-threefold-correspondence-composition. Keep the original native lattice and Hermitian form, but restrict the period chart to

    P = [ a b 0 ; 0 0 c ; 0 0 d ],
    |a|^2+|b|^2<1,  |c|^2+3|d|^2<1.

The native planes {1,2,4} and {3,5,6} remain invariant, giving a product A times B of polarized abelian threefolds with signatures(2,1) and(1,2). Both factors now vary. This is a complex four-dimensional locus in the nine-dimensional Weil chart, with the same overall nonsplit Hermitian determinant -3. The previously fixed inactive elliptic projection need not exist, so it is not used.

Write

    Omega_A=u1 u2 u4=p+i q,  type(2,1),
    Omega_B=u3 u5 u6=r+i s,  type(1,2).

The letters r,s here denote degree-three determinant parts, not the earlier divisor factors. All four are rational flat classes. Let C be the standard CM elliptic curve, with omega=e+i f and integral_C e f=1.

## Two different CM choices on the same underlying elliptic curve

For C times A, choose the conjugate K action on C. The balanced signature is(2,2), Hermitian matrix diag(-1,1,1,-1), determinant1. The Hodge correspondence class is

    gamma_A=f external p-e external q,

with action e to p and f to q.

For C times B, choose the STANDARD K action on C. Now the balanced signature is again(2,2), with Hermitian matrix

    diag(1,1,-1,-3), determinant3.

This is nonsplit: the split determinant in dimension four is1 modulo norms, and 3 is not a norm from Q(i), by the retained modulo-three descent proof. The correct Hodge class is

    gamma_B=f external r+e external s
           =Im(omega external Omega_B).

Its action is e to r and f to -s, so omega maps to conjugate(Omega_B) of type(2,1), as required for a codimension-two H^1-to-H^3 correspondence. Giving both products the same K embedding on C would fail the balanced-signature binding for one of them.

The two K labels are used to identify the respective Weil spaces; the underlying complex elliptic curve C is the same. Ordinary algebraic correspondences on that curve can be composed. No simultaneous K-equivariance with one common elliptic action is assumed.

## Exact theorem coverage, including the nonsplit fourfold

The audited primary Corollary1.6.1 of Markman arXiv:2502.03415v2, PDF9, covers all abelian fourfolds. Its adjacent proof explicitly covers Weil classes for all imaginary quadratic fields and all discriminants. Therefore both gamma_A and gamma_B have rational algebraic representatives

    Gamma_A in CH^2(C times A)_Q,
    Gamma_B in CH^2(C times B)_Q.

This is theorem-backed existence; it does not follow from a split-only theorem for the second factor. The split-sixfold theorem is not being applied to A times B of discriminant -3.

Let tau:C->C be multiplication by -i and put

    Gamma_A_prime=-(tau times id_A)*Gamma_A,
    cl(Gamma_A_prime)=e external p+f external q.

## Composition as actual Chow operations

On the smooth projective sevenfold C times A times B, let pr_CA, pr_CB and pr_AB denote the indicated projections. Define

    T = (pr_AB)_*(pr_CA*Gamma_A . pr_CB*Gamma_B),
    T_prime = (pr_AB)_*(pr_CA*Gamma_A_prime . pr_CB*Gamma_B).

Each flat pullback has codimension2, the product has codimension4, and pushforward along the one-dimensional C factor gives codimension3 on A times B. The intersection product in its Chow ring is legitimate without asserting that arbitrary chosen representatives meet transversely. Rational signed coefficients are allowed.

Use exterior order C,A,B. Moving a degree-one C form past a degree-three A form gives a minus sign. The explicit integration is

    integral_C (f p-e q)(f r+e s) = p s+q r
                                            =Im(Omega_A Omega_B),
    integral_C (e p+f q)(f r+e s) =-p r+q s
                                            =-Re(Omega_A Omega_B).

Only the terms containing e f survive, with integral_C e f=1. No factor of two or isogeny degree is introduced.

The original sixfold marking has

    U=u1 u2 u3 u4 u5 u6=-Omega_A Omega_B,

because moving u4 before u3 is one odd transposition. Therefore

    cl(T_prime)=R,  cl(-T)=I.

This supplies rational algebraic cycle expressions for BOTH Weil components throughout this larger decomposable family, conditional only on the explicitly imported fourfold theorem and standard Chow operations. It is pointwise existence, not a constructed relative cycle family or explicit equations.

## Scope and consequence for candidate obstructions

Neither a fixed inactive elliptic factor nor a common divisor presentation is required anymore. Even with both threefolds varying and with a nonsplit fourfold on one side, the two-correspondence composition realizes the sixfold determinant classes. Thus nonsplit discriminant -3 and failure of divisor generation do not provide a universal obstruction on this larger locus.

The original selected period has all entries nonzero, so it does not lie on this coordinate-block product locus. This excludes only that displayed decomposition; it does not yet exclude a hidden product up to isogeny or rational change of marking. No algebraic witness is thereby transported to the original X.

## Next executable boundary audit

Test whether such a product decomposition can reappear on the original X after isogeny or rational re-marking. Use the already certified NS(X)_Q=Q E, Poincare reducibility and rational invariance of the Neron-Severi rank under isogeny. Distinguish exclusion of abelian product sources from exclusion of arbitrary algebraic threefold supports: simple abelian varieties still contain many nonlinear subvarieties. This is a source-boundary test, not a new all-cycle theorem.

Verification checks both correspondence actions and Hodge types, determinant/discriminant hypotheses, exact exterior integration and all degree/sign conventions. The source audit is consumed as imported mathematics; finite arithmetic does not independently prove that theorem. No proof-assistant certification or Hodge verdict for the original fixed source is claimed.
