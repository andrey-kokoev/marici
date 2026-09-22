# A fixed signed-refinement ladder resolves the frozen midpoint task

## Result

The earlier Nima fixed-method DPC result remains valid: its signed method was frozen at `N=1,000,000`, 192 bits and mesh 32, and returned `UNRESOLVED` on its midpoint task.

A distinct post-DPC refinement certificate uses this three-stage signed-refinement ladder:

    (N=1,000,000, bits=192, mesh=32)
    (N=4,000,000, bits=224, mesh=64)
    (N=16,000,000, bits=256, mesh=128)

The stopping rule is exact threshold separation at the first stage that has it; otherwise the prescribed output is `UNRESOLVED` after stage three. The first two stages remain unresolved. The third gives a gain lower bound above the frozen midpoint threshold, and the exact task engine returns **CERTIFIED_FEASIBLE** with its robust-inner witness.

This does not rescue or alter the DPC prediction. The ladder was chosen after exploratory analysis of the fixed-method tail, so it is a post hoc refinement certificate, not a new blinded performance prediction. It uses the same already-frozen task.

## What was learned

The fixed `N=10^6` direct signed pairing was not intrinsically incapable of resolving the midpoint task. Its certified tail/mesh enclosure was too wide for that deliberately midpoint-adjacent threshold. A predeclared increase of the prime-power cutoff, precision and archimedean mesh sufficed in this instance.

This is evidence for an adaptive signed-refinement route, not a theorem that every near-threshold task resolves by this ladder. Exact equality or a still narrower margin can remain unresolved.

The task, detector, source family, source prior, theta mass/moment bounds, H, L, and threshold-selection contract are unchanged. Only the direct signed pairing enclosure is refined.

## Verification

    uv run --with python-flint python research/grothendieck/checkers/certify_midpoint_signed_refinement.py
    uv run --with python-flint python research/grothendieck/checkers/check_midpoint_signed_refinement.py

Artifacts:

- `research/grothendieck/results/midpoint-signed-refinement-contract.json`
- `research/grothendieck/results/midpoint-signed-refinement.json`
- `research/grothendieck/results/three-channel-source-task-calibration-midpoint-signed-refinement.json`

The checker verifies the frozen task binding, the recorded three-stage schedule, unresolved status before the selected stage, exact threshold separation at the selected stage, calibration identity, and the accepted feasibility witness.
