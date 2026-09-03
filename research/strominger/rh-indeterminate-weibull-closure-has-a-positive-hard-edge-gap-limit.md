# The indeterminate Weibull closure has a positive hard-edge gap limit

## Question

Does the normalized hard-edge gap probability converge to a positive limit for fixed \(X\)?

Let \(\mathcal H\) be the closure of polynomials in the continuous Weibull space and \(P_n\uparrow P_{\mathcal H}\) the polynomial projections. Indeterminacy makes \(\mathcal H\) a reproducing-kernel space of entire functions, with kernel

\[
K_\infty(x,y)=\sum_{j\geq0}P_j(x)P_j(y).
\]

On the compact interval \(C=[0,X]\), bounded evaluation and kernel continuity give

\[
\operatorname{Tr}\mathsf K_C
=
\int_C K_\infty(x,x)d\nu(x)<\infty,
\]

where \(\mathsf K_C=\boldsymbol1_C P_{\mathcal H}\boldsymbol1_C\). Hence \(\mathsf K_C\) is a positive trace-class contraction.

It has no eigenvalue one. Indeed, an eigenvalue-one vector would lift to a nonzero member of \(\mathcal H\) supported in \(C\). Its entire representative would vanish almost everywhere on the open tail \((X,\infty)\), hence identically, a contradiction.

Therefore all eigenvalues satisfy \(0\leq\lambda_j<1\), with \(\sum_j\lambda_j<\infty\), and

\[
\det(I-\mathsf K_C)=
\prod_j(1-\lambda_j)>0.
\]

Local trace-class convergence of the increasing projection kernels gives

\[
\lim_{n\to\infty}rac{D_n^{\geq X}}{D_n}
=
\det(I-\mathsf K_C)>0.
\]

## Disposition

Prove positivity of the fixed-start limiting gap, conditional only on the established indeterminate polynomial-closure RKHS. The finite value near \(0.69642\) is consistent with this theorem but is not identified analytically.

The next leaf is `gap-fredholm-convergence-rate`: derive the \(1/n\) approach to this positive determinant.

## Claim boundary

The theorem is for each fixed \(X\). It gives neither moving-start uniformity nor a formula for the determinant or convergence rate.
