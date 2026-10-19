# Iteration12: task-scoped continuation maps and actual-source hostiles

## Fresh task

The44-node net recommended `continuation-interface`, with the fixed conditional schedule and actual relation/energy examples. The new interface makes command and observation domains explicit rather than inferring reusable identity from a shared dimension or current readout.

## Formal interface

`ContinuationInterface.agda` defines a System with State, step and observe for a fixed Command/Observation task. A Map(A,B) supplies a state map f plus:

    f(step_A(s,c)) = step_B(f(s),c)
    observe_B(f(s)) = observe_A(s).

Agda proves that such maps compose and preserve observations after EVERY finite command word. The proof is conditional on the two supplied laws; it is not evidence that an arbitrary quotient satisfies them.

This is forward task preservation. Reflection, source reconstruction and equivalence of complete retained packages require extra inverse/recovery data. Equality of current observations is neither the step law nor an inverse. The interface covers the total operations declared here; admitting a partial/dependent operation would additionally require transporting its domain and witness, not merely its numeric result.

## State/action/observer/retention table

| Instance | Retained source/context | Declared action/task | Observation | Result |
|---|---|---|---|---|
| Fixed schedule | generated packet, typed binding, forest, grouping policy, d and returned trace | explicit comparison-reference offsets | weighted residual | projection to (weighted mean,d) commutes with tested offsets and their composition |
| Same schedule, broader task | same complete forest/policy | one more retained incoming-family promotion | outer-row count | equal leaf/readout projections do NOT identify32-row and1-row continuations |
| Relation attachment | actual source-derived right-b matrix and coefficients | local linear right-b action | resulting coefficient vector | replacing the attachment with disconnected graded action changes a->ab into a->0 |
| Relation detector | actual nonzero product and zero arrow with SAME endpoints | inspect retained product coefficient | selected coefficient | equal terminal recorder values do NOT supply the detector |
| Energy hostile | actual invertible shared-leg preparations | existing q=1/2 gain | next declared energy | equal current energy and all family means give H/4 versus H/16 |

The schedule operation is an explicitly declared software change to the comparison reference, not a free physical reset or a coordinate change claimed to preserve the old absolute reference. The returned execution trace keeps all preceding states; each terminal still retains its source packet and grouping policy. The step updates the reference assignment and regenerates the checked Terminal object, so stale reference metadata cannot masquerade as a valid continuation.

For both schedule policies, the upper and lower route terminal objects agree for the task while their original construction histories remain distinct. Sequential offsets agree with their summed-offset command. Extending the task to inspect a further outer-family promotion distinguishes the previously equal projected states.

The relation action is the previously checked local module action, including its zero extension on incompatible basis summands. It is not a claim that the underlying typed product arrow can itself be concatenated with b at incompatible endpoints.

The energy test reruns `check_energy_task_reduction.py`, including the actual shared-leg construction. No invented scalar example replaces it. The positive energy predictive quotient and probe/update interface remain the separate next node.

## Verification boundary

The universal finite-word/composition theorem is kernel-checked. The concrete source instances and counterexamples are exact executable checks; this turn does not install them as Agda Map values or infer all-command instance correctness from finite tests. The schedule reference laws also follow directly from exact additive offset composition, but the generic theorem's hypotheses remain visible.

Executed:

    uv run --with sympy python research/strominger/checkers/check_native_continuation_interface.py

Plain environment Python lacked sympy; the successful replay uses the explicit uv dependency environment. The runner replays the actual schedule, relation and energy sources, then performs fresh safe Cubical checking with ignored interfaces and stable inputs. Receipts: `research/strominger/results/continuation-interface-v1.json` and `research/strominger/results/native-continuation-interface-agda-v1.json`.

Eight source checks pass, including four scoped hostile distinctions. These are continuation counterexamples, not a claim of a general mutation-testing suite.

## Net disposition

`continuation-interface` is constructed at the declared task scope. It supplies composition-compatible forward transport and explicitly excludes unproved reflection/full-source identity. The observed counterexamples are attached to this interface and reuse the previously identified sources.

Next: `energy-example-interface-comparison`. Instantiate the positive (a,b) quotient with the actual gain/update/probe functions; retain the full source separately, prove gain composition at the declared scope, and distinguish estimating old statistics from physically restoring a post-probe state. No full mode controllability or additional actuator is a prerequisite.
