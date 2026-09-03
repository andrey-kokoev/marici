# Quarter anti-sign-symmetry inducts the P-matrix property

## Question

Are negative paired almost-principal products sufficient to generate every positive principal minor?

## Claim boundary

The criterion is a general finite-matrix theorem. Its complete exact instantiation is verified for the order-eight transfer. The missing all-order step is proving paired-product negativity for every Hurwitz transfer size.

## Disposition

Desnanot–Jacobi gives

\[
p(S\cup\{i,j\})
=\frac{p(S\cup i)p(S\cup j)-u_{S;i,j}v_{S;i,j}}{p(S)}.
\]

Positive diagonal supplies the size-one base. If all smaller principal minors are positive and \(uv<0\), both terms in the numerator are positive, so the next principal minor is positive. All 247 nontrivial steps reconstruct the exact order-eight determinants, yielding all 256 positive principal minors without assuming them. The next leaf is `quarter-almost-principal-interval-parity`, testing whether the observed base-set sign changes follow the rule \((-1)^{|S\cap(i,j)|}\); this would orient every individual almost-principal minor while retaining opposite paired signs.
