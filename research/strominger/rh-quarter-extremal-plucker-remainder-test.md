# The extremal Hall slack is not a direct Plücker identity

## Question

Can the extremal three-supply/two-demand slack be identified directly with a Plücker or Desnanot–Jacobi relation using only its five source monomials?

## Claim boundary

No. Every source term has bidegree \((1,1)\):

\[
(-1)^{|R|+|K|}\det A_{K^c,R^c}\det B_{K,S}.
\]

For the five extremal labels, the complementary \(A\)-minor labels are

\[
\{1,q\},\qquad q\in\{3,4,5,6,7\}.
\]

Thus the support is a five-ray star, but it contains only diagonal pairings between each \(A_{1q}\) and its complementary \(B\)-minor. A quadratic Plücker relation on four varying indices requires off-diagonal cross-pair products, none of which occur in the Hall slack. Exact enumeration also finds no cancelling proper source-signed subset and no three-term unit-signed cancellation. The positive normalized remainder remains nonzero.

This excludes a direct identity on the observed five monomials. It does not exclude an enlarged identity that introduces cross terms and proves their remainder positive.

## Disposition

Reject the direct Plücker/Desnanot route. The more structural surviving rival is lattice positivity: test whether the absolute source weights are log-supermodular on Gale diamonds. Such a property could organize monotone transport without requiring a local cancellation identity.
