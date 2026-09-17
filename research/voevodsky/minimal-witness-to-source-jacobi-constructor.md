# Minimal Loewner witnesses reduce exactly to the source-moment Jacobi constructor

The minimal-witness Schur obstruction and the prior order-two moment program
are not separate routes.

Fix `x0>1/4` and define

\[
q_k(x_0)=\frac{(-1)^kH^{(k+1)}(x_0)}{(k+1)!}.
\]

If the three infinite matrix families

\[
(q_{i+j})\succeq0,\qquad
(q_{i+j+1})\succeq0,\qquad
\left(\frac{q_{i+j}}{x_0}-q_{i+j+1}\right)\succeq0
\]

hold, the polynomial GNS construction gives multiplication by `z` as a
positive contraction

\[
0\le Z_{x_0}\le x_0^{-1}I.
\]

Set

\[
A=Z_{x_0}^{-1}-(x_0-1/4)I\ge1/4.
\]

The resolvent feature vectors

\[
r_x=(x-1/4+A)^{-1}\Omega
\]

then satisfy

\[
\langle r_x,r_y\rangle
=\frac{H(x)-H(y)}{x-y}.
\]

Consequently every proposed new node is literally a vector in the same GNS
space. Its cross-inner-products form the Schur column `b`, and its squared
norm is the diagonal `d`. Therefore

\[
b\in\operatorname{ran}A_{\rm old},
\qquad d-b^TA_{\rm old}^{\dagger}b\ge0.
\]

This is exactly the negation of both minimal-witness failure modes. The
all-rank impossibility proof is therefore reduced to positivity and support
localization of the three source moment families; no separate classification
of extremal negative node configurations is needed.

The derivative identity

\[
\partial_xq_k(x)=-(k+2)q_{k+1}(x)
\]

supplies resolvent covariance between base points. Since each fixed-base
moment problem has compact support `[0,1/x]`, it is determinate. Thus, once
the three cones hold at every base point, the resulting Jacobi models are
forced to be coordinate presentations of one base-point-independent
resolvent operator rather than independently fitted spectra.

## Exact remaining proof obligation

It is enough to derive, from the labelled completed theta source, for every
finite polynomial `p`,

\[
\sum_{i,j}\bar p_i p_jq_{i+j}(x)\ge0,
\]

\[
\sum_{i,j}\bar p_i p_jq_{i+j+1}(x)\ge0,
\]

and

\[
\sum_{i,j}\bar p_i p_j
\left(\frac{q_{i+j}(x)}x-q_{i+j+1}(x)\right)\ge0.
\]

The first two establish a positive Stieltjes coordinate; the third enforces
the lower spectral edge `A>=1/4`. Existing finite Hankel tests and Gaussian
reconstructions are approximations to these three quantified inequalities,
not additional assumptions.

Free and scalar-density differential operators cannot prove these forms:
the former has the wrong measure class and the latter has the wrong spectral
locations. Any source proof of the quadratic forms must preserve modular
labels through summation, convolution, or a matrix-valued sewing operation.
