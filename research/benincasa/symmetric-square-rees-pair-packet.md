# Symmetric-square Rees packet for conditioned pairs

At a degenerating conditioning variance `b`, resolve each covariance normal as

\[
c_i=\sqrt b\,u_i.
\]

Then every conditioned pair coefficient is

\[
\Xi_{ij}=\frac{c_ic_j}{b}=u_iu_j.
\]

The matrix `Xi` is symmetric, positive semidefinite, and rank at most one.  All
its `2x2` minors vanish.  The deck transformation associated with the square
root acts by `u -> -u`, while `Xi` is invariant.

Thus the many labelled pair coefficients are not independent exceptional
extensions.  They are the labelled components of `Sym^2(u)`.
