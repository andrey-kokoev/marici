# The prime-square countercurrent renormalizes the canonical boundary volume

## Scope correction

The local valuation area is

\[
v_p=1-p^{-1}.
\]

Its divergent logarithmic term is \(p^{-1}\).  Since the primitive local
amplitude has size \(p^{-1/2}\), this is the \(k=2\) prime-square channel.
It is not the \(k=1\) primitive channel.

The distinction is structural:

- the primitive current carries odd coorientation and distinguishes the sign
  of the boundary bivector;
- the prime-square current controls the logarithmic collapse of its scalar
  determinant volume.

## Exact relative volume

At a finite prime cutoff \(X\), define

\[
V_X=\prod_{p\le X}(1-p^{-1})
\]

and retain the square countercurrent before completion:

\[
R_X
=
V_X\exp\left(\sum_{p\le X}p^{-1}\right).
\]

Then

\[
\log R_X
=
\sum_{p\le X}
\left(\log(1-p^{-1})+p^{-1}\right)
=
-\sum_{p\le X}\sum_{m\ge2}\frac{1}{m p^m}.
\]

The double series converges absolutely.  Therefore

\[
R_X\longrightarrow
R_\infty
=
\exp\left(
-\sum_p\sum_{m\ge2}\frac{1}{m p^m}
\right),
\qquad
0<R_\infty<1.
\]

This is a finite, strictly positive relative boundary volume derived at every
cutoff.  No post-limit division by zero is used.

## Three-level interpretation

The calculation assigns distinct jobs to the first source grades:

1. \(k=1\) supplies the oriented primitive line and hence the sign of the
   bivector;
2. \(k=2\) supplies the exponential countercurrent that prevents determinant
   volume collapse;
3. the remaining even connected powers form an absolutely convergent tail.

The scalar boundary object is therefore not one ordinary product.  It is the
relative pair

\[
\left(
\prod_{p\le X}(1-p^{-1}),
\exp\left(\sum_{p\le X}p^{-1}\right)
\right)
\]

whose evaluation is \(R_X\).  Erasing either component before completion
loses reconstructibility.

## What this solves

The ordinary restricted-product scalarizer collapses, but its canonically
square-renormalized relative volume does not.  Thus the completion obstruction
for this particular boundary determinant is removable by an already typed
source current.  No arbitrary heat scale or Hilbert pivot is required.

This does not yet prove the RH Green identity.  The remaining gate is whether
the same relative volume is the scalarization actually produced by the
doubled theta/Tate boundary system, including the archimedean place and the
spectral parameter.  The calculation is source-local at finite places and
spectrally neutral.

## Falsifier

At every cutoff, the declared relative determinant must equal \(R_X\)
exactly.  A different coefficient of \(\sum p^{-1}\), omission of a finite
prime, or mixing with the odd primitive current leaves a divergent or
incorrect limit.  The archimedean extension must multiply this object by a
finite source-derived factor, not redefine its finite-place normalization.

