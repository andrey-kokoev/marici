# Factorial Legendre tail bound for the projected residual

## Question

Can the numerically tiny Legendre tail of the projected residual be bounded analytically without enclosing an \(A^2\) kernel?

## Claim boundary

Yes. Directed Arb subdivision proves \(\|s\|_{L^\infty[-250,250]}<5.386<10\), the exact-decimal-span Arb checker proves \(\|Z\|\leq11.0301<11.2\), and direct Arb evaluation bounds the 25-column endpoint tail after degree 159 by \(1.091\times10^{-452}\). For degrees at least 160, the projection \(Q\) does not alter coefficients because the selected space lies in degrees 0 through 79. A spherical-Bessel majorant then gives a matrix tail bound of order \(4.4\times10^{-13}\), matching the observed tail. The two premise bounds remain to be attached by directed intervals.

## Projection disappears in high degree

Let \(P\) project onto the selected space, contained in

\[
H_{80}=\operatorname{span}\{p_0,\ldots,p_{79}\},
\]

and set \(Q=I-P\). For every \(n\geq80\),

\[
\langle p_n,QAZ\rangle=\langle p_n,AZ\rangle.
\]

Thus the residual tail from degree 160 onward is bounded directly from \(AZ\); no continuum representation of \(Q\) is needed there.

## Spherical-Bessel majorant

For \(x\geq0\), the absolute spherical-Bessel series gives

\[
|j_n(x)|
\leq
\frac{x^n}{(2n+1)!!}
\exp\!\left(\frac{x^2}{2(2n+3)}\right).
\]

Indeed, after extracting \(x^n/(2n+1)!!\), the \(k\)-th absolute term is bounded by

\[
\frac1{k!}
\left(\frac{x^2}{2(2n+3)}\right)^k.
\]

Here \(|u|\leq250\) and \(L=0.35\), so \(x=L|u|\leq87.5\). At \(n=160\), the bound is

\[
|j_{160}(x)|\leq7.494\times10^{-19}.
\]

Successive majorants have ratio below

\[
q=\frac{87.5}{323}<0.271.
\]

## Multiplier coefficient bound

For normalized Legendre functions,

\[
|\widehat p_n(u)|
\leq
2L\sqrt{\frac{2n+1}{2L}}\,|j_n(Lu)|.
\]

Also

\[
|\widehat{Zv}(u)|
\leq\sqrt{2L}\,\|Zv\|
\leq\sqrt{0.7}\,(11.2)\|v\|.
\]

Using interval length 500 and \(\|s\|_\infty\leq10\),

\[
|\langle p_{160},MZv\rangle|
\leq
\frac{500}{2\pi}(10)
\sup|\widehat p_{160}|
\sup|\widehat{Zv}|
\leq8.376\times10^{-14}\|v\|.
\]

Geometric summation gives, for 25 columns,

\[
\left\|
(\langle p_n,MZ e_j\rangle)_{n\geq160,\,1\leq j\leq25}
\right\|_{\mathrm F}
\leq
\frac{5(8.376\times10^{-14})}{\sqrt{1-q^2}}
<4.36\times10^{-13}.
\]

The endpoint rank-two term has the same factorial structure with modified spherical-Bessel argument \(L/2=0.175\), so its degree-160 tail is negligible relative to this bound; its explicit moments permit a separate Arb evaluation.

## Effect on the residual Gram matrix

Write the residual as \(R=R_{<160}+E\), with \(\|E\|\leq\varepsilon\). Then

\[
R^*R
\leq
R_{<160}^*R_{<160}
+\eta R_{<160}^*R_{<160}
+(1+\eta^{-1})\varepsilon^2 I
\]

for every \(\eta>0\). Since \(\|R\|\approx0.008879\) and \(\varepsilon<4.4\times10^{-13}\), the tail correction is negligible at the current \(0.0178\) positivity margin once the premises are interval-enclosed.

## Falsification

All three scalar falsifiers are eliminated: the multiplier supremum is below \(5.386\), the \(Z\)-norm is below \(11.0301\), and the endpoint tail is below \(1.091\times10^{-452}\). The remaining failure mode is inability to interval-enclose the first 160 projected-residual coefficients tightly enough to preserve the lower-form margin. Numerical tail decay alone is not substituted for any of these premises.

## Disposition

The projected residual tail has a source-derived factorial majorant reducing its continuum norm to the first 160 Legendre coefficients plus an explicit tail scalar. The multiplier supremum, \(Z\)-norm, and endpoint moments are now interval-certified; only the first 160 residual coefficients remain. No continuum positivity or RH implication is asserted.
