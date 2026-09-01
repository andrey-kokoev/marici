# Phase-lift obstruction: WP1160

## Question

Does the exact support-four interior point have a unitary phase lift?

## DPC resolution

- **Problem:** test phases for the WP1159 support-four modulus.
- **Conjecture:** phases can make the exact support-four modulus unitary.
- **Rivals:** phase-adjusted lift; two-overlap amplitude obstruction;
  alternate interior point; nonunitary production map.
- **Risky consequences:** row orthogonality, two-overlap cancellation, equal
  amplitude products, and phase compatibility.
- **Falsification attempt:** rows \(0\) and \(3\) overlap only in columns
  \(2\) and \(5\), but their amplitude products are \(1/1764\) and
  \(83/5292\), so cancellation is impossible.
- **Residual:** another support-four interior point may satisfy the
  two-overlap amplitude equations.
- **Disposition:** reject the WP1159 point as unistochastic.

Checker: `research/flavor/checkers/wp1160_phase_lift_no_go.py`

Result: `results/wp1160_phase_lift_no_go.json`
