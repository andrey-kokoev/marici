# The first nontrivial theta Weyl test is a two-height Pick determinant

Epistemic-graph event: 1421.

## Full Pick kernel

For the theta-defined

\`M_Xi(z)=-Xi'(z)/Xi(z)\`,

Nevanlinna positivity is equivalent to positive semidefiniteness, for every
finite set \`z_1,...,z_n\` in the upper half-plane, of the Pick matrices

\`P_ij=[M_Xi(z_i)-conj(M_Xi(z_j))]/[z_i-conj(z_j)]\`.

In terms of \`Xi\` alone,

\`P(z,w)=
[Xi'(conj(w))Xi(z)-Xi'(z)Xi(conj(w))]
/[(z-conj(w))Xi(z)Xi(conj(w))]\`.

This gives a hierarchy of source-only hostile tests: theta integrals and their
derivatives determine every entry, while any negative principal minor
falsifies the Weyl realization and RH.

## Why one-point positivity is automatic

Let the even positive theta kernel be normalized by

\`Xi(z)=integral_0^infinity Phi(u) cos(zu) du\`.

For \`y>0\`, define

\`B(y)=Xi(i y)=integral Phi(u) cosh(yu) du\`,
\`A(y)=B'(y)=integral u Phi(u) sinh(yu) du\`.

Both are positive. Direct differentiation gives

\`M_Xi(i y)=i a(y)\`, where \`a(y)=A(y)/B(y)>0\`.

Hence the scalar Pick test is

\`P(i y,i y)=a(y)/y>0\`.

Thus positivity of the theta kernel proves every one-point test on the
positive imaginary axis, but this is strictly weaker than the Nevanlinna
property. It cannot by itself prove RH.

## First coupled hostile test

At two distinct heights \`y_1,y_2>0\), the Pick matrix is

\`P_jk=[a(y_j)+a(y_k)]/[y_j+y_k]\`.

Its first genuinely coupled condition is

\`Delta_2(y_1,y_2)
=a(y_1)a(y_2)/(y_1 y_2)
-[a(y_1)+a(y_2)]^2/(y_1+y_2)^2 >=0\`.

Substituting the theta moments gives the entirely source-derived inequality

\`[A_1 A_2]/[y_1 y_2 B_1 B_2]
>=[A_1/B_1+A_2/B_2]^2/(y_1+y_2)^2\`.

No zero locations occur in this formula. A single negative value is a finite
falsifier of the proposed positive Weyl boundary. Passing it for sampled
pairs is not a proof: full Nevanlinna positivity requires every finite Pick
matrix at arbitrary upper-half-plane points.

## Real-axis boundary test

Where \`Xi(x)\` is nonzero, the diagonal boundary limit is

\`M_Xi'(x)
=[Xi'(x)^2-Xi(x)Xi''(x)]/Xi(x)^2 >=0\`.

This is the first Laguerre inequality. Higher Pick minors refine it and retain
the phase relations that one-dimensional moment positivity misses.

## Consequence

The positivity program now has a minimal exact test ladder:

1. positive theta density implies the imaginary-axis one-point tests;
2. the two-height determinant is the first nonautomatic source inequality;
3. arbitrary Pick matrices are equivalent to the Nevanlinna/RH gate; and
4. after positivity, Ledger 1382 supplies the compact-resolvent determinant.

The next constructive task is to represent the full Pick kernel as a Gram
kernel of source-defined boundary vectors. Such a factorization would prove
positivity without invoking zeros and would furnish the missing defect map.

A 60-digit exploratory sweep at
\`y in {0.1,0.25,0.5,1,2,5,10,20,50,100}\` found no negative two-height
minor; the smallest sampled value was approximately
\`7.7267797769e-8\` at \`(0.1,0.25)\`. This is a diagnostic algebra check,
not durable evidence for the universal inequality.

## Scope

This derives an exact positivity hierarchy and finite falsifiers. It does not
prove the two-height inequality globally or factor the full Pick kernel.
