# Two actuator profiles are not the controller's predictive memory

**Iteration 1 of the requested ten-turn work-net run.**

**Strength:** exact finite predictive quotient for the supplied segmented machine, with an explicit reconstruction residual. Not a derivation of physical memory, a source update law or independent outputs.

[Current work net](contracts/seed-composition-work-net.v1.json) · [Previous bilinear gate](BILINEAR-CONTROLLER-GATE.md) · [Checker](check_controller_memory.py) · [Receipt](results/controller-memory.v1.json)

## Fresh starting state

The live work net still leaves `admissible-composition-and-independent-separation` and source correspondence open, with no formal outcomes. Recent local checks construct conditional synchronized continuation and two algebraic controller product profiles. They do not supply native control or correlated preparation.

This turn tests a narrower candidate: whether the current right-profile choice is enough context to run the supplied controller. It is not. A small predictive state refinement suffices, but its source realization remains open.

## 1. Declare what prediction must preserve

The 18-state controller has twelve macro-boundary states and six internal composite states. The observation contract retains:

- the output pair and current vertex;
- the owner-labelled primitive arrow emitted next;
- whether that primitive step completes the current macro-edge;
- future counts of these labelled events, including continuation branching.

A completion **marker** is observed, not the full identity of the completed macro or its earlier history. Those identities remain in the original retained records. Changing this observation contract can change the minimal predictor.

## 2. Exactly sixteen predictive classes

There are precisely two pairs of states with the same future behaviour under this contract:

1. first-output boundary BC and the internal state after AB within first-output AC: both must emit BC, complete a macro and then offer the same first-output continuations at C;
2. second-output boundary BA and the internal state after CB within second-output CA: both must emit BA, complete a macro and then offer the same second-output continuations at A.

They are states (1,14) and (10,16) in the existing zero-based controller order. All other states remain distinct.

The checker builds a coefficient-summing quotient Q:Q^18→Q^16. For every labelled primitive/completion transition P_l, it constructs a reduced transition Pbar_l and verifies exactly

    Q P_l = Pbar_l Q.

These identities prove preservation of all future labelled event-word counts by induction, not just through an enumerated finite depth. The initial pair/vertex observations are preserved as well.

Minimality is independently certified: every remaining pair of classes is distinguished either by its initial pair/vertex or by its first-event count signature. Thus no further identification of these starting contexts preserves the stated observations. This is minimality among predictive state identifications, not a claim about the minimal dimension of every possible signed linear representation.

## 3. The current actuator bit is insufficient

At the first output's A, compare boundary AB with boundary AC. Both choose the same primitive AB and therefore the same right-product profile. But:

    boundary AB --AB--> macro completed,
    boundary AC --AB--> macro still in progress.

The same pair, vertex and actuator profile therefore require different completion events. A second witness occurs at the second output's C: boundary CA and boundary CB both emit CB, but only the latter completes immediately.

The two actuator profiles proved sufficient for the coefficient table do not by themselves encode the continuation state. A profile is a command issued by the controller, not a reconstruction of that controller's memory.

After pair and current vertex are retained, there are at most two predictive classes at each attachment. Hence a local binary **parse-state code** is enough to represent the remaining distinction in this supplied finite machine. The receipt gives the entire encoding and reduced transition table.

This is a conditional classical state encoding. It is not a physical qubit, a thermodynamic bit-cost statement or an already-derived source memory. Macro-boundary branching still requires the specified choice/update operation; the table does not select its own execution policy.

## 4. Preserve provenance instead of replacing it with prediction

Q merges coefficients by addition within the two equivalent pairs. It has a two-dimensional kernel. To recover the original eighteen current-state coefficients, retain the two differences

    r1 = x_1 - x_14,
    r2 = x_10 - x_16.

For each pair, its sum and difference recover the two entries by half-sum and half-difference. The checker verifies an exact decoder for the stacked (Q,r1,r2) map, whose rank is eighteen.

These residuals recover the finite current-state coordinates only. They do not reconstruct arbitrary earlier histories; the source path ledger must continue retaining those.

The old unlabelled aggregate micro-matrix already annihilates these two difference directions, because the respective predecessor states have identical aggregate futures. This is another reason not to treat an endpoint-state propagator as a lossless history carrier.

The two new quotient residuals are distinct from the six rejected preparation directions in the preceding audit. They belong to different carriers and must not be merged by matching dimensions or labels.

## 5. Refined next gate

The current construction obligation is now:

1. maintain the output-pair attachment and current vertex;
2. realize and update the local parse-state distinction;
3. issue the appropriate one of the two right-product profiles;
4. preserve both predictor-quotient differences, the six preparation-reject directions and the full history provenance;
5. derive the boundary branch-selection policy and correlated preparation from source operations rather than assigning them to obtain the mode.

The quotient reduces redundant predictive state but does not supply those operations. The broad work-net node remains open; there is a nonredundant executable continuation: test the local parse-state update and boundary-choice rule against the existing retained source.

## Verification

```sh
python research/scattering/seed-composition/check_controller_memory.py
python research/scattering/seed-composition/check_controller_memory.py --check
python research/scattering/seed-composition/check_bilinear_controller_gate.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The new checker recomputes the earlier controller, verifies every labelled transition square, first-event distinguishability and exact residual reconstruction, and records input/checker hashes. It writes only its own receipt. Existing pinned contracts and formal outcomes are unchanged.
