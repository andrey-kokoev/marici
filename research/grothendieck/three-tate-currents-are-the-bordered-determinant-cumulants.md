# Three Tate currents are the bordered determinant cumulants

## Question

The programme previously separated primitive, prime-square, and connected
tail currents.  Does the new source-local bordered determinant derive that
filtration, or must it still be imposed externally?

## Local logarithmic determinant

The infinite valuation-chain boundary determinant at a prime \(p\) is

\[
E_p(s)=\frac1{1-p^{-s}}
\]

in its convergence chamber.  Its logarithm is

\[
\log E_p(s)
=
\sum_{k\ge1}\frac{p^{-ks}}{k}.
\]

Separate the first two determinant cumulants:

\[
\log E_p(s)
=
p^{-s}
+\frac12p^{-2s}
+\sum_{k\ge3}\frac{p^{-ks}}{k}.
\]

These are not fitted counterterms.  They are the first, second, and higher
valuation returns of the source shift seen by the augmentation boundary.

## Global convergence thresholds

Let \(\sigma=\Re s\).  Summing over primes gives three distinct analytic
classes.

The primitive current is

\[
P_1(s)=\sum_pp^{-s}.
\]

It converges absolutely only for \(\sigma>1\).

The square current is

\[
P_2(s)=\frac12\sum_pp^{-2s}.
\]

It converges absolutely only for \(\sigma>1/2\), and reaches the prime
harmonic divergence on the critical seam.

The connected tail is

\[
P_{\ge3}(s)
=
\sum_p\sum_{k\ge3}\frac{p^{-ks}}{k}.
\]

It converges absolutely for \(\sigma>1/3\).  In particular, it is already
ordinary determinant data throughout a neighborhood of the critical seam.

Thus the three-level regularity filtration is forced by the source-local
determinant expansion:

- \(k=1\): primitive distributional boundary current;
- \(k=2\): square current at the Hilbert/non-trace threshold;
- \(k\ge3\): ordinary connected determinant tail.

## Canonical third-order determinant tail

Removing the first two logarithmic cumulants while retaining them as explicit
boundary coordinates gives the local third-order factor

\[
E_p^{[3]}(s)
=
\frac{
\exp\left(-p^{-s}-\frac12p^{-2s}\right)
}{1-p^{-s}}.
\]

Its logarithm is exactly

\[
\log E_p^{[3]}(s)
=
\sum_{k\ge3}\frac{p^{-ks}}{k}.
\]

Therefore

\[
\prod_pE_p^{[3]}(s)
\]

converges absolutely for \(\Re s>1/3\).  The primitive and square channels
must accompany it as typed relative data if finite Euler cutoffs are to be
reconstructed.

This is the exact boundary-determinant analogue of a third-order regularized
Fredholm determinant.

## Reconstruction law

For every finite prime cutoff \(X\),

\[
\prod_{p\le X}E_p(s)
=
\exp\left(
P_{1,X}(s)+P_{2,X}(s)
\right)
\prod_{p\le X}E_p^{[3]}(s).
\]

Hence the full finite Euler seam is reconstructed losslessly from

\[
\left(
P_{1,X},P_{2,X},E_X^{[3]}
\right).
\]

Deleting either of the first two currents changes the finite determinant and
is not a regularization of the same source object.

## Relation to the boundary packet

The determinant architecture now has two independent typed boundary axes:

1. arithmetic cumulant degree \(k=1,2,\ge3\);
2. archimedean continuation orientation, with symmetric coordinate \(1/2\)
   and antisymmetric coordinate \(s-1/2\).

The missing completed operator must couple these axes before either is
compressed.  A scalar product of the regularized Euler tail with the neutral
half carrier loses both the primitive/square data and boundary orientation.

## What remains open

This result derives the correct relative determinant line, but not its global
kernel law.  The hard questions are now:

- how the primitive and square currents enter the reciprocal graph domain;
- whether their archimedean incidence produces the antisymmetric boundary
  coefficient \(s-1/2\);
- whether the combined graph remains completion-stable off the seam;
- whether its relative determinant equals completed \(\xi\) rather than only
  the Euler chamber readout.

No local Euler factor has a nontrivial zero in its convergence chamber.  Any
global zero must arise through the completed coupling, not from a local
valuation-chain kernel.

## Result

The primitive, prime-square, and connected Tate currents are exactly the
first two and remaining logarithmic cumulants of the source-derived bordered
prime determinant.  The previously inferred three-level filtration is now an
operator theorem, not a chosen regularization scheme.
