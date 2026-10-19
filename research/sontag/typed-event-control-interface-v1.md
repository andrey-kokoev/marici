# Typed event/control interface v1

## Scope and result

A source-derived interface for three bounded instances: whole-package WG construction, declared energy gain/probe control, and contextual capability. This is an interface construction, not a universal plant theorem, physical binding, or proof of the successor congruence/naturality gates. Task and success relation are explicit base data, never inferred from a scalar observation.

## Common dependent interface

Fix context C, initial retained state s0:S(C), task τ, and success relation Successτ on retained states or histories. An event dictionary supplies:

- Event(C,s), including payload, provenance and actual witnesses;
- Admit(C,s,e), a dependent precondition/witness type;
- step(C,s,e,w):(C',s'), including declared resource effects;
- observe(C,s,r), where r specifies the admitted reader and its information scope;
- a role tag: control decision, external/context event, observation, or construction.

A history is a dependent chain of admitted event records, not an untyped list. Replay folds step from the recorded initial context/state. Append is defined only at a matching terminal interface. Concatenation preserves all event payloads and witnesses. Its empty-history and associativity laws are those of typed chain concatenation; semantic comparison of alternative source expressions requires the source's comparison witnesses, not literal equality.

The required squares are:

`replay(h ++ [e]) = step(replay(h), e, witness)`

`read(h) = observe(replay(h), reader)`

For a task summary π, a square `π(step(s,e)) = stepτ(π(s),e)` is asserted only for its declared event vocabulary. No quotient of all histories is claimed here. No event order is interpreted as physical time.

Nondeterministic or externally chosen outcomes must be retained as result payloads and admission witnesses. Replay reconstructs the recorded outcome, not the unrecorded counterfactual. Partial information is a compatible-state family I, not an invented fully observed state.

## Dictionary A: retained WG construction

Source: `research/nima/whole-package-generators.md`, `research/nima/agda/WholePackageResolution.agda`, and `research/nima/composable-witness-specialization.md`.

- Context: universe level, dependent index types, generator policy, base WG and refinement interfaces.
- Initial state/history: supplied `Complete` seeds and their resolution derivations. `Complete` contains code and an actual interpreted value.
- Task/success: declared output code/type and an actual complete output with requested recovery/comparison certificates. Merely forming a path code is not success when a filler is requested.
- `E-whole`: payload entire family `F:I→Complete` and selected `i:I`; admission is dependent typing; result retains every entry, including unselected branches.
- `Pi-whole`: payload `I,F`; result retains family and resolved values. No finite enumeration is required for arbitrary index types.
- witnessed comparison: payload complete endpoints, map `e`, and actual proof `p:e(value(a))=value(b)`; admission checks the boundary type.
- resolution: `Resolve` records the generator and every premise derivation; seed inclusion and flattening retain the source histories.
- indexed refinement composition: payload `F:Refinement(L)` and `G:Refinement(compile(F))`; actual extra witnesses are retained as dependent pairs `(e,f)` where `f` can depend on `(r,e)`. `Composite.correct` compares full endpoint-plus-witness packages. `Composite.rebase` is required for the third operand; it is not optional endpoint matching.
- Observation: `El(Code)`/interpreted value or explicit recovery maps; this is a mathematical reader, not a physical detector.
- Role: construction choices supplied by the caller; no actuator authority or arbitrary filler discovery is implied.
- Resources: universe levels and supplied witness obligations. Reifying the entire `Complete` raises the universe level. No source runtime-cost model is supplied.
- Replay sufficiency: actual code, values, families, generators, premise derivations, maps and proof payloads must be retained. Endpoint-only records fail the proof-dependent fixture.
- Equivalence: retained identity, inverse, composite and higher comparison packages, at their stated boundaries. Behavioral units/associativity are witnessed comparisons, not equality of all source records.

## Dictionary B: declared energy task

Source functions: `EnergyTaskState`, `gain_step`, `infer_components` in `research/strominger/checkers/energy_task_reduction.py`; `safe_probe`, `target_gain`, `finish_after_probe` in `research/strominger/checkers/energy_target_controller.py`.

- Context: declared model, admitted gain domain `[0,1]`, exact reader/provenance and retained original source; no physical apparatus is supplied.
- State: `(a,b)` with nonnegative components plus provenance. Predictive observation `H=a+b`; provenance remains in the retained record even when a predictive quotient ignores its text.
- Task/success: requested `h` with `0≤h≤Hcurrent`; success is exact final `H=h`, reached through admitted contractions without reset or amplification.
- `gain(q)`: control choice with exact payload `q`; precondition nonnegative components, provenance, `0≤q≤1`; result `(q²a,q⁴b)` and parent/result/q record.
- `read-total`: exact abstract observation of `H`, retaining reader scope and value. This model reader has no additional state change; physical back-action is unspecified, not assumed absent physically.
- `probe`: composite `read-total; gain(q); read-total`. Retain initial total, chosen gain and after-reading. It changes state through the gain; there is no reset event.
- `identify`: informational reconstruction using `infer_components(H,Hafter,q)` with `0<q<1` and nonnegative inferred values. It recovers the pre-probe components, then `gain_step` reconstructs the current probed state.
- Policy information: before probing, `I(H)={(a,b)≥0:a+b=H}`. Under a gain, transport this family by `(a,b)↦(q²a,q⁴b)`; intersect with the after-reading constraint. Two exact readings identify a unique pair for nontrivial q. Choosing `safe_probe(H,h)` uses only the available initial total and target.
- Feedback: for `0<h<H`, choose `qprobe²=(1+h/H)/2`; infer components and choose `target_gain` from the UPDATED state. Boundary targets use the source's direct endpoint rules, not the interior probe rule.
- Resource effect: visible model energy changes; source/provenance remains retained. No sink, memory reset, reservoir, noise margin or physical timing is supplied.
- Continuation scope: gains and exact energy readings only. Equal current H does not imply equivalent continuation behavior: `(H,0)` and `(0,H)` give H/4 and H/16 for q=1/2.

Gain composition has the explicit summary square `gain(r,gain(q,(a,b)))=gain(rq,(a,b))` on numeric components. Provenance histories on the two routes differ and must remain distinguishable as retained records.

## Dictionary C: contextual capability

Source: `research/sontag/checkers/contextual_capability_coalgebra.py`, functions `advance`, `enabled_actions`, `context_trace`.

- Initial context/state: `(actor,budget)` in `{observer,controller}×{0,1}`.
- Task/success: caller-declared capability task, e.g. availability of `set1`; success is `set1∈enabled_actions(context)`. This is NOT execution of a state-repair operation.
- `grant`: context event with payload command `grant`; `advance` sets actor to controller and preserves budget.
- `replenish`: context event setting budget to 1 and preserving actor.
- Admission: declared finite context/command vocabulary. The source function is permissive on other strings, so the interface rejects them before dispatch.
- Roles: context updates are externally supplied/observed unless a separate grant/replenish authority is admitted. The finite function does not authorize the controller to issue them.
- `read-enabled`: observation via `enabled_actions`; only controller with budget 1 exposes noop/set0/set1.
- Replay: initial full context plus command sequence suffices; `context_trace` records the observations along replay.
- Resources: replenish changes availability; grant changes authority. No budget consumption or implementation of set0/set1 exists in this source. Do not manufacture either as an executable plant transition.
- Equivalence: immediate capability is not a context-update congruence. Full contexts (or the one-step contextual signatures in the source) distinguish the four cases. With partial context knowledge, retain the compatible-context set and transport it through `advance`.

## Acceptance and remaining gates

The three dictionaries instantiate the same dependent history/replay/observation shape without identifying their state or witness types. Controls, construction choices and externally observed context events are distinguished. The static Coherent Resolution descriptor is not a fourth dynamic instance: source transition/actuation maps remain absent.

The accompanying executable check reuses the two Python source interfaces, tests replay/composition, probe targeting from updated state, compatible-state identification, invalid event rejection and the two hostile quotients. WG evidence is source-level reuse of existing typed maps, NOT a fresh Agda recheck or executable Python imitation. General continuation congruence, presentation naturality, feedback realization, physical binding and coverage remain successor obligations.

Contract owner is Nima. This owner-local packet does not alter or resolve the work-net contract; source-owner review and evidence-pin update are required before advancing its frontier.
