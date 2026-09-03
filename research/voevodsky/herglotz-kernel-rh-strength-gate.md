# Herglotz-kernel RH-strength gate

## Question

What positivity statement remains after normalization, reciprocal coherence, and filler completion are established?

## Claim boundary

This identifies and checks the kernel shape. It does not construct its arithmetic Gram realization.

## Kernel criterion

Let \(\Xi(z)=\xi(1/2+z)\) and

\[
F(z)=\frac{\Xi'(z)}{\Xi(z)}
\]

on \(\operatorname{Re}z>0\). The required Herglotz kernel is

\[
K_F(z,w)=
\frac{F(z)+\overline{F(w)}}{z+\overline w}.
\]

For a reciprocal pair of boundary zeros \(\pm i\gamma\), its logarithmic-derivative contribution is

\[
F_\gamma(z)=
\frac1{z-i\gamma}+rac1{z+i\gamma}.
\]

Direct algebra gives

\[
K_\gamma(z,w)=
\frac1{(z-i\gamma)(\overline w+i\gamma)}
+
\frac1{(z+i\gamma)(\overline w-i\gamma)}.
\]

This is a sum of two rank-one Gram kernels. Sums over imaginary-axis zeros remain positive when convergence permits.

Conversely, positivity as a holomorphic kernel on the right half-plane requires \(F\) to be holomorphic there. An off-axis zero of \(\Xi\) creates a pole of \(F\), contradicting that requirement; reciprocal reflection handles the opposite half-plane.

## Hostile boundary

Pointwise positivity and evenness of the completed source do not imply this kernel positivity. Positive Gaussian mixtures already provide source-generated counterexamples with off-axis zeros. Likewise, primewise terms have the wrong sign before endpoint–gamma–prime completion and cannot be assigned separate positive Gram spaces.

## Disposition

The RH-strength target is now exact: construct \(K_F\) as a positive Gram kernel from the fully completed arithmetic source on \(\operatorname{Re}z>0\), without using the zero set. Affine fillers, reciprocal naturality, and normalization do not provide this construction.

## Verification

- `research/voevodsky/herglotz-kernel-rh-strength-gate-v1.json`
- `research/voevodsky/checkers/check_herglotz_kernel_rh_strength_gate.py`
- `research/voevodsky/results/herglotz_kernel_rh_strength_gate.json`
