# Prime vacuum cocycle explains the three Tate regularity levels

## Question

The bilateral valuation shift gives a native local operator, but its global
assembly is ambiguous.  Which source-level object detects the difference
between the primitive, square, and connected prime-power currents before any
scalar augmentation?

## The canonical excitation

For each prime (p), retain the local vacuum (e_{p,0}) and define

\[
b_{p,k}(z)
=
\mathcal J_{p,k}(z)e_{p,0}.
\]

Writing (L_p=\log p), this is

\[
b_{p,k}(z)
=
\frac{p^{-k/2}}k
\left(
e^{kzL_p}e_{p,k}
-e^{-kzL_p}e_{p,-k}
\right).
\]

The vectors (e_{p,k}) and (e_{p,-k}) are orthogonal.  Therefore, for

\[
\sigma=\Re z,
\]

one has the exact norm identity

\[
\lVert b_{p,k}(z)\rVert^2
=
\frac{2p^{-k}}{k^2}
\cosh(2k\sigma\log p).
\]

The family (b_{p,k}) is the vacuum cocycle of the local current.  Unlike an
untyped prime sum of operators, it has a canonical global Hilbert question:
does it belong to the direct sum of the local excitation spaces?

## Exact seam classification

On the critical seam, (sigma=0), so

\[
\sum_p\lVert b_{p,k}(it)\rVert^2
=
\frac2{k^2}\sum_pp^{-k}.
\]

Consequently:

- the primitive cocycle (k=1) is not Hilbert because
  \(sum_p p^{-1}\) diverges;
- the square cocycle (k=2) is Hilbert because
  \(sum_p p^{-2}\) converges, while its scalar amplitude sequence
  \((p^{-1})_p\) is not absolutely summable;
- every (k\ge3) cocycle is Hilbert and its scalar amplitude sequence
  \((p^{-k/2}/k)_p\) is absolutely summable.

Thus the familiar three levels are already forced by the source excitation:

1. primitive current: distributional rather than Hilbert;
2. square current: Hilbert but not absolutely summable at the coefficient
   level;
3. connected tail: absolutely summable.

No analytic continuation of a scalar prime series enters this classification.

## Off-seam windows

The two terms in the cocycle norm behave as

\[
p^{-k+2k\sigma},
\qquad
p^{-k-2k\sigma}.
\]

Both prime sums converge precisely when

\[
k(1-2|\sigma|)>1.
\]

This has three consequences.

- The primitive cocycle is non-Hilbert for every real (sigma), including the
  seam.
- The square cocycle is Hilbert for (|\sigma|<1/4).
- The complete (k\ge3) cocycle tower is Hilbert for
  (|\sigma|<1/3).

Absolute summability of the connected operator coefficients is stricter.  It
requires

\[
k(1/2-|\sigma|)>1,
\]

so the full (k\ge3) tail is absolutely summable for

\[
|\sigma|<1/6.
\]

The Hilbert excitation window and the operator absolute-summability window
are therefore different invariants and must not be conflated.

## Restricted-product meaning

For an infinite tensor product of local vacua, the first-order obstruction to
implementing the product of local transports is measured by the square sum of
their vacuum excitations.  The theorem above therefore explains the exact
roles of the three channels:

- (k=1) must be retained in a distributional boundary rigging;
- (k=2) is a genuine Hilbert excitation but cannot be folded into an
  ordinary absolutely convergent determinant coefficient;
- (k\ge3) forms the ordinary connected interior near the seam.

The first two currents are not arbitrary counterterms.  They are precisely
the components whose vacuum cocycles fall below successive completion
thresholds.

## Correction to the operator-sum picture

The notation

\[
\sum_p\mathcal J_{p,k}
\]

does not determine a global operator.  A block direct sum, an additive
restricted-tensor generator, and a vacuum cocycle have different norms.  The
three-level theorem belongs canonically to the vacuum cocycle.  Any future
global Green or determinant construction must state which assembly functor it
uses and how the two exceptional cocycles enter its domain.

## Next exact target

Construct the restricted-product rigging whose boundary coordinates are the
primitive cocycle and the square cocycle, and prove that reciprocal reflection
acts continuously on all three levels.  Then derive the archimedean incidence
map into those coordinates before scalar augmentation.

The first falsifier is concrete: if the archimedean incidence is continuous
only after deleting the (k=1) cocycle or replacing the (k=2) cocycle by an
absolutely summable surrogate, the proposed completed source space is lossy.

## Result

The three Tate regularity levels are the exact summability strata of the
bilateral prime-vacuum cocycle.  This gives them a source-native operator
meaning and locates the remaining construction problem in the restricted
product and its archimedean boundary map.
