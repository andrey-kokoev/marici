# Canonical-form uniqueness on a fixed five-line arrangement

## Question

Once a projective pentagon arrangement is fixed, do its interval residues and absence of an infinity-divisor pole determine the rational two-form?

## Claim boundary

The theorem assumes five distinct affine facet lines, at most simple poles on their projective closures, prescribed normal-first residues, and no pole along the infinity divisor. It does not select the arrangement.

Let two candidate forms have the same facet residues and set their difference to

\[
\eta=\frac{N(x,y)}{\prod_{i=0}^4a_i(x,y)}dx\wedge dy.
\]

In the chart `x=1/z,y=w/z`, regularity along `z=0` requires `deg N<=2`: a degree-`d` numerator contributes order `z^(2-d)`. Vanishing residue on `a_i=0` means `N` restricts identically to zero on that line, so the irreducible affine linear polynomial `a_i` divides `N`. Distinct facet equations are coprime; therefore their degree-five product divides `N`. The degree bound forces `N=0`, proving uniqueness.

For the explicit reference arrangement, an independent linear-algebra check starts from a general quadratic numerator with six coefficients. Restriction to all five lines gives a coefficient matrix of rank six and zero-dimensional kernel.

Infinity regularity is essential to this argument. The affine form `dx wedge dy` has zero facet residues and can be written with numerator equal to the degree-five denominator, but it has a third-order pole at projective infinity. It is therefore an explicit nonunique rival if the infinity condition is dropped.

## Disposition

Residues and projective regularity uniquely determine the form after the embedded facet arrangement and pole class are admitted. They provide no reverse arrow selecting that arrangement from the common-Jacobian family; positive-geometry or source data must still supply the embedding and supports.
