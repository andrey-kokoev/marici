# Quarter alpha2 is the centered image of three eighths log n

## Question

Which term in the quarter Mellin--Hankel determinant asymptotic is equivalent to \(\alpha_2=-3/16\)?

Let

\[
D_n=\det[(4(i+j)+3)!]_{i,j=0}^{n-1}.
\]

After restoring the variable scale,

\[
a_n^2=\frac{D_{n+1}D_{n-1}}{256D_n^2},
\]

so \(\log a_n^2\) is the centered second difference of \(\log D_n\), apart from the constant \(-\log256\).

If

\[
a_n=A n^4\left(1+rac{\alpha_2}{n^2}+O(n^{-3})\right),
\]

then

\[
\log a_n^2
=2\log A+8\log n+rac{2\alpha_2}{n^2}+O(n^{-3}).
\]

Since

\[
\Delta^2\log n=-\frac1{n^2}+O(n^{-4}),
\]

a term \(\gamma\log n\) in \(\log D_n\) contributes \(-\gamma/n^2\) to \(\log a_n^2\). Therefore

\[
\alpha_2=-\frac3{16}
\quad\Longleftrightarrow\quad
\gamma=rac38.
\]

## Disposition

Resolve the direct determinant target: the quarter-specific proof must establish a \((3/8)\log n\) term in the Mellin--Hankel free energy with centered remainder \(O(n^{-3})\).

The next leaf is `quarter-hankel-three-eighths-log`: derive that logarithmic coefficient from the factorial moment determinant or its Coulomb-gas/Riemann--Hilbert representation.

## Claim boundary

This is an exact equivalence, not a derivation of \(3/8\). A free-energy remainder without controlled centered differences is insufficient.
