# Doubly stochastic support gate: WP1152

## Question

Does a sparse support-at-most-two doubly stochastic fixed-\(q\) S-matrix
modulus survive?

## DPC resolution

- **Problem:** classify sparse support inside the fixed-\(q\) doubly
  stochastic polytope.
- **Conjecture:** a support-two unitary-modulus map satisfies the target.
- **Rivals:** support-one map; support-two doubly stochastic map;
  full-support uniform map; support-three candidate.
- **Risky consequences:** row and column sums one, \(Pq=u\), and every row
  and column support exactly two.
- **Falsification attempt:** all \(67\,950\) support patterns are linearly
  inconsistent with the target; support one is impossible because no
  \(q_j=1/6\). \(J_6/6\) survives with full support.
- **Residual:** a support-three or denser doubly stochastic candidate may
  exist.
- **Disposition:** reject sparse support-two unitary-modulus maps and select
  the support-three question.

Checker: `research/flavor/checkers/wp1152_doubly_stochastic_support_gate.py`

Result: `results/wp1152_doubly_stochastic_support_gate.json`
