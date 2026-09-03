# A sharp overlap cut has a singular cross-Vandermonde interface

## Question

Can the cross-Vandermonde interaction be expanded uniformly across the sharp cut \(A=[0,y_*]\), \(B=[y_*,\infty)\)?

For one local and one far coordinate, the interface factor is

\[
(y-x)^2.
\]

Taking \(x=y_*-\varepsilon\) and \(y=y_*+\varepsilon\) gives

\[
(y-x)^2=4\varepsilon^2\longrightarrow0,
\qquad
2\log(y-x)\longrightarrow-\infty.
\]

Thus no uniform logarithmic expansion exists on the closed adjacent regions. In particular, the far-field expansion

\[
2\log(y-x)=2\log y-2x/y+O((x/y)^2)
\]

requires \(x/y\leq1-\delta\), which fails arbitrarily close to the shared cut.

For \(k(n-k)\) cross pairs, even a bounded per-pair remainder would accumulate at order \(n^2\). The interface estimate therefore needs both geometric separation and particle-number scaling.

## Repair

Use three regions with two cuts,

\[
A=[0,y_-],\qquad C=[y_-,y_+],\qquad B=[y_+,\infty),
\]

where \(y_-/y_+\leq1-\delta_X\). The transition region \(C\) must remain in the exact ensemble; it cannot be discarded. The growing scalar overlap permits both cuts to lie where Laguerre and Weibull descriptions are valid.

## Disposition

Reject a uniform cross-interface expansion at one sharp cut. The next leaf is `buffered-three-region-factorization`: construct the exact multinomial sector decomposition and identify conditions on \(\delta_X\), transition occupancy, and accumulated cross-pair error.

## Claim boundary

The singularity does not invalidate the exact two-region factorization. It blocks only a uniform separated-variable asymptotic of its cross term.
