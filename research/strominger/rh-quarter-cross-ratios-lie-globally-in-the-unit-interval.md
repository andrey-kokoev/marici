# Quarter cross ratios lie globally in the unit interval

## Question

Does determinant-specific total positivity prove recurrence division validity and \(0<\Theta_{n,a}<1\) at every degree and shift?

## Claim boundary

The theorem applies for integers \(n\geq2\) and \(a\geq0\) in the quarter source family. It does not prove decay rate or an asymptotic limit.

## Disposition

Strict total positivity makes every shifted determinant positive. Condensation gives

\[
q_a(n-1)R_{n-1,a}R_{n-1,a+2}
-q_a(0)R_{n-1,a+1}^2
=R_{n,a}R_{n-2,a+2}>0.
\]

The cross term and first term are positive, so their ratio satisfies \(0<\Theta_{n,a}<1\). Every recurrence denominator is also positive. Exact verification covers 377 shifted cases and all seven orientation gates. The next leaf is `quarter-cross-ratio-degree-monotonicity`, testing and seeking a source proof that \(\Theta_{n+1,a}<\Theta_{n,a}\), a comparison input relevant to asymptotic control.
