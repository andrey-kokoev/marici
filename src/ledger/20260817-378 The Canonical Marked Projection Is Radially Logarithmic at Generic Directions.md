---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Canonical Marked Projection Is Radially Logarithmic at Generic Directions

## Question

Entries 372 and 377 leave the finite claim

\[
\boxed{\text{the marked seven-coordinate projection retains an irregular
exceptional-tangent pole after the frozen Rees correction.}}
\]

This tests the three marked rows projected to

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_6,e_7,e_8,e_9).
\]

It does not reconstruct the five exact-lift-gauge coordinates.

## Frozen input

Use the two radial charts

\[
(u,v)=(t,tr),\qquad (u,v)=(tr,t),
\]

of the cusp corner \((u,v)=(E_T,\ell_3)=(0,0)\). The source connection sign
is fixed once by

\[
[E_T^{-2}e_6]\nabla\Omega_{111}=\frac18.
\]

Apply the previously derived Kummer shear

\[
\widehat\Omega_{111}=\Omega_{111}+\frac{e_6}{8u}
\]

and retain the Entry-372 absolute radial weights

\[
w(e_6)=w(e_7)=0,\qquad w(e_8)=w(e_9)=1.
\]

No support factor or frame is fitted after inspecting the pullback.

## Marked radial weights

The raw exact valuations force the same minimal weight on all three marked
generators:

\[
\boxed{
w(\Omega_{111})=w(\Omega_{101})=w(\Omega_{110})=2.
}
\]

For an entry from row \(i\) to column \(j\), the transformed valuation is

\[
\operatorname{ord}_t(A_{ij})+w_i-w_j.
\]

These weights simultaneously regularize every tested exceptional-tangent
entry while leaving the radial connection logarithmic.

## Exact finite test

For each chart and each generic exceptional direction

\[
r\in\{2,3,4,5\},
\]

the four-stratum engine is evaluated at 80 exact points over
\(\mathbf F_{2305843009213693951}\). The \(u\)- and \(v\)-connection rows are
combined by the exact chart Jacobian. The full basis change includes:

1. the global source-sign calibration;
2. the derivative of \(e_6/(8u)\);
3. the invariant \(e_6\)-connection row;
4. re-expression of the old top generator in the sheared basis;
5. the frozen diagonal radial weights.

Bounded rational reconstruction reaches numerator and denominator degree 18.
Across all 336 tested marked coordinates,

\[
\boxed{
\min\operatorname{ord}_t A_t'=-1,
\qquad
\min\operatorname{ord}_t A_r'=0.
}
\]

Thus the radial coefficient is logarithmic and the exceptional-tangent
coefficient is regular at every tested direction in both charts.

## Verdict

The tested claim is falsified at the generic directions sampled:

\[
\boxed{\text{the canonical marked projection extends through the radial
exceptional divisor using the frozen Kummer shear and Rees lattice.}}
\]

No additional generic radial support is observed. The marked weights are a
filtered coefficient-lattice datum; they do not define a new carrier cell.

## Classification

| Datum | Classification |
|---|---|
| radial exceptional divisor | existing flagged normal geometry |
| \(e_6/(8u)\) shear | Tate/Kummer coefficient extension |
| weights \((2,2,2;0,0,1,1)\) | sector-specific Rees coefficient lattice |
| remaining radial logarithmic pole | existing normal divisor |
| generic tangent pole | absent at tested directions |
| new carrier datum | none found |

## Epistemic boundary and next falsifier

This is exact finite-field evidence at four generic values of the exceptional
coordinate, not a symbolic reconstruction of its complete rational support.
It therefore does not exclude a pole at an unsampled exceptional direction.

The next finite falsifier is to reconstruct the transformed leading matrices
as rational functions of \(r\), factor every denominator, and require each
factor to be a strict transform of a frozen energy, soft, conductor, or Cut
divisor. Any additional irreducible factor would be coefficient support or,
if it defines an unavoidable new incidence stratum, a carrier-level failure.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_radial_pullback.rs`;
- `research/benincasa/marked-radial-pullback-certificate.json`;
- `research/benincasa/bivariate_soft_gram_connection.json`;
- `research/benincasa/two-wall-rees-regularization.json`;
- Entries 293, 371, 372, 374, and 377.
