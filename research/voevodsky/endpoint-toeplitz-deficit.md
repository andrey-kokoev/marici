# Endpoint Toeplitz deficit

## Question

Can the positive endpoint scalar term anchor a sectorwise Gram decomposition?

## Claim boundary

The calculation isolates the endpoint deficit. It does not prove that the completed gamma-plus-prime remainder compensates it.

## Exact rank-two failure

The crossed endpoint kernel is

\[
E_\sigma(d)=e^{\sigma/2}\cosh(d/2).
\]

Its two-translate Toeplitz matrix has determinant

\[
E_\sigma(0)^2-E_\sigma(d)^2
=-e^\sigma\sinh^2(d/2),
\]

which is negative for every nonzero \(d\).

The symmetric eigenchannel is positive, but the antisymmetric channel is

\[
E_\sigma(0)-E_\sigma(d)
=-e^{\sigma/2}\left(\cosh(d/2)-1\right)<0.
\]

## Required compensation

Write the completed kernel as

\[
K_\sigma=E_\sigma+R_\sigma,
\]

where \(R_\sigma\) combines gamma and prime channels after continuation. Rank-two positivity requires

\[
R_\sigma(0)-R_\sigma(d)
\geq
e^{\sigma/2}\left(\cosh(d/2)-1\right).
\]

At small separation, the endpoint deficit is

\[
e^{\sigma/2}\frac{d^2}{8}+O(d^4),
\]

so a necessary local condition is

\[
R_\sigma''(0)\leq-\frac{e^{\sigma/2}}4.
\]

## Disposition

Endpoint scalar positivity is diagonal-only and cannot seed a positive Gram summand. Any successful proof must combine endpoint, gamma, and prime sectors before asserting positivity. Small-prime or sectorwise positive perturbation arguments are structurally blocked by the exact antisymmetric deficit.

## Verification

- `research/voevodsky/endpoint-toeplitz-deficit-v1.json`
- `research/voevodsky/checkers/check_endpoint_toeplitz_deficit.py`
- `research/voevodsky/results/endpoint_toeplitz_deficit.json`
