# Local rank-two reweighting no-go: WP1143

## Question

Can a rank-two reweighting candidate retain diagonal-plus-one-partner local
support?

## DPC resolution

- **Problem:** test whether localized production can select the rank-two
  reweighting family.
- **Conjecture:** a rank-two target-compatible map can retain row-local
  support.
- **Rivals:** rank-one full mixing; rank-two full-support map;
  diagonal-plus-one-partner local map; higher-rank local map.
- **Risky consequences:** each local row has support at most two, exact
  interpolation to \(u=1/6\), rank at most two, and nonnegative stochastic
  entries.
- **Falsification attempt:** all \(5^6=15625\) off-diagonal partner
  assignments were tested exactly. There are 729 target-compatible local maps,
  but none has rank at most two.
- **Residual:** support three or more, or a sourced production-adjacency
  packet, may still select a map.
- **Disposition:** reject row-local rank-two reweighting.

## Exact consequence

WP1142's rank-two example has full six-branch support in every row. Under the
tested diagonal-plus-one-partner locality class, rank-two compatibility is
impossible.

Checker: `research/flavor/checkers/wp1143_local_rank_two_no_go.py`

Result: `results/wp1143_local_rank_two_no_go.json`
