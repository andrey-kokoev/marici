# Event-sourced control — Sontag research entry

## Governing conjecture

**The common system underlying mathematical construction and physical processes admits a natural event-sourced control representation: states arise from admissible event histories, operations extend those histories, and observations and feedback respect their composition and retained witnesses.**

[Work net](contracts/event-sourced-control-work-net.v1.json) · Research recipient: `marici.Sontag`.

The net attaches to the foundational common-process, identity–continuation, mathematics, physics and same-source nodes. Its cross-references connect the existing WG programme and potential RH examples at their declared interfaces.

## First task: `typed-event-control-interface`

Construct a common interface table using three existing examples:

1. Whole-package WG composition, recovery and retained proof histories.
2. Strominger's energy gain/probe/controller trace with predictive state `(a,b)`.
3. Your contextual capability example: authority/resource contexts changed by `grant` and `replenish`.

For each, specify:

- initial context and source task/success relation;
- state and history types;
- typed events, preconditions, payloads and witnesses;
- control choices, external/context changes and observation events;
- history extension, replay/reconstruction and composition laws;
- observations, policy information and resource effects;
- the claimed equivalence of states or histories and its continuation scope.

State explicitly which records make replay sufficient. Where information is partial, type the reconstructed information state or compatible-state family. Include observations of disturbances and nondeterministic results according to the chosen model. Distinguish a control decision from an event that the controller merely observes.

The deliverable is an interface contract with concrete event dictionaries and commuting maps. Use source functions already present in the cited packets. Event order denotes construction/composition order; the physical branch supplies any physical-time map.

## Existing results already populated

| Node | Scoped result |
|---|---|
| `retained-history-composition` | Existing WG recovery/composition and source relation attachment witnesses |
| `energy-predictive-quotient` | `(a,b)` predicts energy under the declared gain schedules; safe controller accounts for probe state changes |
| `total-energy-is-sufficient-state` | Rejected by equal current H/means giving H/4 versus H/16 under the same gain |
| `contextual-capability-witness` | Your grant/replenish example distinguishes contexts with identical immediate capability |
| `static-coordinates-determine-plant` | Your Coherent Resolution audit identifies the missing transition/actuation maps; the m=3 middle-entry field defeats boundary-only reconstruction |

Exact source paths are in `artifacts`. Eighteen files are pinned. These are existing scoped results; the population checker validates their provenance snapshot without rerunning their scientific suites.

Your [control-factorization programme](../sontag/control-factorization-programme-index.md) remains the broader control research index. This net packages the new common-system conjecture and reuses its relevant constructions.

## Research structure

```text
WG + energy + contextual capability + static audit
                     |
           typed event/control interface
             /             |              \
 history/state congruence  feedback       physical binding
          |                |                    |
 presentation naturality   |                    |
          +----------------+                    |
 mathematical control realization               |
          +-------------------------------------+
                       |
             same-source comparison
                       |
               extension/coverage
                       |
                  root assembly
```

The state-congruence test transports admissible future interventions and observations under fixed context/resources. Use both the energy hostile and the source relation-attachment witness. Naturality then checks admitted presentation changes and policy transport.

The physical binding names a concrete process, preparation/intervention/readout maps, resource accounting and time interpretation. Select that candidate from available source evidence. If the next action is solely awaiting an external object, mark the node `deferred` with a typed `blocker` and `reopening_condition`; keep it off the actionable frontier.

Coverage has its own gate: specify the intended task classes, generation/completion principles and quantifier order for extending the bounded examples.

## Net mechanics

- **14 nodes:** three scoped constructions, two rejected candidates and nine open tasks.
- `depends_on` records research prerequisites. A counterexample is usable resolved knowledge for successor design.
- Positive assembly additionally requires the named `required_verdicts` to be `constructed` on compatible witnesses.
- Formal four-valued `outcome` is separate and currently null.
- Add research notes/checkers/receipts to `artifacts`, cite their IDs on the affected nodes, then record the scoped verdict.
- Preserve rejected candidates. Changed event vocabularies, state quotients, task classes or resource policies get successor candidates.
- Recompute `frontier` from open nodes with resolved predecessors; update `recommended_start`, or set it to null if none remain.
- For changed evidence, review the source change, choose a fresh pin path and run the checker with `--pin`. Existing pin files are retained.

## Validation

```sh
python research/aspect/scc/scc.py check event-sourced-control-net-v1
```

Direct checker: `research/nima/checkers/check_event_sourced_control_net.py`.
Result: `research/nima/results/event-sourced-control-net-validation.json`.

Thirteen corruption controls cover dependency cycles, unknown edges, lost counterexamples/context, physical gating of mathematical research, same-source and coverage bypass, premature assembly, stale frontier, untyped deferral and stale evidence pins.

Fresh SCC closure passed with 18 source pins and all 13 corruption controls. The handoff to Sontag was admitted in proposal `ep_83e4db3b-00d5-4d47-9d8f-806a9084bc42` (uncommitted). No active computation remains.

The registry entry and foundational navigation are updated incrementally. Local changes are this handoff, the control work contract, Nima checker/pins/result/SCC manifest and registry/navigation entries. Existing research contracts and source-owner files are unchanged. No commit or push.
