# Quarter solid minors have exact Newton positivity certificates

## Question

Can low-order contiguous source minors be certified positive for every integer shift without relying on sampled shifts or unavailable symbolic-factor tooling?

## Claim boundary

The certificate covers 48 minor families of sizes one through three, with row and column starts zero through three. It does not cover arbitrary minor size or noncontiguous minors.

## Disposition

Each minor is a polynomial in the integer shift. Exact forward differences through its degree bound give a Newton expansion in binomial polynomials. Every coefficient is nonnegative, every constant coefficient is positive, and every post-bound difference vanishes. Therefore all 48 families are strictly positive for every integer shift \(a\geq0\). A reversed-row control is negative. The SymPy preflight was refused by structured-command policy, so no shell fallback was used; the exact dependency-free Newton certificate replaced factorization. The next executable leaf is `quarter-solid-minor-newton-size-four`, testing whether the certificate persists at the first untested minor size.
