# Dependent transport at unchanged endpoints

## Result

The unfinished transport test now has an explicit object syntax, local reduction rules, and a checked interpretation into the existing circle double cover.

Active SCC obligations: forward realization, attachment transport, and route/coherencer compatibility.

Formal source: `agda/DependentTransportMachine.agda`.

This is an owner-local companion extension of `research/voevodsky/resolution-net-v1/dependent-machine.md`. The existing choose/flip machine remains unchanged. The two syntaxes are not yet integrated into one evaluator.

## Source and executable rules

Routes contain a variable, an identity route, a circle turn, or an ordered pair of consecutive routes. Terms contain a Boolean literal or a transport instruction with a route and a body. No constructor accepts a host-language function as its execution rule.

Every interpreted route starts and ends at the same base index of `IndexIdentityCoherenceRegression.F`. Its Boolean fiber is the double cover. The supplied circle loop acts by Boolean negation.

The directed rules remove identity transport, execute a turn on a literal, split consecutive transport, and reduce inside a transport instruction. The machine is defined before its semantic interpreter.

| Test | Computed result |
|---|---|
| Identity route on true | true |
| One circle turn on true | false |
| Two consecutive turns on either Boolean | The original Boolean |
| Substitute a turn for the route variable | Exposes the one-turn instruction |

`one-loop`, `two-start`, `two-middle`, and `two-end` check the actual progress function by computation. `normalizes` constructs a finite reduction trace to `run t` for every closed term. This proves a terminating execution exists; it does not assert an all-schedule termination theorem or uniqueness of reduction histories.

## Substitution and semantic preservation

`plug-id`, `plug-compose`, `plug-term-id`, and `plug-term-compose` prove substitution laws for routes and terms. `plug-step` proves that substitution preserves reduction steps.

The interpretation sends route composition to path composition in the existing index type. `step-sound` proves that every reduction preserves the expression's interpreted value. `substitution-sound` proves agreement between syntax substitution and semantic substitution. `run-sound` proves agreement between the independent evaluator and actual dependent transport.

A transport instruction can change its input Boolean while reduction preserves the meaning of the complete instruction. These are different statements.

## Erasure controls

`no-endpoint-only-action` excludes any single Boolean function that claims to implement all routes at these endpoints. Identity transport and one turn give incompatible outputs on true.

`no-route-decoder` excludes recovery of all route syntax from one output Boolean. `no-action-decoder` excludes recovery even from the entire induced Boolean function. Identity and two turns have the same Boolean action but distinct source syntax.

The latter theorem concerns route syntax. This module does not prove that all distinct syntax denotes distinct circle paths, or classify circle winding numbers.

`Completed` retains the source term alongside its result and semantic correctness witness. `source-recovered` checks exact source recovery.

## The certification form

For a fixed source term, `RetainedRun` contains an output and its semantic correctness path. `result-certificate` proves that this type is contractible, with the independently computed output as center. `higher-certificate` certifies that certificate type.

The certificate covers the output and its correctness witness. It does not contract the source route type or the type of execution histories.

## Assumptions and remaining scope

The proof uses Cubical Agda, the existing circle higher inductive type, and the univalent Boolean double cover. The turn instruction's flip rule is supplied explicitly and then proved sound for that family. It is not derived from substitution or from the certification form alone.

This fragment supports one base index, its Boolean fiber, open route variables, identity, positive turns, and composition. It does not implement general dependent binders, arbitrary families, object-level path comparisons, inverse-route syntax, or higher transport syntax. The original cover's no-global-section theorem remains in the checked dependency closure.

## Verification

Fresh safe Cubical compilation and the deliberate endpoint-erasure rejection passed:

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module DependentTransportMachine -ReceiptStem dependent-transport-machine -NegativeModules DependentTransportBadErasure
```

The expected rejection attempts to identify the computed false output of one turn with true. The runner checks the false/true diagnostic and stable source, library, and compiler hashes. Execution reference: `structured_command_execution:e_25120_1791062349223758200_237`.

Receipt: `results/dependent-transport-machine-formal-audit.json`.
Source-bound audit: `checkers/check_dependent_transport_machine.py`.
