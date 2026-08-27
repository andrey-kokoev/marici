# Flat-moment certificate for off-grid optical scatter

## From a pixel grid to a positive measure

Treat the angular scatter field as a positive measure on one coordinate rather
than assuming fixed detector-bin locations. Freeze two off-grid atoms at
`-1/2` and `1` with weights `2/5` and `3/5`. Their first six moments are

```text
1, 2/5, 7/10, 11/20, 5/8, 47/80.
```

The checker constructs the order-one and order-two Hankel moment matrices. The
first has determinant `27/50` and rank two. The second is positive by an exact
Vandermonde-weight factorization, has rank two, and has determinant zero.
Rank has stabilized: the extension is flat.

## What flatness buys

The one-dimensional kernel of the larger Hankel matrix gives the annihilating
polynomial

```text
x^2 - x/2 - 1/2.
```

Its roots recover the off-grid positions `-1/2` and `1`. The first two moments
then recover the positive weights `2/5` and `3/5`. No pixel-grid support was
inserted.

The fifth moment is not used to reconstruct the atoms. It is predicted as
`47/80` and then checked, giving an out-of-sample falsifier rather than another
fit coordinate.

## A surprisingly sharp failure

Changing only the fourth moment by `1/100` makes the larger Hankel matrix rank
three. The two-atom flat certificate disappears. More numerical precision or
a preferred two-peak fit cannot restore it.

This separates two statements:

- the measured truncated sequence has a unique positive two-atom flat
  extension;
- the physical source is governed by a finite-atomic scattering law.

The first is an instrument-and-data theorem. The second still needs source
authority. A continuous field, signed quasidistribution, multidimensional
angle, or noisy moment interval requires a different certificate.

## Optical implementation

Calibrated spatial-mode projections onto monomials or an equivalent orthogonal
polynomial basis can estimate the needed angular moments. Direct monomials are
often poorly conditioned experimentally; the exact algebra is basis-invariant
only when the calibration and covariance are transported with the basis.

## Claim boundary

The checker covers an exact positive univariate two-atomic measure. It does not
prove finite atomicity for an arbitrary optical source and does not treat noisy
moments, signed measures, or two-dimensional scattering.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_scatter_flat_moment_certificate.py
```
