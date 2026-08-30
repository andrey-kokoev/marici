---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2234 — Recovering Homogeneous Occurrences Requires a Rank-Two Port Adapter

## Minimal missing lens

At homogeneous triangle kinematics, the existing momentum score detects the
trivial line \(\mathbb Q(1,1,1)\). Faithful reconstruction additionally
requires two independent difference directions, for example

\[
(1,-1,0),
\qquad
(0,1,-1).
\]

Together these form the rational cyclotomic representation of \(C_3\), and
the complete detector has rank three. Hence the minimal additional readout
has rank two:

\[
\boxed{
\mathcal A_{\rm occ}\simeq\mathbb Q(\zeta_3).
}

## Source interpretations

An admissible adapter could arise from:

- an anisotropic boundary kernel depending on the full momentum vector;
- an independently declared occurrence-tagged source;
- a detector geometry that distinguishes the three edge directions.

None is supplied by the homogeneous isotropic scalar source. They are
candidate sector-specific readout lenses, not new Carrier cells: the three
occurrence labels already exist in the Carrier.

Adding such an adapter solely to recover a desired hidden class would be
post hoc. Its source and transformation law must be frozen independently.

## Evidence

- Entries 2232–2233
- `research/benincasa/checkers/occurrence_adapter_minimal_rank.rs`

