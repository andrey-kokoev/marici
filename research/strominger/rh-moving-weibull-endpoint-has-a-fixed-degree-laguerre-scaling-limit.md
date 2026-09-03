# The moving Weibull endpoint has a fixed-degree Laguerre scaling limit

## Question

What does translation and dilation actually prove about the shifted endpoint kernel as the tail start \(X=\log q\) diverges?

## Scaling

For \(0<\beta<1\), put

\[
L_X=\frac{X^{1-\beta}}{2a\beta},\qquad y=L_Xz.
\]

After removing the constant factor \(e^{-2aX^\beta}\), the shifted weight has exponent

\[
\Phi_X(z)=2a\big[(X+L_Xz)^\beta-X^\beta\big].
\]

For fixed \(z\), Taylor expansion at \(X\) gives

\[
\Phi_X(z)
=z-\frac{1-\beta}{4a\beta}X^{-\beta}z^2
+O(X^{-2\beta}z^3).
\]

Thus the rescaled weight converges locally to \(e^{-z}\), and the norm carries the Jacobian \(L_X\).

## Fixed-degree consequence

On every fixed polynomial-degree space, moment matrices converge after the corresponding diagonal basis rescaling to the Laguerre moment matrix. Hence the normalized degree-\(K\) endpoint kernel satisfies

\[
K_{X,K}^{\rm norm}(0,0)
\sim \frac{K+1}{L_X}
=2a\beta(K+1)X^{\beta-1}.
\]

Restoring the quadrature endpoint coefficient gives

\[
\eta_{q,K}^{\rm end}
\sim
\frac{2a\beta(K+1)}{q(\log q)^{1-\beta}}
\]

for each fixed \(K\).

## Uniformity obstruction

The limiting Laguerre endpoint kernel grows as \(K+1\). Therefore this scaling theorem is not uniform in degree. It proves the fixed-degree decay seen in the grids but supplies no estimate for

\[
\sup_K\eta_{q,K}^{\rm end}.
\]

A uniform argument must use the far Weibull tail, outside this local Laguerre scaling window, because that tail is what changes the moment problem from determinate to indeterminate.

## Disposition

Resolve `translated-kernel-scaling` at fixed degree. Do not promote it to the moving endpoint-kernel cap. The next leaf is a two-region kernel estimate retaining both the Laguerre window and the far subexponential tail.
