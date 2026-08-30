# Commuting-square pushforward auditor

## Purpose

The auditor decides whether a new constructor rung is more information about the same acquisition or a different empirical model. Bell statistics are downstream and are not interpreted until this decision passes.

For a parent packet `P`, refined packet `R`, refinement compiler `c`, and forgetful compiler `f`, the required square is:

```text
raw acquisition --c--> R
       |               |
       p               f
       |               |
       v               v
       P ------------- P
```

The equality is exact when both views are compiled from the same immutable event ledger. Statistical tolerance is inappropriate there: every parent event identifier must occur exactly once after forgetting refinement fields, and every coarse count cell must agree exactly.

Separate-run comparisons are a different operation. They test distributional stability and require uncertainty thresholds, but they cannot certify an eventwise forgetful map.

## Admission order

1. Verify packet identity, compiler versions, setting map, outcome convention, and no-click inclusion.
2. Check event conservation: no loss, duplication, or mutation of parent identifiers.
3. Forget the newly added fields and compare every `(A setting, B setting, A outcome, B outcome)` cell.
4. Localize discrepancies by route label, frame, coincidence class, and reset identifier.
5. Only after steps 1–4 pass, compute the inherited Bell witness.

## Verdicts

- `same_experiment_refined`: the square commutes exactly; obstruction comparison is admitted.
- `selection_detected`: event identifiers or inclusive cells were removed.
- `duplication_detected`: a parent event has multiple refined descendants where the compiler promised one.
- `context_mutation_detected`: settings or outcomes changed under forgetting.
- `cross_wing_label_detected`: a nominal local refinement depends on a remote field.
- `new_experiment_required`: the apparatus or measurement map changed; register a new parent packet.

## Explanatory consequence

This instrument prevents a false explanation. A changed Bell number cannot be attributed to a newly observed local mechanism until the auditor proves that the mechanism was added without changing the empirical model. Conversely, a failed square is itself informative: it identifies the precise constructor through which selection or intervention entered.

The current execution uses synthetic aggregate packets and hostile mutations. Physical immutable event-ledger packets remain unrun.
