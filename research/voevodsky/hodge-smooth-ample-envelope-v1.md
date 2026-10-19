# Smooth ample envelopes exclude the primitive class, not all algebraic supports

## Fresh task and fixed source

The fresh workbench selects smooth-ample-envelope-control. Keep X smooth projective of dimension six, polarization E, and alpha=R with E cup alpha=0 and alpha nonzero. These are the exact fixed-source results of the quadratic-pairing note. All cohomology below is rational. L denotes cup product with E, not a new line bundle.

## The complete smooth-divisor support image

Let i:D->X be a smooth ample divisor with class mE, m>0. Weak Lefschetz gives an isomorphism

    i*:H^4(X,Q) -> H^4(D,Q),

since 4<dim_C D=5. Purity and localization identify the support-forgetting map with the Gysin map

    H_D^6(X,Q) = H^4(D,Q)(-1) --i_*--> H^6(X,Q).

The Tate twist records Hodge type; the underlying rational vector-space calculation is

    i_* i*(eta) = m E cup eta.

Thus the ENTIRE degree-six support image of D is L H^4(X,Q), not merely the span of divisor-product classes.

Hard Lefschetz gives L^2:H^4(X)->H^8(X) an isomorphism. If alpha=L eta, then 0=L alpha=L^2 eta implies eta=0 and alpha=0, a contradiction. Consequently

    alpha|_(X minus D) != 0

for every such smooth ample divisor D. In fact the image intersects the primitive degree-six space only in zero. On the fixed Hodge space QE^3 plus QR plus QI, its intersection is exactly QE^3: E^3 is L(E^2), while R,I are primitive.

This uses weak/hard Lefschetz, purity and the projection formula as standard imported theorems. The primitive and nonzero checks are exact exterior calculations on the fixed X.

## What follows for a putative algebraic support

Suppose alpha is supported on an algebraic codimension-three subset Z, meaning alpha restricts to zero on X minus Z. If Z is contained in a smooth D of class mE, restriction further to X minus D would also be zero, contradicting the preceding calculation. Therefore any such support cannot admit a smooth ample envelope of this class.

This does NOT prove that Z cannot exist. Every proper algebraic support is contained in divisors of sufficiently high ample degree by ideal-sheaf generation, but those divisors need not be smooth along Z. Bertini guarantees generic smoothness away from the base locus; its hypotheses do not erase a prescribed base locus. Rational signed cycle supports are finite unions, so assuming smoothness of each component would not repair this missing envelope claim either.

## Fixed-X known-algebraic falsifier to eventual smooth enveloping

Choose k sufficiently large that a line bundle A with c1(A)=kE is very ample. Three general sections give a smooth complete intersection Z of dimension three. Then

    [Z]=k^3 E^3,
    N_(Z/X)=A|Z direct_sum A|Z direct_sum A|Z.

Z IS contained in a smooth ample divisor of class kE: choose the first of its three defining divisors. This is an actual algebraic control for the Gysin formula; its class is in L H^4 as required.

Now consider any divisor D of class mE containing this SAME Z. Its defining section determines the normal first derivative along Z,

    sigma_D in H^0(Z,N*_(Z/X) tensor O_X(D)|Z).

A point of Z is singular on D exactly when this normal derivative vanishes, because the tangential derivative vanishes along Z. Thus smoothness along all of Z requires a nowhere-zero section of this rank-three bundle. A nowhere-zero section would force its top Chern class to vanish.

Each of its three summands has first Chern class (m-k)E|Z (a possible degree-zero line-bundle factor does not affect this calculation), so

    integral_Z c3(N* tensor O_X(D)|Z)
       = (m-k)^3 integral_Z E^3
       = 2160 k^3 (m-k)^3.

For every m>k this is strictly positive. Therefore EVERY containing divisor of class mE is singular somewhere on Z, even though Z is smooth, algebraic and originally contained in a smooth ample divisor of smaller degree. Containing divisors of sufficiently high degree do exist. The conclusion is not vacuous.

At m=k the top Chern obstruction is zero, and the explicit defining divisor confirms smooth existence. Zero top Chern number is NOT in general asserted sufficient for a nowhere-zero section. For m>k no assertion of the number or type of singularities is made without a transversality argument.

This known-algebraic example refutes the shortcut 'increase the degree and apply Bertini to obtain a smooth envelope'. Singular containing divisors are not by themselves evidence of nonalgebraicity of the enclosed class.

## Disposition and next construction

Constructed: the full Gysin image for smooth ample envelopes. Alpha is excluded from it. Rejected: extending that exclusion to all algebraic supports using an unjustified smooth-envelope theorem. A fixed-X complete intersection gives a genuine algebraic countercontrol to eventual smooth enveloping.

Next executable test: for this same known algebraic Z and sufficiently high degree, analyze the generic normal derivative section. Prove or disprove transversality, determine whether its zeros give ordinary double points of the containing divisor, and only then interpret the top Chern number as a singularity count. This establishes a calibrated singular-envelope source model before trying to extract any invariant that could distinguish alpha. Neither a nonzero singularity count nor a local singularity is automatically a class-level Hodge obstruction.

No universal algebraic-support exclusion or Hodge verdict is established. Verification combines the written general arguments with exact primitive, intersection and Chern-polynomial controls; it is not proof-assistant certification or a computation of all hypersurfaces on X.
