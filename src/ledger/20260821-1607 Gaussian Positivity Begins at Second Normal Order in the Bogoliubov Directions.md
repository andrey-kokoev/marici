# Entry 1607 — Gaussian Positivity Begins at Second Normal Order in the Bogoliubov Directions

## Claim

The marked phase-space first jet of Entry 1605 recovers all Gaussian tangent
coordinates, but it cannot certify positivity in the anomalous directions.
That physical constraint begins at second normal order.

## Calculation

For \(\beta=x+iy\) and statistical occupation \(n\), the one-mode
uncertainty excess is

\[
\mathfrak U
=(n+\tfrac12)^2-|\beta|^2-\tfrac14
=n+n^2-x^2-y^2.
\]

Therefore

\[
\operatorname{gr}^{(1)}\mathfrak U=n,
\qquad
\operatorname{gr}^{(2)}\mathfrak U=n^2-x^2-y^2.
\]

The statistical line is constrained at first order.  The two Bogoliubov
directions lie tangent to the pure-vacuum boundary and first enter the
uncertainty condition quadratically.  A pure squeezed deformation requires

\[
n_2=x^2+y^2
\]

at second order.

## Consequence

\[
\boxed{
\text{first phase-space jet identifies the Gaussian tangent;
second Rees grade decides physical integrability.}
}
\]

This is independent evidence, within the Gaussian cosmology layer, for the
same distinction already forced by the three-site elliptic quartic:

\[
\text{first normal jet}\not\Rightarrow
\text{control of the first physical nonlinear deformation}.
\]

It does not identify the Gaussian and elliptic coefficient objects; it
identifies a shared higher-normal requirement in the comparison calculus.

## Next falsifier

Compute the second-order Dyson source for the statistical coordinate and test
whether it supplies the required positive completion of the first-order
Bogoliubov correction on the finite EFT carrier.

## Artifacts

- `research/benincasa/checkers/gaussian_uncertainty_rees_grade.rs`
- `research/benincasa/results/gaussian-uncertainty-rees-grade.json`
- `research/benincasa/gaussian-uncertainty-rees-grade.md`

Allocator claim: `seqclaim-c8beeeef17eeb915d5a42cb8`.
