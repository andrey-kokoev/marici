# D positive-real diagonal Gram certificates

## Question

Can the bounded Cayley pairs be certified positive real by an exact positive-semidefinite polynomial Gram object?

## Claim boundary

For `N=P+R` and `A=P-R`,

\[
\operatorname{Re}(N(i\omega)\overline{A(i\omega)})
=|P(i\omega)|^2-|R(i\omega)|^2.
\]

In all 21 tested cases this polynomial is represented by a diagonal Gram matrix in the monomial vector `(1,omega,...)`; every diagonal entry is strictly positive. Dimensions range from 4 upward with no zero entry. This exactly certifies strict boundary positive-realness for the bounded Cayley pairs. It is not a standard state-space KYP matrix and does not prove uniform positivity. The governing DPC case remains `rh-quarter-D-imaginary-axis-dominance.md`.

## Disposition

The bounded-real backend now has explicit positive-definite Gram certificates. The all-order obligation is precisely to derive the Gram diagonal entries recursively as positive source expressions; no additional finite matrix census is needed.
