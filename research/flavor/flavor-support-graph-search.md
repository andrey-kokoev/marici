# Support-three graph search: WP1155

## Question

Does any support-three graph admit a unistochastic-compatible fixed-\(q\)
solution?

## DPC resolution

- **Problem:** search support-three graphs after the WP1154 witness
  obstruction.
- **Conjecture:** some support-three graph avoids single-overlap obstruction
  and supports fixed-\(q\) mixing.
- **Rivals:** single-overlap graph; two-block complete graph; fixed-\(q\)
  balanced block; support-four graph.
- **Risky consequences:** \(297\,200\) row-support-three patterns, no row or
  column support overlap one, \(200\) graph-compatible patterns, and
  fixed-\(q\) block sum \(1/2\).
- **Falsification attempt:** all \(200\) graph-compatible patterns are two
  complete \(3\times3\) blocks; fixed-\(q\) would require a three-column
  \(q\)-sum of \(1/2\), impossible for integer numerators summing to \(23\).
- **Residual:** support four is the next possible sparse class.
- **Disposition:** reject support-three unistochastic-compatible fixed-\(q\)
  maps.

Checker: `research/flavor/checkers/wp1155_support_graph_search.py`

Result: `results/wp1155_support_graph_search.json`
