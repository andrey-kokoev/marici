# Exact rational boundary difference cells compose strictly

## Result

For each of the 48 A12 cutoff-boundary coordinates, define the exact difference cell as the transported lower-ambient source word minus the independently selected higher-ambient word. Every such cell is an exact rational source syzygy.

The direct A12-to-A16 cell was compared with the sum of:

1. the A12-to-A14 cell transported to A16; and
2. the A14-to-A16 cell.

All 48 coefficient dictionaries agree exactly. Direct and composite supports both range from 53 to 85 terms, and the total residual support is zero.

## Disposition

N5b3c2 and N5b3 are completed. Exact rational direct/composite coherence is established for the cutoff-boundary source corrections across ambient degrees 12, 14, and 16.

The coherent object is not a literally transported source representative. Literal transport failed for every target. Coherence is carried by exact source-syzygy difference cells, whose direct and composite representatives agree coefficientwise.

This is a finite ambient coherence theorem. It does not provide an unbounded ambient recurrence, a surviving p-normal quotient line, a horn comparison, a relative Bockstein, a contour, or a physical period.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_exact_difference_composition.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_exact_difference_composition.json`
- Exact syzygy prerequisite: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_exact_difference_syzygies.py`
