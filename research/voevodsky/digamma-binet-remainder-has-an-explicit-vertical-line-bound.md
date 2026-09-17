# The digamma Binet remainder has an explicit vertical-line bound

For `z=a+ib` with `a,b>0`, Binet's formula is

\[
\psi(z)=\log z-\frac1{2z}
-2\int_0^\infty
\frac{t}{(t^2+z^2)(e^{2\pi t}-1)}dt.
\]

Expand

\[
\frac1{t^2+z^2}
=\sum_{m=0}^{N-1}\frac{(-1)^m t^{2m}}{z^{2m+2}}
+rac{(-1)^Nt^{2N}}{z^{2N}(t^2+z^2)}.
\]

The denominator obeys

\[
|t^2+z^2|^2=(t^2+a^2-b^2)^2+4a^2b^2,
\qquad |t^2+z^2|\ge2ab.
\]

Therefore the complex remainder after `N` Binet integral terms satisfies

\[
\boxed{
|\mathcal R_N(z)|
\le
\frac{1}{ab|z|^{2N}}
\frac{\Gamma(2N+2)\zeta(2N+2)}{(2\pi)^{2N+2}}.}
\]

The same bound applies to its real part. On the required line

\[
z=\frac14+\frac{iu}{2},
\]

this becomes

\[
|\Re\mathcal R_N(u)|
\le
\frac8{u|z|^{2N}}
\frac{(2N+1)!\zeta(2N+2)}{(2\pi)^{2N+2}}.
\]

It decreases monotonically with `u` once the tail starts. Multiplication by
`u^{-k}` and integration gives a scalar remainder bound for every plain
moment. The oscillatory moments may use the same absolute bound or one further
integration-by-parts step.

Together with the exact rational coefficients through `u^-20`, choosing
`N=10` closes the analytic remainder required by the 476-moment tail
constructor.
