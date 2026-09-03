# Paired-Hadamard and Laplace convergence

## Question

Do the standard zero-count and critical-strip bounds suffice to justify the convergence and interchange steps in the general-complex-zero heat expansion?

## Claim boundary

Yes, conditional on the classical inputs. The majorant proofs are elementary. Exact theorem text and authoritative citations for those inputs remain to be inspected.

## Classical inputs

Assume:

1. \(N(T)=O(T\log T)\);
2. every nontrivial zero lies in \(0<\beta<1\);
3. a zero-free compact region below ordinate \(1/2\) gives
   \[
   \inf_\rho|\gamma_\rho|>\frac12.
   \]

The third bound is much weaker than the known verified zero height; only strict separation from \(1/2\) is used.

## Paired product convergence

Write

\[
a_\rho=\rho-\frac12.
\]

In the dyadic shell

\[
2^k\leq|a_\rho|<2^{k+1},
\]

the zero count is

\[
O(2^k k).
\]

Each inverse-square term is at most \(2^{-2k}\). Hence the shell contributes

\[
O\left(\frac{k}{2^k}\right).
\]

Since

\[
\sum_{k\geq1}\frac{k}{2^k}<\infty,
\]

one obtains

\[
\sum_{[a]}\frac{m_a}{|a|^2}<\infty.
\]

The paired genus-zero product

\[
\prod_{[a]}
\left(1-\frac{x}{a^2}\right)^{m_a}
\]

therefore converges normally on compact sets.

## Logarithmic derivative

On a compact \(x\)-set avoiding poles, sufficiently large \(|a|\) satisfy

\[
\left|\frac1{x-a^2}\right|
\leq
\frac{C_K}{|a|^2}.
\]

The inverse-square summability gives locally uniform convergence of

\[
\sum_{[a]}
\frac{m_a}{x-a^2}.
\]

Termwise logarithmic differentiation is consequently justified away from the pole set.

## Heat convergence

For

\[
\lambda_\rho=-a_\rho^2,
\]

the critical strip gives

\[
\operatorname{Re}\lambda_\rho
=
\gamma^2-(\beta-1/2)^2
\geq
\gamma^2-\frac14.
\]

For \(t\geq t_0>0\),

\[
|e^{-t\lambda_\rho}|
\leq
 e^{-t_0(\gamma^2-1/4)}.
\]

The zero count makes this Gaussian majorant summable. Thus the general-complex heat series converges normally on every region \(t\geq t_0>0\).

Every term tends to zero as \(t\to\infty\). Dominated convergence yields

\[
H(t)\to0.
\]

## Inverse-Laplace interchange

For \(x\) to the right of all poles,

\[
\int_0^\infty
e^{-xt}e^{-t\lambda_\rho}\,dt
=
\frac1{x+\lambda_\rho}.
\]

After separating finitely many low zeros, the absolute integral is bounded at large ordinate by a constant multiple of \(|a_\rho|^{-2}\). The paired inverse-square sum converges, so sum and integral may be interchanged absolutely in that half-plane.

This yields

\[
\int_0^\infty e^{-xt}H(t)\,dt
=
\sum_{[\rho]}
\frac{m_\rho}{x+\lambda_\rho}.
\]

## What remains bibliographic

Metadata-verified candidate references now exist for:

- the Xi-function Hadamard theory;
- Riemann--von Mangoldt zero counting;
- verified low-zero exclusion;
- Laplace-transform interchange.

Their exact theorem statements and page content have not been inspected. Metadata verification alone does not establish that they state the hypotheses used here.

## Disposition

Given the three classical inputs, paired-product convergence, logarithmic differentiation, normal heat convergence, decay, and inverse-Laplace interchange follow by explicit majorants. The unresolved source obligation has narrowed to inspection and citation of the input theorems plus joint normalization review.

## Verification

- `research/voevodsky/paired-hadamard-laplace-convergence-v1.json`
- `research/voevodsky/checkers/check_paired_hadamard_laplace_convergence.py`
- `research/voevodsky/results/paired_hadamard_laplace_convergence.json`
