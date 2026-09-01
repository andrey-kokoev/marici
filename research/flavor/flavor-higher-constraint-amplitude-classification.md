# Higher-constraint amplitude classification: WP1164

## Question

What remains of the higher-constraint support-four amplitude systems?

## DPC resolution

- **Problem:** classify the remaining support-four amplitude systems after
  excluding both minimal classes.
- **Conjecture:** a higher-constraint support-four carrier may contain a
  phase-compatible fixed-\(q\) interior point.
- **Rivals:** \(C_4+C_8\) carrier; three-\(C_4\) carrier; semialgebraic
  witness; structural no-go.
- **Risky consequences:** \(16\,200\) \(C_4+C_8\) carriers, \(1\,350\)
  three-\(C_4\) carriers, \(20\) or \(24\) amplitude constraints, and
  fixed-\(q\) affine dimension eight.
- **Falsification attempt:** \(C_4+C_8\) systems have log-amplitude rank
  \(15\) and nullity \(9\); three-\(C_4\) systems have rank \(12\) and
  nullity \(12\). Neither count alone decides existence.
- **Residual:** a semialgebraic witness search over the nonlinear amplitude
  constraints remains required.
- **Disposition:** classify the higher-constraint systems and select the
  witness search.

Checker: `research/flavor/checkers/wp1164_higher_constraint_amplitude_classification.py`

Result: `results/wp1164_higher_constraint_amplitude_classification.json`
