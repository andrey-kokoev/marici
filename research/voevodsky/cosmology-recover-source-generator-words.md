# Recover source-generator words

## DPC conjecture

The exact seed JSONs durably encode canonical source-generator words sufficient for a downstream geometric comparison.

Rivals are that `full_reconstruction` is only a solver outcome, that coefficient vectors existed only transiently, or that raw-relation provenance is external and unreferenced.

Risky consequences are canonical target IDs, source-basis digests, sparse rational coefficient words, equation digests, and checker paths.

## Falsification

Across 1,224 IBP, nonmarked-K, and q seed records, zero records contain all five fields. Many records assert `full_reconstruction=true`, but none serializes the basis or coefficient word. The reconstruction therefore cannot be replayed, compared, or geometrized from the durable result.

The conjecture is rejected. Exact absorption remains a checker result, but its witness words are not a durable interface.

## Disposition

Regenerate exact certificates with canonical IDs, basis and equation digests, sparse rational words, and checker provenance. The next leaf defines that serialization and deliberate replay contract.

## Verification

- `research/voevodsky/check_cosmology_recover_source_generator_words.py` — exit 0
- `research/voevodsky/results/cosmology_recover_source_generator_words.json` — zero of 1,224 records recoverable
