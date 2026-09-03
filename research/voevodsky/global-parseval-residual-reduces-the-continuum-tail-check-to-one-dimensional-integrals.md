# Global Parseval residual reduces the continuum tail check to one-dimensional integrals

## Question

Can the residual correction be bounded without constructing the continuum complementary projector or a two-variable kernel for the squared operator?

## Claim boundary

Yes conditionally on a positive numerical margin for the stronger global-norm test. Every required quantity then reduces to finite coefficient algebra, one-dimensional frequency integrals, and explicit endpoint moments. No numerical positivity for this stronger test has yet been obtained because the SciPy scout command is not admitted by the current structured-command policy.

## Polynomial Fourier coordinates

Let \(L=0.35\), and let

\[
p_n(x)=\sqrt{\frac{2n+1}{2L}}P_n(x/L)
\]

on \([-L,L]\), extended by zero. With the Fourier convention

\[
\widehat f(u)=\int_{\mathbb R}f(x)e^{-iux}\,dx,
\]

one has

\[
\widehat p_n(u)
=
2L\sqrt{\frac{2n+1}{2L}}(-i)^n j_n(Lu),
\]

where \(j_n\) is the spherical Bessel function. Thus every Fourier transform needed for a degree-159 trial map is an explicit finite linear combination of these functions.

## Multiplier norm

Let \(s(u)\) be the cutoff-250 multiplier and let \(M\) be its zero-extension Fourier multiplier. Parseval gives

\[
\|Mf\|_{L^2(\mathbb R)}^2
=
\frac1{2\pi}\int_{-250}^{250}
|s(u)|^2|\widehat f(u)|^2\,du.
\]

For a matrix-valued polynomial map \(Z:\mathbb R^{25}\to L^2[-L,L]\), its multiplier Gram matrix is therefore

\[
G_M=
\frac1{2\pi}\int_{-250}^{250}
|s(u)|^2\widehat Z(u)^*\widehat Z(u)\,du.
\]

This is a \(25\times25\) matrix of one-dimensional integrals. The established geometric panels and Gauss remainder method apply entrywise after replacing the integrand by the corresponding product.

## Endpoint term

Write

\[
Ef=e^{x/2}\langle e^{-x/2},f\rangle
+e^{-x/2}\langle e^{x/2},f\rangle.
\]

Its Legendre moments are explicit because

\[
\int_{-L}^{L}p_n(x)e^{ax}\,dx
=
2L\sqrt{\frac{2n+1}{2L}}i_n(aL),
\]

with the parity relation \(i_n(-z)=(-1)^n i_n(z)\). Hence the endpoint Gram matrix

\[
G_E=(EZ)^*(EZ)
\]

requires only finite ball arithmetic once the polynomial coefficients are frozen.

## Projector-free residual bound

The true residual is \(QAZ\), so

\[
\|QAZv\|\leq\|AZv\|_{L^2[-L,L]}
\leq\|MZv+EZv\|_{L^2(\mathbb R)}.
\]

For every \(\eta>0\),

\[
\|MZv+EZv\|^2
\leq
(1+\eta)\|MZv\|^2
+(1+\eta^{-1})\|EZv\|^2.
\]

Therefore

\[
G_R\leq(1+\eta)G_M+(1+\eta^{-1})G_E.
\]

A sufficient finite certificate is positivity of

\[
J-40\bigl((1+\eta)G_M+(1+\eta^{-1})G_E\bigr).
\]

The split inequality is not necessary. The exact global Gram matrix is

\[
G_{\rm global}=G_M+G_E+G_{ME}+G_{ME}^*,
\]

where Parseval reduces the cross term to the one-dimensional integral

\[
G_{ME}=\frac1{2\pi}\int_{-250}^{250}
 s(u)\widehat Z(u)^*\widehat{EZ}(u)\,du.
\]

Consequently, positivity of \(J-40G_{\rm global}\) is a tighter projector-free certificate with the same one-dimensional integration structure. The split tests remain useful only as independently checkable upper bounds.

## Falsifier

If every tested \(\eta\) makes this stronger matrix indefinite, the global norm loses too much directional information. The branch must then return to the exact projected residual Gram matrix rather than weakening the inequality or claiming that a small grid residual supplies a continuum bound.

## Disposition

The numerical falsifier rejects this projector-free route. For the cutoff-\(1/40\) candidate, the exact-global lower form is about \(-427.43\), the split upper-bound route is below \(-1447\), and even the interval-output full-residual form is about \(-387.92\). The projected residual is essential; replacing it by a global or unprojected norm loses too much directional information. These formulas remain a valid rejected rival but are removed from the certificate frontier. No continuum certificate or RH implication is asserted.
