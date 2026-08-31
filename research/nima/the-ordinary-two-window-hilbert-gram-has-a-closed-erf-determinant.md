# The ordinary two-window Hilbert Gram has a closed erf determinant

## Window as a smoothed interval

With

\[
\rho(q)=e^{-\pi q^2},
\qquad
W_t=-(\mathbf1_{[-t,t]}*\rho),
\]

the Gaussian autocorrelation is

\[
\gamma(z)=(\rho*\widetilde\rho)(z)
=2^{-1/2}e^{-\pi z^2/2}.
\]

Therefore

\[
\langle W_a,W_b\rangle
=\int_{-a}^a\int_{-b}^b\gamma(x-y)\,dx\,dy.
\]

## Closed primitive

Put

\[
\alpha=\sqrt{\frac\pi2},
\]

and define the even function

\[
R(x)
=\frac{x}{2}\operatorname{erf}(\alpha x)
+\frac{e^{-\pi x^2/2}}{\pi\sqrt2}.
\]

A direct differentiation gives

\[
R''(x)=\gamma(x).
\]

Integrating \(R''(x-y)\) over the two centered intervals yields

\[
\boxed{
\langle W_a,W_b\rangle
=2\left(R(a+b)-R(|a-b|)\right).
}
\]

This is an ordinary Lebesgue-Hilbert identity.  It does not use the endpoint
Stieltjes metric.

## Adjacent-window Gram

For \(a=L\), \(b=2L\), set

\[
A(L)=2\bigl(R(2L)-R(0)\bigr),
\]

\[
D(L)=2\bigl(R(4L)-R(0)\bigr),
\]

\[
C(L)=2\bigl(R(3L)-R(L)\bigr).
\]

Then

\[
G_L^{(0)}
=
\begin{pmatrix}A(L)&C(L)\\C(L)&D(L)\end{pmatrix}
\]

and

\[
\boxed{
D_0(L)
=4\left[
\bigl(R(2L)-R(0)\bigr)
\bigl(R(4L)-R(0)\bigr)
-igl(R(3L)-R(L)\bigr)^2
\right].
}
\]

Strict positivity follows independently from linear independence of the two
window transforms.

## Asymptotics with the constant exposed

Since

\[
R(x)=\frac{|x|}{2}+O(e^{-\pi x^2/2})
\qquad(|x|\to\infty),
\]

while

\[
R(0)=\frac1{\pi\sqrt2},
\]

the entries satisfy

\[
A(L)=2L-\frac{\sqrt2}{\pi}+O(e^{-2\pi L^2}),
\]

\[
D(L)=4L-\frac{\sqrt2}{\pi}+O(e^{-8\pi L^2}),
\]

\[
C(L)=2L+O(e^{-\pi L^2/2}).
\]

Consequently

\[
D_0(L)
=4L^2-\frac{6\sqrt2}{\pi}L+\frac{2}{\pi^2}
+O\bigl(Le^{-\pi L^2/2}\bigr).
\]

The leading \(4L^2\) term used in the asymptotic oriented-margin argument is
therefore exact.

## Consequence for the remaining finite gate

The conservative oriented positivity test can now be written without any
numerical quadrature:

\[
4\left[
(R(2L)-R(0))(R(4L)-R(0))
-(R(3L)-R(L))^2
\right]
>\frac{\kappa_p^2}{4}.
\]

An interval-certified checker needs only rigorous bounds for `erf`, the
exponential, and the rapidly convergent theta-derivative series defining
\(\kappa_p\).  The resolved determinant is larger by positive-Gram domination.

Typed assembly, source-topology closed range, and radical descent remain
separate gates.  No RH conclusion is authorized.
