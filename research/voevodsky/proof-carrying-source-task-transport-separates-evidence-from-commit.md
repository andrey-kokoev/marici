# Proof-carrying source-task transport separates evidence from commit

## Result

The deadline experiment now transports a compact **replayable task frame**, rather than treating B's conclusion as a trusted message. A receiver with the declared signed calibration can recompute the certified status and necessary cost from the frame.

Each frame binds:

- the signed-pairing calibration SHA-256;
- the frozen-input package SHA-256;
- private/reuse mode, budget and automatic-witness policy;
- all three exact raw interval records;
- claimed status and exact necessary cost;
- the corresponding portable source-task chain SHA-256.

The receiver rejects a changed calibration binding, status claim, necessary cost, positive row, or a missing positive row. The result is task-specific sufficiency, not a claim that this JSON representation is information-theoretically shortest among every possible encoding.

## Why the positive row is the causal dependency

The two valid frozen worlds share the entire coarse payload

    vacuum = 1/100,
    crossed = 0,

but differ in the positive raw interval. Under the same signed calibration one is `CERTIFIED_FEASIBLE` and the other `CERTIFIED_INFEASIBLE`.

Consequently the coarse rows cannot determine a definite answer for this pair of worlds. This is a direct necessity result **within the declared contrasting task family**. It does not establish a universal lower bound for all source tasks or all encodings.

The calibration binding is equally essential: with the older theta-only calibration these same tasks are unresolved. A receiver needs both the distinguishing source row and the specified signed refinement, not merely a clock signal or an asserted conclusion.

## Integration with deadline availability

`check_signed_certificate_deadline.py` now transports these frames. With fast delivery, A independently replays B's certificate at the deadline. With delayed delivery, A sees the same coarse transcript in the two opposite worlds and safely abstains.

Thus the causal dependency graph is explicit:

    raw positive row + signed calibration identity + source-task contract
        -> replayable frame -> local definite task certificate.

Mutual acknowledgement is downstream of local proof availability and is not needed for the independent deadline policy tested here.

## Reproduction

Create and validate the frames:

    uv run --with python-flint python research/voevodsky/checkers/certify_signed_task_transport.py

Use them in the causal deadline experiment:

    uv run --with python-flint python research/voevodsky/checkers/check_signed_certificate_deadline.py

Artifacts:

- `research/voevodsky/results/signed-task-transport.json`
- `research/voevodsky/results/signed-certificate-deadline.json`

This remains a conditional reliable-message experiment over fixed mathematical artifacts. It does not assert a physical measurement, authentication infrastructure, delivery guarantee in an open network, or a universal consensus result.
