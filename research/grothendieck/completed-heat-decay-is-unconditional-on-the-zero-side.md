# Completed heat decay is unconditional on the zero side

## Question

Is the decay premise needed to force the endpoint atom itself RH-strength?

## General zero parameter

For a nontrivial zero

\[
\rho=\beta+i\gamma,
\qquad 0<\beta<1,
\]

put

\[
\lambda_\rho=-(\rho-1/2)^2
=\gamma^2-(\beta-1/2)^2-2i\gamma(\beta-1/2).
\]

The completed Gaussian explicit formula has zero-side factors

\[
e^{-t\lambda_\rho}.
\]

RH is the assertion that the imaginary parts of all `lambda_rho` vanish, not the assertion that their real parts are positive.

## Decay estimate

Because `|beta-1/2|<1/2`,

\[
\operatorname{Re}\lambda_\rho
\ge \gamma^2-1/4.
\]

A source-authorized zero-free compact region containing `|gamma|<=1/2` therefore gives a uniform positive lower bound for `Re(lambda_rho)`. More generally, discreteness plus an admitted lower bound `|gamma|>1/2` suffices.

Using the classical zero count `N(T)=O(T log T)`, for every fixed positive `t_0` the series

\[
\sum_\rho e^{-t\lambda_\rho}
\]

converges normally for `t>=t_0`, dominated by a Gaussian ordinate sum. Dominated convergence then gives

\[
H(t)\longrightarrow0
\qquad(t\longrightarrow\infty).
\]

No condition `beta=1/2` enters this decay argument.

## Effect on the endpoint reduction

Once the completed Gaussian explicit formula and the low-ordinate zero-free bound are admitted, decay is not the remaining RH gate. Combining it with all-rank positivity of the gamma-plus-prime remainder localizer forces the exact atom

\[
c_h(t)\delta_{e^{h/4}}
\]

and leaves a positive completed localizer.

Thus the only RH-strength source target in this reduction is the remainder Hankel cone.

## Source boundary

The argument requires an exact zero-side identity for the completed source with the general complex factors `exp(-t lambda_rho)`, not the numerical validation sum over ordinates that silently sets `beta=1/2`. It also requires a cited zero-free bound below ordinate `1/2` and the standard zero-count estimate. These inputs are classical but must be attached before the decay claim is promoted to a theorem.

## Disposition

Treat completed heat decay as an unconditional analytic lemma pending source citation. Do not allocate prime-number-theorem-scale cancellation work merely to prove the limit from the endpoint--gamma--prime presentation; transfer decay through the exact Gaussian explicit formula instead.