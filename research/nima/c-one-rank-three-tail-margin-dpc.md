# Coherent c=1 rank-three certificate — prime-support retraction

## Correction

The directed rank-three certificate is retracted. Its prime-component artifact was replaced by `marici.grothendieck.interval-c-one-prime-and-jets.invalidated.v1` with no valid rows.

## Exact defect

The earlier prime-power loop was capped at `1024`, but the undilated baseline and translated profiles have support-derived cutoffs reaching `3495` and `13978`. Therefore the cells consumed by the Gram certificate omitted supported prime powers. Positive Sylvester minors computed from those cells do not certify the support-complete form.

Execution `structured_command_execution:e_13072_1788355108188546900_4` verifies the durable invalidation and retracts interpretations of executions `structured_command_execution:e_11792_1788314192719668300_41` and `structured_command_execution:e_11792_1788314363951379100_44`.

## Surviving result

The exact Sylvester robustness theorem remains conditional: any valid entry boxes inside the tested margins imply rank-three positivity. The directed moment intervals and outward-quantization method also survive. No unconditional coherent c=1 Gram certificate remains.

## Reopening condition

Implement a faster exact spline evaluator or partition support-complete prime sums into resumable certified chunks through each profile's actual cutoff, then regenerate the entry boxes and rerun the independent Sylvester consumer.

## Evidence

- `research/nima/checkers/check_c_one_n4_artifact_gram.py`
- `research/grothendieck/results/interval-c-one-prime-and-jets.json`
