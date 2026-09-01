# Support-five unistochastic candidate: WP1170

## Question

Does a constrained support-five fixed-\(q\) polytope contain a numerical
unistochastic candidate?

## DPC resolution

- **Problem:** search the zero-diagonal support-five polytope under unitary
  constraints.
- **Conjecture:** a real orthogonal fixed-\(q\) witness exists.
- **Rivals:** polygon-only obstruction; real orthogonal witness; complex phase
  witness; exact algebraic certificate.
- **Risky consequences:** zero diagonal, thirty nonzero entries, orthonormal
  rows and columns, and row \(q\)-expectation \(1/6\).
- **Falsification attempt:** numerical optimization converged to a real
  candidate with maximum residual \(5.95\times10^{-9}\).
- **Residual:** the candidate is numerical; exact real-algebraic certification
  remains open.
- **Disposition:** accept a bounded numerical candidate and select
  exactification.

Checker: `research/flavor/checkers/wp1170_support_five_unistochastic_candidate.py`

Result: `results/wp1170_support_five_unistochastic_candidate.json`
