# Quarter staircase shift curvature is a product of LU-pivot curvatures

## Question

Can the global common-shift ratio be reduced to a local sequence of LU pivots?

Define

\[
d_n(\mathbf s)=\frac{S_n(\mathbf s)}{S_{n-1}(\mathbf s)}
\]

and its common-shift curvature

\[
c_n(\mathbf s)=
\frac{d_n(\mathbf s+1)^2}
{d_n(\mathbf s)d_n(\mathbf s+2)}.
\]

Telescoping gives the exact product

\[
R_m(\mathbf s)=
\frac{S_m(\mathbf s+1)^2}
{S_m(\mathbf s)S_m(\mathbf s+2)}
=\prod_{j=1}^m c_j(\mathbf s).
\]

Dividing the vector-shifted condensation recurrence by
\(S_{n-1}(\mathbf s)S_{n-1}(\mathbf s+2)\) also gives

\[
\frac{d_n(\mathbf s)}{d_{n-1}(\mathbf s+2)}
=q_{n-1}(\mathbf s)-q_0(\mathbf s)R_{n-1}(\mathbf s).
\]

Thus the shift-ratio problem is a closed pivot/product system rather than a difference of large determinants.

If

\[
c_n(\mathbf s_0)=1+\frac2n+O(n^{-2}),
\]

then \(R_m\) has the required power \(m^2\). The amplitude target becomes

\[
\lim_{m\to\infty}
\frac1{m^2}\prod_{j=1}^m c_j(\mathbf s_0)
=rac{104}{1575}.
\]

## Disposition

Resolve the exact LU-pivot reduction. The next leaf is `quarter-pivot-curvature-two-over-n`: prove the local expansion \(c_n=1+2/n+O(n^{-2})\) from the closed system. Its summable remainder must then yield the amplitude product.

## Claim boundary

The exact product does not prove convergence. An \(O(n^{-2})\) local remainder controls the amplitude only when its coefficient sequence is summable with a justified product limit.
