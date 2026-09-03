# The full interface is an exact multiplicative Fredholm determinant

## Question

Can the Laguerre--Weibull interface be retained without splitting particles or expanding cross pairs?

After the dilation \(y=L_Xz\), write

\[
e^{-\Phi_X(z)}=g_X(z)e^{-z},
\qquad
g_X(z)=e^{z-\Phi_X(z)}.
\]

Let \(K_n^{\rm Lag}\) be the rank-\(n\) Laguerre projection. The orthogonal-polynomial ensemble multiplicative-functional identity gives the exact finite-rank formula

\[
\frac{D_n[e^{-\Phi_X}]}{D_n[e^{-z}]}
=
\mathbb E_{\rm Lag}
\left[\prod_{i=1}^n g_X(z_i)\right]
=
\det\left(I+(g_X-1)K_n^{\rm Lag}\right).
\]

Equivalently, in the Laguerre polynomial basis this is the determinant of

\[
\left[
\int_0^\infty P_i(z)P_j(z)g_X(z)e^{-z}dz
\right]_{i,j=0}^{n-1}.
\]

This identity retains local, transition, and far particles in one operator. No occupancy selection or independent regional minimization occurs.

## Nonperturbative boundary

Concavity gives \(\Phi_X(z)\leq z\), so \(g_X\geq1\). In the far region, \(z-\Phi_X(z)\) is not uniformly small and grows without bound. Therefore expanding the Fredholm determinant in powers of \(g_X-1\) is not authorized by the local overlap estimate.

## Disposition

Construct the exact nonperturbative interface determinant. The next leaf is `fredholm-log-determinant-asymptotic`: extract the linear, constant, and \(1/n\) terms of its logarithm while retaining the unbounded far multiplier.

## Claim boundary

The identity is finite-rank and exact. It supplies no trace-norm smallness, limiting determinant, or asymptotic coefficient.
