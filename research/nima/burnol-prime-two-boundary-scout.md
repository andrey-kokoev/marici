# Burnol's prime-two boundary is pointwise indefinite but support-positive in the first Galerkin scout

Status: numerical reconnaissance; no continuum positivity claim

## Exact boundary problem

At the support boundary \(c=\sqrt2\), Burnol's proof exposes the multiplier

\[
\alpha(\tau)=
\frac{8\sqrt2\cos(\tau\log2)}{1+4\tau^2}
-\log\pi
+\Re\psi\!\left(\frac14+\frac{i\tau}{2}\right).
\]

A high-precision scout finds

\[
\min_{0\le\tau\le20}\alpha(\tau)
\approx-1.04068425705481
\]

at

\[
\tau\approx2.06499924367117.
\]

The positive-axis crossings are approximately \(0.89044917\) and
\(6.40634873\). Thus Burnol's argument cannot reach \(c=\sqrt2\) by asserting
pointwise nonnegativity of \(\alpha\).

## Support-constrained compression

The relevant test functions are not arbitrary Fourier densities. Their
logarithmic representatives are confined to an interval of length \(\log2\).
We therefore compressed the Fourier multiplier to that interval and computed
its lowest Galerkin eigenvalues using a unitary padded FFT.

Across spatial resolutions 128, 256, and 512 and padding factors through 128,
the lowest eigenvalue remained positive. The best frequency-resolution pair
at 256 support points gave

\[
\lambda_1\approx0.00132501183043,
\qquad
\lambda_2\approx0.0727802744605,
\qquad
\lambda_3\approx0.660360424836.
\]

The 512-point scout with padding 64 gives

\[
\lambda_1\approx0.00132758094046.
\]

## Shape of the nearly-null mode

The lowest mode is even to numerical precision and has no internal zero. Its
correlation with the first Dirichlet mode is

\[
\left|\left\langle v_1,
\cos\frac{\pi x}{\log2}\right\rangle\right|
\approx0.9992665277.
\]

It places about \(69.6\%\) of its Fourier mass inside the negative multiplier
band. The energy balance is nearly exact:

\[
E_-\approx-0.4663343600,
\qquad
E_+\approx0.4676619409.
\]

The bare cosine has Rayleigh quotient \(0.0026545988\), so it captures the
shape but not the sharp margin. Even Dirichlet subspaces of dimensions
\(1,2,4,8,16,32\) give lowest values

\[
0.00265460, 0.00159014, 0.00157656,
0.00150736, 0.00143449, 0.00138586.
\]

Their slow convergence reveals a boundary layer. The endpoint-to-peak sample
ratio decreases from \(0.0441\) to \(0.0382\) to \(0.0344\) under successive
spatial doubling, rather than behaving like a fixed smooth cosine profile.

## Interpretation

The boundary is pointwise indefinite but apparently positive after imposing
the source support constraint. The very small first eigenvalue makes this a
near-critical uncertainty-principle problem, not broad positivity.

This is evidence for the prime-two contraction, not a proof. A theorem now
needs a directed lower bound for the compressed operator, or an analytic
**logarithmic uncertainty inequality** showing that no \(\log2\)-supported
function can place enough Fourier mass in the negative band of \(\alpha\).

The slow boundary layer makes a small fixed polynomial basis unattractive.
Burnol's native conductor-operator language, \(\log|x|+\log|D|\), is better
matched to the asymptotic symbol and should be the next analytic comparison.

The next finite work is to compare the compressed boundary operator with the
known conductor operator or a Sonine-space restriction, isolate the compact
prime-two correction, and seek a certified lower bound on the resulting
ground-state energy.

## Exact finite-rank reduction

The rational prime-two/endpoint part of \(\alpha\) has an elementary inverse
Fourier transform. With the convention \(d\tau/(2\pi)\),

\[
\frac{8\sqrt2\cos(\tau\log2)}{1+4\tau^2}
\longleftrightarrow
\sqrt2\left(e^{-|r-\log2|/2}+e^{-|r+\log2|/2}\right).
\]

For \(|r|\le\log2\), which is exactly the difference range of the support
interval, this simplifies to

\[
2\cosh(r/2).
\]

Hence the compressed boundary operator is exactly rank two:

\[
B
=2|c\rangle\langle c|-2|s\rangle\langle s|,
\qquad
c(x)=\cosh(x/2),\quad s(x)=\sinh(x/2).
\]

The FFT action agrees with this real-space formula to about \(9\times10^{-10}\)
in the current padding census.

Let \(A_\infty\) be the compression of

\[
-\log\pi+\Re\psi\!\left(\frac14+\frac{i\tau}{2}\right).
\]

Its first six sampled eigenvalues are

\[
-1.28588046, 0.08480089, 0.58205825,
0.92724298, 1.17515436, 1.37844630,
\]

with alternating even/odd parity. Thus the observed archimedean index is one,
carried by the even sector. Standard rank-one inertia reduces positivity to
two scalar resolvent gates:

\[
1+2\langle c,A_\infty^{-1}c\rangle\le0
\quad\text{(even)},
\]

\[
2\langle s,A_\infty^{-1}s\rangle\le1
\quad\text{(odd)}.
\]

At the finest current resolution these evaluate to approximately

\[
-0.00119900,\qquad 0.14115981.
\]

The odd gate has wide margin. The prime-two boundary theorem is therefore
concentrated almost entirely in the near-critical even secular inequality,
together with a proof that \(A_\infty\) has index one on the support interval.

## Exact real-space conductor form

The digamma identity gives

\[
h_\infty(\tau)
=h_\infty(0)
+\int_0^\infty
\frac{e^{r/2}}{\sinh r}
\bigl(1-\cos(\tau r)\bigr)\,dr,
\]

where

\[
h_\infty(0)
=-\log\pi+\psi(1/4)
=-\log\pi-\gamma-\frac\pi2-3\log2.
\]

For a zero-extended function supported on an interval \(I\) of length
\(L=\log2\), Parseval converts this into

\[
\begin{aligned}
\langle f,A_\infty f\rangle
={}&C_L\|f\|^2\\
&+\frac12\int_0^L
\frac{e^{r/2}}{\sinh r}
\int_{\mathbb R}|f(x+r)-f(x)|^2\,dx\,dr,
\end{aligned}
\]

with

\[
C_L=h_\infty(0)+
\int_L^\infty\frac{e^{r/2}}{\sinh r}\,dr
\approx-2.37847682784580.
\]

Thus the archimedean operator is an explicit positive logarithmic difference
energy minus a scalar mass. Its index-one theorem is a nonlocal Poincaré
theorem, not an opaque spectral assertion.

For the normalized trial function

\[
f_0(x)=\sqrt{2/L}\cos(\pi x/L),
\]

the autocorrelation for \(0\le r\le L\) is exactly

\[
R_0(r)=\left(1-\frac rL\right)\cos\frac{\pi r}{L}
+\frac1\pi\sin\frac{\pi r}{L}.
\]

Direct 80-digit quadrature gives

\[
\langle f_0,A_\infty f_0\rangle
\approx-1.12744036888818,
\]

and

\[
2|\langle\cosh(x/2),f_0\rangle|^2
\approx1.13009549396338.
\]

Their sum is

\[
\boxed{0.00265512507519669>0.}
\]

This independently confirms the FFT normalization. The remaining theorem is
a rank-one-strengthened logarithmic Poincaré inequality at the arithmetic
width \(L=\log2\), extending this balance from the cosine trial mode to every
supported function.

The universal lower comparison

\[
\frac{e^{r/2}}{\sinh r}\ge\frac1r
\]

is too coarse. On the same cosine it supplies difference energy only

\[
1.05878776646842,
\]

and would yield the negative total bound

\[
-0.189593567414004.
\]

Therefore the prospective theorem is not generic support uncertainty for the
logarithmic Laplacian. It must retain the finer completed archimedean weight;
that source coefficient carries essential positivity information.
