# TP2 signed-autocorrelation implication

## Question

Do positive log-concave coefficient sequences with monotone likelihood-ratio order automatically satisfy the signed autocorrelation inequality required by D dominance?

## Claim boundary

No. For `a(x)=1+x` and `b(x)=1+10x+100x^2`, both coefficient sequences are positive and log-concave, and `b_i/a_i` increases on common support. Nevertheless the `omega^2` coefficient of

\[
|a(i\omega)|^2+2\operatorname{Re}(a(i\omega)\overline{b(i\omega)})
\]

is `-179`. This refutes the generic implication, not the observed D-family inequality. The governing DPC case remains `rh-quarter-D-imaginary-axis-dominance.md`.

## Disposition

Reject log-concavity plus ordinary TP2 as sufficient. The counterexample localizes the missing condition to alternating convolution and the coefficient of `b` beyond the common support. The next test must use D-specific alternating Toeplitz/Hurwitz minors or a positive-real ratio condition rather than ordinary coefficient order.
