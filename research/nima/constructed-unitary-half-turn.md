# Operational unitary half-turn: assembled

`agda/TickConstructedUnitaryHalfTurn.agda` constructs
`operational-machin-half-turn : OperationalMachinHalfTurn`.

The record combines the checked all-scale flow with both endpoints of the **same** `phase machinPi`:

- `phase machinPi zeroCompletion = oneComplex`;
- `phase machinPi oneCompletion = complex (-oneCompletion) zeroCompletion`;
- the flow's norm, continuity, and all-increment derivative specialize to that same `machinPi` and operational phase.

Opaque law presentations prevent unnecessary unfolding of Taylor schedules during record checking; public definition equalities expose both exact endpoint types. No operational law is assumed.

## Verification boundary

The operational record is kernel-proved. Its identification with standard pi remains the **explicitly operator-accepted written proof**, pinned through `results/pi-mixed-level-accepted.json`. Neither the Agda module nor the receipt claims kernel verification of the standard-real interpretation.

Fresh safe `--ignore-interfaces` closure passed in **1541.065 seconds**. The checker also validates and pins the accepted identification evidence, including stability across the kernel run. Receipt: `results/constructed-unitary-half-turn-fresh.json`.

The net records `operational-unitary-half-turn` as **++ at the accepted mixed level**. The two earlier +- attempts remain in its history; they are not rewritten as successes.

## Next goal

`prove/operational-spectral-whole-return-certificate` is now the only ready unresolved node. It still requires complex/tensor operator algebra, external metric interval and gluing, local unitarity and native endpoints, piecewise generator compatibility, reconstruction/swap coherence, fixed-source faithfulness, and explicit correspondence to the exported standard witness. This half-turn record does not discharge those obligations automatically.

```text
python research/nima/checkers/check_constructed_unitary_half_turn.py --timeout 3000
python research/nima/checkers/test_completion_refinement_net.py
python research/nima/checkers/test_completion_refinement_planning.py
python research/nima/checkers/check_completion_refinement_planning.py
python research/nima/checkers/check_completion_refinement_net.py
```
