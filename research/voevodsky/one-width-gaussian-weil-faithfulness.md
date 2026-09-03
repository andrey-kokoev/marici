# One-width Gaussian Weil faithfulness

## Question

Must Gaussian width tend to zero to recover positivity of the completed spectral distribution from translate Gram positivity?

## Claim boundary

The reduction assumes positive definiteness of the source-derived difference kernel at one width. It does not prove that positivity.

## Fixed-width kernel

Choose \(\sigma>0\) and let

\[
\mu_\sigma=e^{-2\sigma u^2}\rho,
\qquad
K_\sigma(d)=\langle\mu_\sigma,e^{-idu}\rangle.
\]

If every finite Toeplitz matrix

\[
[K_\sigma(a_i-a_j)]_{i,j}
\]

is positive semidefinite, Bochner–Schwartz identifies \(\mu_\sigma\) as a positive tempered measure.

## Local division

For any nonnegative compactly supported smooth test \(\phi\), define

\[
\psi(u)=e^{2\sigma u^2}\phi(u).
\]

The function \(\psi\) remains compactly supported, smooth, and nonnegative. Therefore

\[
\langle\rho,\phi\rangle
=
\langle\mu_\sigma,\psi\rangle
\geq0.
\]

Thus \(\rho\) is a positive distribution. Strict positivity of the Gaussian makes a width limit unnecessary.

## Falsifier

A negative spectral atom remains negative after multiplication by every positive Gaussian. The checker retains this deliberate failure and verifies the finite positive-atom Gram factorization and exact local-division identity.

## Disposition

The faithful contract has one analytic parameter rather than a width tower: select one explicit \(\sigma>0\) and prove all finite Toeplitz matrices of the imaginary-character kernel positive semidefinite without zero-location input. This condition is equivalent to positivity of the completed spectral distribution.

## Verification

- `research/voevodsky/one-width-gaussian-weil-faithfulness-v1.json`
- `research/voevodsky/checkers/check_one_width_gaussian_weil_faithfulness.py`
- `research/voevodsky/results/one_width_gaussian_weil_faithfulness.json`
