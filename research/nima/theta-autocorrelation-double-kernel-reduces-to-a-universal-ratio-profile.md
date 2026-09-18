# Finite-cutoff theta autocorrelation kernel reduces to a universal ratio profile

For

$$
r=\frac{me^t}{n},
$$

every term of the completed-theta autocorrelation double sum has the common scale factor `e^(t/2)/n`. Using

$$
\Gamma(9/2)=\frac{105}{16}\sqrt\pi,
\quad
\Gamma(7/2)=\frac{15}{8}\sqrt\pi,
\quad
\Gamma(5/2)=\frac34\sqrt\pi,
$$

the three terms simplify and combine to

$$
A_\Phi(t)
=\frac{3e^{t/2}}2
\sum_{n,m\ge1}\frac1n
\frac{r^2\left(-6+23r^2-6r^4\right)}
     {(1+r^2)^{9/2}},
\qquad r=\frac{me^t}{n}.
$$

Thus the source interaction is governed by the universal ratio profile

$$
\kappa(r)
=\frac{3}{2}
\frac{r^2(-6+23r^2-6r^4)}{(1+r^2)^{9/2}}.
$$

Its numerator factors through the roots of

$$
6x^2-23x+6=0,
\qquad x=r^2,
$$

namely

$$
x_\pm=\frac{23\pm\sqrt{385}}{12},
\qquad x_+x_-=1.
$$

Therefore `kappa(r)` is positive only in the reciprocal interval

$$
\sqrt{x_-}<r<\sqrt{x_+}
$$

and negative outside it. It also obeys the reciprocal scaling relation induced by `r -> 1/r`, matching exchange of the two theta labels together with `t -> -t`.

This sign-changing ratio kernel explains why the forcing reservoir cannot be assembled from isolated positive prime channels. The arithmetic current decomposition must retain ordered-pair ratio information and reciprocal orientation until after polarization.

The formula is finite-cutoff only. Along common scaling rays its unrestricted sum has a harmonic divergence, so completion requires Poisson or anomaly-line renormalization.

Status: finite-cutoff autocorrelation reduced to an explicit ratio kernel; completion-compatible renormalization remains open.
