# The normalized-pivot cubic is not an independent coefficient

## Question

Does the coefficient \(-13/50\) add an independent constraint?

Let

\[
R_m=Cm^2\left(1+\frac{a}{m}+O(m^{-2})\right).
\]

Using \(m=n-1\),

\[
R_{n-1}=Cn^2
\left(1+\frac{a-2}{n}+O(n^{-2})\right).
\]

For the quarter source vector,

\[
q_{n-1}=n^4
\left(1+\frac{3}{2n}+O(n^{-2})\right).
\]

The exact relation \(1-A_n=q_0R_{n-1}/q_{n-1}\), where \(A_n\) is the normalized pivot ratio, therefore gives

\[
1-A_n
=q_0C n^{-2}
\left(1+\frac{a-7/2}{n}+O(n^{-2})\right).
\]

Substituting

\[
q_0=\frac{105}{32},\qquad
C=\frac{104}{1575},\qquad
a=\frac{47}{10}
\]

yields

\[
q_0C=\frac{13}{60},
\qquad
a-\frac72=\frac65,
\qquad
q_0C\left(a-\frac72\right)=\frac{13}{50}.
\]

Hence the normalized-pivot cubic coefficient is a consequence of the amplitude and first global correction. Treating it as a third independent datum would double-count the same asymptotic information.

## Disposition

Resolve this leaf by removing the cubic coefficient as an independent proof obligation. The two genuine analytic gates are `quarter-pivot-renormalized-product`, proving \(C=104/1575\), and `quarter-global-shift-first-correction-proof`, proving \(a=47/10\).

## Claim boundary

The dependency calculation is exact conditional on the two candidate constants. It proves neither candidate.
