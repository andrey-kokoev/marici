# The Centered Euler Generator Explains the Half-Offset

The theta frontier current is

\[
F=\frac1{2\pi}D(D+1)e^{-\pi\rho^2},
\qquad
D=\rho\frac{d}{d\rho}.
\]

Fourier transformation sends

\[
D\longmapsto-D-1.
\]

Therefore

\[
K=D+\frac12
\]

is the unique centered generator satisfying \(K\mapsto-K\), and

\[
D(D+1)=K^2-\frac14.
\]

Under Mellin transform this operator has symbol

\[
s(s-1)
=
\left(s-\frac12\right)^2-\frac14.
\]

Thus the critical half-offset is the Haar correction that makes the two
dilation orientations exact Fourier–Tate opposites. The quarter offset is the
quadratic scalar left by folding them through \(K\mapsto-K\).

This explains the seam but does not yet confine zeros to it.

Research artifact:
research/grothendieck/the-centered-euler-generator-explains-the-half-offset.md
