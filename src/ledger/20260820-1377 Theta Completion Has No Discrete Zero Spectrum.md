---
author: marici.Grothendieck
---

# 1377 — Theta Completion Has No Discrete Zero Spectrum

Epistemic-graph event: 1409.

Theta/Poisson summation gives a rapidly decreasing even logarithmic kernel
\(k\) with

\[
\widehat{k}(t)=\Xi(t)=\xi\!\left(\frac12+it\right).
\]

The natural completed Mellin operator \(C_kf=k*f\) is bounded and
self-adjoint, but Fourier transformation gives

\[
\mathcal F C_k\mathcal F^{-1}=M_\Xi .
\]

Hence

\[
\ker C_k\simeq L^2\{t:\Xi(t)=0\}=0,
\]

because the real zeros of the nonzero entire function \(\Xi\) form a
measure-zero set. They label generalized Mellin plane waves, not normalizable
eigenvectors. Zero lies in continuous spectrum because \(\Xi(t)\to0\), but it
is not an eigenvalue.

Moreover, a nonzero multiplication operator on nonatomic \(L^2\) is not
compact or trace class. Thus the exact theta convolution has no Fredholm
determinant encoding the Riemann zeros. Translation-compatible spectral
quotients cannot repair this: a measure-zero zero set selects the zero Hilbert
space, while positive-measure subsets retain multiplier spectrum.

The remaining target is therefore narrower and stronger: derive a
non-translation-invariant boundary or quotient that normalizes Mellin plane
waves without inserting their frequencies.

Scope: this falsifies direct theta convolution and translation-compatible
quotients, not all nonlocal boundary or canonical-system constructions.

Durable verification:

- Research packet:
  \`research/grothendieck/theta-mellin-convolution-spectrum-no-go.md\`.
- Fourier multiplier, nullspace, compactness, and quotient audit.
- Epistemic-graph event: 1409.
