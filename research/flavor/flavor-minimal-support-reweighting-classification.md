# Minimal-support reweighting classification: WP1144

## Question

What is the minimal support and rank of target-compatible local reweighting
maps?

## DPC resolution

- **Problem:** determine the smallest local support before invoking a source
  packet.
- **Conjecture:** a two-support local map can satisfy the target, and its rank
  may be as low as two.
- **Rivals:** support-one diagonal map; support-two rank-two map; support-two
  rank-three map; higher-rank local map.
- **Risky consequences:** support one requires \(q_j=1/6\); support two
  requires exact interpolation; rank is computed for every valid partner
  assignment; rows are nonnegative and stochastic.
- **Falsification attempt:** no support-one row exists. Among 729 support-two
  maps, ranks are 3, 4, or 5; the minimum rank is 3.
- **Residual:** six rank-three support-two candidates remain executable
  algebraic rivals.
- **Disposition:** classify minimal support two and minimal local rank three.

## Exact result

The support-two rank histogram is

\[
\operatorname{rank} 3:6,\qquad
\operatorname{rank} 4:162,\qquad
\operatorname{rank} 5:561.
\]

Thus support two suffices for the target but never yields rank two.

Checker: `research/flavor/checkers/wp1144_minimal_support_reweighting_classification.py`

Result: `results/wp1144_minimal_support_reweighting_classification.json`
