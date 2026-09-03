# The Laguerre Fredholm logarithm needs global Weibull bulk renormalization

## Question

Can the \(1/n\) compact-truncation coefficient be read directly from

\[
\log\det(I+(g_X-1)K_n^{\rm Lag})?
\]

No. This determinant compares two different global tail classes. For the Laguerre weight, the monic off-diagonal recurrence coefficient is

\[
a_n^{\rm Lag}=n.
\]

For the \(\beta=1/4\) Weibull weight, the exact finite diagnostic identifies

\[
a_n^{\rm Wei}\asymp c n^4.
\]

After the fixed dilation by \(L_X\), the relative recurrence scale therefore grows as

\[
\frac{a_n^{\rm Wei}/L_X}{a_n^{\rm Lag}}
asymp \frac{c}{L_X}n^3.
\]

By the determinant second-difference identity,

\[
\frac12\Delta^2\log
\frac{D_n[e^{-\Phi_X}]}{D_n[e^{-z}]}
=
\log\frac{a_n^{\rm Wei}/L_X}{a_n^{\rm Lag}},
\]

so the Fredholm logarithm contains a bulk term of order \(n^2\log n\). This dominates the compact-truncation \(1/n\) term.

## Required renormalization

The Laguerre interface determinant is an exact constructor, but its logarithm must first be renormalized by the global unshifted-Weibull determinant. Only the quotient

\[
\log D_n^{(X),\rm Wei}-\log D_n^{\rm Wei}
\]

cancels the common \(n^2\log n\) tail class and exposes the compact-deletion coefficient.

## Disposition

Reject direct extraction of \(\gamma_X\) from the unrenormalized Laguerre Fredholm logarithm. The next leaf is `renormalized-fredholm-cocycle`: construct a quotient or cocycle of the shifted and unshifted multiplicative determinants in which the Weibull bulk cancels exactly.

## Claim boundary

The bulk scaling uses the current finite \(n^4\) diagnostic as motivation; the need for common-tail renormalization is structural, while its full asymptotic coefficient remains unproved.
