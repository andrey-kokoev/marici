# Logarithmic uncertainty controls the shrinking prime-power edge channel

Let a new prime-power shift `a=log n` enter at `L=a/2`, and put
`delta=2L-a`. The new overlap is supported on an interval of length `delta`.
After the rescaling

\[
f(x)=\delta^{-1/2}g((x-x_0)/\delta),
\]

its Fourier transform satisfies

\[
\widehat f(u)=\delta^{1/2}e^{-iux_0}\widehat g(\delta u).
\]

For the archimedean multiplier `q(u)=log|u|+O(1)` this gives

\[
Q_\infty(f,f)
\ge (\log(1/\delta)-C_{\log})\|f\|_2^2,
\]

where `C_log` is the compact-support logarithmic uncertainty constant

\[
C_{\log}=-\inf_{\operatorname{supp}g\subset[0,1],\|g\|=1}
 \int \log(2+|v|)|\widehat g(v)|^2dv + C_q.
\]

The constant is finite by the compact-support logarithmic uncertainty
inequality.

The entering arithmetic channel has coefficient

\[
c_n=\Lambda(n)/\sqrt n
\]

and its two-sided quadratic contribution is bounded below by
`-c_n ||f||^2`. Consequently the edge channel is positive whenever

\[
\log(1/\delta)>C_{\log}+c_n,
\qquad
\delta<\exp(-C_{\log}-c_n).
\]

Uniformly,

\[
c_n\le \frac{\log n}{\sqrt n}\le\frac2e,
\]

because `log x/sqrt(x)` is maximized at `x=e^2`. Hence the single collar

\[
\delta<\exp(-C_{\log}-2/e)
\]

works at every prime-power threshold. Moreover `c_n` tends to zero along the
prime powers, so the asymptotic collars improve.
The non-norm-continuous translation is therefore not itself a fatal global
obstruction: its norm-one vectors pay divergent archimedean energy as the
edge shrinks.

What remains for a uniform threshold theorem is an explicit directed value of
`C_log` and a decomposition showing that edge--bulk cross terms are absorbed
by half of this logarithmic margin. Away from the collars, ordinary
finite-support continuation applies.
