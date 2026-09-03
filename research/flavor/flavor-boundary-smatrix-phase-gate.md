# Boundary S-matrix phase gate: WP1259

## Question

Can boundary S-matrix phase data select a quotient matching class?

## DPC resolution

- **Problem:** materialize boundary S-matrix phase data distinguishing the
  three quotient matching classes.
- **Bold conjecture:** boundary S-matrix phases or fixed-\(q\) unitary
  moduli may select one of the three quotient matching classes.
- **Named rivals:** universal Hadamard phase; fixed-\(q\) S-matrix
  matching; sparse support-two modulus; support-three search.
- **Risky consequences:** \(H_6\) moduli are universal; matching maps are
  fixed-\(q\) and nonuniversal; fixed-\(q\) doubly stochastic maps form a
  20-dimensional affine family; 67,950 support-two patterns are tested.
- **Strongest falsification attempt:** Hadamard phases are
  class-independent, every rank-three matching fails double stochasticity,
  and every support-two pattern is linearly inconsistent with the fixed-
  \(q\) target.
- **Exact residual:** decide whether support three admits a fixed-\(q\)
  doubly stochastic solution.
- **Disposition:** retain exact phase/disjointness/support classifications;
  reject current S-matrix packet.

Checker: `research/flavor/checkers/wp1259_boundary_smatrix_phase_gate.py`

Result: `results/wp1259_boundary_smatrix_phase_gate.json`
