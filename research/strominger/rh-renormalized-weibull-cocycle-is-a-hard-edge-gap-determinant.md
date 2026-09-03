# The renormalized Weibull cocycle is a hard-edge gap determinant

## Question

Can the shifted/unshifted common-tail quotient be written as one exact operator without a Laguerre bulk term?

Let \(D_n\) be the Hankel determinant for the full Weibull measure on \([0,\infty)\), and \(D_n^{\geq X}\) the determinant for its restriction to \([X,\infty)\). Andréief's identity identifies their ratio with a gap probability in the full size-\(n\) Weibull polynomial ensemble:

\[
\frac{D_n^{\geq X}}{D_n}
=
\Pr\{x_1,\ldots,x_n\geq X\}.
\]

If \(K_n^{\rm Wei}\) is the full Weibull projection kernel, the determinantal gap identity gives

\[
\frac{D_n^{\geq X}}{D_n}
=
\det\left(I-oldsymbol 1_{[0,X]}
K_n^{\rm Wei}oldsymbol 1_{[0,X]}\right).
\]

This is the required renormalized Fredholm cocycle. Both numerator and denominator have the same far Weibull tail, so the \(n^2\log n\) bulk cancels before asymptotic analysis.

Translation to \(y=x-X\) and normalization of the restricted measure add explicit dilation or linear-in-\(n\) determinant factors. They do not change the compact-deletion gap determinant once those conventions are tracked.

## Disposition

Construct the exact common-tail cocycle. The observed expansion

\[
\log(D_n^{\geq X}/D_n)
=\alpha_Xn+\beta_X+\gamma_X/n+\cdots
\]

is now typed as a hard-edge Weibull gap asymptotic. The next leaf is `weibull-hard-edge-gap-asymptotic`.

## Claim boundary

The Fredholm identity is exact. No large-\(n\) gap theorem, trace-class limit, or formula for \(\gamma_X\) is supplied.
