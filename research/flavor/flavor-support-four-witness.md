# Support-four witness: WP1156

## Question

Does a sparse maximum-row-support-four fixed-\(q\) doubly stochastic map
exist?

## DPC resolution

- **Problem:** test the next sparse class after support-three graph exclusion.
- **Conjecture:** a support-four algebraic witness exists.
- **Rivals:** support-three witness; support-four perturbation;
  unistochastic-compatible graph; nonunitary map.
- **Risky consequences:** nonnegative entries, row and column sums one,
  \(Pq=u\), and maximum row support four.
- **Falsification attempt:** the added edge \((0,4)\) is rebalanced exactly
  and passes all four algebraic tests.
- **Residual:** the witness has a single-overlap row pair and is not
  unistochastic-compatible.
- **Disposition:** accept support-four algebraic existence and select the
  support-four graph search.

The witness has \(17\) nonzero entries, row supports \((4,3,2,3,3,2)\), and
column supports \((3,3,3,2,4,2)\).

Checker: `research/flavor/checkers/wp1156_support_four_witness.py`

Result: `results/wp1156_support_four_witness.json`
