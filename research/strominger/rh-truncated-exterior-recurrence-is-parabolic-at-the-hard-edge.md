# The truncated exterior recurrence is parabolic at the hard edge

## Question

What recurrence mechanism can produce algebraic rather than exponential continuation across the deleted compact interval?

For truncated orthonormal polynomials,

\[
a_{n+1}Q_{n+1}(x)
=(x-b_n)Q_n(x)-a_nQ_{n-1}(x).
\]

At fixed exterior \(x<X\), the coefficient scale is \(a_n,b_n\asymp n^4\), so \(x/a_{n+1}\) is lower order. The relevant hard-edge defect is

\[
\varepsilon_n=
\frac{a_n+a_{n+1}-b_n}{a_{n+1}}.
\]

If \(\varepsilon_n\to0\) and \(a_n/a_{n+1}\to1\), the limiting recurrence is

\[
Q_{n+1}+2Q_n+Q_{n-1}=0,
\]

whose characteristic polynomial is \((\lambda+1)^2\). This double root is parabolic: subleading coefficient terms select power-law solutions. A hyperbolic limiting recurrence would instead produce exponential growth or decay and would not explain the observed \(n^{-2}\) compact mass.

The finite truncated grid shows the edge defect decreasing through the available degrees and the ratio \(b_n/(a_n+a_{n+1})\) approaching one.

## Disposition

Resolve the recurrence mechanism as a parabolic hard-edge problem. The next leaf is `parabolic-recurrence-indicial-exponent`: derive the power exponent from two-term asymptotics of \(a_n\), \(b_n\), and \(\varepsilon_n\).

## Claim boundary

Finite approach to a double root does not prove coefficient asymptotics or select the recessive solution. No exterior-mass bound follows without an indicial analysis and normalization control.
