# Correction source-word ambient compatibility

## Test

The 30-row pole-0 and 50-row pole-1 lower-edge correction words were decoded into relation-family, pole, marked-level, axis/mark, monomial, and coefficient descriptors. Monomial exponents were normalized by the target boundary coordinate before comparing the inclusions 12-to-14 and 14-to-16.

## Result

The normalized coefficient words are not identical.

| K pole | terms | 12-to-14 digest | 14-to-16 digest |
|---:|---:|---|---|
| 0 | 30 | `dc8fb421...ee63` | `5971c092...62b2` |
| 1 | 50 | `9133dc54...760c` | `4057b64b...0361` |

Thus invariant trace lengths and family counts do not imply coefficient-level transport of the deterministic source words.

## Disposition

N3b5b3b is falsified as literal normalized source-word compatibility. The source words remain exact witnesses for each inclusion separately.

N3b5b3 is not yet exhausted: two source words for compatible correction cells may differ by a source syzygy. The next child N3b5b4 should translate the 12-to-14 correction word into degree 16, subtract the 14-to-16 word, and test whether that difference is a relation among original `T` and `S_K` generators. Passing would provide a higher coherence cell; failing would exhaust this induction route at source-word level.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility.json`
