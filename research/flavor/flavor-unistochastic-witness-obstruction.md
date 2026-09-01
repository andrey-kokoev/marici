# Unistochastic witness obstruction: WP1154

## Question

Does the WP1153 support-three witness have a unistochastic lift?

## DPC resolution

- **Problem:** test whether the support-three doubly stochastic witness is the
  modulus of a unitary S-matrix.
- **Conjecture:** phase adjustment makes the witness unistochastic.
- **Rivals:** phase-adjusted lift; support obstruction; alternate
  support-three witness; nonunitary production map.
- **Risky consequences:** row orthogonality, single-overlap cancellation
  impossibility, nonzero product \(11/480\), and support-graph admissibility.
- **Falsification attempt:** rows \(0\) and \(2\) overlap only in column
  \(0\), so their unitary inner product would be one nonzero term; no phases
  can cancel it.
- **Residual:** another support-three pattern may have an admissible support
  graph.
- **Disposition:** reject the WP1153 witness as unistochastic.

Checker: `research/flavor/checkers/wp1154_unistochastic_witness_no_go.py`

Result: `results/wp1154_unistochastic_witness_no_go.json`
