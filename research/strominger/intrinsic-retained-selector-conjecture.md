# Intrinsic selection of retained transport: conjecture and native falsifier

## Conjecture

The full retained state, including its context, ordered history and coherence witnesses, determines a unique next admissible transport operation without an externally supplied stage schedule. Apparent alternatives such as PN and reader advance result from an incomplete readout. Iterating the selector produces seven-stage presentations and quarter-chart handoffs rather than imposing them.

Stronger extension: four emergent seven-stage blocks realize the proposed P/E exchange with retained suspension.

Falsifier: the same fully specified retained state admits two distinct continuations satisfying the stated constraints.

## Tested meaning of full state

Use the existing `GenerativeAssemblyRules` contract, augmented by explicitly retained ordered operation history and actual complex coefficient values. The source snapshot includes:

- active packet, realization origin and full five-slot coefficients;
- every retained packet, chart and primitive cell;
- all marked reference points, including context outside the active cell;
- occurrence/phase frames;
- ordered operation history with coefficients before and after each event;
- assembly contact witnesses and currently offered operations.

Two fresh replays produce byte-equivalent semantic snapshots before branching. Snapshot hashes and complete source records are retained in the receipt. Generated geometry caches are implementation details, not extra physical state.

## Result: uniqueness fails under this contract

Test all24 ordered seed markings and four exact history prefixes:

1. empty history;
2. one reader advance;
3. two reader advances;
4. PN followed by inverse-PN, retaining both the operation history and the N packet.

For each of the96 identical-source forks, both futures pass:

    S -- PN ------------------> N -- NE --> E
    S -- reader advance --> P' -- PN --> N' -- NE --> E'.

These are not two encodings of one retained endpoint: their origins differ by one, their full coefficient vectors differ for the chosen nondegenerate preparation, and their ordered histories differ.

Both branches satisfy the existing checks for native occurrence identification, phase increments, invertible coefficient transport, actual shared faces, global C/M role consistency and contact witnesses. Each extends to an E exit with every retained packet able to reach an exit and every occupied cell on an entry/exit path. All required contacts are witnessed and no pending contact remains.

This gives **192 certified continuations from96 retained sources**. A nonempty PN/inverse-PN history is not collapsed to the root: the snapshot retains its N packet and both events, and branching still survives. The failure is therefore not repaired by retaining those histories.

Hostile controls confirm that a wrong coefficient permutation or phase increment is rejected by the native validator.

## What this does and does not refute

**Refuted:** the claim that the implemented native retained-state and assembly admissibility rules already leave exactly one next operation. Adding the tested ordered histories and requiring an eventual certified E exit do not select one.

**Not refuted:** a fully specified richer global theory that adds a selection constraint or distinguishes the admissible kinds of next step. This audit does not supply every analytical esd7 witness or an unconstructed global field state. Such a theory must declare those data before replaying the test; simply calling an unspecified state more complete is not a testable repair.

Also, two admissible successors do not rule out the mathematical existence of a deterministic selector. One can impose a preference. They show that uniqueness does not follow from the current admissibility contract.

PN has phase increment0; reader advance has phase increment1. The grammar does not identify these with the same physical time step. A requested event type or task may be the missing input, rather than additional hidden state. Each operation kind can already have a unique local realization without there being a unique kind to execute next.

## Consequence

Do not derive a seven- or28-stage clock from admissibility alone. Before another geometric or Fourier construction, specify what a **single next evolution step** means and what source-backed rule selects its operation kind. Preserve this fixture as a regression gate for that proposal.

## Task-relative follow-up

The [task-relative test](task-relative-retained-transport-conjecture.md) now fixes an observable realization-advance task as well as the retained state. Eight N fixtures still admit two certified continuations. Requiring the same carrier versus crossing a face separates those choices where either task is available; this is a geometric task requirement, not an emergent stage clock.

## Reproduction

```sh
node research/strominger/checkers/check_intrinsic_retained_selector.mjs
```

**98 named checks passed; native-contract uniqueness falsified.** [Receipt](results/intrinsic-retained-selector.json) includes all96 complete source snapshots, both certified continuations for each, coefficient histories and source hashes. Native constructors are unchanged.

Related: [native FCC end-to-end binding](native-fcc-end-to-end-binding.md), [earlier native candidate audit](global-28-stage-pe-candidate-audit.md), [global28-stage conjecture](global-28-stage-pe-fibration-conjecture.md).
