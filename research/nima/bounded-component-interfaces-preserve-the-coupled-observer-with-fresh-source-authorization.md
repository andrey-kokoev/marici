# Bounded component interfaces preserve the coupled observer with fresh source authorization

## DPC disposition

The bounded-interface DPC is **corroborated for the declared atomic interface contract**. A cached-position interface fails; an explicit source-authorized interface preserves every permission and output of the frozen protocol and supports its origin-audit extension.

The implementation has three separately maintained components:

| Component | Retained state | Local carrier size |
| --- | --- | --- |
| Source authority | current endpoint mask; faithfully retained origin bit | 18 |
| Acquisition buffer | absent or one immutable source-bound observation frame | 3 |
| Recipient ledger | delivered frame or absence; issued value or absence | 5 |

Their unconstrained local product has 270 combinations. Only **70** are jointly reachable. These correspond bijectively to the verified 70-state origin-audit observer and project onto its 62-state current observer. No complete source word or execution journal is exchanged.

The comparison covers all 638 original coupled states and 11,484 reference state/action checks. Checked initialization and one-step correspondence establish the result for every finite interleaving of declared operations, not merely selected traces.

## Frozen outputs and interfaces

The outputs remain the typed source corner, locally received validated value and issued value. Preservation of all numerical assembled-observer readouts is not claimed.

A compact observation frame contains the run binding, task binding, actual vacuum-row binding, observation corner (0,3), and value zero or one. In this finite contract all metadata are fixed; each component stores either no frame or its value, with a decoder restoring the immutable bindings. This is a finite representation, not a general compression claim for arbitrary certificates.

The source authority stores the current endpoint and the origin bit initialized from the known initial prefix. The prefix [0,1] initializes one; [1,0] initializes zero. The source need not retain subsequent event order or retained marks because those details do not affect the frozen protocol's remaining guards and outputs.

Ports are explicit:

- **Source advance:** source-local check of the actual unused-event/workflow rule.
- **Acquire:** source authority checks that the current endpoint is mask 3 and evaluates the declared unit vacuum row. The acquisition buffer stores precisely that authorized record, if empty.
- **Deliver:** the named acquisition buffer supplies its exact immutable record; the recipient validates its bindings and stores it. Duplicate delivery is idempotent.
- **Issue:** the recipient requires its delivered value, no prior issuance, and source authorization that event 3 has occurred. It can issue only the matching value.
- **Audit origin:** the source authority tests its faithfully retained origin bit against the requested value.

Each component reads only its own state and the declared port response. The acquisition component does not inspect the recipient ledger. The recipient does not reconstruct the source word or read the producer's private state outside the delivery port.

## Attacks on insufficient interfaces

### Stale acquisition permission

Start with the canonical prefix and no acquired record. Advance through event 3, then request acquisition.

The reference rejects: acquisition was authorized only at the earlier cut. An acquisition component using cached mask 3 instead accepts. The stale interface invents an acquisition permission after its allowed cut has passed.

### Stale issuance permission

Acquire and deliver the earlier record, then advance through event 3 and request the matching issuance.

The reference now accepts. A recipient still using cached pre-cut source position rejects. Thus stale information can cause false rejection as well as unsound admission.

These failures identify the missing interface obligation: source position used to authorize a cut-sensitive operation must be authoritative at its declared linearization point.

### Individually valid components need not form a valid joint state

Consider endpoint 11 and origin one, with producer record one but recipient record zero. Every local component state occurs somewhere in the protocol, but their proposed combination is unreachable. The recipient's zero record cannot have been delivered by that producer in this execution.

The composition therefore retains a source-bound message constructor and checks joint reachability; it does not admit arbitrary Cartesian products of valid local states.

## The repair and its atomicity boundary

The repaired acquisition and issuance operations consult the source authority at the declared operation's atomic linearization point. Source validation and the associated local commit are part of that operation. Delivery transports the exact source-authorized buffer contents.

This is an explicit semantic requirement, not a theorem about arbitrary network delays. The checker exhausts interleavings of these atomic operations, including rejected stutters and duplicate-delivery loops. It does not exhaust unmodeled interleavings inside an RPC or prove that a distributed implementation supplies the required linearization points.

A later asynchronous implementation must either prove a refinement to these ports or introduce explicit reservation, delivery and availability states and compare the resulting behavior under a new contract. The stale-position counterexamples forbid simply declaring an ordinary cached snapshot equivalent to this authority port.

No claim about physical acquisition time, common commit barriers, message loss or irreversible distributed action is established here.

## Verified behavioral correspondence

Each original source/evidence state maps to

    (endpoint, origin bit, producer record, received record, issued value).

The producer explores the reachable implementation graph from both known initial source orders. For every one of the 18 labels at every original state, the implementation and reference agree on acceptance, rejection and successor image. Rejection leaves the state unchanged.

The implementation maps onto all 62 old observer classes and bijectively onto all 70 extended classes. All outputs and transition squares commute. Its extra eight distinctions are precisely the retained origin distinctions needed for the specified upgrade, not a hidden execution journal.

The old class plus the source-local origin bit agrees everywhere with the previously verified lift table. Thus the declared upgrade is possible after any old-language execution, provided the origin bit was initialized truthfully and retained faithfully.

## Integrity is not authentication

Changed run, task, row, observation corner and invalid value fields are rejected. But a fabricated same-run zero/one value can be syntactically well formed. Field checks or hashes cannot establish that it was actually acquired in this run.

Soundness instead depends on the declared execution constructors: the source authorizes the actual value, the acquisition buffer stores that exact frame, and the reliable delivery port transports that same frame. These are trust and admission assumptions. An authenticated channel, crash-recovery mechanism or defense against an equivocating source is not supplied.

Likewise, a corrupted origin bit can select the wrong upgraded state. The interface does not recover erased provenance by compression.

## Reproduction

    python research/nima/checkers/check_compositional_observer_interfaces.py
    python research/nima/checkers/verify_compositional_observer_interfaces.py

The producer freshly invokes the existing quotient/lift verifier. The independent interface verifier reconstructs the component transition rules, checks reachability and all reference comparisons, verifies both quotient maps and the origin-bit lift, and replays the stale-permission and mixed-state controls. Both pass.

Artifacts:

- `research/nima/results/compositional-observer-interface-contract.json`
- `research/nima/results/compositional-observer-interfaces.json`
- `research/nima/results/compositional-observer-interface-verification.json`

The result is a usable finite component contract and a precise boundary: bounded state suffices, but separately maintained components must exchange correctly bound records and obtain the source authorization their cut-sensitive operations require.
