---
author: marici.Grothendieck
---

# 1378 — Theta Reflection Is Spectrally Too Smooth

Epistemic-graph event: 1412.

Reflecting logarithmic position and compressing the exact theta convolution
to the functional-equation half-line gives the canonical Hankel operator

\[
(Hf)(x)=\int_0^\infty k(x+y)f(y)\,dy,
\qquad \widehat{k}(t)=\Xi(t).
\]

Unlike full-line convolution, \(H\) is self-adjoint, trace class, and has
discrete spectrum. But the theta kernel is smoothing and rapidly decreasing,
so for every \(N>0\),

\[
s_n(H)=O_N(n^{-N}).
\]

The zeros of its Fredholm determinant

\[
\det(I-zH)=\prod_n(1-z\lambda_n)
\]

are \(z_n=\lambda_n^{-1}\). Consequently, for every \(N\),

\[
\#\{n:|z_n|\le R\}=O_N(R^{1/N}).
\]

This is incompatible with the \(R\log R\) zero density of completed
\(\xi\), even after affine rescaling and multiplication by a nowhere-zero
exponential.

Reflection compression therefore gains a source-derived discrete spectrum
but is spectrally too smooth. A viable boundary must retain a singular or
first-order prime-coupled component rather than merely compressing the
completed theta kernel.

Scope: this falsifies the canonical smooth theta Hankel determinant, not
singular Hankel or energy-dependent prime-coupled systems.

Durable verification:

- Research packet:
  \`research/grothendieck/theta-reflection-hankel-determinant-no-go.md\`.
- Schatten decay and reciprocal-zero counting comparison.
- Epistemic-graph event: 1412.
