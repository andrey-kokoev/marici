# Hardy threshold eliminates half of the subexponential flat candidates

## Question

For the weighted coefficient space

\[
w_{a,\beta}(n)=n^{1/2}e^{a(\log n)^\beta},
\]

do the logarithmic-label polynomials have a nontrivial orthogonal complement?

## Moment measure

Continuity of the augmentation identifies the positive discrete measure

\[
\mu_{a,\beta}
=
\sum_{n\ge2}rac{1}{n e^{2a(\log n)^\beta}}
\delta_{\log n}.
\]

A flat coefficient vector would determine a nonzero vector in
\(L^2(\mu_{a,\beta})\) orthogonal to every polynomial.

## Hardy exponential-square-root test

A sufficient Stieltjes-determinacy condition is the existence of \(c>0\) such that

\[
\int e^{c\sqrt{x}}\,d\mu_{a,\beta}(x)<\infty.
\]

The sum has the same tail convergence as

\[
\int_0^\infty
\exp\!\left(c\sqrt t-2at^\beta\right)dt.
\]

If \(\beta>1/2\), the negative term dominates for every fixed \(c>0\). If \(\beta=1/2\), the integral converges for every \(0<c<2a\). Thus \(\mu_{a,\beta}\) is Stieltjes determinate throughout

\[
\frac12\leq\beta<1.
\]

Determinacy makes the polynomials dense in \(L^2(\mu_{a,\beta})\). Consequently their orthogonal complement is zero, so the coefficient completion contains no nonzero vector annihilating every logarithmic moment.

## Pair consequence

A joint-flat ordered-pair packet cannot be obtained by tensoring one-copy flat vectors in this parameter range because no one-copy factor exists. More strongly, the same determinate one-coordinate marginal prevents a tensor-product orthogonal-complement construction.

## Disposition

The range \(1/2\leq\beta<1\) is eliminated as a host for the proposed completion witness even though it lies on the non-analytic side of the earlier Denjoy--Carleman test. Absence of a forced analytic neighborhood was necessary but not sufficient.

Only

\[
0<\beta<\frac12
\]

survives this Hardy determinacy obstruction. Failure of the Hardy condition in that range does not prove indeterminacy or polynomial non-density for the discrete measure.

## Claim boundary

This result applies to the stated weighted Hilbert family. It neither selects the surviving range from theta-source data nor constructs a flat sequence there. It does not infer discrete indeterminacy from the corresponding continuous Weibull density.
