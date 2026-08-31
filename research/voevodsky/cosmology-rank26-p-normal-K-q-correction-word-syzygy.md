# Naive correction-word difference is not a syzygy

## Test

The 12-to-14 lower-edge correction word was translated by adding 2 to every source-row second monomial exponent, then the 14-to-16 correction word was subtracted in the degree-16 module.

## Result

The differences are nonzero:

| K pole | translated terms | target terms | difference support |
|---:|---:|---:|---:|
| 0 | 30 | 30 | 39 |
| 1 | 50 | 50 | 57 |

Thus the two adjacent correction words do not differ by a zero source relation under direct vertical translation.

## Disposition

N3b5b4 is falsified. This was a stronger condition than compositional coherence requires: adjacent correction cells have different q-representative boundaries.

The proper next child N3b5b5 must construct the direct 12-to-16 correction for vertical translation by 4 and compare it with the composite of the translated 12-to-14 correction plus the 14-to-16 correction. Their difference has matching boundary and is the admissible candidate source syzygy. Failure of that comparison would exhaust the tested vertical-induction coherence route.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_correction_word_syzygy.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_correction_word_syzygy.json`
