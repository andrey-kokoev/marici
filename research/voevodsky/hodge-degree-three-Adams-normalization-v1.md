# An exact rational K-theory normalization of a supplied Weil readout

## Fresh task and domain

Execute degree-three-Adams-normalization on the unchanged smooth projective abelian sixfold X. All operators below have domain K0(X)_Q of algebraic vector-bundle classes. Coherent sheaf inputs are interpreted through the regular-scheme identification with G0, as in the preceding syzygy construction. No class representing R is supplied by defining an operator on this domain.

Write e=c1(H), cl(e)=E, and deg(e^6)=2160. The rational Chern character is an isomorphism

    ch:K0(X)_Q -> direct sum_(j=0)^6 CH^j(X)_Q.

This standard smooth-variety statement concerns CHOW groups, not their cohomological images. Its injectivity cannot be replaced by injectivity of the Betti cycle-class map.

## Explicit degree selector

Adams operations are algebraic K-operations built from exterior powers. Their Chern-character compatibility is

    ch_j(psi^2(v))=2^j ch_j(v).

Define the rational polynomial

    p(T)=((T-1)(T-2)(T-4)(T-16)(T-32)(T-64))/(-1806336),
    P3=p(psi^2).

The denominator is exactly (8-1)(8-2)(8-4)(8-16)(8-32)(8-64). Thus p(2^j) is1 for j=3 and0 for the other six degrees. It follows that

    ch_j(P3 v)=0 for j!=3,
    ch3(P3 v)=ch3(v),
    P3^2=P3.

Idempotence in rational K-theory follows from the rational Chow Chern-character isomorphism. The expression is finite: powers of psi^2 are psi^(2^a), so expansion uses only psi^1,psi^2,...,psi^64 with rational coefficients. It is an additive rational projector, not a ring homomorphism or a claim of integral divisibility.

## A divisor-cube class and an entirely K-theoretic coefficient

Let

    d=(1-[H^(-1)])^3,
    b=P3(d).

Since ch(d)=(1-exp(-e))^3 starts in degree3 with e^3, one has ch(b)=e^3, with all other degrees zero.

For v in K0(X)_Q define

    lambda(v)=chi(X,v b)/2160.

This uses the bilinear Euler pairing on rational K-classes, not an assumed geometric representative of their primitive component. The tangent bundle of an abelian variety is trivial, so Td(X)=1. Hirzebruch-Riemann-Roch gives

    chi(X,v b)=deg(ch3(v) e^3),
    chi(X,b^2)=deg(e^6)=2160,
    lambda(b)=1.

Thus the normalization can be evaluated using algebraic K-operations and Euler characteristics alone on any supplied input.

## Primitive normalization and its exact scope

Set

    N(v)=P3(v)-lambda(v)b.

Then

    ch_j(N(v))=0 for j!=3,
    ch3(N(v))=ch3(v)-lambda(v)e^3,
    deg(ch3(N(v))e^3)=0.

Also P3(b)=b and lambda(P3(v))=lambda(v), so N^2=N. In cohomology the retained Hodge-space certificate identifies this orthogonal complement of E^3 with Q R plus Q I. Hence

    cl(ch3(N(v)))=P_W(cl(ch3(v))).

This is precisely the Weil readout on algebraic inputs, now normalized by an explicit finite rational K-operation. It does not enlarge the image of the algebraic cycle-class map or prove that R belongs to that image.

The output has virtual rank zero. A nonzero rank-zero virtual class is not an actual positive-rank vector bundle; an actual rank-zero bundle is zero. Adding a formal trivial rank does not prove that the resulting virtual class is represented by a bundle, much less by a stable or polystable one.

## Exact control and terminal-syzygy tests

For the actual complete intersection cut out by three sections of H^k,

    v_k=[O_(Z_k)]=(1-[H^(-k)])^3,
    ch3(v_k)=k^3 e^3,
    P3(v_k)=k^3 b,
    N(v_k)=0 in K0(X)_Q.

Here exact zero is justified because all Chow components of ch(N(v_k)) vanish, not merely because its cohomology vanishes. The preceding unipotent moving control has the same K-class by its flag and regular-section Koszul formula, so the same exact test applies to that family.

Every ample-twist presentation term P_i in the six-step cycle resolution is a sum of powers of H. Its normalized K-class vanishes exactly. Therefore

    N([K6])=N([O_Z]),

and for a d-step terminal bundle the sign is (-1)^d. The terminal-syzygy readout reduction is compatible with this actual operator; it is not eliminated by it.

## Zero Betti readout is weaker than zero K-class

For a line bundle M with c1(M)=a e+p in CH^1(X)_Q, where cl(p)=0, the normalized degree-three Chow character is

    ch3(N([M]))=((a e+p)^3-a^3 e^3)/6.

Its cohomology is zero. It has NOT thereby been proved zero in Chow or K0. Likewise, the previous generated semihomogeneous-bundle class has zero Weil readout, but that cohomological conclusion alone does not imply N vanishes on it as a rational K-operation.

No nonvanishing assertion for this displayed homologically trivial expression is needed for the distinction. Only the specific divisor-power/Koszul controls above have been shown to be killed exactly.

## Disposition and next source-typing test

Constructed: an explicit idempotent rational algebraic K-operation, including an Euler-pairing divisor subtraction, isolating degree-three primitive cohomology of supplied classes. Verified: exact annihilation of the actual complete-intersection and unipotent controls and compatibility with terminal syzygies. Unchanged: no input realizing R, and no algebraicity or nonalgebraicity verdict.

Next test the proposed passage from normalized virtual data to an actual positive-rank bundle. Under explicit H-polystability and vanishing discriminant-degree hypotheses, the Hermitian-Einstein/Chern-Weil equality case forces projective flatness and constrains higher Chern characters. Derive that precise boundary, but do not assign polystability to a virtual K-class or claim all realizing bundles satisfy the equality hypothesis. This gives a concrete hypothesis check on potential bundle realizations, not a new universal obstruction.

Verification checks all seven Adams weights, polynomial idempotence modulo their characteristic polynomial, Euler/cup normalization, exact Koszul controls and a formal homologically trivial Chow variable. Rational Chern-character and Adams compatibility, HRR and the retained Hodge certificate are the written mathematical inputs, not consequences of finite arithmetic checks. No proof-assistant certification is claimed.
