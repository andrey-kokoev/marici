# Stopped Dirichlet repair is Volterra-positive at two and fails universally at eight

Author: `marici.Nima`

## 1. Exact stopped-packet identity

Let

\[
D_v(z)=\sum_{n\le e^v}\chi_n(z),
\qquad
\chi_n(z)=n^{-1/2-iz}.
\]

As a right-continuous step function, its Stieltjes derivative is

\[
dD_v(z)=\sum_{n\ge2}\chi_n(z)\,\delta_{\log n}(dv).
\]

The logarithmic repair packet is

\[
R_v(z)=i\partial_zD_v(z)
=\sum_{n\le e^v}(\log n)\chi_n(z).
\]

Stieltjes integration by parts gives the exact identity

\[
\boxed{
R_v(z)=\int_{[0,v]}q\,dD_q(z)
=vD_v(z)-\int_0^vD_q(z)\,dq.}
\]

Consequently the Clark fold and logarithmic repair do not remain separate:

\[
\boxed{
(1-av)D_v+aR_v
=D_v-a\int_0^vD_q\,dq.}
\]

If

\[
(Vf)(v)=\int_0^vf(q)\,dq,
\]

the repaired stopped packet is (T_af=(I-aV)f).

This identity uses finite stopped packets only.  It does not use (Xi),
zero locations, Herglotz positivity, or the Weil criterion.

## 2. Exact Hermitian part on a finite horizon

On (L^2(0,L;dv)),

\[
(V+V^*)f(v)=\int_0^Lf(q)\,dq.
\]

Therefore

\[
\boxed{
H_{a,L}:=\frac{T_a+T_a^*}{2}
=I-\frac a2|1\rangle\langle1|.}
\]

In the orthogonal decomposition into the normalized constant direction
(L^{-1/2}1) and any normalized mean-zero direction, the first finite
matrix is

\[
\boxed{
\begin{pmatrix}
1-aL/2&0\\
0&1
\end{pmatrix}.}
\]

Thus (H_{a,L}\ge0) exactly when

\[
aL\le2.
\]

## 3. Prime-two gate

For the canonical Clark normalization (a=1) and first arithmetic horizon
(L=log2),

\[
\lambda_{\rm const}
=1-\frac{\log2}{2}
=0.6534264097\ldots>0.
\]

So the first (N=2) seam passes with a large exact margin.  This is a genuine
finite success of the stopped-packet repair, but it is universal: no theta
or Poisson property entered.

## 4. Smallest universal finite falsifier

For an integer stopping horizon (L=log N), the constant eigenvalue is

\[
1-\frac12\log N.
\]

Since

\[
\log7<2<\log8,
\]

the first integer horizon at which it becomes negative is (N=8):

\[
\boxed{
1-\frac12\log8
=-0.0397207708\ldots<0.}
\]

Equivalently, the source-local matrix

\[
\boxed{
M_8=
\begin{pmatrix}
1-\frac12\log8&0\\
0&1
\end{pmatrix}}
\]

has negative determinant.

This falsifies every proposed global orientation law derived only from:

1. the stopped Dirichlet jump structure;
2. the logarithmic derivative repair;
3. the Volterra summation-by-parts identity; and
4. Hermitian polarization in the unweighted packet coordinate.

## 5. What the falsifier does not say

The actual theta construction carries the rapidly decaying primitive weight,
reciprocal doubling, and a Poisson correspondence.  These can change the
relevant Hilbert metric and add a boundary term.  Therefore (M_8) does not
disprove a theta-specific weighted inequality.

It proves that such an inequality cannot follow from stopped-packet algebra
alone.  Any successful estimate must use a property that rejects hostile
positive primitives satisfying the same translation, seam, and Volterra
identities.

## 6. Consequence for (C_Y)

The preferred route gives a sharp disposition:

- the (N=2) seam is locally positive;
- universal stopped-packet monotonicity fails already at (N=8);
- the exact positive rank-one seam current is insufficient;
- no independent inequality for the coupled (C_Y) follows.

The only admissible continuation is a theta-specific primal--dual Poisson
law on the weighted doubled seam blocks.  Unless that law contributes a
new positive boundary term or changes the metric before scalar projection,
the Lakatos block remains closed.
