# Support-four interior point: WP1159

## Question

Does the support-four carrier have an interior fixed-\(q\) doubly stochastic
point?

## DPC resolution

- **Problem:** decide whether the WP1158 carrier polytope is boundary-only.
- **Conjecture:** the support-four carrier has a point with every allowed edge
  positive.
- **Rivals:** boundary-only polytope; interior algebraic point; phase lift;
  physical production map.
- **Risky consequences:** all \(24\) carrier entries positive, minimum
  positive entry \(1/42\), row and column sums one, and \(Pq=u\).
- **Falsification attempt:** the exact rational matrix passes every algebraic
  test and realizes exact row/column support four.
- **Residual:** a unitary phase lift and physical production map remain
  unestablished.
- **Disposition:** accept interior algebraic existence and select the
  phase-lift test.

Checker: `research/flavor/checkers/wp1159_support_four_interior_point.py`

Result: `results/wp1159_support_four_interior_point.json`
