# Dual-number Gröbner provenance for local curvature

## Motivation

The provenance-corrected rank-seven matrices have high rational degree in
base coordinates. Reconstructing global slice formulas is therefore the wrong
derivative oracle. Mixed curvature only requires the first derivative at one
point.

## Constructor

Coefficients are evaluated over

\[
\mathbb F_p[\epsilon]/(\epsilon^2).
\]

For an invertible leading coefficient,

\[
(a+\epsilon b)^{-1}=a^{-1}-\epsilon b a^{-2}.
\]

This rule is propagated through monic normalization, S-polynomials,
Buchberger reduction, primitive provenance, and exact normal-form traces. The
leading monomial is frozen by the ordinary coefficient at a generic point.

## Verification

For all three base directions at A, B, and HOMA, with a second-prime
replication at A:

- the dual basis has the same 36 ordinary basis elements;
- each dual basis element reconstructs from the four dual source generators;
- seven probe targets reduce and reconstruct exactly;
- every direction carries nonzero basis and target tangent data.

## Scope

This validates the local derivative engine. It does not yet compute the
derivatives of the final rank-seven coordinate matrices or their mixed
curvature. That integration is the next gate.

## Artifacts

- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`
- `research/benincasa/checkers/check_cm_dual_groebner_provenance.py`
- `research/benincasa/results/cm-dual-groebner-provenance.json`

