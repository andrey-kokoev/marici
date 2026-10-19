# Odd-sector source: a CM elliptic correspondence on a split Weil fourfold

## Fresh task and fixed control scope

Execute joint-family-odd-sector-correspondence. Work on the specified joint-family control X_joint=A times B, not on the original full off-diagonal sixfold. A has native coordinates1,2,4, signature(2,1), and polarization of native Hermitian matrix diag(1,1,-1). The previous exact certificate gives NS(A)_Q=Q E_A and excludes mixed rational divisor classes between A and B.

## The active rank-two determinant Hodge structure

Set

    Omega_A=u1 wedge u2 wedge u4=p+i q,
    L_A=Q p plus Q q inside H^3(A,Q).

The native K-eigenspace on H^1(A) has holomorphic dimension2 and antiholomorphic dimension1 throughout this family. Hence Omega_A has type(2,1), its conjugate has type(1,2), and L_A is a rational rank-two sub-Hodge structure. In particular

    D_J p=-q, D_J q=p.

For the native K generator T=i, the determinant action is i^3=-i, so

    T*p=q, T*q=-p.

These two actions are different: the infinitesimal Hodge operator and the K endomorphism must not be identified.

After the Tate twist (1), L_A(1) has weight one and types(1,0),(0,1). Take C=C/(Z+iZ), with real integral basis e=dx, f=dy and omega=e+i f of type(1,0), normalized by integral_C e wedge f=1. Equip C with the K action i acting by multiplication by -i, the CONJUGATE of the standard CM embedding. Then

    e -> p tensor t, f -> q tensor t

is a rational K-compatible Hodge isomorphism H^1(C,Q)->L_A(1), where t denotes the formal rational generator of Q(1). Equivalently H^1(C)(-1)->L_A maps the corresponding twisted basis to p,q. Tate comparison factors are recorded by the twists, not silently set equal to ordinary untwisted period numbers.

This is an isomorphism of Hodge structures; it has not yet been produced by an algebraic cycle.

## Explicit correspondence class and its action

On C times A use the order C then A and define the rational degree-four class

    gamma = f external p - e external q.

External products mean pullback from C followed by pullback from A in that order. Its complex expression is

    gamma=(omega external conjugate(Omega_A)
                  - conjugate(omega) external Omega_A)/(2i).

Both summands have type(2,2). Thus gamma is a rational Hodge class of codimension two. Its cohomological correspondence action is

    Gamma_gamma(eta)=(pr_A)_*(pr_C*eta cup gamma),
    Gamma_gamma(e)=p, Gamma_gamma(f)=q.

The degree shift is 2(r-dim C)=2(2-1)=2, so H^1(C) maps to H^3(A). The action has Hodge bidegree(1,1), equivalently a morphism into H^3(A)(1). The minus sign in gamma is forced by integral_C f wedge e=-1. Replacing it with a plus sign is not the same Hodge correspondence.

The pure H^1(C) tensor H^3(A) tensor lies outside the divisor-product sector at this control point. Indeed C is isomorphic to an elliptic factor of B as an underlying complex abelian variety, and the previous Picard certificate excludes mixed H^1(A) tensor H^1(C) rational divisor classes. On C times A the divisor space is Q E_C plus Q E_A, whose codimension-two products have even degree on each factor. Gamma has odd degrees(1,3). This is another non-divisor-generation statement, not nonalgebraicity.

## An exact split Weil classification of the correspondence ambient

The K action on C is the conjugate one chosen above. Combining it with the native K action on A gives multiplicities(2,2) on the holomorphic tangent space of C times A. This abelian fourfold is of balanced Weil type.

In native K coordinates, the C coordinate is conjugate to its holomorphic coordinate and has Hermitian weight -1 for the positive polarization E_C. With the active A weights, the native Hermitian matrix is

    diag(-1,1,1,-1).

Its determinant is +1, and it is split over Q(i): vectors (1,1,0,0) and (0,0,1,1) span a totally isotropic two-plane. Thus the correspondence ambient belongs to a split Weil-fourfold class, unlike the original nonsplit sixfold of discriminant -3.

The native determinant on C times A is

    U4=conjugate(omega) external Omega_A,

of type(2,2); gamma=-Im(U4). This identifies the ACTUAL correspondence class with a Weil determinant component, rather than merely matching dimensions or signatures abstractly. The embedding choice for K on C is essential; the standard embedding would give the wrong multiplicities for this construction.

## Algebraic gate and next theorem audit

If a rational codimension-two cycle on C times A has class gamma, its action supplies the required algebraic H^1-to-H^3 correspondence. Nothing in a weight-one Hodge isomorphism, its explicit tensor, or the absence of divisor products alone establishes such a cycle. In particular the theorem that H^1 morphisms of abelian varieties are algebraic does not directly apply to a target embedded in H^3(A).

The split Weil-fourfold identification gives a sharply scoped next test: audit retained literature for an algebraicity theorem for its Weil classes and match dimension, K field, polarization/discriminant, decomposition and specialization hypotheses to THIS actual fourfold and gamma. Do not borrow the original nonsplit-sixfold status or a generic-only statement without checking its scope. No theorem is invoked here to assert algebraicity; the mathematical reduction is ready for that bounded audit.

Even a successful correspondence construction would first concern this control family. Transport to the original fixed sixfold, and any realization of its alpha, remain separate unsolved tasks.

Verification checks the real exterior tensor, Hodge and K actions, correspondence signs and degree shift, and the explicit Hermitian split plane. Standard torus Hodge theory, Tate twists and correspondence formalism are imported background. No proof-assistant certification, algebraic representative of gamma or Hodge verdict is claimed.
