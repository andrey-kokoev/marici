# Noisy resolution of two nearby optical scatter atoms

## Exact rank is not operational resolution

Take two equal scatter atoms at positions `0` and `d`. A single atom at their
centroid `d/2` has the same total power and first moment. Their first separating
record is the second central moment:

```text
two atoms: variance = d^2/4
one centroid atom: variance = 0.
```

The same quantity is the determinant of the first Hankel moment matrix. It is
positive for every nonzero `d`, so exact algebra declares two atoms at arbitrary
separation. A physical instrument cannot make that conclusion unless its
calibrated uncertainty excludes zero variance.

## Exact frozen threshold

Freeze `d=1/10`. The two-atom and one-atom models share total and centroid. The
second-moment gap is `1/400`.

- With second-moment error `1/500`, the one-atom model is excluded.
- With error `1/400`, the one-atom moment lies on the compatible interval
  boundary and multiplicity is no longer identified.

Halving separation quarters the variance witness. The required absolute
second-moment accuracy therefore improves quadratically with desired angular
resolution.

## A counterintuitive higher-moment fact

For small `d`, the third-moment gap is `3d^3/8`, which shrinks even faster than
the variance witness. Merely measuring a higher moment does not guarantee a
better close-pair discriminator. The instrument must compare signal scaling,
noise, and basis conditioning, not moment degree alone.

## Optical implications

A calibrated spatial-mode demultiplexer that directly targets the variance
mode can outperform naive image-plane peak fitting in this declared model.
But diffraction, mode mismatch, and covariance must be propagated into the
variance interval. Exact nonzero Hankel determinants are not sufficient
experimental evidence.

The relevant completion record is set-valued: report whether the admissible
moment interval excludes every rank-one positive measure. A fitted rank or a
singular-value threshold chosen after seeing the desired atom count is not an
authorized certificate.

## Claim boundary

The checker compares two equal atoms with one centroid atom, assumes exact
total and centroid, and places symmetric bounded error only on the second
moment. Unequal weights, errors in all moments, and optical transfer functions
require a covariance-bearing robust moment problem.

## Verification

```text
python research/aspect/checkers/check_noisy_two_atom_resolution.py
```
