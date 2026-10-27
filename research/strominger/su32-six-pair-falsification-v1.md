# Falsification attempt: six signed-pair outputs at the middle

## Result

The conditional six-pair task **survives the joint-information test**, but its labelled correspondence is not unique. There are **10 admissible pair assignments per complete geometric cover, 40 in total**.

A stronger rival is falsified: the same active pair cannot always be reconstructed from either existing operand independently. This stronger requirement is not inferred from the operator's P/E duality.

Neither result establishes or refutes a completed native outgoing wiring.

## Frozen problem, not a new native requirement

Fix `reading:0:-1`, its four independent signed input records and the four complete middle covers from the preceding trace. Conditionally interpret the six outputs as precisely

```
P+P-, P+E+, P+E-, P-E+, P-E-, E+E-.
```

The specification presents this six-unordered-pair interpretation conditionally; this experiment does not promote it to an established source law.

Each of the six fixed labelled middle groups must receive exactly one pair, and every pair must appear exactly once. Original operands and provenance may be retained. No capacities, scalar amplitudes, cyclic orders, scattering rules or central-to-peripheral communication are added.

Two access models are tested separately:

1. **Joint access:** both records of the chosen pair occur in the union of the group's two offered operands.
2. **Either-operand access:** both records must already be recoverable from each offered operand separately, with no communication or added state.

The second condition is strictly stronger than the first. It is not equivalent to reversing a whole process.

## Exhaustive global test

Enumerate all `6! = 720` pair-to-group bijections for each complete cover, then check each restriction. This is **2,880 assignments per access model**, not a greedy local routing search.

| Complete cover | Joint-access assignments | Either-operand assignments |
|---|---:|---:|
| 0 | 10 | 0 |
| 1 | 10 | 0 |
| 2 | 10 | 0 |
| 3 | 10 | 0 |

All 40 joint solutions are retained in the receipt. They are distinct assignments to the marked channels. No quotient by a proposed geometric or gauge symmetry was taken, so no count of physically inequivalent solutions is claimed.

For every joint solution, a conditional information codec stores the selected active pair, remaining offered records as context, and both full input operand trees. Serialization and recovery preserve the exact four-record registry and both operand histories: **40 recovery checks passed**.

Keeping the full operands makes information recovery explicit, but does not constitute an implementation of a native reversible interaction. These are feasible active/context labellings, not derived middle dynamics, and the codec is not claimed minimal. Indeed, the complete set of six active pairs already contains every input record; context and derivation retention serve the larger reference/provenance task.

## Actual falsification of independent operand recovery

No offered E-side view contains both P+ and P-. Likewise, no offered P-side view contains both E+ and E-. Thus the required same-role pairs have no eligible channel under the either-operand rule. A required singleton pair with zero eligible channels is already a Hall obstruction to the demanded bijection.

This is not merely a failed schema check. For every group and the relevant side, the checker changes one missing input record while keeping all others fixed. The **complete existing operand tree** stays identical, while the required same-role pair changes. There are **48 such full-operand counterexample instances** across the covers.

One example has E-view `{E+,P+}`. Changing P- leaves that entire operand unchanged but changes `(P+,P-)`. No function of that operand alone can recover the pair for all independent inputs.

This falsifies independent recovery without additional information. It does not falsify joint recovery, communication through a specified later operation, or P/E duality itself.

## What was and was not falsified

- **Joint six-pair information feasibility:** not falsified; explicit witnesses exist in all four covers.
- **Unique labelled correspondence from the present constraints:** falsified; even fixing one cover leaves ten choices.
- **Each offered operand alone suffices for every chosen pair:** falsified.
- **Native six-output wiring:** undecided. The source still lacks the middle and outgoing occurrence maps.

Consequently, raw record availability is not the obstruction to the weak joint task. The unresolved issue is which correspondence is native and how it acts on outgoing occurrences. The surviving candidates cannot select themselves merely by being lossless.

## Replay and evidence

```
node research/strominger/checkers/check_sulfur32_middle_layer.mjs
node research/strominger/checkers/check_su32_fixed_reading_trace.mjs
node research/strominger/checkers/check_su32_six_pair_falsification.mjs
```

The falsification checker validates the preceding trace's source hashes before testing. Fresh execution passed the exhaustive enumeration, all recovery checks and all full-operand counterexamples.

Receipt: `results/su32-six-pair-falsification-v1/verification.json`.

No native operation was modified or supplied. In particular, there is still no layer-6 or outgoing-N payload map; the experiment does not hide that gap behind its information codec.
