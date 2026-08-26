# Spin-memory contour cospark attack

## Question

The leverage theorem proves that every two deleted contours preserve the
21-dimensional magnetic packet. It does not identify the first deletion set
that actually destroys faithfulness. That threshold is controlled by the
cospark of the 45-by-21 contour matrix: the smallest support of a nonzero
measurement vector.

## Exact hostile packet

Consider the real \(m=\pm1\) packet

\[
F(z,\phi)=
\left(P_4^1(z)-\frac5{54}P_2^1(z)\right)\sin\phi.
\]

The cap and curvature weights are nonzero and diagonal in degree, so the
corresponding source coefficients can be rescaled to produce this measured
packet without changing its zero set.

On the five apparatus latitudes, the radial factor vanishes exactly at

\[
z=-\frac23,\quad 0,\quad \frac23.
\]

Thus three complete rings, comprising 27 ports, are dark. On each surviving
ring, \(\sin(2\pi j/9)\) vanishes only at \(j=0\), because the longitude count
is odd. Two additional ports are dark. The packet therefore has

\[
45-27-2=16
\]

nonzero contour readings.

Deleting precisely those 16 ports leaves a nonzero magnetic state invisible.
Consequently the apparatus cannot tolerate every set of 16 deletions, and its
universal erasure tolerance is at most 15.

## Why this hostile is structural

Exact latitude-block enumeration shows:

- no nonzero \(l=2,3,4\) packet can vanish identically on four of the five
  latitude rings;
- only two triples of dark rings are possible;
- for the outer-ring/equator triple, the surviving harmonic sector is exactly
  \(|m|=1\).

The 16-support state is therefore a product-geometry cocircuit, not a small
singular value or a preferred-minor accident. Its three radial zeros consume
the available degree freedom, while the odd azimuthal grid permits one more
sampled zero.

## Current exact bracket

Combining this hostile with the leverage theorem gives

\[
2\leq e_{\mathrm{universal}}\leq15.
\]

Equivalently, the cospark \(d\) satisfies

\[
3\leq d\leq16,
\qquad e_{\mathrm{universal}}=d-1.
\]

The upper endpoint is an exact construction. Equality \(d=16\) is not yet a
theorem: packets with fewer than three completely dark rings could in
principle have smaller total support through correlated partial zeros. The
next proof must rule those out or exhibit a smaller cocircuit.
