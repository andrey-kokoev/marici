# Interval logarithmic Gårding remainder criterion

## Question

What exact comparison would turn periodic log-ellipticity into the required high-Dirichlet-subspace estimate?

## Claim boundary

This packet proves a sufficient interval criterion. It does not prove that the zero-extended archimedean Weil multiplier satisfies the bounded-remainder hypothesis.

## Dirichlet reference operator

On \((-L,L)\), let \(D_L=\sqrt{-\Delta_D}\) with sine eigenvalues

\[
\mu_n=\frac{\pi n}{2L}.
\]

Define the logarithmic reference form

\[
g_L(f)=\left\langle f,\log(1+D_L)f\right\rangle.
\]

If \(f\) is orthogonal to the first \(M\) sine modes, spectral calculus gives

\[
g_L(f)\ge
\log\left(1+\frac{\pi(M+1)}{2L}\right)\lVert f\rVert^2.
\]

## Bounded-remainder criterion

Suppose the interval archimedean form satisfies

\[
\Gamma_L(f,f)=g_L(f)+k_L(f,f),
\qquad
|k_L(f,f)|\le C_L\lVert f\rVert^2.
\]

Then on the same high-mode subspace,

\[
\Gamma_L(f,f)
\ge
\left[
\log\left(1+\frac{\pi(M+1)}{2L}\right)-C_L
\right]\lVert f\rVert^2.
\]

Combining a prime-sector norm bound \(C_{\rm prime}(L)\) gives a nonnegative tail whenever

\[

a_M:=
\log\left(1+\frac{\pi(M+1)}{2L}\right)
-C_L-C_{\rm prime}(L)
\ge0.
\]

Endpoint representers remain in the finite trial space.

## Finite-tail Schur completion

Let the finite block have coercivity \(m_M>0\), and let the finite-tail coupling norm be \(b_M\). The full form is nonnegative if

\[
b_M^2\le m_Ma_M.
\]

This condition is independent of tail positivity and becomes fragile when \(m_M\) is small.

## Strongest falsification attempt

A boundary remainder whose expectation on normalized high sine modes grows without bound cannot satisfy a fixed \(C_L\). The checker models the hostile residual \(-\log(n+1)\), which exactly cancels the reference growth and destroys every positive logarithmic reserve. Thus compactness of the embedding does not imply the required order-zero remainder.

## Disposition

The missing interval theorem is reduced to a single typed analytic object: an explicit bounded form remainder

\[
K_L=\Gamma_L-\log(1+D_L).
\]

If source analysis bounds \(\lVert K_L\rVert\), the high-mode Gårding estimate and mode threshold follow immediately. Without that bound, the periodic argument does not descend to the interval.

## Verification

- `research/voevodsky/checkers/check_interval_log_garding_remainder_criterion.py`
- `research/voevodsky/results/interval_log_garding_remainder_criterion.json`
