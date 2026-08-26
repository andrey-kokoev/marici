# Finite spin-memory contour apparatus

## Apparatus

Fix five latitude values

\[
x_a=\cos\theta_a\in
\left\{-\frac23,-\frac13,0,\frac13,\frac23\right\},
\]

and nine equally spaced longitudes

\[
\phi_j=\frac{2\pi j}{9},\qquad 0\leq j<9.
\]

At each of the resulting 45 centers, place the positively oriented boundary
of the geodesic cap of angular radius

\[
\rho=\frac{\pi}{3}.
\]

Each port is the counter-orbiting-light time delay around that contour.
All contours have the same shape and radius; only their centers change.

## Exact rank theorem

For a spherical harmonic \(Y_{lm}\), Stokes' theorem and the Funk--Hecke
formula give a cap response proportional to

\[
\mu_l\,w_l(\rho)\,Y_{lm}(\theta_a,\phi_j),
\qquad
\mu_l=(l-1)l(l+1)(l+2),
\]

where

\[
w_l(\rho)=2\pi\int_{\cos\rho}^{1}P_l(x)\,dx.
\]

At \(\cos\rho=1/2\), the integrals before the common \(2\pi\) factor are

\[
\frac{3}{16},\qquad
\frac{3}{128},\qquad
-\frac{15}{256}
\]

for \(l=2,3,4\). None vanishes.

The nine-longitude discrete Fourier transform separates all azimuthal
characters \(m=-4,\ldots,4\), because no two differ by a nonzero multiple of
9. For fixed \(m\), the five latitude evaluations of
\(P_l^{|m|}(x_a)\) have rank equal to the number of admitted degrees

\[
l\in\{\max(2,|m|),\ldots,4\}.
\]

Summing the block ranks gives

\[
3+3+3+3+3+2+2+1+1=21,
\]

where the blocks are grouped by \(|m|\), equivalently

\[
3+2(3+3+2+1)=21.
\]

Therefore the 45-by-21 physical contour matrix has rank 21. It reconstructs
the complete magnetic \(l=2,3,4\) packet.

## What has and has not been explained

This construction removes the continuum idealization. It uses a finite,
uniform, reproducible geometry derived from the bandlimit:

- \(2L+1=9\) longitudes resolve azimuthal frequencies through \(L=4\);
- five latitudes provide a uniform interpolation set through degree four;
- one common nonexceptional cap radius preserves every admitted degree.

It is not minimal. Rank-nullity requires at least 21 scalar contours, while
this symmetric product apparatus uses 45. No claim is made that 45 is
hardware-optimal or that a 21-contour subfamily selected by row reduction has
source authority.

The construction is also not deletion-tolerant by theorem. Robustness under
missing ports, finite timing error, displaced centers, and unequal cap radii
requires a separate frame-bound calculation in the physical contour metric.

## Explanatory status

The finite apparatus establishes operational possibility without fitted
harmonic coefficient ports:

\[
\text{Bondi spin-memory effect}
\longrightarrow
\text{45 uniform cap contours}
\longrightarrow
\text{rank-21 low-mode readout}.
\]

The remaining Deutsch question is no longer whether finite recovery is
possible. It is which physical resource should be optimized: contour count,
symmetry, conditioning, erasure tolerance, or detector locality.
