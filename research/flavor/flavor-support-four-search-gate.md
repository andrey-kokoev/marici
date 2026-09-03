# Support-four search gate: WP1261

## Question

Do graph-compatible support-four candidates contain an exact fixed-\(q\)
interior point?

## DPC resolution

- **Problem:** test support-four sparse candidates for fixed-\(q\) doubly
  stochastic and unistochastic-compatible solutions, then derive source phase
  authority selecting a production map.
- **Bold conjecture:** a graph-compatible support-four carrier contains a
  fixed-\(q\) doubly stochastic interior point and a physical phase lift.
- **Named rivals:** support-four algebraic witness; single-overlap-free
  graph; carrier polytope point; interior algebraic point; phase lift.
- **Risky consequences:** WP1156 gives a support-four algebraic witness;
  all 67,950 support-four regular graphs are single-overlap-free; WP1158
  gives an exact carrier-polytope boundary point; WP1159 gives 24 positive
  carrier entries with minimum \(1/42\).
- **Strongest falsification attempt:** the exact rational interior point
  passes every algebraic test, but no phase-lift certificate is found.
- **Exact residual:** test whether the exact support-four modulus has a
  unitary phase lift.
- **Disposition:** accept support-four algebraic and graph existence; reject
  promotion to a kernel.

Checker: `research/flavor/checkers/wp1261_support_four_search_gate.py`

Result: `results/wp1261_support_four_search_gate.json`
