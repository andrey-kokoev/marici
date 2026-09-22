# Causal dependency closure repairs noncompositional observer minimization

## Structural result

The critical-path DPC has a concrete finite construction and a counterexample to its naive alternative.

**Minimizing components for their isolated user-visible behavior and then combining their states is insufficient.** On the actual coupled protocol, the intersection of those local equivalences has 61 classes, but the combined current language requires 62.

The missing distinction is exposed by the alternating word

    acquire ; deliver.

A dependency-derived interface retains it. The constructed interface has 70 jointly reachable states, presents the current 62-state observer as a view, and supports the declared 70-state origin-audit observer without recovering discarded history.

The governing distinction is between **what a component currently displays** and **what another component can later make observable through its interface**.

## 1. Freeze rules before synthesis

The contract fixes the actual source/acquisition/delivery/issuance protocol, its origin-audit extension, observable rejection, and the output tuple

    (typed source corner, locally received value, issued value).

Operational guards and updates are represented as a small explicit expression language. Variable reads are inspectable; there are no opaque callbacks that can secretly inspect a source history. Variable ownership, initialization and source/task/run bindings are declared separately.

The state vocabulary is end, origin, pending, received and issued. This vocabulary and the operational semantics were supplied from the already constructed protocol. The experiment does **not** claim to discover physical causal laws or unmentioned historical dependencies automatically.

The interface extractor runs before reference graph exploration or minimization. The existing 62/70-state quotient certificates are consulted only for subsequent validation.

## 2. Construct the retained interface from dependencies

The constructor starts with fields read by the declared outputs and admission guards. It closes that set under the update expressions of retained fields, then assigns requirements to their owning components.

It produces:

| Component | Derived retained fields |
| --- | --- |
| Source authority | endpoint, origin |
| Acquisition | pending record |
| Recipient | received record, issued flag |

Cross-component requirements are generated per operation and separated into guard reads and accepted payload reads. For example:

- acquisition needs the current source endpoint for authorization, then the actual source-bound value for its accepted update;
- delivery needs the pending record that will become locally received evidence;
- issuance needs the delivered value, issuance state and current source authorization;
- origin audit needs the retained initialization distinction.

Rejected actions do not fetch update payloads. Guard validation and accepted update refer to the same stipulated authoritative snapshot. Field reads are delivered only under the fixed source/task/run binding.

This is an executable dependency-closure construction, not a definition of the interface as whatever the eventual global quotient happens to need. Its semantic adequacy is tested against the independently bound reference.

## 3. The actual mixed-continuation counterexample

Consider the two known initial prefixes [0,1] and [1,0], both at corner (0,3), with no acquired, delivered or issued record. Their current user-visible outputs agree.

Restrict the current language separately to:

- source advances;
- acquisition;
- delivery and issuance.

The two states are equivalent under every one of these isolated languages:

- source advances alone do not reveal the origin through the declared outputs;
- acquisition alone changes the pending record but not the received value or issued result;
- the recipient alone cannot deliver a record that has never been acquired.

Nevertheless, acquisition followed by delivery yields different locally received values, zero and one. The two operations together expose a distinction absent from each local behavioral quotient.

The three local partitions have 43, 44 and 61 classes. Their joint partition has 61 classes. The full current language has 62. Thus plain local minimization does not commute with composition even on this small actual protocol.

These partitions use the same frozen user-visible output tuple on the common state carrier. They are not the richer boundary-aware component interfaces produced by dependency closure.

## 4. Why boundary closure repairs this failure

The accepted acquisition update depends on the source origin, and delivery depends on the pending record. The dependency chain is explicit:

    retained source distinction -> pending observation -> received value.

The intermediate pending record is not a current user verdict, but it is observable to a future consumer. Eliminating it—or identifying source states that will produce different such records—would erase a dependency crossing the component boundary.

The derived local carriers have sizes 18, 3 and 5. Their source-compatible reachable product has 70 states, not all 270 Cartesian combinations. For example, source origin one with pending value one and received value zero is individually plausible component-by-component but jointly unreachable.

This construction therefore needs both:

1. dependency-complete interfaces;
2. joint admission of their bindings and state combinations.

Neither a product of local states nor equality of current verdicts supplies the second condition.

## 5. Views and upgrades of one retained causal state

The constructed 70-state carrier yields the existing current 62-state observer when viewed through the current language. Under the declared origin-audit extension, it yields the 70-state minimal observer.

The current view can compress more aggressively because eight origin distinctions no longer affect its current continuation language after the acquisition cut. The retained interface keeps those distinctions because the anticipated audit still requires them.

Every selected field has an exported omission witness: two reachable states agree on the other four coordinates but belong to different extended observer classes. This establishes necessity relative to the proposed coordinate representation and frozen extension, not a universal lower bound on every possible encoding.

All 638 original concrete states and 11,484 state/label cases match the reference. Complete distinguishing-word certificates establish the 62- and 70-state minimal quotients. Correct initialization and one-step correspondence cover arbitrary finite declared interleavings, including rejection and duplicate-delivery loops.

## 6. What the constructor refuses to infer

An action referring to an undeclared historical field, such as delivery-before-cut, fails dependency validation. The constructor does not invent the missing bit, its initialization or its update law. A new extension needs a newly justified declaration before claiming preservation.

A foreign source/task/run binding is rejected. A tuple of locally valid but jointly incompatible component values is outside the reachable admitted carrier.

These checks are not authentication. Truthful origin initialization, faithful retention and source-authorized delivery remain assumptions. Nor does static dependency extraction prove that a delayed network implementation supplies the stipulated atomic source checks.

No coupling to the separately bound theta-task evidence family is manufactured. The analytical branch results motivate the same principle—retain what future combination needs—but remain a different admitted object until explicit cross-protocol constructors are provided.

## 7. Higher-level disposition

The unqualified equation “joint minimization equals the intersection of isolated local minimizations” fails here.

The repaired, tested principle is:

> Construct source-bound, dependency-complete interfaces first; then derive observational quotients appropriate to the declared language.

This explains why acquisition history can be redundant when its consequences persist, why origin provenance can remain necessary after those consequences vanish, and why a current verdict is often too compressed to support future interaction.

It does not resolve all structural DPCs universally. The result covers this explicit operational family and its audit extension. Analytical truth, decision separation, real delivery bounds, authentication and undeclared future operations remain independent obligations.

## Verification

    python research/nima/checkers/construct_causal_observer_interface.py
    python research/nima/checkers/verify_causal_observer_interface.py

Artifacts:

- `research/nima/results/causal-interface-construction-contract.json`
- `research/nima/results/causal-interface-construction.json`
- `research/nima/results/causal-interface-construction-verification.json`

The independent replay reconstructs the read-dependency closure and ports, checks the concrete transition semantics and reachability, verifies both minimal quotients and their distinguishing words, checks the local congruences and mixed counterexample, and rechecks every reference transition comparison. Both runs pass.
