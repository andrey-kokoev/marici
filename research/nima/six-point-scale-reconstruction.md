# Six-point reconstruction of positive channel scales

## Question

After the five six-point binomial relations pass, can the nine channel scales be reconstructed without fitting ambiguity?

## Claim boundary

The reconstruction applies to positive weights in the declared channel and triangulation ordering. Signed or complex weights require additional sign or root-branch data.

The `14 by 9` incidence matrix `A` has full column rank. Therefore

\[
L=(A^T A)^{-1}A^T
\]

is a rational left inverse with `L A=I_9`. For factorable positive weights,

\[
\log w=A\log\lambda,
\qquad
\log\lambda=L\log w,
\]

so each scale is the explicit monomial

\[
\lambda_c=\prod_T w_T^{L_{cT}}
\]

with the unique positive real roots. The result is independent of this particular left inverse on the factorable locus: two left inverses differ by rows in the left-kernel annihilator, whose binomials equal one there.

The checker records all `9 by 14` rational exponents and verifies `L A=I_9`. It assigns distinct primes to the nine channel scales, generates all fourteen triangulation weights, and reconstructs every prime valuation exactly. No floating logarithms or approximate roots are used.

## Disposition

Passing six-point weights determine unique positive channel scales. The owner acceptance flow is now constructive: test five binomials, then apply the recorded monomials. This reconstruction cannot authenticate the weights or extend to signs without a separate orientation analysis.
