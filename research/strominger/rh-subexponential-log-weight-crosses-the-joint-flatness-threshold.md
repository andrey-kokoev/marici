# Subexponential log weight crosses the joint-flatness threshold

## Question

Is there a coefficient completion on which every logarithmic moment is continuous but the associated Dirichlet transform need not be analytic near the moment basepoint?

## Weight family

For parameters \(a>0\) and \(0<\beta<1\), put

\[
w_{a,\beta}(n)=n^{1/2}\exp\!\left(a(\log n)^\beta\right).
\]

Use the Hilbert carrier with norm

\[
\|c\|_{a,\beta}^2=\sum_{n\ge1}|c_n|^2w_{a,\beta}(n)^2,
\]

and its Hilbert tensor square for ordered pairs. The factor \(n^{1/2}\) is the reciprocal of the native theta half-density; the subexponential factor is functional calculus of logarithmic degree. This defines a candidate family, not a source-selected member.

## Moment continuity

The squared dual norm of the \(k\)-th logarithmic moment is controlled by

\[
\sum_{n\ge2}\frac{(\log n)^{2k}}
 {n\exp(2a(\log n)^\beta)}.
\]

The integral test reduces this to

\[
\int_0^\infty t^{2k}e^{-2at^\beta}\,dt
=
\frac1\beta(2a)^{-(2k+1)/\beta}
\Gamma\!\left(\frac{2k+1}{\beta}\right),
\]

which is finite for every fixed \(k\). Hence every one-copy moment and every joint product-ratio moment is continuous.

## No analytic neighborhood

For every \(\delta>0\), the corresponding positive exponential moment contains

\[
\sum_{n\ge2}
\frac{n^{2\delta}}
 {n\exp(2a(\log n)^\beta)}.
\]

After \(t=\log n\), its integral exponent is

\[
2\delta t-2at^\beta,
\]

which tends to positive infinity because \(\beta<1\). Thus the dual moment transform has no forced analytic neighborhood of the origin. The entire-Dirichlet argument that killed the rapid-label completion no longer applies.

## Denjoy--Carleman threshold

Let \(M_k\) be the square root of the displayed moment integral. Stirling asymptotics give

\[
M_k^{-1/k}\asymp k^{-1/\beta}.
\]

Therefore

\[
\sum_{k\ge1}M_k^{-1/k}<\infty
\qquad(0<\beta<1).
\]

This is the non-quasi-analytic side of the Denjoy--Carleman threshold. At \(\beta=1\), the comparison becomes harmonic and returns to the quasi-analytic boundary.

## Disposition

The family \(w_{a,\beta}\) passes the necessary topology test: all joint moments are continuous, while moment flatness is not prohibited by analyticity. It does not yet construct a nonzero discrete ordered-pair packet with all moments zero, prove continuity of polarized theta synthesis or the boundary current, or select \(a,\beta\) from the source. Those are separate gates.

## Claim boundary

Non-quasi-analyticity permits compactly supported flat functions in the corresponding continuous theory; it does not automatically produce a flat sequence on the discrete logarithmic label set. No coefficient witness is claimed here.
