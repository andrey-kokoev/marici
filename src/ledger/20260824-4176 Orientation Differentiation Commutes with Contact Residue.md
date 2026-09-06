---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 4176 — Orientation Differentiation Commutes with Contact Residue

## Linear naturality

Canonical forms are additive under the declared subdivision, and residues
are linear. For any residue functional \(r\), Boolean comparison \(Z\), and
orientation tangent \(\delta\mu\),

\[
r(Z\delta\mu)=(rZ)(\delta\mu).
\]

Therefore taking the orientation derivative before contact residue gives the
same result as transporting the residue to overlap coordinates and then
differentiating.

Applied to the three edge tangents,

\[
\boxed{
\operatorname{Res}_{\rm ct}\,d_w\Omega
=d_w\operatorname{Res}_{\rm ct}\Omega.
}
\]

## Status of the selector

Entries 2208–2209 and 4176 establish that the selector is:

- independent of overlap versus resolved-cell coordinates;
- unique inside the frozen Boolean cover;
- compatible with the contact residue operation.

It is therefore an intrinsic first-order class of the weighted geometry,
not merely presentation memory of its \((-2)^j\) formula.

The remaining limitation is physical rather than geometric. The source does
not say that orientation-weight tangents are realizable cosmological
deformations or observables. The next admissible enlargement must derive a
physical family whose induced tangent lands in this already fixed geometric
class.

## Evidence

- Entries 2207–2209
- `research/benincasa/checkers/orientation_tangent_residue_naturality.rs`