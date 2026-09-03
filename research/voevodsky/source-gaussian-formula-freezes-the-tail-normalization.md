# The source Gaussian formula freezes the tail normalization

## Question

What exact gamma scale and prime absolute constant enter the explicit time--band tail dimension?

## Claim boundary

Under the Fourier convention already used by the source Gaussian formula, the complete gamma multiplier is

\[
\frac{1}{4\pi}
\left[
\operatorname{Re}\psi\left(\frac14+\frac{iu}{2}\right)-\log\pi
\right],
\]

and the fixed-support prime absolute constant is

\[
C_{\rm prime}(L)
=
\sum_{\log n\leq2L}
\frac{\Lambda(n)}{\sqrt n}.
\]

This freezes the constants needed by the tail estimate. It does not evaluate the finite sum for a selected \(L\) or provide rigorous numerical digamma enclosures.

## Fourier convention

Use

\[
\check h(x)
=
\frac1{2\pi}
\int_{\mathbb R}h(u)e^{iux}\,du.
\]

For \(h_t(u)=e^{-tu^2}\),

\[
\check h_t(x)
=
\frac{1}{2\sqrt{\pi t}}
 e^{-x^2/(4t)}.
\]

## Gamma normalization

The source Gaussian formula contains

\[
-\frac{\log\pi}{4\sqrt{\pi t}}
+
\frac1{4\pi}
\int_{\mathbb R}
 e^{-tu^2}
\operatorname{Re}\psi\left(\frac14+\frac{iu}{2}\right)du.
\]

Since

\[
\int_{\mathbb R}e^{-tu^2}du
=
\sqrt{\frac\pi t},
\]

the constant term equals

\[
\frac1{4\pi}
\int_{\mathbb R}
 e^{-tu^2}(-\log\pi)du.
\]

Thus the complete multiplier is exactly

\[
m_\Gamma(u)
=
\frac{d(u)}{4\pi},
\]

where

\[
d(u)
=
\operatorname{Re}\psi\left(\frac14+\frac{iu}{2}\right)-\log\pi.
\]

Therefore

\[
C_{\rm low}^{\Gamma}
=
\frac{\gamma+\pi/2+3\log2+\log\pi}{4\pi},
\]

and

\[
m_R^{\Gamma}
=
\frac{1}{4\pi}
\left[
\operatorname{Re}\psi\left(\frac14+\frac{iR}{2}\right)-\log\pi
\right].
\]

## Prime normalization

For an autocorrelation \(g=f*f^*\), the centered half-divisor convention gives

\[
P_L(f,f)
=
-\sum_{\log n\leq2L}
\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}g(\log n).
\]

Cauchy--Schwarz gives

\[
|g(a)|
\leq
\lVert f\rVert_2^2.
\]

Hence

\[
|P_L(f,f)|
\leq
C_{\rm prime}(L)\lVert f\rVert_2^2
\]

with the stated finite sum.

For the Gaussian, substitution of \(\check h_t(\log n)\) reproduces

\[
-\frac1{2\sqrt{\pi t}}
\sum_{n\geq2}
\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/(4t)},
\]

matching the source formula.

## Explicit dimension formula

The sufficient condition is now

\[
M+1
>
\frac{2LR}{\pi}
\frac{m_R^\Gamma+C_{\rm low}^\Gamma}
{m_R^\Gamma-C_{\rm prime}(L)},
\]

provided

\[
m_R^\Gamma>C_{\rm prime}(L).
\]

## Disposition

The normalization blocker is removed. The next executable object is a chosen support value \(L\), exact enumeration of prime powers through \(e^{2L}\), and a rigorous enclosure of the single digamma value at a chosen \(R\). The finite Schur positivity gate remains RH-bearing.

## Sources

- `research/grothendieck/explicit-two-variable-weil-heat-source-formula.md`
- `research/grothendieck/source-formula-for-the-gaussian-translation-rectangle.md`
- `research/grothendieck/archimedean-weil-form-is-bounded-on-every-positive-sobolev-scale.md`

## Verification

- `research/voevodsky/checkers/check_source_tail_normalization.py`
- `research/voevodsky/results/source_tail_normalization.json`
