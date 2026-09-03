# One fixed Gaussian width is already Weil-faithful

## Difference kernel

For any fixed `sigma>0`, define

\[
K_\sigma(d)
=
\left\langle
\rho,e^{-2\sigma u^2}e^{-idu}
\right\rangle,
\]

where `rho` is the centered completed Weil distribution. The imaginary-character continuation packet gives this function explicitly from the endpoint, gamma, and prime source.

## Fixed-width equivalence

If `rho` is positive, then the Gaussian-weighted distribution

\[
\mu_\sigma=e^{-2\sigma u^2}\rho
\]

is positive, and its Fourier transform `K_sigma` is positive definite.

Conversely, suppose every finite translate matrix

\[
[K_\sigma(a_i-a_j)]_{i,j}
\]

is positive semidefinite. By the Bochner--Schwartz theorem, `K_sigma` is the Fourier transform of a positive measure. Fourier injectivity identifies that measure with `mu_sigma`.

The Gaussian multiplier is strictly positive. For every nonnegative compactly supported smooth test `phi`,

\[
\langle\rho,\phi\rangle
=
\left\langle
\mu_\sigma,e^{2\sigma u^2}\phi(u)
\right\rangle
\ge0,
\]

because the divided test remains nonnegative and compactly supported. Hence `rho` is positive as a distribution.

Therefore PSD of the source difference kernel at one arbitrary fixed Gaussian width is equivalent to full Weil positivity. Varying widths is unnecessary for faithfulness.

## Relation to Gaussian-translate density

The Hermite--Gaussian density argument supplies a constructive extension inside Schwartz space. The fixed-width Bochner argument is stronger as an equivalence statement: strict positivity of the multiplier permits local division and recovers the unsmoothed distribution directly.

Neither argument proves PSD. They show that no limit in width, cutoff family, or additional source probes are needed once one fixed-width difference kernel is positive definite.

## Exact source target

Choose and freeze one `sigma>0`. Using the verified continuation,

\[
K_\sigma(d)
=
 e^{-d^2/(8\sigma)}
\Theta\!\left(2\sigma,-\frac{id}{4\sigma}\right)
\]

up to a common positive constant. Prove every finite Toeplitz matrix formed from this function is PSD. This single-width theorem is already RH-equivalent.

## Disposition

Remove width variation and Gaussian-limit passage from the minimal proof contract. The sole remaining target is positive definiteness of one explicit fixed-width source difference kernel. Scalar heat jets and separated rank-two inequalities remain necessary projections of that target, not independent gates.
