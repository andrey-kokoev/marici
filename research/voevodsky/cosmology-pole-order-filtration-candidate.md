# Pole-order filtration candidate

## Result

Define the column grade by K-pole order plus the five q levels. Give each `T`, `S_K`, or `Q` generator the maximum grade of its incidence-row columns. This yields a finite exhaustive increasing filtration of the A12 algebraic presentation.

All 43,564 incidence rows preserve the filtration. All 87,128 squared-axis transport checks preserve grade. The column grades range from 5 through 12; generator grades range from 6 through 12.

## Falsification

This is not a DNC filtration. No center ideal, Rees parameter, generic/special fiber map, or proof identifying pole grade with an induced I-adic filtration exists. A fabricated DNC record containing only pole grades is rejected.

## Disposition

Retain the exhaustive transport-compatible pole-order filtration. Do not populate the DNC-filtration contract field.

The first missing typed object is a source-derived DNC center ideal and Rees construction. Its acceptance test is recorded once. Continue to the independent executable exceptional-specialization interface audit rather than opening a waiting-only DNC branch.

## Verification

- `research/voevodsky/check_cosmology_pole_order_filtration_candidate.py` — exit 0
- `research/voevodsky/results/cosmology_pole_order_filtration_candidate.json`
