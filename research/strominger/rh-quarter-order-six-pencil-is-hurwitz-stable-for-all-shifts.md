# Quarter order-six pencil is Hurwitz stable for all shifts

## Question

Can all degree-64 Hurwitz minors be certified without separate determinant interpolation?

## Claim boundary

The theorem covers source order six. It does not prove the observed Bernstein positivity at arbitrary source order.

## Disposition

A shared 65-node rational grid was used. At each node, one exact Routh array yields every principal Hurwitz determinant by cumulative products of its first-column entries. Degree bounds then reconstruct all 64 minor polynomials. Every Bernstein coefficient is strictly positive, and the degree-dropped endpoint is Hurwitz stable. Thus the order-six pencil is Hurwitz stable for every \(t\in[0,1]\), and covariance extends this to every \(s\geq0\). The run takes 19 seconds. Repeating source orders is now stopped. The next leaf is `quarter-hurwitz-mixed-column-minors`, testing the stronger mechanism that each Bernstein coefficient is a positive sum of mixed column determinants of the two endpoint Hurwitz matrices.
