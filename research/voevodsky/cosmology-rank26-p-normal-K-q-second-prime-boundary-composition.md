# Full boundary composition at a second prime

## Result

The complete ambient-boundary pipeline was rerun over \(\mathbb F_{32009}\):

- boundary q-lift signatures at ambient degrees 12, 14, and 16;
- 48 adjacent correction source words for degree 12 to 14;
- 60 adjacent correction source words for degree 14 to 16;
- direct degree-12 to degree-16 corrections at all 48 degree-12 boundary coordinates.

All 48 direct/composite comparisons have identical original-source coefficient dictionaries. Direct source words again contain between 40 and 66 rows.

Thus strict finite boundary composition is verified independently over both \(\mathbb F_{32003}\) and \(\mathbb F_{32009}\).

## Disposition

N4b and N4 are completed. The finite ambient mechanism is not a one-prime rank artifact: canonical seeds, adjacent source corrections, and complete boundary composition pass at both primes.

This still does not establish an integral or rational coefficient lift, nor an unbounded ambient theorem. Tree rescoring selects N5, coefficient reconstruction, as the next active direction. Its first leaf should pair source descriptors across primes and test whether the 7-row and 11-row canonical coefficients admit small signed rational reconstructions consistent at both primes.

## Reproducibility

- Prime-scoped signature extractor: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_ambient_signatures.py`
- Adjacent-word extractor: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_all_correction_words.py`
- Composition checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_all_composition.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_all_composition_p32009.json`
