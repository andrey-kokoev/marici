# Adjacent exact syzygy cells do not stabilize literally

## Conjecture

A single ambient-independent adjacent syzygy cell, transported by vertical descriptor shift, supplies the recurrence from degree A to A+2.

## Test and result

For corresponding boundary coordinates, the shifted adjacent cell from the first edge of each triple was compared coefficientwise with the adjacent cell on the second edge.

| triple | cells | stabilized matches | residual support |
|---|---:|---:|---:|
| A12/A14/A16 | 48 | 0 | 53–85 |
| A14/A16/A18 | 60 | 0 | 53–85 |

Literal adjacent-cell stabilization is falsified on every tested coordinate. Strict direct/composite coherence does not imply that successive adjacent cells are equal.

## Disposition

P5d2a is falsified. An ambient-independent fixed correction cell cannot serve as the induction recurrence for these selected exact representatives.

P5d2b becomes active: test whether normalized adjacent cells obey a finite-order dependence on ambient degree, while retaining the distinction between a fitted coefficient pattern and a source-derived recurrence. With only three adjacent edges available, any polynomial fit is underdetermined as a theorem; admissible progress requires a constrained relation with a new-degree falsifier or derivation from source constructors.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_exact_adjacent_cell_stabilization.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_exact_adjacent_cell_stabilization.json`
