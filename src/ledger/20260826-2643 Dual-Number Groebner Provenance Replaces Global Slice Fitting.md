# 2643 — Dual-Number Gröbner Provenance Replaces Global Slice Fitting

## Problem

Entry 2629 identifies three exact-generator coherence directions. The common
lift then produces pointwise rank-seven matrices, but their primitive Gröbner
coefficients have rational slice degree beyond the former bounded fitting
regime. A global reconstruction is unnecessary for mixed curvature, which is
local and first order.

## Source-defined constructor

The tracked reducer now operates over

\[
\mathbb F_p[\epsilon]/(\epsilon^2),
\]

using

\[
(a+\epsilon b)^{-1}=a^{-1}-\epsilon b a^{-2}
\]

for every generic leading coefficient. Dual coefficients propagate through
monic normalization, S-polynomials, Buchberger reduction, primitive traces,
and normal forms.

## Replicated audit

Across all three base directions at A, B, and HOMA and at two primes:

- the ordinary projection of the dual basis equals the 36-element tracked
  basis termwise;
- every dual basis element reconstructs from the four dual source generators;
- all seven probe reductions reconstruct from their dual remainder and trace;
- every direction has nonzero tangent data.

## Narrow conclusion

The high-degree slice-fitting obstruction is removed at the correct level.
Local derivatives of provenance-carrying reductions can now be computed
exactly without reconstructing global rational functions.

The next gate is to feed the seven lifted frame classes through this dual
pipeline, solve their coordinate matrices over dual numbers, and test all
three mixed curvatures at independent points and primes.

## Artifacts

- `research/benincasa/cm-dual-groebner-provenance.md`
- `research/benincasa/checkers/check_cm_dual_groebner_provenance.py`
- `research/benincasa/results/cm-dual-groebner-provenance.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

Ledger sequence claim: `seqclaim-abc1db89265aeb5e0fcb64f7`.

Epistemic event: `ev-000000003992-a52556b7-9bf0-46af-8377-9b4c2ff93ce9`.
