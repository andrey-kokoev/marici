# Literal shifting of complete exact source words is falsified

## Test

For each ambient degree 12, 14, and 16, the complete exact canonical source word was shifted descriptorwise by every monomial of degree at most \(A-7\).

## Result

The test fails before linear reconstruction. Some q rows in the exact canonical word already lie near the ambient exponent ceiling. Literal multiplication moves them outside the admitted graded q family; examples include attempted pole-1 descriptors with exponents `(0,12)`, `(0,14)`, and `(0,16)` at ambient degrees 12, 14, and 16.

This does not contradict the earlier finite-field shift closure. That closure shifts only the canonical q-coefficient template and then permits a newly reduced `T+S_K` correction word. It never asserted that the complete base correction word shifts literally.

## Disposition

The original N5c3b formulation is falsified. No rational interior-family claim follows by literal multiplication of the 27-row and 45-row complete source words.

The corrected leaf is N5c3c: shift only the exact rational q template, form the corrected target, extract a fresh `T+S_K` dependency closure for each interior shift, and solve that bounded closure over the rationals. This preserves grading and tests the actual quotient statement.

## Evidence

- Failing checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_seed_exact_interior_shifts.py`
- Reproduced failures at ambient degrees 12, 14, and 16.
