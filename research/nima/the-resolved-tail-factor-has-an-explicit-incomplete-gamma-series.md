# The resolved tail factor has an explicit incomplete-gamma series

## Exact tail evaluation

For \(u\ge0\), the completed theta kernel is

\[
\Phi(u)=\sum_{n\ge1}e^{u/2}e^{-x_n(u)}
\bigl(4x_n(u)^2-6x_n(u)\bigr),
\qquad
x_n(u)=\pi n^2e^{2u}.
\]

Define

\[
K(u)=\int_u^\infty\Phi(s)\,ds.
\]

For one label, substitute \(x=\pi n^2e^{2s}\).  Then

\[
e^{s/2}=\left(\frac{x}{\pi n^2}\right)^{1/4},
\qquad
ds=\frac{dx}{2x},
\]

and therefore

\[
\int_u^\infty e^{s/2}e^{-x_n(s)}
 (4x_n(s)^2-6x_n(s))\,ds
=(\pi n^2)^{-1/4}
\int_{x_n(u)}^\infty(2x^{5/4}-3x^{1/4})e^{-x}\,dx.
\]

Writing

\[
\Gamma(\alpha,x)=\int_x^\infty t^{\alpha-1}e^{-t}\,dt,
\]

gives the explicit source identity

\[
\boxed{
K(u)=\sum_{n\ge1}(\pi n^2)^{-1/4}
\left[
2\Gamma\!\left(\frac94,\pi n^2e^{2u}\right)
-3\Gamma\!\left(\frac54,\pi n^2e^{2u}\right)
\right].
}
\]

The interchange of sum and tail integration is justified directly by the
positive summands: on the integration range, \(x\ge\pi>3/2\), so
\((2x^{5/4}-3x^{1/4})e^{-x}>0\).  Rapid Gaussian decay then gives finite
mass.

## Fully explicit mixed resolved entry

Set

\[
K_+(u)=\mathbf1_{[0,\infty)}(u)K(u),
\qquad
\rho(q)=e^{-\pi q^2},
\qquad
F=K_+*\rho.
\]

For \(L=\log p\), the mixed resolved-window scalar is now the source-only
quadrature

\[
\boxed{
g_p=2\int_{\mathbb R}F(q)
\bigl(F(q+L)-F(q+3L)\bigr)\,dq,
}
\]

with \(K\) given by the boxed incomplete-gamma series above.  Equivalently,

\[
g_p=2\bigl(A_F(L)-A_F(3L)\bigr)>0.
\]

Thus neither \(b_\Phi\), \(\Xi_\Phi\), nor an unspecified spectral factor
remains in this entry.  What remains absent is a collapse of this explicit
series/quadrature to a simpler arithmetic coefficient-side constant.

## Scope

This is an exact analytic evaluation formula, not a typed comparison with the
endpoint Stieltjes form and not the arithmetic calibration of the oriented
Stokes block.  It closes the request for an explicit source identity for the
resolved spectral factor, while leaving the constructor transport, radical
descent, and global closed-range gates open.  No RH conclusion is authorized.
