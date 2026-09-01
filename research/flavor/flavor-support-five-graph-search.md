# Support-five graph search: WP1168

## Question

Do graph-compatible support-five carriers contain fixed-\(q\) interior points?

## DPC resolution

- **Problem:** search the first sparse class after the support-four and
  boundary exclusions, correcting an earlier overgeneralized full-support
  claim.
- **Conjecture:** graph-compatible support-five carriers supply fixed-\(q\)
  interior points.
- **Rivals:** empty graph class; derangement-only algebra; zero-diagonal
  witness; phase lift.
- **Risky consequences:** \(37\,476\) graph-compatible carriers, \(720\)
  derangement carriers, and a strictly positive off-diagonal witness.
- **Falsification attempt:** all \(720\) derangement carriers pass exact
  linear feasibility, and the identity carrier has an explicit interior point.
- **Residual:** the displayed identity witness fails row/column
  sqrt-product polygon inequalities and has no phase lift.
- **Disposition:** accept support-five graph and algebraic existence; select
  the phase-compatible search.

Checker: `research/flavor/checkers/wp1168_support_five_graph_search.py`

Result: `results/wp1168_support_five_graph_search.json`
