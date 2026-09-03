# Repaired transport composition at A16

## Result

The repaired labelled transport was composed along four two-step paths from A12 through A14 to A16: x4, x2y2, y2x2, and y4.

- 262,112 descriptor-composition checks passed across `T`, `S_K`, `Q`, and `nx` target generators.
- All 4,896 transported certificate equations have zero exact residual.
- The x2y2 and y2x2 transported-word digests agree for every certificate.
- Rational coefficients remain unchanged along every path.

Thus the labelled exponent-shift map composes on the tested A12/A14/A16 presentations, and the two squared-axis generators commute. Together with the constructor identity, this supplies the finite generating coherence needed for iteration.

## Claim boundary

This is a source-typed algebraic morphism on finite labelled relation presentations. Promotion to every even ambient degree requires stating and checking the induction domain and boundary closure. It still supplies no source differential, geometric support, DNC specialization, exceptional comparison, or horn consequence.

## Verification

- `research/voevodsky/check_cosmology_repaired_transport_composition_a16.py` — exit 0
- `research/voevodsky/results/cosmology_repaired_transport_composition_a16.json`
