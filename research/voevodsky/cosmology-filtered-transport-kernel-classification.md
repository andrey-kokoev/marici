# Filtered transport-kernel classification

## Result

All 24 exact kernel dimensions now have explicit quotient representatives.

- eight generators use one quotient-coordinate term;
- sixteen use two terms;
- every generator is supported in a single exponent-parity sector.

The representatives are verified by mapping their exact source quotient coordinates through the relevant squared-axis embedding and reducing to zero in the target filtered quotient.

## Relation to the twelve classes

No tested distinguished class ray lies in an immediate kernel: all 24 A14 and 48 A16 transported classes remain nonzero. This excludes intersection for each individual one-dimensional ray at the tested steps.

It does not establish injectivity on the two-variable cyclic span generated jointly by the twelve classes. A linear combination of transported orbit elements could meet one of the explicit parity-pure kernels even though each generator survives separately.

## Claim boundary

Coordinates use the fixed exact row-echelon convention in the algebraic pole filtration. They have no DNC, exceptional, or geometric interpretation.

## Verification

- `research/voevodsky/check_cosmology_filtered_transport_kernel_classification.py` — exit 0
- `research/voevodsky/results/cosmology_filtered_transport_kernel_classification.json`
