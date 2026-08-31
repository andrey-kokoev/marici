# Exact rational A18 cutoff-boundary identities

## Question

Do the 84 square A18 boundary closures survive exact rational reconstruction, or does the next even degree expose a characteristic-zero obstruction hidden by modular closure?

## Result

All 84 A18 top-three-degree K targets have exact rational `T+S_K+Q` source words. Every selected 130-by-130-or-smaller system is nonsingular and reconstructs the complete target.

- Targets verified: 84 of 84.
- Largest system: 130 by 130.
- Maximum coefficient denominator: 18,816.
- Source words are retained by typed descriptor for subsequent transport tests.

No A18 characteristic-zero identity obstruction appears. The maximum denominator is lower than at A12, A14, and A16, so coefficient height does not grow monotonically across these finite samples.

## Disposition

P5d1b1 is completed. P5d1b2 becomes active: verify that A14-to-A16, A16-to-A18, and A14-to-A18 transport differences are exact A18 source syzygies, then compare direct and adjacent-composite difference cells coefficientwise.

This exact solve extends finite evidence by one degree. It does not establish an unbounded recurrence or induction theorem.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_exact_all_solves.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_exact_all_a18.json`
