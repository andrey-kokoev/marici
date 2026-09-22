# The positive-middle-gain conjecture is falsified by signed pairing

## The prediction and its refutation

The conjecture was explicitly:

    E_actual > tau,  tau = y_lower/(499/400),

for the frozen middle-threshold task, with unchanged detector, observations and order-16 source budget. It predicted compatibility and a source witness strictly within budget.

The newer owning calculation, [Signed fixed-hat pairings resolve the frozen middle case](../grothendieck/signed-fixed-hat-pairings-resolve-the-frozen-middle-case.md), contradicts that prediction. Fresh numerical and exact checker runs passed.

Approximate displays are:

    E_upper = 6.280464194187088e-193,
    tau     = 6.280468234234755e-193,
    tau-E_upper = 4.0400476672693204e-199 > 0.

The actual comparison is performed on exact rational endpoints. Because the certified enclosure contains the actual gain, E_actual <= E_upper < tau. The strict-gain conjecture is **falsified**, not merely uncorroborated.

Both private and reuse middle tasks are CERTIFIED_INFEASIBLE. The normalized necessary cost is bounded below by approximately

    40.000025679423985 > 40.

Even the largest possible certified gain requires more positive source amplitude than the prior permits after paying for the separately measured vacuum coefficient 1/100. Additional coefficients cannot cancel the nonnegative prior cost or repair the separately labelled local reading.

## What changed in the proof, not the experiment

The signed-pairing method evaluates the relevant fixed functional through the actual digamma/von Mangoldt response law. It does not enlarge the detector or add measurements. Its proof retains signed finite contributions, rigorous whole-cell Taylor remainders, origin cancellation and complete prime-power tail bounds.

The deployed filters, frozen observations, source family and prior remain unchanged. Their hashes are checked against the earlier attack contract. The 408-dimensional projection timeout remains a historical failure of that particular bounded attempt; it is neither used nor reinterpreted as a mathematical obstruction.

The fresh checks were:

    uv run --with python-flint python research/grothendieck/checkers/certify_signed_pairing_task.py
    uv run --with sympy python research/grothendieck/checkers/check_signed_pairing_task.py
    python research/grothendieck/certificates/verify_source_task_transition.py research/grothendieck/results/portable-source-task-transitions/private-middle_threshold-signed-pairing.json
    python research/nima/checkers/falsify_positive_middle_gain_conjecture.py

The portable task verifier checks exact task implications conditional on the analytical enclosure. The owning signed-pairing proof supplies that enclosure; it is not independently reproved by the portable task verifier.

Artifact: `research/nima/results/positive-middle-gain-conjecture-falsification.json`.

## Relation to coherent cut reversal

Voevodsky's [history/possibility cut reversal](../voevodsky/history-and-possibility-swap-under-coherent-cut-reversal.md) is consistent with this result. Joint relation transport preserves admitted developments; it does not create them. If a genuine transport of the fully constrained joint fiber were supplied, its bijectivity would preserve emptiness.

The cut-language checker was also freshly replayed: all 255 nonempty length-three languages and 20,480 composition instances pass. That finite construction still does not supply a reversal map for the assembled noncommutative, marked and calibrated observer. We do not infer physical reversibility or an actual dynamic history from it.

Here the conclusion is an empty compatible fiber for the frozen data/prior contract—not two admitted histories requiring opposing actions. Neither Cartesian recombination nor reversal of a description can rescue feasibility under that same contract.

## What survives criticism

The earlier feasibility prediction must be abandoned. The evidence supports a different explanation: the norm-only pairing enclosure hid an actual budget incompatibility, and evaluating the relevant signed functional exposed it.

The broader methodological proposal—seek enough analytical structure to decide the fixed task without new acquisition—succeeded in this instance, but with the opposite answer from the conjecture. This is not evidence for universal timely decidability, and it makes no assertion about physical observations or sources outside the declared model.
