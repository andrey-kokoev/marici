---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Special-Fiber Scalar Is a Tested Unit but Not a Low-Degree Invariant

## Record

Status: finite-field unit census and bounded rational-reconstruction no-go.
This continues Entries 400 and 410.

## Question

Entry 410 established
\[
e_6+\lambda_\pm v_{\rm alg}=0
\]
on the two components of
\[
D=E^4-X_1^2X_2^2.
\]
The next proposed step was to reconstruct \(\lambda_\pm\) and compare it
directly with the unit residues of \(d\log D\).

That proposal silently assumes that the scalar produced by pointwise RREF is
itself a small intrinsic rational function. This entry tests that assumption.

## Frozen test

For each component \(D_\pm\), sample
\[
u=3,\ldots,170
\]
over \(\mathbf F_{2305843009213693951}\). Normalize the additional gauge row
by its \(e_6\) coefficient and extract \(\lambda_\pm\) from the nonzero
\(e_8\) coefficient of \(v_{\rm alg}\).

Cross-check the exact-form degree-8 value against degree 10 at
\[
u=3,5,7,11,19,37.
\]
Then seek a rational function with numerator and denominator degrees at most
70 through all 168 samples on each component.

## Result

For both \(D_-\) and \(D_+\):

- all 168 values of \(\lambda_\pm\) are nonzero;
- all six degree-8/degree-10 cross-checks agree;
- no rational fit with numerator and denominator degrees at most 70 exists.

Thus
\[
\boxed{
\lambda_\pm\text{ is a nonzero tested special-fiber scalar, while its
RREF normalization is not a bounded low-degree invariant.}
}
\]

## Interpretation

The intrinsic data are:

1. the divisor \(D=0\);
2. its simple tested Fitting multiplicity;
3. the special-fiber line represented by \(v_{\rm alg}\).

The scalar multiplying a generator after full pointwise row reduction depends
on a large exact-lift minor and on the chosen affine gauge. It should not be
identified with the canonical quotient connection coefficient
\[
\alpha_{\rm alg}=d\log D.
\]

At every tested generic point of either component, \(\lambda_\pm\ne0\), so
the local relation introduces no additional support there. This is compatible
with the unit residue of \(d\log D\), but it is not an independent
connection-residue derivation.

## Narrow correction

The next frontier stated in Entry 410 was too strong as phrased. Rationally
reconstructing the RREF scalar is neither necessary nor evidently canonical.
Failure of a degree-70 fit is not evidence for new geometry.

The surviving claim is smaller:
\[
\text{exact-lift special-fiber line}
=
\text{algebraic Gysin line},
\]
while their global comparison must be made by a gauge-invariant line or
determinant construction, not by the pointwise RREF coefficient.

## Epistemic boundary

This is a bounded negative reconstruction result, not proof that no rational
formula exists. Nonvanishing on finite samples is not a symbolic unit theorem.
No physical-chain or integral-lattice statement follows.

## Next falsifier

Construct a gauge-invariant map of line bundles: compare the first Fitting
normal line of the exact-lift presentation with the algebraic quotient line
\(\langle e_6,v_{\rm alg}\rangle/\langle e_6\rangle\) using determinant
lines or an adjugate/kernel--cokernel pairing. Test whether the induced divisor
map is a unit on both components. Do not use the RREF scalar as the comparison
map.

## Evidence

- `research/benincasa/exact-lift-valg-unit-census.json`
- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`
