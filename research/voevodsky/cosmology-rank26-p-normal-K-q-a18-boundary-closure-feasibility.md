# A18 boundary closure feasibility

## Question

Does the next even ambient degree remain within the bounded exact-solve regime, or do the top-three-degree source closures exhibit a new rank or depth obstruction?

## Result

All 84 A18 cutoff-boundary targets reduce over the full `T+S_K+Q` source family at prime 32003.

| pole | targets | closure range | Q-row range | maximum depth | largest system |
|---:|---:|---:|---:|---:|---:|
| 0 | 42 | 67–108 | 15–19 | 4 | 108-by-108 |
| 1 | 42 | 81–130 | 15–19 | 4 | 130-by-130 |

Every selected closure remains square. Relative to A16, maximum size rises from 110 to 130 while dependency depth remains 4. No new finite-field closure obstruction appears.

## Disposition

P5d1a is completed. P5d1b becomes active: exact-solve the 84 A18 boundary systems, materialize descriptor-keyed words, then test A14/A16/A18 exact syzygy and direct/composite coherence. This census is only feasibility evidence and does not establish rational identities or a recurrence.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_full_source_closure_census.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_full_source_closure_census_a18.json`
