# The gamma multiplier is strictly increasing on positive frequency

Let

\[
q(u)=\frac12\left(\Re\psi\left(\frac14+\frac{iu}{2}\right)-\log\pi\right).
\]

The absolutely convergent trigamma series gives, for `a>0`, `b>0`,

\[
\psi'(a+ib)=\sum_{n\ge0}\frac1{(n+a+ib)^2},
\]

and hence

\[
\Im\psi'(a+ib)
=-2b\sum_{n\ge0}
\frac{n+a}{((n+a)^2+b^2)^2}<0.
\]

Differentiating with `a=1/4`, `b=u/2` yields

\[
q'(u)=-\frac14\Im\psi'\left(\frac14+\frac{iu}{2}\right)>0
\qquad(u>0).
\]

Therefore

\[
q(u)\ge q(R)\quad (u\ge R),
\]

and Plancherel gives the operator inequality

\[
\Gamma_{[R,\infty)}\ge q(R)(I-K_R).
\]

This proves the monotonicity premise used by the rank-670 gamma-floor
reduction without numerical subdivision.
