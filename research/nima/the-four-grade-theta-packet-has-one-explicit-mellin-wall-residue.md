# The four-grade theta packet has one explicit Mellin-wall residue

## Moment asymptotic

For \(r>-1\), set

\[
\Theta_r(u)
=
e^{ru}
\sum_{n\ge1}
n^r e^{-\pi n^2e^{2u}}.
\]

As \(u\to-\infty\), the integral term in the Euler--Maclaurin expansion gives

\[
\sum_{n\ge1}
n^r e^{-\pi n^2e^{2u}}
=
\frac12
\pi^{-(r+1)/2}
\Gamma\!\left(\frac{r+1}{2}\right)
e^{-(r+1)u}
+
O(1).
\]

Hence

\[
\Theta_r(u)
=
C_r e^{-u}+o(e^{-u}),
\]

where

\[
C_r
=
\frac12
\pi^{-(r+1)/2}
\Gamma\!\left(\frac{r+1}{2}\right).
\]

The important point is that every half-density grade has the same leading
wall character \(e^{-u}\).

## Four-grade wall coefficient

For \(L=\log p\), the synthesized pretranslation packet is

\[
\Psi_p(u)
=
\sum_{j=0}^{3}
c_{j,p}\Theta_{j+1/2}(u),
\]

with

\[
(c_{0,p},c_{1,p},c_{2,p},c_{3,p})
=
(-2\pi L^2,\,8\pi L,\,4\pi^2L^2,\,-8\pi^2L).
\]

Using

\[
\Gamma\!\left(\frac74\right)
=
\frac34\Gamma\!\left(\frac34\right),
\qquad
\Gamma\!\left(\frac54\right)
=
\frac14\Gamma\!\left(\frac14\right),
\]

and

\[
\Gamma\!\left(\frac94\right)
=
\frac5{16}\Gamma\!\left(\frac14\right),
\]

the even grades contribute

\[
\frac12
L^2\pi^{1/4}
\Gamma\!\left(\frac34\right)e^{-u},
\]

while the odd grades contribute

\[
-\frac14
L\pi^{-1/4}
\Gamma\!\left(\frac14\right)e^{-u}.
\]

Therefore

\[
\Psi_p(u)
=
\rho_p e^{-u}+o(e^{-u}),
\]

with the exact wall coefficient

\[
\rho_p
=
\frac12
L^2\pi^{1/4}\Gamma\!\left(\frac34\right)
-
\frac14
L\pi^{-1/4}\Gamma\!\left(\frac14\right).
\]

Equivalently,

\[
\rho_p
=
\frac{L\pi^{-1/4}}4
\left(
2\sqrt\pi\,L\Gamma\!\left(\frac34\right)
-
\Gamma\!\left(\frac14\right)
\right).
\]

## Consequence

Compact-local smoothness does not extend to the raw Mellin wall. The four
grades coalesce there into one coefficient direction, but their coefficient
sum is generally nonzero.

Thus the completed comparison must first route

\[
\rho_p e^{-u}
\]

through the independently typed wall carrier. It is not authorized to discard
this term as a failure of convergence, nor to subtract it after analytic
representation without proving that it is the image of the coefficient wall.

After this one-dimensional leading wall is removed in coefficient space, the
remaining packet is lower order than \(e^{-u}\). Establishing membership of
that remainder in the relative Green space is the next analytic gate.

## Even--odd interaction at the wall

The wall coefficient is not supplied by the even packet alone. It is the
signed sum of:

- a quadratic even contribution in \(L\);
- a linear reciprocal-odd contribution in \(L\).

Consequently, projection to reciprocal-even data before label synthesis gives
the wrong wall normalization. The ordered odd channel changes the coefficient
of the same leading wall character rather than producing a separate
asymptotic exponent.

## First-prime test

For \(p=2\), \(L=\log2\), so the exact first-prime residue is

\[
\rho_2
=
\frac12
(\log2)^2\pi^{1/4}\Gamma\!\left(\frac34\right)
-
\frac14
(\log2)\pi^{-1/4}\Gamma\!\left(\frac14\right).
\]

This is the scalar that the coefficient-wall incidence must reproduce before
the relative Green comparison with

\[
d_2=W_{2\log2}-W_{\log2}
\]

can be attempted.

## Hostile

Removing the four grades separately after synthesis can erase the common
\(e^{-u}\) direction with four unrelated counterterms. That reproduces a
finite remainder but destroys the source fact that all four moments coalesce
into one wall coordinate with the single coefficient \(\rho_p\).
