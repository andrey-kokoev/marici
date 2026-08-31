# Monomial-shift closure of canonical K q-lifts

## Test

The pole-0 and pole-1 canonical q-lift coefficient lists were shifted by each of the 66 retained monomials of total degree at most 10. Shifted q rows were required to exist in the degree-14 source presentation, and each resulting identity was reduced independently modulo `T + S_K`.

## Result

For each pole:

- all 36 shifts of total degree at most 7 exist and reconstruct exactly;
- all 30 shifts of degrees 8, 9, or 10 request at least one q source row beyond the retained q-monomial cutoff;
- no existing shifted identity has a nonzero residual.

Thus 72 of the 132 residual identities are generated exactly by the two canonical templates. The remaining 60 are cutoff-boundary cases, not algebraic counterexamples to the identities within their defined domain.

## Disposition

N3b3c is exhausted as a claim of complete shift closure: two templates do not generate all 132 rows inside the degree-14 truncated source presentation. Its bounded positive domain is exact through shift degree 7.

The active branch remains N3b3. The next child N3b3d should extract boundary templates at shift degrees 8–10 rather than silently extending unavailable q rows. A compact result would require at most one template per boundary degree and pole; failure would leave row-dependent boundary corrections.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_lift_shift_closure.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_lift_shift_closure.json`
