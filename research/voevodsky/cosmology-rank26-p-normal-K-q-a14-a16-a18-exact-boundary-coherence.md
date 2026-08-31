# Exact rational boundary coherence at A14, A16, and A18

## Question

Does the exact source-syzygy coherence found at A12/A14/A16 survive the next even ambient degree, or was it a three-degree overfit?

## Result

Every transported-minus-local exact word is a rational source syzygy:

- A16 to A18: 72 of 72 zero evaluations, support 40–65.
- A14 to A18: 60 of 60 zero evaluations, support 53–85.

For all 60 A14 boundary coordinates, the direct A14-to-A18 difference cell equals coefficientwise the A14-to-A16 cell transported to A18 plus the A16-to-A18 cell. Direct and composite supports are 53–85 terms; residual support is zero.

## Disposition

P5d1b2 and the bounded A18 overfit test P5d1 are completed. The stable-even-degree conjecture survives through A18: exact identities and strict syzygy-cell composition now hold on the overlapping triples A12/A14/A16 and A14/A16/A18.

This additional finite triple still does not prove an ambient recurrence. P5d2 becomes active: derive or falsify a source-level recurrence that constructs the next exact identity and difference cell from bounded predecessor data. Merely checking A20 would add finite evidence but would not discharge this induction gate.

## Reproducibility

- Exact syzygies: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_exact_difference_syzygies.py`
- Composition: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_exact_difference_composition_a14_a16_a18.py`
- Results: corresponding A18 syzygy and A14/A16/A18 composition JSON files.
