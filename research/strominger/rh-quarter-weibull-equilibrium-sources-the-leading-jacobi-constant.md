# Quarter-Weibull equilibrium sources the leading Jacobi constant

## Question

Which part of the Mellin-Hankel determinant-ratio asymptotic follows directly from the source potential?

For

\[
V(x)=2x^\beta,
\]

the one-cut hard-edge equilibrium endpoint \(b_n\) satisfies

\[
n=\frac1{2\pi}\int_0^{b_n}
\frac{xV'(x)}{\sqrt{x(b_n-x)}}dx
=\frac{\beta}{\pi}
B\!\left(\beta+\frac12,\frac12\right)b_n^\beta.
\]

Hence

\[
b_n=
\left[
\frac{\pi}{\beta B(\beta+1/2,1/2)}
\right]^{1/\beta}n^{1/\beta}.
\]

The leading Jacobi coefficient is one quarter of the support endpoint. For \(\beta=1/4\),

\[
a_n\sim A n^4,
\qquad
A=\frac14
\left[
\frac{\pi}{\beta B(\beta+1/2,1/2)}
\right]^4
=189.072720\ldots.
\]

This agrees with the exact degree-twenty-two determinant extrapolation \(189.072733\) to relative error below \(7\times10^{-8}\).

## Disposition

Resolve the leading term of the Mellin-Hankel asymptotic. Homogeneity produces an exact \(n^4\) equilibrium scale with no shift at equilibrium order, but it does not control the first fluctuation correction to the recurrence coefficient.

The next leaf is `hard-edge-first-fluctuation`: determine whether the hard-edge fluctuation expansion has an \(n^{-1}\) term for source density exponent zero. Its vanishing is the remaining analytic content of \(a_1=0\).

## Claim boundary

The equilibrium calculation proves the leading constant, not

\[
a_n=A n^4(1+O(n^{-2})).
\]

A strong asymptotic theorem or direct determinant analysis is still required for that remainder.
