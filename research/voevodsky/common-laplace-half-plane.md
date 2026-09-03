# Common Laplace half-plane

## Question

On what single open domain do the endpoint--gamma--prime transform, the Euler product, and the general-complex-zero heat transform all converge before meromorphic continuation?

## Claim boundary

The common domain is the half-plane \(\operatorname{Re}x>1/4\), conditional only on the existing gamma-kernel absolute-control derivation. The low-zero exclusion now has inspected source text. The Xi Hadamard source text remains uninspected.

## Principal square root

Use the principal square root and set

\[
s=\frac12+\sqrt x.
\]

For \(x=a+ib\) with \(a>0\),

\[
(\operatorname{Re}\sqrt x)^2
=
\frac{|x|+a}{2}
\geq a.
\]

Therefore

\[
\operatorname{Re}x>\frac14
\quad\Longrightarrow\quad
\operatorname{Re}\sqrt x>\frac12
\quad\Longrightarrow\quad
\operatorname{Re}s>1.
\]

The Euler expansion for \(\zeta'/\zeta(s)\) is absolutely convergent throughout this half-plane.

## Endpoint transform

The endpoint kernel satisfies

\[
\int_0^\infty
e^{-xt}e^{t/4}\,dt
=
\frac1{x-1/4}
\]

for

\[
\operatorname{Re}x>\frac14.
\]

This boundary is sharp for the endpoint term considered separately.

## Prime and gamma transforms

On the same half-plane, \(\operatorname{Re}s>1\), so the prime Euler sum is absolute before applying the square-root Laplace identity. The existing gamma-kernel packet derives its transform under the same initial control region.

Thus the three arithmetic pieces use one common transform prescription rather than separate continuations.

## Zero-side transform

For

\[
\lambda_\rho
=-\left(\rho-\frac12\right)^2,
\]

one has

\[
\operatorname{Re}\lambda_\rho
\geq
\gamma_ho^2-\frac14.
\]

Platt--Trudgian, arXiv:2004.09765, Theorem 1, states that RH is verified through height

\[
3{,}000{,}175{,}332{,}800.
\]

In particular there is no nontrivial zero with \(|\gamma|\leq1/2\). Hence every \(\operatorname{Re}\lambda_\rho\) is strictly positive.

For \(\operatorname{Re}x>1/4\), every factor

\[
e^{-t(x+\lambda_\rho)}
\]

decays, and the Gaussian zero-count majorant gives absolute sum--integral interchange.

## Identity and continuation

Both constructions therefore define holomorphic functions on the connected open half-plane

\[
\operatorname{Re}x>\frac14.
\]

There they equal

\[
B'(x)
=
\frac{\xi'/\xi(1/2+\sqrt x)}{2\sqrt x}.
\]

Equality on this common initial domain fixes their meromorphic continuation uniquely. Endpoint, gamma, and prime pieces are presentations of the same completed function; they cannot supply extra poles that cancel isolated zero-side poles after the identity is established.

## Remaining audit

The final source-completion tasks are:

1. inspect authoritative theorem text for the symmetric Xi Hadamard product;
2. verify the gamma integral's absolute control on the entire complex half-plane, not only the real ray;
3. jointly compare the principal-root and multiplicity conventions against the source-owned checkers.

## Disposition

The common-domain obligation is resolved at the mathematical level and the low-zero premise is source-backed. Only Hadamard citation inspection and joint cross-artifact review remain before the equivalence skeleton can be promoted to a source-complete theorem.

## Verification

- `research/voevodsky/common-laplace-half-plane-v1.json`
- `research/voevodsky/checkers/check_common_laplace_half_plane.py`
- `research/voevodsky/results/common_laplace_half_plane.json`
