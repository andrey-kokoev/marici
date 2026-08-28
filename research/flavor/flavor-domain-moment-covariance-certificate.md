# Exchangeable flavor slots require a covariance certificate: WP967

## Question

What quantitative instrument certificate is sufficient to distinguish
repeatable WP97 preparation from WP966's common-mode hostile?

## Exact exchangeable law

Let X_1 through X_N be calibrated sign slots with zero mean, unit variance, and
common pairwise covariance rho. Slot labels describe one joint preparation
packet; they are not assigned physical time or causal order. For

\[
\widehat m_1=\frac1N\sum_{k=1}^N X_k,
\]

the covariance sum gives

\[
\operatorname{Var}(\widehat m_1)
=\frac{N+N(N-1)\rho}{N^2}
=\frac{1+(N-1)\rho}{N}
=\frac{1-\rho}{N}+\rho.
\]

The corresponding effective independent sample count is

\[
N_{\mathrm{eff}}=\frac{N}{1+(N-1)\rho}.
\]

For rho=0 this is the IID result N. For rho=1 it is one for every N, exactly
WP966. For any fixed rho>0,

\[
\lim_{N\to\infty}\operatorname{Var}(\widehat m_1)=\rho,
\qquad
\lim_{N\to\infty}N_{\mathrm{eff}}=\frac1\rho.
\]

Thus more slots cannot overcome a nonzero common-mode component.

## Calibrated certificate

If an admitted joint-preparation instrument supplies the bound
0 <= rho <= rho_max, then

\[
\operatorname{Var}(\widehat m_1)
\leq \frac{1-\rho_{\max}}{N}+\rho_{\max}.
\]

Chebyshev gives the distribution-free decision bound

\[
\Pr(|\widehat m_1-m_1|\geq\eta)
\leq
\frac{(1-\rho_{\max})/N+\rho_{\max}}{\eta^2}.
\]

A requested error probability delta is impossible under this certificate when
rho_max >= delta eta^2. When rho_max < delta eta^2, it suffices that

\[
N\geq
\frac{1-\rho_{\max}}{\delta\eta^2-\rho_{\max}}.
\]

## Classification

This is a conditional non-selector instrument theorem. It does not manufacture
decorrelation. It types the missing physical datum and supplies a falsifier:
an observed variance floor above rho_max invalidates the reset certificate.
The source must define the slot family and the covariance calibration; an
observer-side declaration of IID is not authority.

Reproduce with:

    python research/flavor/checkers/wp967_domain_moment_covariance_certificate.py

Generated result:
research/flavor/results/wp967_domain_moment_covariance_certificate.json.
