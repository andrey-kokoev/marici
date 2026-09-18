# The completed theta autocorrelation is the inverse Mellin square of Xi

Use the completed Riemann function

$$
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
$$

From

$$
K(s)=\frac{s(1-s)}{\sqrt\pi}
\Gamma\left(1+\frac s2\right)
\Gamma\left(1+\frac{1-s}{2}\right),
$$

apply the gamma recurrence twice:

$$
K(s)=
\frac{s^2(1-s)^2}{4\sqrt\pi}
\Gamma(s/2)\Gamma((1-s)/2).
$$

Therefore

$$
K(s)\zeta(s)\zeta(1-s)
=\xi(s)\xi(1-s).
$$

By the functional equation,

$$
\xi(1-s)=\xi(s),
$$

so

$$
\boxed{
K(s)\zeta(s)\zeta(1-s)=\xi(s)^2.
}
$$

Hence the unregulated Barnes expression collapses formally to

$$
A_\Phi(t)
=\frac{e^{t/2}}{2\pi i}
\int_{(c)}\xi(s)^2e^{-ts}\,ds,
$$

with the contour interpreted in the source-ordered/completed sense established before interchange.

The apparent poles of the separate zeta factors at `s=0,1` are removable: they are cancelled exactly by the completion differential encoded in `K(s)`. There is no residual zeta-pole anomaly in the fully assembled source kernel.

This is the sought global arithmetic assembly at the scalar autocorrelation level: primitive, square, connected, and archimedean factors recombine into the square of the completed Xi section. It is a two-copy statement, as required by polarization.

What remains is the typed lift: prove that the pair-to-Euler cyclic trace and Wronskian/Haar ports realize this scalar identity before trace, with seam and determinant-line labels retained.

Status: scalar completed two-height forcing kernel assembled exactly as an inverse Mellin transform of `xi^2`; typed operator lift remains open.
