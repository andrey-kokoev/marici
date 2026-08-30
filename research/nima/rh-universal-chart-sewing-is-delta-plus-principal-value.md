# RH universal chart sewing is delta plus principal value

## Question

Can the universal Fourier part of the two-chart comoving sewing be constructed
before solving arithmetic completion continuity?

## Exact chart decomposition

Away from the Heaviside convention at the origin, the two comoving profiles
satisfy

\[
T=a_-+a_+=-1,
\qquad
O=a_--a_+=\operatorname{sgn}(u).
\]

Hence

\[
a_-=\frac{T+O}{2},
\qquad
a_+=\frac{T-O}{2}.
\]

With Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(u)e^{-2\pi i u\xi}\,du,
\]

the distributional transforms are

\[
\widehat T=-\delta_0,
\qquad
\widehat O=\operatorname{pv}\frac{1}{\pi i\xi}.
\]

Therefore

\[
\widehat a_-
=-\frac12\delta_0
+\frac12\operatorname{pv}\frac{1}{\pi i\xi},
\]

\[
\widehat a_+
=-\frac12\delta_0
-\frac12\operatorname{pv}\frac{1}{\pi i\xi}.
\]

This is the exact universal sewing of the two front charts.

## Parity and faithfulness

Reflection fixes the delta channel and reverses the principal-value channel.
The chart-to-boundary coefficient map is

\[
\begin{pmatrix}
d\\p
\end{pmatrix}
=
\begin{pmatrix}
-1/2&-1/2\\
1/2&-1/2
\end{pmatrix}
\begin{pmatrix}
c_-\\c_+
\end{pmatrix},
\]

where (d) is the delta coefficient and (p) the principal-value
coefficient. Its determinant is (1/2), so the full distributional sewing is
faithful on the two chart directions.

Projecting to delta alone has rank one and kills the anti-diagonal orientation
direction. Thus Fourier transform is not the lossy step. Delta-only scalar
compression is.

## Crossing with arithmetic grades

The same universal matrix acts independently on the primitive exponential and
square tempered coefficient grades. Algebraically this gives a block-diagonal
four-lane map with determinant (1/4):

```text
primitive inner/outer → primitive delta/principal-value
square inner/outer    → square delta/principal-value
```

This establishes the finite and distributional form of the sewing. It does
not prove that the primitive coefficient measure acts continuously on the
principal-value boundary after infinite prime aggregation.

## Refined analytic frontier

The remaining theorem is no longer an unspecified Fourier--Tate comparison.
It is the continuity of two arithmetic coefficient systems against two fixed
universal boundary distributions:

1. primitive exponential coefficients against delta and principal value;
2. square tempered coefficients against delta and principal value.

Relative archimedean sewing must then show which combinations are defined,
which require finite-part pairing, and whether the odd principal-value channel
survives completion with a nonzero margin.

## Falsifiers

- A proposed Fourier sewing that maps both charts to the same delta coefficient
  is rank one and erases orientation.
- A reflection law fixing the principal-value channel has the wrong character.
- A scalar finite part that cancels principal-value coefficients between
  arithmetic grades without a cross-grade pairing manufactures continuity.
- A cutoff-dependent test space does not define the required completion
  constructor.

## Claim boundary

This packet constructs the universal two-chart distributional transform and
its finite coefficient matrix. It does not establish arithmetic continuity,
relative finite-part sewing, chamber preservation, zero confinement, or RH.

## Disposition

Universal chart sewing is closed and faithful as delta plus principal value.
The live obstruction has moved entirely to arithmetic coefficient continuity
and the lawful relative pairing of these boundary distributions.

