# Half-Weibull staircase ratios do not expose a simple product

## Question

Does the relative staircase factor

\[
\frac{S_n(2,5/2)}{S_n(1,3/2)}
\]

collapse to an evident product of low-complexity linear factors?

Exact rational evaluation through \(n=10\) gives

\[
1,
\frac{11}{7},
\frac{879}{307},
\frac{155443}{27659},
\ldots.
\]

The successive quotients begin

\[
\frac{11}{7},
\frac{6153}{3377},
\frac{47721001}{24312261},
\ldots,
\]

and by \(n=10\) their numerator and denominator each contain roughly two hundred bits. No cancellation to a visible ratio of short linear-factor products occurs in this exact grid.

## Disposition

Complete the exact ratio reconnaissance without proposing a product formula. The staircase factor remains the obstruction; arithmetic complexity means product recognition is not currently an asymptotic method.

The next leaf is `half-weibull-staircase-lu-recurrence`: derive an LU or condensation recurrence for \(S_n(a,b)\) whose parameter shift \((a,b)\mapsto(a+1,b+1)\) can be analyzed asymptotically.

## Claim boundary

Failure to recognize a simple product through ten degrees is not a proof that no product or special-function representation exists. The repaired checker removed an unbounded trial-factorization step that timed out; it now records exact ratios with bounded bit-size metadata.
