# Rank-uniform positivity needs a semibounded form, not a bounded GNS operator

## Question

Is uniform boundedness of normalized finite prime matrices necessary for the all-rank cone?

## Claim boundary

No. It is a strong sufficient condition, not a necessary one. The correct higher object may be an unbounded closable quadratic form with lower bound `-1` relative to the positive reference form. All-rank positivity controls the lower spectral edge but does not control the upper operator norm.

## Finite compression distinction

Let `G_N>0` be the reference Gram matrix and `P_N` the coupled gamma-remainder-plus-prime matrix. Define

\[
T_N=G_N^{-1/2}P_NG_N^{-1/2}.
\]

The completed finite cone is exactly

\[
I+T_N\ge0,
\]

or

\[
\lambda_{\min}(T_N)\ge-1.
\]

This imposes no upper bound on `lambda_max(T_N)` and therefore does not imply

\[
\sup_N\|T_N\|<\infty.
\]

A positive unbounded multiplication operator supplies the elementary model: every finite compression is positive, while compression norms diverge.

## Correct completion object

On the polynomial core in the positive reference Hilbert space, let `p[p]` denote the coupled remainder quadratic form. The required conditions are:

1. the form is densely defined and symmetric;
2. it is closable, or admits a specified closed extension;
3. it obeys the lower bound
   \[
   p[p]\ge-\|p\|_\Gamma^2;
   \]
4. the polynomial core remains a form core for the closure.

The representation theorem for closed semibounded forms then produces a possibly unbounded self-adjoint operator `T` with

\[
\inf\operatorname{spec}(T)\ge-1.
\]

Bounded Riesz representation is only the special case where the form is bounded on the reference Hilbert norm.

## Near-null warning

The first gamma correction on `p_m=(1-y)^m` has relative size of order `log log m` against the leading small-heat reference energy in the fixed-ratio saddle calculation. This does not by itself prove unboundedness of the exact fixed-parameter form, because that asymptotic was not uniform over unrestricted `m`. It does show that a degree-uniform two-sided norm bound is not the natural quantity and cannot be assumed from fixed-rank asymptotics.

Positive growth in selected directions is harmless for the cone; only the lower edge matters.

## Strongest falsification attempt

Replacing boundedness by semiboundedness does not make the RH gate easier: proving closability and the lower bound still requires source-valid control of the regularized prime cosine functional. It only prevents rejection of a valid positive form because its upper spectrum is unbounded.

## Disposition

Revise the GNS gate from uniform operator norm to compatible closability plus a uniform lower form bound. Continue to track finite normalized matrices by their least eigenvalues and negative parts, not their full norms.