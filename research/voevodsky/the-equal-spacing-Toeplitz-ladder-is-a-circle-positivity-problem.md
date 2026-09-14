# The equal-spacing Toeplitz ladder is a circle positivity problem

## Circle pushforward

Fix Gaussian width \(\sigma>0\) and spacing \(h>0\). Let

\[
\rho_\sigma=e^{-2\sigma u^2}\rho
\]

be the damped completed spectral distribution. Push it to the unit circle by

\[
u\longmapsto e^{-ihu}.
\]

Call the resulting circle distribution \(\mu_{\sigma,h}\). Its Fourier coefficients are exactly

\[
\widehat\mu_{\sigma,h}(m)
=
K_\sigma(mh).
\]

## Herglotz equivalence

The rank-\(n\) equally spaced translate packet has Toeplitz matrix

\[
T_n=
\left[
K_\sigma((i-j)h)
\right]_{0\leq i,j<n}.
\]

For a coefficient vector \(c\), its quadratic form is

\[
c^*T_nc
=
\left\langle
\mu_{\sigma,h},
\left|
\sum_{j=0}^{n-1}c_jz^j
\right|^2
\right\rangle.
\]

Consequently every matrix in the contiguous Toeplitz ladder is positive semidefinite if and only if \(\mu_{\sigma,h}\) is a positive circle distribution. This is the Herglotz moment theorem.

Contiguous packets suffice: any finite subset of integer lattice positions is contained in one sufficiently large contiguous packet, and its Gram matrix is a principal submatrix.

## Use

The ranks-two-through-thirteen computation is evidence about one circle distribution

\[
\mu_{0.005,0.25}.
\]

Instead of certifying increasingly ill-conditioned determinants separately, one may seek a direct source formula proving positivity of this periodized distribution. Such a factorization would prove the complete lattice ladder at once.

## Aliasing boundary

One spacing does not recover positivity on the real line. The circle map identifies frequencies differing by integer multiples of

\[
\frac{2\pi}{h}.
\]

Negative and positive real-line components may therefore combine after pushforward. Circle positivity at \(h=0.25\) is weaker than RH.

A family of positive circle pushforwards for spacings tending to zero would remove this aliasing on every fixed compact frequency window and recover the unaliased positivity target under the appropriate distributional continuity.

## Verification

```text
python research/voevodsky/checkers/check_toeplitz_ladder_circle_pushforward.py
```

The checker verifies exact positive atomic factorizations through rank eight and retains a signed-circle-measure hostile failing at rank two.

Artifacts:

- `research/voevodsky/checkers/check_toeplitz_ladder_circle_pushforward.py`
- `research/voevodsky/results/toeplitz_ladder_circle_pushforward.json`
