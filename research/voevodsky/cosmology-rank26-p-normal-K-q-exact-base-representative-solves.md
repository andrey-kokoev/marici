# Exact rational representative interior base corrections

## Result

Canonical, median, and maximal-size dependency closures were solved over exact rational arithmetic for both K poles at ambient degrees 12, 14, and 16.

All 18 rectangular systems have full source-column rank and reconstruct the complete corrected target. The largest tested system is the degree-16 pole-1 maximal closure with 170 source unknowns and 190 retained equations.

The largest denominator is stable across shifts and degrees:

- pole 0: 1,134;
- pole 1: 1,111,065,984.

Thus maximal closure size introduces no new denominator beyond the canonical exact q template.

## Disposition

The representative phase of N5c3c2b is completed successfully. No exact obstruction appears at canonical, median, or maximal closure size.

The leaf remains active through an all-shift completion: run the same exact rectangular solve for every one of the 224 corrected targets. The representative results justify this bounded expansion but do not themselves prove the complete interior family.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves.py`
- Results: corresponding `..._a12.json`, `..._a14.json`, and `..._a16.json` files.
