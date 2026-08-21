# The fifth blind spectral edge is interval-certified

For test point `x`, outward Sturm pivots

\[
 d_0=a_0-x,\qquad d_k=a_k-x-\frac{b_k}{d_{k-1}}
\]

count eigenvalues below `x` whenever no pivot box meets zero. Bisection between
certified inertia counts four and five gives

\[
 u_{\max}^{(5)}\in
[0.00499898469148721484,\ 0.00499898469353575090].
\]

Directed propagation yields

\[
 \boxed{\widehat\gamma_1^{(5)}\in
[14.1347310022873317,\ 14.1347310051870944]}.
\]

The width is about `2.9e-9`. Almost all of the roughly `5.9e-6`
post-construction discrepancy from the standard first ordinate is therefore
finite-rank approximation error, not arithmetic uncertainty.

## Scope

This certifies an eigenvalue of the finite source-derived interval matrix. It
does not certify the external comparison, identify the limiting edge, or prove
RH. No zero enters the matrix or bisection.

## Durable verification

- Checker: `checkers/quarter_point_fifth_ritz_interval.py`
- Result: `results/quarter-point-fifth-ritz-interval.json`
