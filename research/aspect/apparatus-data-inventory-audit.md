# SCC apparatus-data inventory audit

## Result

No unindexed raw or physically calibrated SCC/optical record was found under `research/aspect`.

The fixture inventory contains only:

- `fixtures/deutsch-source-associators.v1.json`;
- `fixtures/hardware-bound-pushforward-synthetic-packet.v1.json`.

The latter declares `status=synthetic_reference`. The comparison-loop binding declares `hardware_identity_bound=false`, `physical_calibration_loaded=false`, and `physical_trials_run=false`.

`contracts/aspect-optical-bench-acquisition.v1.json` is a protocol schema. It names trial and promotion fields, including `raw_record`, `calibration_authority`, and `uncertainty_rule`, but contains no trial records or calibration payload. Its network protocol names `source_covariance`, but no measured covariance samples are included.

Repository searches under `research/aspect` found:

- no `raw_data` records;
- no `detector_pullback` dataset;
- no `loss_counts` dataset;
- no `joint_noise` samples;
- no transfer matrix outside preregistration/checker declarations.

## Reusable protocol gates

The route-residue protocol may reuse, as schemas only:

- self/pairwise overlap and orientation-loop record names;
- no-click retention and setting-health requirements;
- independent-source flags and source-covariance slot;
- confidence/tolerance fields;
- raw-record, calibration-authority, uncertainty-rule, hostile-outcome, and claim-boundary promotion gates;
- scalar comparison-loop error budgets;
- synthetic event provenance, frames, resets, bins, and coincidence-window identifiers.

## Blocking data object

The first missing object is an apparatus-bound acquisition bundle containing:

1. hardware and mesh identities with calibration authority;
2. raw complex transfer matrices with channel/mode labels and units;
3. the shell-to-mode embedding and route-frame map;
4. detector effect/pullback records;
5. emitted, transmitted, detected, and no-click/loss counts;
6. synchronized joint noise samples sufficient to estimate covariance;
7. calibration timestamps, uncertainty rules, and immutable provenance;
8. the evaluable map from those records to the radial bulk and Wilson coordinates.

Until that bundle exists, reusable gates remain protocol-level and apparatus-data status remains blocked. No physical promotion follows.
