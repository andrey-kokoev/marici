# The finite-vector arithmetic resolvent conjecture is false

## Conjecture tested

The proposed constructor required a self-adjoint operator \(A\) and a Hilbert vector \(\Omega\) satisfying

\[
\frac{\Xi'(z)}{\Xi(z)}
=
\left\langle
\Omega,
\left((z-iA)^{-1}+(z+iA)^{-1}\right)
\Omega
\right\rangle,
\]

up to polar or affine elementary terms.

## Resolvent asymptotic

For positive real \(x\), the spectral theorem gives

\[
\left|
\left\langle
\Omega,
\left((x-iA)^{-1}+(x+iA)^{-1}\right)
\Omega
\right\rangle
\right|
\leq
\frac{2\lVert\Omega\rVert^2}{x}.
\]

Therefore every such finite-vector resolvent coefficient tends to zero as \(x\) tends to infinity.

## Xi asymptotic

Stirling's formula in the completed logarithmic derivative gives

\[
\frac{\Xi'(x)}{\Xi(x)}
=
\frac12\log\left(\frac{x}{2\pi}\right)
+O(1/x).
\]

This diverges logarithmically. Polar terms decay rationally, and affine terms cannot cancel a logarithm.

The two sides therefore cannot be equal.

## Disposition

The bold conjecture is falsified as stated. In particular, the endpoint–gamma–prime logarithmic derivative cannot be the ordinary paired resolvent matrix coefficient of one finite-norm cyclic vector.

## Surviving repairs

Two materially different conjectures remain possible:

1. subtract the full explicit archimedean logarithmic reference before seeking a finite-vector resolvent for the remainder;
2. use a rigged or distributional cyclic vector with infinite spectral mass, while requiring its Gaussian regularizations to be genuine Hilbert vectors.

The second option fits the heat-kernel construction better, but it loses the simple bounded resolvent estimate and requires a declared rigged Hilbert domain. Neither repair has been constructed.

## Verification

```text
python research/voevodsky/checkers/check_arithmetic_resolvent_asymptotic_no_go.py
```

Artifacts:

- `research/voevodsky/checkers/check_arithmetic_resolvent_asymptotic_no_go.py`
- `research/voevodsky/results/arithmetic_resolvent_asymptotic_no_go.json`
