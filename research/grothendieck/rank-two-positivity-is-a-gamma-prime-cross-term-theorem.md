# Rank-two positivity is a gamma--prime cross-term theorem

## Question

Does the first remainder Hankel determinant decompose into separately positive gamma and prime contributions?

## Exact decomposition

Let

\[
g_n=\Gamma(s_n)-\Gamma(s_{n+1}),
\qquad
p_n=P(s_n)-P(s_{n+1}),
\qquad
s_n=t+nh.
\]

For `a_n=g_n+p_n`, the first determinant is

\[
D_2=a_0a_2-a_1^2
=D_2^\Gamma+D_2^{\mathbb P}+C_{\Gamma,\mathbb P},
\]

where

\[
D_2^\Gamma=g_0g_2-g_1^2,
\qquad
D_2^{\mathbb P}=p_0p_2-p_1^2,
\]

and

\[
C_{\Gamma,\mathbb P}=g_0p_2+p_0g_2-2g_1p_1.
\]

## Numerical falsification of sectorwise positivity

An uncertified source scan with prime cutoff `200000` gave:

- at `(t,h)=(0.01,0.005)`,
  `D2_gamma=-2.074e-4`, `D2_prime=-2.389e-6`,
  cross term `+3.451e-4`, total `+1.353e-4`;
- at `(t,h)=(0.05,0.01)`,
  `D2_gamma=-8.331e-6`, `D2_prime=-8.626e-6`,
  cross term `+1.703e-5`, total `+7.553e-8`.

Thus both sector determinants are negative in the transition and larger-heat samples. The positive total is supplied by the gamma--prime cross term and becomes a small residual after cancellation.

At `(0.001,0.001)` the gamma determinant dominates positively while the prime contribution is exponentially suppressed, matching the short-heat regime.

## Consequence

No block-diagonal Gram factor

\[
R=R_\Gamma\oplus R_{\mathbb P}
\]

can prove the remainder cone uniformly, because its rank-two sector minors already have the wrong signs. The source factor must contain an off-diagonal gamma--prime coupling whose rank-two shadow is exactly `C_(Gamma,P)`.

This is more restrictive than the earlier statement that sector terms change sign: the first nonlinear cone inequality quantitatively requires cross-sector repair.

## Candidate analytic target

The first source theorem should prove

\[
C_{\Gamma,\mathbb P}
\ge -D_2^\Gamma-D_2^{\mathbb P}
\]

uniformly in `t,h>0`, with a strict residual matching the completed zero-side determinant. Any proof by separate lower bounds that discards the correlation among `g_0,g_1,g_2` and `p_0,p_1,p_2` is structurally too weak in the observed cancellation regime.

## Boundary

The scan is not interval-certified and the prime tail is truncated. The signs at the displayed parameters are numerically well separated except the final positive residual, but they remain observations rather than theorems.

## Disposition

Reject sectorwise Gram and sectorwise log-convexity routes. Search for a coupled gamma--prime bilinear identity or integral transform that makes `C_(Gamma,P)+D2_gamma+D2_prime` positive as one object.