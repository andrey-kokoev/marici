# The quarter-Weibull weight has no closed polynomial string equation

## Question

Can the canonical first Jacobi shift be proved zero by the usual polynomial Freud/string equation?

For the untruncated weight

\[
w(x)=e^{-2x^{1/4}},
\]

integration by parts gives

\[
0=\int_0^\infty \frac{d}{dx}
\left(x^{k+1}w(x)\right)dx
=(k+1)m_k-\frac12m_{k+1/4},
\]

where \(m_s=\int_0^\infty x^s w(x)dx\). Equivalently,

\[
(k+1)m_k=\frac12m_{k+1/4}.
\]

The right side is a fractional-index moment. It is not an entry of the integer Hankel matrix defining the polynomial Jacobi recurrence. Thus integration by parts does not close to a finite polynomial string equation for \(a_n,b_n\).

For fixed truncation start \(X>0\), translation to \(y=x-X\) introduces

\[
V_X'(y)=\frac12(X+y)^{-3/4},
\]

which is likewise nonpolynomial, together with endpoint terms. The standard polynomial Freud route therefore cannot prove \(a_1=0\) here.

## Disposition

Reject the proposed finite Freud/string-equation derivation. The analytic-zero question remains open and must pass through `mellin-hankel-first-shift`: obtain the two-term asymptotic of Hankel determinant ratios from the exact Mellin moments

\[
m_k=4\,\frac{\Gamma(4k+4)}{2^{4k+4}},
\]

then use the previously sourced \(n^{-3}\) fixed-start perturbation to transfer the first shift to \(X>0\).

## Claim boundary

Failure of polynomial closure does not prove \(a_1\ne0\), nor does it exclude a nonlocal or fractional string formalism. It only removes the finite polynomial Freud equation as a valid proof route.
