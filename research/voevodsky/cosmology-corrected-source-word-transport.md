# Corrected source-word transport audit

## Result

After repairing the target interface from p-tangent `T` rows to `nx` derivative rows, all 2,448 shifted bases solve with the original coefficient words. No coefficient changes and no basis enlargement are required.

The previous 780 span failures were checker artifacts caused by comparing different derivative directions.

## Claim boundary

This verifies A12-to-A14 algebraic transport only. A16 composition and all geometric comparison data remain unverified.

## Verification

- `research/voevodsky/check_cosmology_corrected_source_word_transport.py` — exit 0
- `research/voevodsky/results/cosmology_corrected_source_word_transport.json` — 2,448 resolved, zero changed
