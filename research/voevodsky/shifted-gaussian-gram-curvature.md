# Shifted-Gaussian Gram curvature

## Question

What is the exact Gram identification for shifted spectral Gaussians, and what does rank-two positivity require?

## Claim boundary

This closes the identification and rank-two reduction. It does not prove the arithmetic inequality or higher minors.

## Polarization

For

\[
g_a(u)=e^{-t(u-a)^2/2},
\]

direct completion of squares gives

\[
g_a(u)g_b(u)=
e^{-t(a-b)^2/4}
e^{-t(u-(a+b)/2)^2}.
\]

Hence, up to the common positive normalization fixed in the explicit formula,

\[
G_t(a,b)=
e^{-t(a-b)^2/4}
\Theta\left(t,\frac{a+b}{2}\right).
\]

This formula applies to shifted spectral multiplication probes. It does not correct the prior translation-versus-modulation objection and is not yet the translated-source Weil Gram entry.

## Rank two

For positive \(\Theta\), a two-point determinant is nonnegative exactly when

\[
\Theta(t,a)\Theta(t,b)
\geq
e^{-t(a-b)^2/2}
\Theta\left(t,\frac{a+b}{2}\right)^2.
\]

Define

\[
Q_t(\xi)=\log\Theta(t,\xi)+t\xi^2.
\]

The determinant inequality is midpoint convexity of \(Q_t\). Locally it becomes

\[
\partial_\xi^2\log\Theta(t,\xi)+2t\geq0.
\]

## Heat direction

Let \(\tau=1/(4t)\), suppose \(U_\tau=U_{\xi\xi}\), and write \(F=\log U\). For

\[
q=F_{\xi\xi}+\frac1{2\tau},
\]

differentiation gives

\[
q_\tau=q_{\xi\xi}+2F_\xi q_\xi+2q^2-\frac2\tau q.
\]

At a first zero spatial minimum, \(q_\xi=0\) and \(q_{\xi\xi}\geq0\), so \(q_\tau\geq0\). Curvature positivity propagates only forward toward broader smoothing. It cannot prove the narrow regime by reversal.

## Disposition

The midpoint identification is explicit only for spectral multiplication probes. The translated-source Weil Gram entry still requires the character-weighted centered Gaussian interface with fixed Fourier constants. The curvature inequality is therefore a rank-two test for the spectral multiplication family, not yet the full Weil Gram family.

## Verification

- `research/voevodsky/shifted-gaussian-gram-curvature-v1.json`
- `research/voevodsky/checkers/check_shifted_gaussian_gram_curvature.py`
- `research/voevodsky/results/shifted_gaussian_gram_curvature.json`
