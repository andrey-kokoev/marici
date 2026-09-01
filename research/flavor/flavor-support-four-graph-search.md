# Support-four graph search: WP1157

## Question

Are support-four graphs free of the single-overlap unistochastic obstruction?

## DPC resolution

- **Problem:** search support-four graphs for the necessary unitary support
  condition.
- **Conjecture:** support four is the first support class whose regular graphs
  all pass the single-overlap test.
- **Rivals:** support-three two-block graph; support-four complement graph;
  fixed-\(q\) polytope point; phase lift.
- **Risky consequences:** \(67\,950\) zero-complement patterns, row and column
  support four, no support overlap one, and remaining polytope and phase tests.
- **Falsification attempt:** every support-four regular graph has row and
  column support overlaps of size \(2\), \(3\), or \(4\), never \(1\).
- **Residual:** no nonnegative fixed-\(q\) witness or phase lift is
  established by graph compatibility alone.
- **Disposition:** accept support-four graph compatibility and select the
  support-four polytope test.

Checker: `research/flavor/checkers/wp1157_support_four_graph_search.py`

Result: `results/wp1157_support_four_graph_search.json`
