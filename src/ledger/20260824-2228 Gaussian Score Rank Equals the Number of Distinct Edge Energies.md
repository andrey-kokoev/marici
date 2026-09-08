---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2228 — Gaussian Score Rank Equals the Number of Distinct Edge Energies

## Physical pullback

A translationally invariant boundary state supplies one deformation function
\(\kappa(y)\). For edge energies \(y_1,\ldots,y_m\), its labelled values are

\[
\kappa\longmapsto
(\kappa(y_1),\ldots,\kappa(y_m)).
\]

Let \(d\) be the number of distinct values among the \(y_e\). Evaluation of
the jet basis

\[
1,y,\ldots,y^{d-1}
\]

on those distinct values has nonzero Vandermonde determinant. Repeated
occurrences produce duplicate rows. Therefore

\[
\boxed{
\operatorname{rank}(\operatorname{ev}_{\{y_e\}})=d.
}
\]

## Interpretation

The occurrence-labelled tangent space has rank \(|E|\), while the physical
momentum-function lens sees only one direction per distinct edge energy.
Energy collisions are therefore readout-rank-loss loci. They do not erase the
underlying occurrence labels or create new Carrier strata.

This gives an all-graph criterion for when one Gaussian source function is a
faithful detector of deletion-route information.

## Evidence

- Entries 2213 and 2227
- `research/benincasa/checkers/energy_collision_score_rank.rs`
