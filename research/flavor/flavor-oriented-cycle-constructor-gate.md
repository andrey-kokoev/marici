# Oriented-cycle constructor gate: WP1203

## Question

Can an oriented cycle construct the path partial isometry?

## DPC resolution

- **Problem:** derive the partial-isometry source relation rather than
  declaring it.
- **Bold conjecture:** removing a marked return port from a lossless cycle
  derives the required partial-isometry relation.
- **Named rivals:** declared path relation; oriented boundary compression;
  microscopic flavor cycle realization; calibrated boundary readout.
- **Risky consequences:** \(C=(I-P_0)U=U(I-P_3)\); \(J=P_0-P_3\) reverses
  with cycle and port; three surviving singular values are unit; the
  uncompressed cycle has no boundary current.
- **Strongest falsification attempt:** the constructor derives normalization
  and orientation only after changing the groupoid to the stabilizer of
  marked source and sink.
- **Exact residual:** microscopic flavor cycle, map from \(J\) to normalized
  contrast, threshold intertwiner, and calibrated physical16 readout remain
  open.
- **Disposition:** construct the oriented-cycle normalizer; reject completed
  physical realization.

Checker: `research/flavor/checkers/wp1203_oriented_cycle_constructor_gate.py`

Result: `results/wp1203_oriented_cycle_constructor_gate.json`
