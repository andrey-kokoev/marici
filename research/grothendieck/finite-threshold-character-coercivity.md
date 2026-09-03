# Finite-threshold character coercivity for the shifted-Gaussian Weil kernel

## Question

Can loss of positivity at a finite positive Gaussian parameter escape through unbounded character translations?

## Claim boundary

Fix a compact parameter interval

\[
I=[t_0,T]\subset(0,\infty).
\]

For the symmetrized Guinand--Weil normalization

\[
\Theta_{\mathrm{sym}}(t,\xi)
=K_{\mathrm{end}}(t,\xi)+K_\Gamma(t,\xi)+K_{\mathrm{pr}}(t,\xi),
\]

one has

\[
K_\Gamma(t,\xi)
=\frac{1}{\sqrt{\pi t}}\log\frac{|\xi|}{2\pi}+o_I(1)
\qquad(|\xi|\to\infty),
\]

uniformly in `t` on `I`, and therefore

\[
\lim_{R\to\infty}\inf_{t\in I,\,|\xi|\ge R}
\Theta_{\mathrm{sym}}(t,\xi)=+\infty.
\]

This excludes escape to infinity near every finite positive threshold. It does not exclude a finite double contact.

## Normalization pullback

The prior Marici kernel uses one shifted Gaussian and counts the positive half-divisor once. The literature-search normalization uses the even test

\[
h_{t,\xi}(u)=e^{-t(u-\xi)^2}+e^{-t(u+\xi)^2}
\]

and the full symmetrized divisor. Since the archimedean kernel is even, termwise comparison gives

\[
K_{\mathrm{end}}^{\mathrm{sym}}=4K_{\mathrm{end}}^{\mathrm{Marici}},
\quad
K_\Gamma^{\mathrm{sym}}=4K_\Gamma^{\mathrm{Marici}},
\quad
K_{\mathrm{pr}}^{\mathrm{sym}}=4K_{\mathrm{pr}}^{\mathrm{Marici}}.
\]

Hence

\[
\Theta_{\mathrm{sym}}=4\Theta_{\mathrm{Marici}}.
\]

The factor is positive, so coercivity and the zero set are invariant under this normalization change. Publication use still requires direct checking against the cited Guinand--Weil source rather than relying only on comparison with the supplied literature report.

## Proof

Put

\[
q(u)=\operatorname{Re}\psi\!\left(\frac14+\frac{iu}{2}\right)-\log\pi.
\]

The sectorial digamma expansion gives

\[
q(u)=\log|u|-\log(2\pi)+O(u^{-2})
\]

as `|u|` tends to infinity. The function `q` is even, smooth on the real line, and bounded below. Evenness reduces the symmetrized archimedean term to

\[
K_\Gamma(t,\xi)=\frac1\pi\int_{\mathbb R}e^{-t(u-\xi)^2}q(u)\,du.
\]

After `u=xi+v`, split the integral at `|v|=|xi|/2`. On the central region,

\[
q(\xi+v)=\log|\xi|-\log(2\pi)
+O\!\left(\frac{|v|+1}{|\xi|}\right).
\]

The zeroth and first Gaussian moments are bounded uniformly for `t` in `I`. On the complementary region, Gaussian decay is bounded by `exp(-t_0 xi^2/4)`, while `q` has logarithmic growth. This proves the uniform asymptotic.

The endpoint satisfies

\[
|K_{\mathrm{end}}(t,\xi)|\le 4e^{T/4-t_0\xi^2}.
\]

For the prime term,

\[
|K_{\mathrm{pr}}(t,\xi)|
\le
\frac{2}{\sqrt{\pi t_0}}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\exp\!\left(-\frac{(\log n)^2}{4T}\right)=M_I<\infty.
\]

The log-Gaussian factor dominates every negative power after a sufficiently large index, so the series converges. The positive logarithmic growth of the archimedean term dominates the bounded prime term and the decaying endpoint uniformly on `I`.

## Threshold consequence

If `t_j` tends to a finite `t_* > 0` and `Theta(t_j,xi_j)` tends to zero, coercivity makes `|xi_j| -> infinity` impossible. Combined with continuity and broad-smoothing positivity, any first loss at a finite threshold is attained at a finite character. At such an attained minimum,

\[
\Theta(t_*,\xi_*)=0,
\qquad
\partial_\xi\Theta(t_*,\xi_*)=0.
\]

The surviving RH-equivalent problem is finite double-contact exclusion.

## Sources and verification status

- Bondarenko--Radchenko--Seip, *Fourier Interpolation with Zeros of Zeta and L-Functions*, Constructive Approximation 57 (2023), arXiv:2005.02996. The downloaded arXiv source has SHA-256 `5ee4bbde5a3f4396e972ed214d394f4dc237439f3a5438f02e2efbb196657a58`; source lines 98--110 state formula (1.1), the Fourier convention, admissibility conditions, zero node, and multiplicity convention.
- NIST/DLMF 5.11.2 for the sectorial digamma asymptotic.

Direct transcription verifies that Bondarenko--Radchenko--Seip place the prime sum and zero sum on the right of (1.1); solving for the zero sum therefore gives positive endpoint and gamma terms and a negative prime term. Their Fourier convention is `exp(-2 pi i x xi)`, their node is `(rho-1/2)/i`, and zeros are counted with multiplicity. The symmetrized shifted Gaussian is entire and has Gaussian decay uniformly on every closed substrip, so it lies in their admissible class.

`checkers/explicit_two_variable_weil_heat_source.py` checks that substitution of the symmetrized Gaussian transforms the endpoint, gamma-integral, and prime-sum coefficients by the common positive factor four relative to the prior Marici convention and deliberately rejects factor two; its result is `results/explicit-two-variable-weil-heat-source.json`. An effective digamma remainder constant remains open. The claimed 2026 compact-window bounds from Zhu are not used here and remain independently unverified.

## Disposition

Escape to infinity at a finite positive threshold is removed from the live frontier. The explicit-formula transcription and normalization pullback are verified; an effective radius still requires explicit remainder constants. Finite double contact remains unresolved.
