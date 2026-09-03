# Empty q certificates at an independent point

## Test

Regenerate all 960 q p-normal derivative targets at the original point `(3,6,-3)` and the noncollinear point `(4,5,-3)`. Both lie on the declared p-normal wall with nonzero total energy. Exact rows were reconstructed over the same four primes; original rows were checked against stored target digests.

## Result

The support partition is identical at both points:

- 576 targets are empty at both;
- 384 targets are nonempty at both;
- no target changes class.

The partition depends only on q index. Indices 0, 2, and 4 contribute 192 empty targets each. Indices 1 and 3 contribute 192 nonempty targets each. Pole, level, and parity descriptors do not alter this split.

The empty words are therefore not peculiar to the original evaluation point. Their q-index pattern suggests a structural derivative-support rule. Two finite evaluations do not prove identity on the full p=0 source locus, so canonical zero status remains withheld pending derivation from the raw q-row constructor.

## Disposition

Derive why the nx derivative kills exactly q indices 0, 2, and 4 and not 1 and 3. Only that constructor-level identity can promote the empty certificates to structural zero words and define their transport behavior.

## Verification

- `research/voevodsky/check_cosmology_empty_q_certificates_independent_point.py` — exit 0
- `research/voevodsky/results/cosmology_empty_q_certificates_independent_point.json`
