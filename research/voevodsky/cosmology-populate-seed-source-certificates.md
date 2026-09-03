# Populate seed source certificates

## Result

The clean tracked nonmarked-K generator now emits `source_certificate` for every one of its 248 seeds. Each certificate contains a descriptor-derived target ID, ordered `T`/`S_K` origin IDs, source-basis and exact-row digests, equation-column and target digests, a normalized sparse rational coefficient word, and generator path/source digest. The generator replays every certificate against its recomputed exact rows and target before writing output.

Execution completed with exit 0: all 248 exact contractions and certificate replays passed.

## Ownership boundary

Pre-edit Git inspection reported the IBP and q generator paths as untracked, while the nonmarked-K generator was clean and tracked. Their ownership is therefore ambiguous. They were not modified. Consequently 976 certificates remain unpopulated: 16 IBP and 960 q.

## Scope

These are algebraic replay certificates. They establish neither geometric support nor a source differential, DNC specialization, or exceptional transport.

## Disposition

This leaf is partially completed and blocked at the ownership crossing. Obtain ownership authority for the untracked IBP and q generators, then apply the same tested helper and replay all remaining records.

## Verification

- `research/voevodsky/cosmology_exact_source_certificate.py`
- `research/voevodsky/check_cosmology_nonmarked_K_exact_seeds.py`
- `research/voevodsky/results/cosmology_nonmarked_K_exact_seeds_a12.json`
- command exit 0; 248 generator-internal certificate replay assertions passed
