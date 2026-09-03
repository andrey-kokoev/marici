# A Jacobi n-minus-three correction is a Hankel-ratio one-over-n term

## Question

What growing-Hankel asymptotic would source the observed off-diagonal relative correction?

Let

\[
D_n=\det(\mu_{i+j})_{i,j=0}^{n-1},
\qquad
D_n^{(X)}=\det(\mu_{i+j}^{\geq X})_{i,j=0}^{n-1},
\]

and put

\[
L_n(X)=\log\frac{D_n^{(X)}}{D_n}.
\]

The monic norm identity gives

\[
\log\frac{a_n^{(X)}}{a_n}
=
\frac12\big[L_{n+1}(X)-2L_n(X)+L_{n-1}(X)\big].
\]

A measure-normalization change adds a linear function of \(n\) to \(L_n\), which the second difference annihilates.

If

\[
L_n(X)=\alpha_X n+\beta_X+\frac{\gamma_X}{n}+O_X(n^{-2}),
\]

then

\[
\log\frac{a_n^{(X)}}{a_n}
=
\frac{\gamma_X}{n^3}+O_X(n^{-4}).
\]

Thus the finite-grid constant near \(0.089\) at \(q=12\) is a diagnostic for \(\gamma_X\), not an entrywise moment coefficient.

## Disposition

Resolve the determinant-level reduction. The source theorem needed for the off-diagonal correction is a \(1/n\) term in the compact-truncation Hankel determinant ratio after arbitrary linear normalization is removed.

The next leaf is `hankel-ratio-one-over-n-test`: reconstruct finite second-difference invariants and test whether a common \(\gamma_X\) fits the exact coefficient grid.

## Claim boundary

This is an exact reduction plus a conditional asymptotic implication. It does not prove the determinant expansion or identify \(\gamma_X\) analytically.
