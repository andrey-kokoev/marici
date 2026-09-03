# Paired Hadamard normalization is symbolically consistent

## Question

Does the functional-equation pair convention reproduce both the zero resolvent and the polar endpoint heat term used by the source checker?

## Verified identities

With `s=1/2+y`, `x=y^2`, `a=rho-1/2`, and `lambda=-a^2`, the exact checker verified

\[
\frac1{2y}\left(\frac1{y-a}+\frac1{y+a}\right)
=\frac1{x+\lambda}.
\]

It also verified the elementary completed factors

\[
\frac1{2y}\left(\frac1s+\frac1{s-1}\right)
=\frac1{x-1/4}.
\]

The inverse-Laplace kernels are consequently

\[
\frac1{x+\lambda}
\longleftrightarrow e^{-t\lambda},
\qquad
\frac1{x-1/4}
\longleftrightarrow e^{t/4},
\]

in their respective right half-planes of convergence.

Thus one functional-equation pair contributes one squared-resolvent term. On RH, that pair is the conjugate pair associated with one positive ordinate, matching the repository's zero-heat convention.

## Repaired checker defect

The first checker version asked SymPy to evaluate the endpoint Laplace integral while declaring only `x>0`; convergence actually requires `x>1/4`, so SymPy retained conditional structure and the assertion failed. The checker was repaired to verify the universal positive-rate Laplace integral and the exponent substitutions separately. It then passed.

## Remaining boundary

The checker certifies finite algebraic normalization, not the infinite Hadamard sum. Still required are the symmetric convergence prescription, exact multiplicity accounting for repeated zeros, and a citation proving interchange with inverse Laplace transformation.

## Artifacts

- `research/grothendieck/checkers/xi_paired_hadamard_normalization.py`
- `research/grothendieck/results/xi-paired-hadamard-normalization.json`

## Disposition

Use one term per `rho,1-rho` functional pair and retain the endpoint kernel `exp(t/4)`. Do not double the positive-ordinate spectral trace by separately counting the same functional pair.