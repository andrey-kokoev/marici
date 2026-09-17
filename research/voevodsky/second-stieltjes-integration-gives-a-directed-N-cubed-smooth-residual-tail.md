# Second Stieltjes integration gives an `N^-3` smooth residual-Gram tail

After subtracting all interior value jumps, let `h:[-1,1]->C^m` be continuous
and piecewise `C^1`, with `dh'` a finite vector measure. Write

\[
A_n=\frac{\sqrt{L(2n+1)/2}}{2n+1},
\qquad Q_n=P_{n+1}-P_{n-1}.
\]

The first integration by parts gives

\[
r_n=-A_n\int_{-1}^1Q_n(t)h'(t)dt.
\]

Define

\[
R_n(t)=
\frac{P_{n+2}(t)-P_n(t)}{2n+3}
-
\frac{P_n(t)-P_{n-2}(t)}{2n-1}.
\]

Then `R_n'=Q_n` and `R_n(+/-1)=0`. A second Stieltjes integration yields the
exact identity

\[
r_n=A_n\int_{(-1,1)}R_n(t)\,dh'(t).
\]

Using the Bernstein bounds on the four Legendre terms gives, for `n>=3`,

\[
|R_n(t)|
\le\frac{4\sqrt{2/\pi}}{n^{3/2}}
(1-t^2)^{-1/4},
\]

and hence

\[
\|r_n\|
\le\frac{4\sqrt{L/\pi}}{n^2}
\mathcal V^{(2)}_{1/4}(h).
\]

The second variation includes both the absolutely continuous second derivative
and first-derivative jump rows.

For the matrix-oriented version, dominate `dh'=v dnu` and define

\[
G^{(2)}_{1/4}=
\left(\int w\,d\nu\right)
\int w(t)v(t)^*v(t)d\nu(t),
\qquad w(t)=(1-t^2)^{-1/4}.
\]

Then

\[
(r_n^{smooth})^*r_n^{smooth}
\preceq\frac{16L}{\pi n^4}G^{(2)}_{1/4}.
\]

Since

\[
\sum_{n=N}^\infty n^{-4}\le\frac1{3(N-1)^3},
\]

we obtain the directed tail bound

\[
\sum_{n=N}^\infty(r_n^{smooth})^*r_n^{smooth}
\preceq
\frac{16L}{3\pi(N-1)^3}G^{(2)}_{1/4}.
\]

This supplies the missing analytic power of `N`. The remaining computation is
finite: assemble `G^(2)` from polynomial second derivatives, first-derivative
jumps at the four translation boundaries, and two derivatives of the smooth
band-multiplier output.
