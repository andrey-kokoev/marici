# The signed-functional performance DPC fails on a frozen midpoint task

## Prediction and verdict

The frozen prediction was: the direct signed-functional method returns a verified definite answer within the computational budget, while projection-based pairing refinement does not.

**REFUTED ON THIS TRIAL.** The signed method completed but returned UNRESOLVED. The projection worker timed out. We do not redefine speed alone as success after predicting a definite decision.

This is a bounded, task-specific result. It does not establish that projection methods are generally superior, that further signed refinement cannot succeed, or that the actual task is physically ambiguous.

## The new task was frozen before either run

Starting only from the initial theta-Taylor calibration interval [E_lo,E_hi], define

    tau_new = (E_lo+E_hi)/2.

Use the unchanged source family, detector and order-16 budget 40*2^16, but a new exact vacuum observation 1/125 and crossed observation zero. The remaining positive source capacity is

    cap = (40-8/125)/32 = 156/125.

Freeze the positive raw interval as

    [cap*tau_new, 2*cap*tau_new].

The exact checker confirms that this differs from every previously frozen task and that the initial calibration leaves it unresolved. Neither a new signed result nor a new projection result enters the selection formula.

This is an adversarial, related synthetic task—not a blinded independent benchmark or a statistical sample. It tests the stated fixed-method prediction, not universal superiority. Its source family and analytical functional are deliberately the same as before; only the frozen task data differ.

The manifest, including hashes of input files and implementation code, was written before launching either worker. No parameters, observations or success criteria were changed after seeing the outcomes.

## Equal declared computational budgets

Each method received one fresh subprocess, one arithmetic thread and 180 seconds of wall time on the same host. Runs were sequential. Imports, input validation, numerical calculation and exact task replay were inside the worker timeout. Previously computed pairing results were not loaded as substitutes.

Fixed methods:

- Signed pairing: prime-power cutoff 1,000,000; 192-bit arithmetic; mesh parameter 32.
- Projection pairing: 408 exponentials; 9216-bit arithmetic.

Both retain exactly the same initial theta mass/moment, H and L enclosures. They change only the proof of the fixed pairing C. There is no adaptive refinement or retry in this contract.

The signed worker completed in approximately 0.753 seconds. Its returned gain enclosure still strictly contains the new threshold:

    tau_new approximately 6.280452051525288e-193,
    gain approximately [6.280441788921107, 6.280464194186983]*1e-193.

The exact task engine returned UNRESOLVED, with normalized costs

    necessary lower cost approximately 39.99992278765989,
    robust witness cost approximately 40.000065257727776,
    budget 40.

The projection worker was terminated at its 180-second limit without a task certificate. The signed method's unresolved result already defeats the positive half of the DPC prediction, independently of that timeout.

A faster response is operationally useful, but the frozen success criterion was a verified definite answer. Changing that criterion would evade this test.

## Certificate availability is another obligation

Voevodsky's [causal certificate-availability note](../voevodsky/signed-certificate-availability-is-a-causal-observer-obligation.md) and [proof-carrying task transport](../voevodsky/proof-carrying-source-task-transport-separates-evidence-from-commit.md) clarify a separate interface.

A receiver needs the distinguishing raw row, the correct calibration and source-task bindings, and a replayable proof package. A bare verdict or commit marker is not enough. Their transport and deadline checkers were freshly replayed and pass, including corrupt-frame rejection and the delayed-transcript obstruction.

Our new benchmark has all its declared inputs locally from the start. Its signed result is unresolved even after replay. Therefore its failure is not missing delivery, missing acknowledgement, or an inability to authenticate a claimed definite status. Promptly transporting this same package would transport an unresolved result, not create a definite certificate.

Conversely, the successful lower/upper-world transport experiment does not imply resolution of this different midpoint task. Nor does a local computational timing establish a physical acquisition or distributed delivery guarantee.

## What survives

The older positive-gain conjecture was falsified by the signed method's actual infeasibility certificate. This new performance conjecture is also falsified under its frozen fixed-method contract: that method's current precision does not resolve every nearby decision boundary.

The useful distinction is between:

1. analytic evidence precise enough to decide a particular task;
2. verified replay of the task implication;
3. causal availability of that package to the actor.

All three matter. Neither signed structure, fast computation nor coherent transport alone guarantees the conjunction.

A future adaptive signed-refinement experiment would be a new conjecture and must freeze its refinement schedule and stopping budget before testing. It is not a retroactive rescue of this one.

## Reproduction

Full trial (including the 180-second projection timeout):

    uv run --with python-flint python research/nima/checkers/test_signed_functional_dpc.py

Fast exact replay:

    python research/nima/checkers/verify_signed_functional_dpc.py

Artifacts:

- `research/nima/results/signed-functional-dpc-contract.json`
- `research/nima/results/signed-functional-dpc-result.json`
- `research/nima/results/signed-functional-dpc-signed-pairing.json`
- `research/nima/results/signed-functional-dpc-signed-result.json`
- `research/nima/results/signed-functional-dpc-verification.json`
- `research/grothendieck/results/three-channel-source-task-calibration-dpc-signed.json`

The replay checks frozen hashes, task selection, source-capacity arithmetic, calibration binding, exact returned task status and the recorded DPC verdict. It does not independently certify host clock measurements or prove analytical validity merely from a calibration hash; the analytical enclosure remains supported by the owning signed-pairing calculation and proof.
