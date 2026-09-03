# Gamma log-curvature overwhelms prime indefiniteness in the small-heat rank-two limit

## Question

How can the completed rank-two form remain positive when each small-heat prime atom has negative rank-two curvature?

## Claim boundary

In the confluent mesh limit, the gamma leading term has a positive rank-two curvature margin of order `t^-5 log(1/t)^2`, while every fixed prime atom is exponentially small. The completed determinant is therefore positive at sufficiently small heat. This explains the coupling mechanism locally; it does not control non-small heat or rank growth.

## Confluent determinant

Let

\[
g(t)=-H'(t).
\]

For the endpoint-free rank-two Bernstein block,

\[
\begin{pmatrix}
\Delta_hH&\Delta_h^2H\\
\Delta_h^2H&\Delta_h^3H
\end{pmatrix},
\]

the determinant satisfies

\[
\det=h^4\bigl(g g''-(g')^2\bigr)+O(h^5)
=h^4g^2(\log g)''+O(h^5).
\]

Thus the confluent rank-two condition is log-convexity of `-H'`.

## Gamma leading margin

Put

\[
L=\log(1/t),
\qquad
H_0(t)=A t^{-1/2}L,
\qquad
A=\frac1{8\sqrt\pi}.
\]

Then

\[
g_0(t)=-H_0'(t)
=\frac A2 t^{-3/2}(L+2),
\]

and direct differentiation gives

\[
(\log g_0)''
=\frac1{t^2}
\left[
\frac32+rac1{L+2}-\frac1{(L+2)^2}
\right]>0.
\]

Consequently

\[
g_0g_0''-(g_0')^2
\sim \frac{3}{512\pi}t^{-5}L^2.
\]

This is a strict positive margin, not merely positive diagonal data.

## Prime comparison

For a prime displacement `a=log n`, every fixed derivative of

\[
t^{-1/2}e^{-a^2/(4t)}
\]

is a polynomial in `t^-1` times the same exponential. The full differentiated prime sum is bounded, at each fixed derivative order, by

\[
C t^{-M}e^{-(\log2)^2/(4t)}.
\]

The endpoint derivatives are bounded. Therefore their contributions to `g`, `g'`, and `g''`, and hence to the rank-two curvature, are lower order than the positive gamma margin as `t` tends to zero. The negative determinant of an isolated prime atom is overwhelmed by cross-sector terms involving the gamma entries.

## Interpretation

Sectorwise determinants are nonlinear and do not add. Writing

\[
M=M_\Gamma+M_P+M_E
\]

produces determinant cross terms that are absent from `det M_Gamma+det M_P+det M_E`. The positive gamma curvature controls precisely those couplings near the small-heat boundary.

## Strongest falsification attempt

The exponential prime suppression holds for fixed derivative order. When rank grows with `1/sqrt(t)`, Laguerre derivative order grows and the fixed-order estimate is no longer uniform. The turning-point regime remains untouched.

## Disposition

Use the completed log-curvature `(-H')^2 (log(-H'))''`, not sectorwise rank-two determinants, as the scalar confluent diagnostic. Its first unresolved regime is coupled growth of derivative order with inverse heat.