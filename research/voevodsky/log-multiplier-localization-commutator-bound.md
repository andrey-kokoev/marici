# Log-multiplier localization commutator bound

## Question

What computable source datum controls the localization commutators in the interval order-zero remainder?

## Claim boundary

This packet proves a Fourier-chart sufficient bound for commutators with the logarithmic multiplier. It does not identify the repository's actual partition functions or their normalization.

## Fourier commutator

On a periodic chart, let

\[
\Lambda e_n=\log(1+|n|)e_n
\]

and let multiplication by a chart function \(\chi\) have Fourier coefficients \(\widehat\chi_k\). The commutator matrix is

\[
[\Lambda,M_\chi]_{nm}
=
\bigl(\log(1+|n|)-\log(1+|m|)\bigr)
\widehat\chi_{n-m}.
\]

Since \(x\mapsto\log(1+x)\) is one-Lipschitz on the nonnegative axis,

\[
\left|
\log(1+|n|)-\log(1+|m|)
\right|
\le |n-m|.
\]

The Schur test therefore gives

\[
\lVert[\Lambda,M_\chi]\rVert
\le
\sum_{k\in\mathbb Z}|k|\,|\widehat\chi_k|.
\]

Thus a finite first absolute Fourier moment of every localization function supplies an explicit order-zero commutator constant.

## Exact fixture

For \(\chi(x)=\cos x\), the only nonzero Fourier coefficients are \(\widehat\chi_{\pm1}=1/2\), so the bound is one. The checker verifies the finite-section row and column sums never exceed one.

A hostile coefficient family \(|\widehat\chi_k|=1/k^2\) has

\[
\sum_{k\ge1}k|\widehat\chi_k|=
\sum_{k\ge1}\frac1k,
\]

which diverges. This does not prove the commutator unbounded, but it falsifies this certificate and shows why qualitative smoothness must be replaced by a quantitative coefficient bound.

## Interval application

For a two-chart interval localization, sum the constants for the declared partition functions and coordinate transfers. Combined with the principal constant

\[
\pi+4+\frac12\log20,
\]

this yields a publication-grade \(C_L\) once the actual chart Fourier coefficients and normalization are supplied.

## Disposition

The localization gate is reduced to a finite, source-readable datum:

\[
C_{\rm loc}
=
\sum_j\sum_k|k|\,|\widehat\chi_{j,k}|

together with coordinate-transfer constants. The next task is extraction of the actual partition functions; no abstract pseudodifferential claim is needed for this sufficient route.

## Verification

- `research/voevodsky/checkers/check_log_multiplier_localization_commutator.py`
- `research/voevodsky/results/log_multiplier_localization_commutator.json`
