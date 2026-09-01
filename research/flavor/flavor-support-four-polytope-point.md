# Support-four polytope point: WP1158

## Question

Does a graph-compatible support-four carrier contain a fixed-\(q\) doubly
stochastic point?

## DPC resolution

- **Problem:** test the first single-overlap-free sparse carrier class.
- **Conjecture:** a support-four carrier contains a fixed-\(q\) doubly
  stochastic point.
- **Rivals:** empty carrier polytope; boundary polytope point; interior
  support-four point; phase lift.
- **Risky consequences:** carrier row support four, nonnegative entries, row
  and column sums one, and \(Pq=u\).
- **Falsification attempt:** an exact rational boundary point passes all
  algebraic tests on the carrier.
- **Residual:** eight carrier edges are zero, so an exact support-four
  interior point and phase lift remain open.
- **Disposition:** accept carrier-polytope existence and select the
  interior-point test.

The carrier has \(24\) allowed edges; the witness uses \(16\) and leaves
\(8\) boundary zeros.

Checker: `research/flavor/checkers/wp1158_support_four_polytope_point.py`

Result: `results/wp1158_support_four_polytope_point.json`
