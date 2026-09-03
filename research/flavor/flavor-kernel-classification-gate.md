# Kernel-classification gate: WP1257

## Question

Can support/rank/orbit algebra select the Physical16 production kernel?

## DPC resolution

- **Problem:** derive the Physical16 gain/interference law while the
  channel-cascade handoff remains active.
- **Bold conjecture:** locality, rank, or equal-weight symmetry may select
  a target-compatible production kernel.
- **Named rivals:** rank-two local map; support-two rank-three map; six
  perfect matchings; twin-swap orbit; production-matching packet.
- **Risky consequences:** all 15625 partner assignments were tested; 729
  support-two maps satisfy the target; their ranks are 3, 4, or 5; six
  rank-three candidates are perfect matchings; the twin swap gives three
  two-element orbits.
- **Strongest falsification attempt:** zero rank-two local maps, matching
  certificates, Physical16 coupling maps, same-frame gain certificates,
  physical exchange certificates, or kernel invariance certificates exist.
- **Exact residual:** materialize a production-matching packet selecting
  one matching with couplings, gain \(3/2\), and localization certificate.
- **Disposition:** accept exact support/rank/orbit classification; reject
  current source-selected kernel.

Checker: `research/flavor/checkers/wp1257_kernel_classification_gate.py`

Result: `results/wp1257_kernel_classification_gate.json`
