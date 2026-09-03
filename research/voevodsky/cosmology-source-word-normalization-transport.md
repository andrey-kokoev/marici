# Source-word normalization and transport audit

## Result

All 1,224 certificates pass canonical normalization:

- 1,224 globally unique descriptor-derived target IDs;
- family-typed bases: IBP uses `T`, K uses `T` and `S_K`, q uses `T` and `Q`;
- basis indices are unique and ordered;
- every stored rational is nonzero, reduced, and has positive denominator;
- basis, row, equation-column, and target digests are structurally complete.

No certificate contains a transport record. The aggregate states square transport and naturality conclusions in prose, but it does not serialize the action of multiplication by either squared axis on target IDs and ordered source-basis IDs, the transported coefficient word, or a commutation residual. Transport stability of the serialized words is therefore unverified.

## Oddball

Of 960 q certificates, 576 have empty source words and zero-dimensional exact systems; IBP and K have none. The certificates replay because their reconstructed target rows are empty. This is an unresolved observation until one distinguishes a source-derived zero target from vanishing caused by the fixed protocol evaluation point or descriptor indexing. The cheapest discriminating test regenerates representative empty and nonempty q targets at an independent admissible exact point and compares support.

## Claim boundary

Retained: all A12 seed contractions are normalized and generator-recompute replayable.

Withheld: stability of their coefficient words under arbitrary-even constructor transport. No geometric, differential, DNC, or exceptional claim follows.

## Verification

- `research/voevodsky/check_cosmology_source_word_normalization_transport.py` — exit 0
- `research/voevodsky/results/cosmology_source_word_normalization_transport.json`
