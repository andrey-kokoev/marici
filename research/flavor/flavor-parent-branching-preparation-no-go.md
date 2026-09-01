# Parent-branching preparation no-go: WP1131

## Question

Can parent branching act as the sourced preparation operator?

## DPC resolution

- **Conjecture:** parent branching is a sourced preparation operator producing
  \(q=(6,8,1,4,2,2)/23\).
- **Rivals:** representation branching as preparation; normalized dimension
  trace as preparation; dynamical parent branching operator; no branching
  preparation.
- **Risky consequences:** sourced parent states, six conditional branch
  probabilities, a stochastic branching map, a dimension-proportional measure,
  and common parent preparation/clock.
- **Falsification attempt:** the source has one parent cell and six sectors
  but zero parent states, zero conditional probabilities, zero stochastic
  maps, and five residual mass blocks. The target \(q\) follows only after
  assuming dimension proportionality.
- **Residual:** future parent dynamics could supply state populations and
  branch transition probabilities.
- **Disposition:** reject parent branching as a preparation operator; retain
  \(q\) only as dimension data.

## Boundary

A representation decomposition is not a stochastic map. Sector dimensions can
define \(q\) only after a dimension-proportional measure is sourced.

Checker: `research/flavor/checkers/wp1131_parent_branching_preparation_no_go.py`

Result: `results/wp1131_parent_branching_preparation_no_go.json`
