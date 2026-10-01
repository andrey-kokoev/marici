# Fixed-tour observer under schedule violations

## Precisely declared stress model

Start with a four-reading prefix identifying the current (tour,slot). At a shared current source vertex A or B, replace that state with any slot of the OTHER tour having the same source vertex, then follow the replacement tour without further switches. The next emitted observation is the target of the newly chosen outgoing occurrence. This is a finite stress model, not a native or physical switching law.

`check_seed_observer_switching.py` reuses the actual fixed-tour observer and successor. There are sixteen possible switches under this convention.

## Exact detection result

| Additional vertex readings after switching | Cases first rejected |
|---|---:|
|1|8|
|2|4|
|3|4|

All sixteen cases eventually contradict the synchronized original history. Eight switches change the currently selected outgoing primitive edge and are detected immediately. Eight preserve that edge and are initially silent, but following the other tour thereafter causes a contradiction within three readings.

Thus none of these single sustained switches is indefinitely invisible to a synchronized full-history observer. Detecting a contradiction does not diagnose switching uniquely: corrupted readings or another model violation could also cause it.

## Four-reading memory has a conditional guarantee

After the switch and enough steps on the new tour, its latest four readings uniquely identify the new state. But the full history has no fixed-tour explanation. The checker verifies both facts for all sixteen cases.

Consequently the earlier equality of rolling-window and full-history reconstruction depends on the no-switch assumption. Automatically resetting to the latest four readings silently discards a detected violation. An implementation intending to monitor that assumption must retain a failure flag or the contradictory history/witness; reacquisition should be a separate explicit operation.

A history starting only after a switch can be a completely valid new-tour suffix. Such observations alone cannot certify that no earlier switch occurred.

## Broader hidden-mode control

A separately labelled, BROADER model permits arbitrary slot re-selection before every step, not only single sustained changes at A/B. Choosing the other tour's slot with the same primitive edge emits the same next vertex. Repeating a prescribed choice can reproduce the full edge word of a fixed tour while using different internal mode-selection records.

This control shows that endpoint/edge observations do not in general identify private scheduler labels. It is not a counterexample to the single-switch detection result, since its scheduling assumptions differ. An independently retained scheduler-change receipt is needed if that internal distinction is part of the intended observation. Fresh traversal IDs identify executions but do not themselves prove a schedule-mode change.

## Synthesis

Separate three interfaces:

1. prediction within the fixed-tour model;
2. monitoring whether new observations remain consistent with that model;
3. explicitly authorized reset/reacquisition or a supplied switching model.

The current observer implements the first and detects inconsistency for the tested second. No switching probabilities, physical costs, native emission rule or automatic reset policy were added.

## Retained monitor closure

`check_seed_observer_monitor.py` adds the three explicit statuses: tracking, inconsistent and reacquired. Tracking retains the current candidate set and episode history. The first incompatible reading latches an inconsistent state with the minimal failed prefix (its preceding prefix was still compatible). Later valid suffixes do not clear that failure.

Reacquisition requires an explicit nonempty caller reset receipt and a four-reading suffix identifying exactly one state. The new episode retains the entire rejected monitor as parent. Subsequent readings preserve this parent and receipt; a subsequent failure still retains that reset provenance. A receipt is a record of a caller choice, not an authorization proof or an authenticated native capability.

All sixteen switch cases are tested through detection, sticky failure, reacquisition, continuation and another failure. Sixty-four complete monitor records then pass through both existing rung transport candidates. Both routes preserve the records, failure prefixes, reset receipts and rejected parent episodes exactly. Candidate counts are merely diagnostic numeric payloads; the reader recovers the full records rather than treating their mean as authorization.

This closes failure handling for the conditional finite observer. These Python functions are a checked local prototype, not a secured input boundary: arbitrary externally constructed Monitor objects are not claimed to be validated or authenticated. No native source operation emits these events or authorizes the reset merely because its receipt is retained.

Further scheduling extensions are deferred. The remaining source task is the actual binding and execution/admission policy described in `native-seed-event-emission-boundary.md`. Additional finite-model experiments cannot derive that missing policy.

## Verification

    python research/nima/checkers/check_seed_observer_switching.py

Fresh checks pass for all sixteen sustained switches, exact detection delays, full-history versus rolling-window distinction, and the separately scoped hidden-mode control. Imported path, spectrum, transport and observer regressions also pass.
