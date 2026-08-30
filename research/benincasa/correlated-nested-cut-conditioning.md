# Correlated nested Cuts require conditional coefficient pushforward

Let internal Gaussian occurrences \(3,4\) have covariance

\[
\mathbb E[q_3^2]=\nu_3,
\qquad
\mathbb E[q_4^2]=\nu_4,
\qquad
\mathbb E[q_3q_4]=\kappa.
\]

The joint Wick contraction is

\[
\mathbb E[q_3^2q_4^2]
=
\nu_3\nu_4+2\kappa^2.
\]

Composing the two marginal Cut functionals as if the occurrences were independent gives only \(\nu_3\nu_4\). It misses the connected pairing

\[
\boxed{2\kappa^2.}
\]

The correct sequential operation is conditional. Given \(q_3\),

\[
\mathbb E[q_4\mid q_3]=\frac{\kappa}{\nu_3}q_3,
\qquad
\operatorname{Var}(q_4\mid q_3)
=
\nu_4-\frac{\kappa^2}{\nu_3}.
\]

Taking the conditional expectation and then integrating \(q_3\) reproduces \(\nu_3\nu_4+2\kappa^2\). Reversing the conditioning order gives the same result.

Thus correlated nested Cut sewing remains associative only when the coefficient state is transported conditionally. Naive occurrencewise marginal pushforward is mistyped. The missing \(2\kappa^2\) is a connected coefficient pairing carried by the existing joint process object, not a new carrier incidence.
