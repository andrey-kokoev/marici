# The differentiated eta Euler tail is exponentially controlled

For `s>0`, let

\[
 d_k(s)=\Delta^k(n^{-s})|_{n=1}
 =\frac1{\Gamma(s)}\int_0^\infty
 t^{s-1}e^{-t}(1-e^{-t})^k\,dt.
\]

Differentiating introduces `log(t)-psi(s)`. On the central scan interval
`1/2<=s<=3/5`, use `1/Gamma(s)<=1` and `|psi(s)|<2`. Split the logarithmic
integral at `t=1`.

For `0<t<=1`, `1-e^-t<=t`, giving

\[
 \int_0^1t^{k+s-1}|\log t|\,dt=\frac1{(k+s)^2}.
\]

For `t>=1`, put `u=e^-t`. The function
`t^(s-1) log(t)` is at most `1/(e(1-s))<=1`, while

\[
 \int_0^{e^{-1}}(1-u)^k\,du\le\frac1{k+1}.
\]

Also `d_k(s)<=1/(k+s)`. Hence, for `k>=1`,

\[
 |d_k'(s)|\le\frac2{k+s}+\frac1{(k+s)^2}+\frac1{k+1}
 \le\frac3k+\frac1{k^2}.
\]

The differentiated Euler tail after depth `N` therefore satisfies

\[
 \left|\sum_{k=N}^\infty\frac{d_k'(s)}{2^{k+1}}\right|
 \le 2^{-N}\left(\frac3N+\frac1{N^2}\right).
\]

At `N=120` this is about `1.89e-38`. Even multiplying by the previous worst
boundary-stencil amplification and an additional factor ten for quotient
propagation leaves about `2.83e-22`, far below the revised `3.4e-20` chord
gap.

This closes the eta-prime truncation item in the finite central certification
budget. The remaining analytic item is correlated derivative propagation of
the digamma asymptotic remainder. This result does not certify the entire
chord computation or prove RH.

## Durable verification

- Checker: `checkers/eta_derivative_euler_tail_bound.py`
- Result: `results/eta-derivative-euler-tail-bound.json`
