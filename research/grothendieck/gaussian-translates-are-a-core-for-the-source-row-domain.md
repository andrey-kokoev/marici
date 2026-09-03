# Gaussian translates are a core for the gamma row, not yet the completed source domain

## Question

Can the open Bargmann--Fock graph-core gate be reduced to standard weighted `L^2` approximation?

## Sector bounds at fixed width

Work first on the real spectral line and transport the result unitarily to Fock space.

The endpoint row would be bounded after Bargmann transport only if the original endpoint functional is proved to intertwine with evaluation by a Fock reproducing-kernel vector. Generic bounded point evaluation in Fock space does not establish this source identity.

For the labelled prime row, every adjacency part has operator norm at most one. Hence

\[
\|A_{\mathbb P}f\|^2+
\|B_{\mathbb P}f\|^2
\le
\left(\sum_nq_n\right)\|f\|^2.
\]

At fixed Gaussian width the log-Gaussian coefficients satisfy

\[
\sum_nq_n<\infty.
\]

Therefore the full labelled prime row is bounded.

The only unbounded sector is gamma. Its positive and negative feature norms combine to the weighted norm

\[
\int |w_\Gamma(u)|\,|f(u)|^2\,du,
\]

with `|w_Gamma(u)|=O(log(2+|u|))`. Thus the common source-row domain is the weighted space

\[
\mathcal D_\Gamma
=
L^2\!\left((1+|w_\Gamma|)du\right)
\]

up to bounded endpoint and prime summands.

## Gaussian translate core

Let `g_sigma` be the fixed Gaussian and set

\[
\mathcal G_\sigma
=
\operatorname{span}\{g_\sigma(\cdot-a):a\in\mathbb R\}.
\]

Derivatives of the translation orbit at `a=0` are polynomial--Gaussian functions. Each derivative is the weighted-`L^2` limit of finite differences of real translates because logarithmic weight is dominated by the Gaussian envelope.

Polynomial--Gaussian functions generate the Hermite span. The Hermite span is dense in Schwartz space, and Schwartz functions are a core for multiplication by `sqrt(|w_Gamma|)`: truncate a weighted-`L^2` function, approximate on the compact region by smooth functions, and then use Schwartz cutoff approximation.

Consequently

\[
\overline{\mathcal G_\sigma}^{\|\cdot\|_{\mathcal D_\Gamma}}
=
\mathcal D_\Gamma.
\]

This proves a gamma-sector core theorem. The prime row is bounded at fixed width, but the endpoint functionals generally require two-sided exponential Fourier control. They cannot be discarded from the completed graph topology without the missing intertwining theorem.

## Boundary of the theorem

This proves the core statement only after the completed form has the stated source-row realization:

- gamma is the real logarithmic multiplication form;
- endpoint evaluation is represented by bounded Fock kernel vectors;
- the prime row uses absolutely summable fixed-width labelled coefficients.

It does not prove positivity or construct the Douglas contraction. It proves that positivity on all finite Gaussian translate spans would extend to the entire common row domain.

## Disposition

The gamma-sector topology gate is discharged at fixed width. The completed form-core gate remains open: prove the endpoint--Fock intertwiner and density of Gaussian translates in the combined endpoint-exponential, gamma-logarithmic, and prime-row graph topology. Only after that step does positivity on the Gaussian core extend to the full source domain.
