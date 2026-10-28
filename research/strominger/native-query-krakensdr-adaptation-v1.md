# KrakenSDR adaptation for the frozen native-query fragment

Status: desk-level adaptation and fail-closed hardware inventory template. No hardware inspected, assembled, calibrated, energized, or authorized by this document.

## Purpose and scope

Adapt the existing KrakenSDR conducted-RF plan to test whether the actual available kit realizes any of the eight frozen native-query generators. Do not presume it does. The frozen task is `contracts/native-query-source-fragment.v1.json`: a 12-label A4 carrier and Boolean pointer, two triangle left actions, six state-dependent pointer XOR queries, all on every `(g,b)` and composable as arbitrary literal words. The mathematical target pairing is in `contracts/native-query-realization-equivalence.v1.json`; it does not supply a physical RF encoding, preparation, reader, or apparatus law.

The existing KrakenSDR successor tests conventional RF component composition and joint-IQ observation. That is useful infrastructure but is not this compiler. A calibrated scalar transfer function, five coherent receiver channels, or controlled marker flip does not by itself implement the 12-state carrier, six equality-controlled writes, or the two A4 translations.

## Hardware inventory gate (first action; no energizing)

Populate `contracts/native-query-krakensdr-inventory.template.v1.json` from the actual kit. Record make/model/serial/firmware, physical presence and condition, connectors, manuals and port limits, available passive parts, and which instruments can transmit, receive, route, switch, store, or control. Distinguish operator recollection, label/manual claim, and measured fact. Attach dated photos/manual references and provenance; do not infer that the historical SDG2042X, KrakenSDR, DHO924, NanoVNA and divider/cable list is present or serviceable.

Inventory is complete only when all signal paths and unused-port terminations can be drawn and all active outputs and safety limits identified. This gate authorizes no connection or powered test. Then independently review safe link budget and manuals before any energization decision.

## Operation-by-operation capability audit

For each proposed encoding, fill a transition table on all 24 target basis states and a physical operation table. A candidate must say how every input carrier label and pointer label is prepared, how its complete successor is retained, and how auxiliaries return. Record unavailable operations as unavailable; do not substitute software relabeling, postselection, a detector-created label, or a new mixer/control.

| Frozen operation | Required action | RF capability question |
|---|---|---|
| `L_ABC`, `L_ADB` | Permute all twelve carrier labels by the exact left action; leave pointer unchanged | Is there a characterized coherent, low-loss twelve-mode permutation/router with repeatable inverse and composition? |
| Each `Q_xy` | Leave carrier label intact; toggle pointer iff the named equality predicate holds | Is there a physical conditional interaction coupling the encoded carrier mode to a writable two-state pointer, on all labels and both pointer inputs? |
| Every word | Execute chronologically with intermediate state and literal history retained | Does concatenation preserve the same encoding, reference frame, calibration and returned auxiliaries, without hidden reset? |
| Reading | Read pointer at authorized boundaries without destroying future continuation | Is there a separately justified nondestructive readout, or is the actual instrument explicitly destructive and therefore a different contract? |

The KrakenSDR is a receiver, not an assumed controlled actuator. A two-channel AWG, splitter, cable delay, attenuation insert, or scalar phase response must not be treated as a coherent mode router or controlled XOR absent a measured and source-matched operation.

## Candidate encoding and falsifiers

No encoding is selected. During inventory, consider only encodings the present hardware can physically prepare and access. For each candidate, provide an explicit injective map from the twelve labels and pointer states into measured RF modes/fields, an operation dictionary for all eight generators, and an observation map. Check the complete table, not only one initial state or output scalar. If the available kit only gives scalar conducted transfer blocks, document that mismatch rather than extending the apparatus silently.

A candidate operation passes a mathematical interface test only if its predicted physical transformation agrees with the frozen basis transition table on every one of the 24 states, its inverse/return behavior is specified, and its independently calibrated uncertainty bound is within a frozen tolerance. Then test arbitrary finite words on sealed compositions. Endpoint-only agreement is insufficient: compare retained intermediate records and auxiliary returns. Preserve unexecuted words as untested.

## Calibration sequence after a separate safety authorization

1. Verify inventory, current manuals, DC/bias state, terminations, link budget and safe margins.
2. Calibrate source, receiver channels, coherent reference, passive paths, cross-talk, linearity, drift and joint noise; retain raw IQ, power/loss, no-signal and no-click/missing records.
3. Freeze a candidate encoding and operation hypotheses using pilot data only. Use independently calibrated component/actuator maps; do not fit each target generator or held-out composition independently.
4. Freeze numerical tolerances, uncertainty propagation, randomized order, calibration/evaluation partition, and held-out words before evaluation labels are opened.
5. Compare physical transition estimates with the exact target action under the frozen realization-equivalence contract. Report failure/incompatibility as such; no post-failure primitive additions within this version.

This is not currently an acquisition preregistration: tolerances, calibration, encoding, operation inventory, and safety evidence are unfilled. Hardware energization remains unauthorized by this packet.

## Immediate deliverable

Complete the inventory template from actual hardware. The first decision is a capability disposition, not a bench run: (a) identify a present operation source for each required primitive, (b) locate a concrete missing capability, or (c) state that evidence is insufficient. Only after that should a revised physical-model contract be considered. Any enlargement (extra router, nonlinear interaction, memory, or feedback) needs an explicit new model/version and fresh review.
