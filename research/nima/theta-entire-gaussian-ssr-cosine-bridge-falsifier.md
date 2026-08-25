# Entire Gaussian falsifier for the SSR-to-cosine bridge

## Purpose

The earlier two-exponential witness showed that spectral
\(\mathrm{SSR}_\infty\) does not force real cosine-transform zeros, but its
transform was rational rather than entire. The separation persists in the
even positive Schwartz class.

## Source-local sign-regular family

Use

\[
K(s,\lambda)=e^{-s\lambda},\qquad s,\lambda>0.
\]

This is strictly reverse-sign-regular of all orders. Pull it back through
the monotone chart \(s=u^2\) on \(u>0\), and choose the two positive,
distinct labels \(\lambda=1,2\):

\[
\phi(u)=e^{-u^2}+e^{-2u^2}.
\]

The source is even, strictly positive, Schwartz, and is a positive sum of
two labelled modes from an \(\mathrm{SSR}_\infty\) family.

## Entire cosine transform

Its bilateral Fourier transform is

\[
F(z)
=\sqrt\pi\,e^{-z^2/4}
+\sqrt{\frac\pi2}\,e^{-z^2/8}.
\]

This is entire and even. Dividing by the first nonzero Gaussian factor gives

\[
F(z)=0
\quad\Longleftrightarrow\quad
1+\frac1{\sqrt2}e^{z^2/8}=0.
\]

Therefore

\[
\frac{z^2}{8}
=\log\sqrt2+(2k+1)\pi i,
\qquad k\in\mathbb Z.
\]

Every such solution is nonreal and off both coordinate axes. For \(k=0\),

\[
z\approx3.7455173478+3.3550426943\,i.
\]

Thus the bridge fails within the same broad analytic class relevant to
completed theta transforms:

\[
\boxed{
\text{positive even Schwartz mixture of an SSR}_{\infty}\text{ family}
\not\Rightarrow
\text{real-zero entire cosine transform}.
}
\]

## Normal-current interpretation

At any upper-half-plane zero \(z_0\) of \(F\),

\[
\partial_y|F(z_0)|^2=0.
\]

Hence spectral sign regularity cannot imply the strict normal-modulus law
required by the denominator-free de Branges kernel. The failure occurs
after the positive summation and oscillatory transform constructors, not in
the labelled spectral family.

## Constructor diagnosis

The labelled map

\[
\{c_\lambda\}\longmapsto
\sum_\lambda c_\lambda e^{-\lambda u^2}
\]

is variation diminishing. Selecting the single positive coefficient vector
\((1,1)\) and then Fourier transforming is a different constructor tree.
The summation lens collapses coefficient directions, and the Fourier
constructor introduces complex interference. No coherence cell transports
spectral minors into de Branges-kernel positivity.

The additional RH-bearing law must therefore act directly on the fully
integrated two-copy normal current or denominator-free Loewner kernel. It
cannot be a generic closure property of positive Schwartz summation.

## Finite falsifier

The complete exact witness is:

\[
\lambda_1=1,\quad\lambda_2=2,\quad c_1=c_2=1,
\]

\[
z^2=8\left(\log\sqrt2+\pi i\right).
\]

Substitution makes the two nonzero Gaussian transform terms cancel exactly.

