# Quarter Barnes curvature reduces to a rational argument product

## Question

How can a global Barnes asymptotic produce the rational amplitude \(104/1575\)?

Suppose the parameter-dependent constant in the staircase asymptotic has the form

\[
K(t)=A+Bt+\sum_r \varepsilon_r\log G(t+a_r),
\]

where \(G\) is the Barnes function and the signed multiplicities \(\varepsilon_r\) are integers. The affine terms cancel from the second common-shift difference. The functional equation

\[
G(z+1)=\Gamma(z)G(z)
\]

gives

\[
2\log G(a+1)-\log G(a)-\log G(a+2)
=-\log a.
\]

Therefore

\[
\exp\bigl(2K(1)-K(0)-K(2)\bigr)
=\prod_r a_r^{-\varepsilon_r}.
\]

This explains how Barnes constants can cancel while leaving a rational amplitude. The target \(C=104/1575\) is equivalent to the signed argument-product constraint

\[
\prod_r a_r^{\varepsilon_r}
=\frac{1575}{104}
=\frac{3^2 5^2 7}{2^3 13}.
\]

## Disposition

Resolve the global cancellation mechanism. The next leaf is `quarter-barnes-multiplicity-extraction`: derive the arguments \(a_r\) and multiplicities \(\varepsilon_r\) from a parameter-uniform determinant asymptotic and test their signed product.

## Claim boundary

No Barnes representation for the staircase determinant has yet been derived. The argument-product constraint is necessary and sufficient only within the displayed Barnes ansatz; it is not a proof of the amplitude.
