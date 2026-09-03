# Mellin exponential evaluations are bounded on the order completion

## Question

Does the source-derived adjacent-gap completion admit exponential Mellin evaluations on logarithmic labels?

## Claim boundary

Yes for each positive Mellin parameter: exponential evaluation extends to a bounded functional on the order completion, with an explicit cutoff-independent norm bound. The same argument applies to fixed polynomial Mellin jets. This is not yet the Gaussian completed-heat probe, whose dependence is quadratic in the logarithmic label. Density of these Mellin Riesz vectors and action of the completed gamma-plus-prime form remain separate questions.

## Evaluation functional

For a finite zero-sum coefficient packet, define

\[
L_t(c)
=
\sum_i c_i e^{-t\lambda_i},
\qquad t>0.
\]

Write

\[
c
=
\sum_i a_i(e_i-e_{i+1}).
\]

Then

\[
L_t(c)
=
\sum_i a_i
\left(
e^{-t\lambda_i}-e^{-t\lambda_{i+1}}
\right)
\]

and

\[
\lVert c\rVert_{\rm ord}^2
=
2\sum_i
(\lambda_{i+1}-\lambda_i)|a_i|^2.
\]

Therefore the exact squared dual norm on a finite cutoff is

\[
\lVert L_t\rVert_*^2
=
\sum_i
\frac{
|e^{-t\lambda_i}-e^{-t\lambda_{i+1}}|^2
}{
2(\lambda_{i+1}-\lambda_i)
}.
\]

## Uniform bound

For \(F_t(\lambda)=e^{-t\lambda}\), Cauchy--Schwarz on each adjacent interval gives

\[
\frac{|F_t(\lambda_i)-F_t(\lambda_{i+1})|^2}
{\lambda_{i+1}-\lambda_i}
\leq
\int_{\lambda_i}^{\lambda_{i+1}}
|F_t'(u)|^2du.
\]

Summing disjoint intervals yields

\[
\lVert L_t\rVert_*^2
\leq
\frac12
\int_{\lambda_0}^{\infty}
 t^2e^{-2tu}du
=
\frac t4e^{-2t\lambda_0}.
\]

The bound is independent of the conductor cutoff. Hence \(L_t\) extends continuously to \(\mathcal H_{\rm ord}\).

## Mellin jets

For each fixed integer \(m\geq0\), replace \(F_t\) by

\[
F_{t,m}(\lambda)
=
\lambda^m e^{-t\lambda}.
\]

Its derivative is square-integrable on \([\lambda_0,\infty)\) for \(t>0\). The same interval estimate therefore makes

\[
c
\longmapsto
\sum_i c_i\lambda_i^m e^{-t\lambda_i}
\]

a bounded functional on the order completion.

## Coherencer consequence

The order completion and the heat/Mellin probe family are not topologically disjoint. Every positive-heat probe has a Riesz vector in \(\mathcal H_{\rm ord}\). This supplies a bounded observation arrow

\[
\mathcal H_{\rm ord}
\longrightarrow
\mathbb C
\]

for each \((t,m)\).

This is weaker than the required source--Weil comparison. Scalar probes do not by themselves construct an operator between the arithmetic and zero-side Hilbert spaces.

## New residual

The next residual is whether the Riesz vectors of all \(L_{t,m}\) form a graph-norm-dense core for a completed arithmetic form operator. Three facts remain missing:

1. density or joint faithfulness of the full heat-jet family in \(\mathcal H_{\rm ord}\);
2. a source-derived closed or closable operator representing the gamma-plus-prime form;
3. a lower bound uniform over the heat-polynomial family.

## Gaussian-corona comparison

The Gaussian regularized corona has generator norm growing like its width parameter. The present heat-functional bound instead behaves as

\[
\lVert L_t\rVert_*
\leq
\frac{\sqrt t}{2}e^{-t\lambda_0}.
\]

Any proposed identification between the two must specify a source-derived relation between the Gaussian width and heat parameter and show that these opposed scales yield a bounded map. No such relation is supplied here.

## Disposition

A necessary compatibility gate has passed: positive-heat Mellin jets act continuously on the source-positive order completion. `common_closed_form_domain` remains blocked at density and completed-form action.

## Verification

- `research/voevodsky/checkers/check_heat_evaluation_order_bound.py`
- `research/voevodsky/results/heat_evaluation_order_bound.json`
