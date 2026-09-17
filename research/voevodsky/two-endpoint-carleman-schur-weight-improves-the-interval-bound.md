# A two-endpoint Schur weight improves the interval Carleman bound

Scale the interval to `(0,1)` and let

\[
K(x,y)=\frac1{x+y}+\frac1{2-x-y}.
\]

Choose the positive Schur weight

\[
w(y)=\frac1{\sqrt{y(1-y)}}.
\]

The beta-integral identities give

\[
\int_0^1\frac{w(y)}{x+y}dy
=\frac\pi{\sqrt{x(x+1)}},
\]

\[
\int_0^1\frac{w(y)}{2-x-y}dy
=\frac\pi{\sqrt{(1-x)(2-x)}}.
\]

After division by `w(x)`, the Schur row ratio is

\[
\pi\left[
\sqrt{\frac{1-x}{1+x}}+
\sqrt{\frac{x}{2-x}}
\right].
\]

The bracket is symmetric about `x=1/2`, increases on `(0,1/2)`, and has
maximum `2/sqrt(3)`. Therefore

\[
\boxed{\|K\|\le\frac{2\pi}{\sqrt3}.}
\]

The unitary Weil form carries logarithmic coefficient `1/2`, so its direct
two-endpoint boundary budget is

\[
\boxed{C_\partial\le\frac\pi{\sqrt3}\approx1.81380.}
\]

This is rigorous and improves the separate-endpoint triangle bound `pi`
without introducing an IMS partition. It also agrees with the Nyström scout,
whose unscaled two-endpoint norm is about `3.27`, below `2pi/sqrt(3)`.
