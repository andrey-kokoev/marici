# The two-variable Weil kernel determines every Gaussian-translate Gram matrix

## Completed spectral form

Let `rho` denote the centered completed Weil distribution in the spectral variable, and define its Gaussian regularization

\[
\Theta(t,\xi)=\langle\rho,e^{-t(u-\xi)^2}\rangle.
\]

The explicit endpoint--gamma--prime formula materializes this shifted spectral-Gaussian pairing without assuming a zero measure. This paragraph defines a multiplication form on spectral probes; it does not identify that form with the source-translation Weil pairing.

Fix one width and use Gaussian translate probes

\[
g_a(u)=e^{-\frac t2(u-a)^2}.
\]

Their product has the exact midpoint factorization

\[
g_a(u)g_b(u)
=
 e^{-\frac t4(a-b)^2}
 e^{-t(u-(a+b)/2)^2}.
\]

Therefore the completed Weil Gram matrix is read directly from the materialized two-variable kernel:

\[
G_{ij}
=
 e^{-\frac t4(a_i-a_j)^2}
 \Theta\!\left(t,\frac{a_i+a_j}{2}\right).
\]

Any normalization factor common to the Gaussian convention is positive and does not affect positive semidefiniteness.

## Consequences

The diagonal entries are

\[
G_{ii}=\Theta(t,a_i).
\]

Thus pointwise all-translate positivity is exactly diagonal Gram positivity, not full Gram positivity. The first coupled condition is

\[
\Theta(t,a)\Theta(t,b)
\ge
 e^{-\frac t2(a-b)^2}
 \Theta\!\left(t,\frac{a+b}{2}\right)^2.
\]

Equivalently, wherever `Theta` is positive,

\[
\xi\longmapsto \log\Theta(t,\xi)+t\xi^2
\]

must be midpoint-convex. Continuity upgrades midpoint convexity to ordinary convexity. This rank-two inequality is strictly stronger than pointwise positivity.

For higher rank, every matrix is obtained from the same source function by midpoint evaluation and Gaussian difference damping. This identifies the Gram matrix only for the spectral multiplication form. Under the source Fourier convention, translating a Gaussian produces a spectral phase rather than a shifted spectral Gaussian, so a separate Fourier comparison is required.

## Faithfulness

Voevodsky's Gaussian-translate density theorem then applies: positivity of these matrices for one fixed width and all finite translate tuples extends by Schwartz continuity to the full completed Weil form. The remaining RH-equivalent gate is direct PSD of the displayed source matrices.

## Disposition

Retain the midpoint formula as an exact theorem for spectral multiplication probes only. Do not use it as the source-translation Weil Gram matrix. The missing crossing must Fourier-transform source translations to character-weighted centered spectral Gaussians with all constants fixed; only that kernel may enter the density argument.
