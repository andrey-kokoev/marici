# Cubic evolution of a finite non-Gaussian density mixture

Start from a physical Gaussian density state and mix two `Q`-displacements:

\[
\mu_1=2d,
\qquad p_1=\frac13,
\qquad
\mu_2=-d,
\qquad p_2=\frac23.
\]

The mixture is centered and density-representable.  If the common within-state
`Q` variance is `a`, then

\[
A=a+2d^2,
\qquad
\kappa_3(Q)=2d^3,
\qquad
\kappa_4(Q)=-6d^4.
\]

For the cubic shear, put `D=1+2aty`.  The complete generating germ is

\[
M(x,y)=e^{by^2/2+tAy}D^{-1/2}
\sum_{j=1}^2p_j
\exp\!\left(
\frac{ax^2+2\mu_jx-2ty\mu_j^2}{2D}
\right).
\]

Thus the Gaussian rational/logarithmic generator acquires one finite
log-sum-exp factor.  The first cubic third-cumulant response is

\[
\kappa_{QQ\Pi}
=-t\bigl(2A^2+\kappa_4(Q)\bigr),
\]

so a standalone input `kappa_3` is not dynamically closed.
