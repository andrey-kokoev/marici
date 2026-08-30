# Minimum Norm Does Not Canonically Trivialize an Actuator Torsor

Consider the lift torsor

\[
B_t=\begin{pmatrix}1\\t\end{pmatrix},
\qquad t\in\mathbb R.
\]

A positive-definite actuator metric (G) selects a unique minimum-cost lift by
minimizing

\[
\mathcal E_G(t)=B_t^TGB_t.
\]

But the selected origin depends on (G). For

\[
G_c=\begin{pmatrix}1&c\\c&1\end{pmatrix},
\qquad |c|<1,
\]

one has

\[
\mathcal E_{G_c}(t)=1+2ct+t^2,
\]

whose unique minimizer is

\[
t_*=-c.
\]

Thus three equally positive metrics with (c=0,1/2,-1/2) select the three
different lifts (t=0,-1/2,1/2). Only the first preserves the protected
logical coordinate in the earlier fixture.

The Moore–Penrose or minimum-energy prescription is therefore canonical only
after a source metric, adjoint, and topology have been frozen. It cannot supply
those data itself. Choosing the metric so that the desired nondisturbing lift
is orthogonal to the kernel torsor fits the answer.

## Completion gate

For cutoff families (G_N), pointwise positive definiteness is insufficient.
The metrics must be uniformly equivalent to the authorized source norm:

\[
m\|x\|^2\le x^*G_Nx\le M\|x\|^2
\]

with fixed (0<m\le M<\infty). Even then, varying cross terms may move the
chosen torsor origin unless the source supplies a coherent metric transport.
The selected lifts must separately satisfy logical nondisturbance and successor
naturality.

## Falsifiers

- Different authorized-looking positive metrics choose different lifts.
- The metric is introduced only to make the desired shear vanish.
- Positive-definite cutoff metrics lose uniform equivalence.
- The pseudoinverse is computed in an untransported Euclidean chart.
- Minimum cost is reported as physical executability without a cost
  constructor.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
9/10. Metric minimizer, metric dependence, nondisturbance, and uniformity were
frozen.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Strict convexity supplied a unique origin only relative to a chosen
metric; exact positive metrics selected different logical shears. Minimum norm
does not canonically trivialize the torsor without source metric authority.
