# Rank-three matching gate: WP1145

## Question

What are the six rank-three support-two candidates, and are any
source-selected?

## DPC resolution

- **Problem:** test the six minimal-rank reweighting candidates against
  production locality and source provenance.
- **Conjecture:** one candidate is selected by source production locality.
- **Rivals:** six algebraic perfect matchings; source-derived matching; single
  selected matching; no source selection.
- **Risky consequences:** each candidate is a perfect matching with three
  identical two-support row pairs; source selection requires production
  adjacency, couplings, and same-frame gain.
- **Falsification attempt:** all six candidates are exact perfect matchings,
  but the source supplies zero matching certificates, physical16 coupling
  maps, or same-frame gain certificates.
- **Residual:** a production-matching packet or symmetry-orbit reduction may
  select among them.
- **Disposition:** reject current source selection and record the
  production-matching blocker.

## Typed blocker

`production_matching_packet` must derive one of the six matchings, its
physical16 couplings, gain \(3/2\), and localization in one frame.

Checker: `research/flavor/checkers/wp1145_rank_three_matching_gate.py`

Result: `results/wp1145_rank_three_matching_gate.json`
