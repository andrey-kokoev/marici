# Theta Q bounded-interval majorant

Author: `marici.Grothendieck`
Status: numerical sweep only; analytic sign unverified
Predecessor: `theta-H-local-bochner-moments.md`

## Question

Does the exact two-component residual

\[
Q(x,p(x))
\]

remain positive on the bounded interval not covered by the endpoint and asymptotic arguments?

## Bounded sweep

A dependency-free Python evaluation used the exact displayed rational formulas for \(\Delta'\), \(\Delta''\), \(\Delta'''\), \(C\), and

\[
p(x)=\frac{4(4x-3)e^{-3x/2}/(x-3)}
{1+4(4x-3)e^{-3x/2}/(x-3)}.
\]

The grid \(x=6+k/1000\), \(0\le k\le94000\), gave

\[
\min Q=27602.7488794206
\]

at \(x=6\), with

\[
Q(100)=7637944680.030292.
\]

Execution reference: `structured_command_execution:e_19044_1788236251038823700_12`.

## Monotonicity reconnaissance

Because

\[
\frac{dp}{dx}=pq\frac{\Delta'}{2x}<0,
\]

the exact derivative can be organized as

\[
\frac{dQ}{dx}=Q_x+Q_p\,pq\frac{\Delta'}{2x},
\]

where \(Q_x\) and \(Q_p\) are rational in \(x\) and polynomial in \(p\). A centered-difference sweep on the same grid, with step \(10^{-5}\), found its smallest derivative estimate at the endpoint:

\[
\min Q'\approx27374.98330097878
\qquad(x=6).
\]

Execution reference: `structured_command_execution:e_19044_1788236355579918500_13`.

No sampled loss of monotonicity occurred. The large derivative margin makes an exact lower bound more appropriate than interval subdivision.

## Exact polynomial reduction in the mixture weight

Because

\[
C=c_1+p\Delta'',
\qquad q=1-p,
\]

the residual is exactly quadratic in \(p\):

\[
Q=Q_0+pQ_1+p^2Q_2,
\]

with

\[
\begin{aligned}
Q_0&=4\Delta'\Delta'''-(\Delta'')^2
 +(6\Delta''+8c_1)(\Delta')^2+(\Delta')^4,\\
Q_1&=-4\Delta''(\Delta')^2-6(\Delta')^4,\\
Q_2&=6(\Delta')^4.
\end{aligned}
\]

Differentiation gives

\[
Q'=Q_0'+pQ_1'+p^2Q_2'
+p'(Q_1+2pQ_2).
\]

Here \(p'<0\). Moreover,

\[
Q_1+2pQ_2
=-4\Delta''(\Delta')^2
-6(1-2p)(\Delta')^4<0
\]

on \(x\ge6\), using the earlier derivative bounds. Hence the entire \(p'\)-term is positive and may be discarded in a lower bound. The monotonicity proof is reduced to the rational inequality

\[
Q_0'+pQ_1'+p^2Q_2'>0.
\]

This removes differentiation of the exponential weight from the hard part; only the small envelope \(0<p<28e^{-9}\) remains.

## Coefficient-derivative signs

Put

\[
A=-\Delta'>0,
\qquad B=-\Delta''>0,
\qquad D=-\Delta'''>0.
\]

Since \(d\Delta'/dx=\Delta''/(2x)\),

\[
Q_2'=24(\Delta')^3\frac{d\Delta'}{dx}>0.
\]

For the linear coefficient,

\[
Q_1'=
\frac{2A}{x}
\left(DA+2B^2-6A^2B\right).
\]

The established bounds \(3x<A<4x\), \(4x<B<6x\), \(D<20x\) show

\[
6A^2B>216x^3,
\qquad
DA+2B^2<152x^2,
\]

so \(Q_1'<0\) for \(x\ge6\).

Because \(0<p<1/200\), the derivative lower bound sharpens to

\[
Q_0'+pQ_1'+p^2Q_2'
\ge
Q_0'+\frac1{200}Q_1'.
\]

The remaining monotonicity gate is now one parameter-free rational inequality.

## Exact rational certification

Clearing the positive denominators in

\[
Q_0'(x)+\frac1{200}Q_1'(x)
\]

and translating \(x=y+6\) produces a degree-103 numerator polynomial in \(y\). Exact rational expansion finds every coefficient strictly positive; the smallest coefficient is

\[
4979965382996599203779798542319616.
\]

The denominator also has nonnegative shifted coefficients and is strictly positive on \(y\ge0\). Therefore

\[
Q_0'+\frac1{200}Q_1'>0
\qquad(x\ge6).
\]

Combined with the coefficient-sign and \(p'\)-term results, this proves

\[
Q'(x)>0
\qquad(x\ge6).
\]

Since the exact endpoint estimate gives \(Q(6)>0\), the two-component residual is positive on the full range.

Checker: `research/grothendieck/checkers/theta_q_rational_positivity.py`.
Result: `research/grothendieck/results/theta_q_rational_positivity.json`.
Execution: `structured_command_execution:e_19044_1788236772804621000_15`.

The deliberate-failure test replaces \(p<1/200\) by the unsafe bound \(p\le1\); its endpoint lower bound is

\[
-\frac{133424640}{343}<0,
\]

so the checker detects the predicted loss of domination.

## Claim boundary

The exact rational checker certifies the two-component residual only. It does not control the omitted components \(n\ge3\). It does not certify positivity between grid points or validate the endpoint decimal as an exact bound. It identifies no interior dip and indicates that monotonicity from the endpoint is the cheapest analytic target.

## Disposition

The bounded interval produced no numerical counterexample and a large observed margin. The next test is an exact sign proof for \(Q'\), using rational bounds and \(p' = p(1-p)\Delta'\); until then, the two-component local margin remains unproved.
