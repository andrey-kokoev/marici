# Boundary transport correction cells

## Result

Literal vertical transport of boundary q-lift representatives fails, but quotient-level transport succeeds.

For every source boundary lift, its q combination was translated by

\[
(i,j)\longmapsto(i,j+2),
\]

then the independently selected target q combination was subtracted. Every difference reduces to zero modulo the target `T + S_K` relation space.

| inclusion | differences tested | base-exact |
|---|---:|---:|
| 12 to 14 | 48 | 48 |
| 14 to 16 | 60 | 60 |

Before reduction, the differences have supports between 30 and 45 columns. They are nontrivial representative changes, not literal equality.

## Interpretation

Vertical multiplication by the second integration variable squared defines a compatible boundary transition in the quotient by `T + S_K`. The independently selected q-lift representatives are related by correction cells in that base relation space.

## Disposition

N3b5b2 is completed. The earlier literal-transition failure is repaired at the correct quotient type.

N3b5b remains active through N3b5b3: retain original `T` and `S_K` coefficients for representative correction cells and test whether those coefficients themselves transport uniformly. Current reduction proves existence but does not provide a source-natural formula or uniqueness.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_correction_cells.py`
- Results:
  - `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_correction_A12_to_A14.json`
  - `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_correction_A14_to_A16.json`
