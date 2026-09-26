# Tree-class termination, simulation and local diamonds

## Admitted class

A pure history is the seed/unary/binary reference syntax with matching package, layer and rule-witness data. A configuration is a result tree of reconstructed constructors and pending F(h), where each h is pure and has positive layer. Pending regions cannot contain another F. Layered seed evidence remains pure. Wires enter constructors through principal ports and F through its result auxiliary port. Shared histories, cycles and general interaction graphs are excluded.

`tree_audit.py` recognizes this class independently of the evaluator. The old topology validator alone is insufficient: arbitrary labels, layer mismatches and mismatched rule inputs can pass it. Four such mutations now fail the stronger audit. This is currently a separate admission/observation tool, not a trusted new runtime API.

## Decreasing measure

Define s(seed)=1 and s(step(h_i))=1+sum_i s(h_i); do NOT descend into a seed's retained evidence when counting its outer layer. Let mu be the sum of s(h) over pending F(h) regions. The regions are disjoint by admission.

* F(seed(d)) rewrites to d, so mu decreases by1.
* F(step(w,h_i)) rewrites to step(w,F(h_i)), so mu decreases from1+sum s(h_i) to sum s(h_i).

Other regions are unchanged. Thus every rewrite decreases a nonnegative integer by exactly1. In the admitted class every F has a constructor principal partner, so a normal form has no F; a compiled flattening request takes exactly s(h) rewrites under every schedule. This counts rewrite steps, not the cost of whole-net audits or compilation.

## Simulation

Interpret a pure constructor as its reference derivation and interpret F(h) as reference flatten(h). Reconstructed constructors interpret compositionally. Each of the three rewrites preserves this interpretation by the corresponding defining equation of flatten, including rule witness and ordered premise histories. Compilation has denotation flatten(input); normal-form readback has that same denotation. No evaluator call to flatten is required: flatten appears only in the independent semantic observer.

## Local commutation

Distinct pending F regions are disjoint pure subtrees. Their active pairs do not share agents or wires: each root output connects to its own ordered parent slot, and neither active pair lies in the other's pure region. Rewriting either pair preserves the other pair and its external interface. Performing the other rewrite produces the same labelled tree modulo fresh agent identifiers. Fresh integer allocation prevents literal dictionary equality, so equality here must be alpha-renaming, not numeric ID equality.

Termination and these local diamonds give unique normal forms modulo fresh identifiers for this admitted finite tree class. This is a written structural argument, NOT a new Agda-checked theorem and NOT a confluence claim for graphs with sharing, erasure, or arbitrary F placements.

## Executable checks

`python research/voevodsky/resolution-net-v1/check_tree_soundness.py` passes37 explored states,32 one-step measure/simulation checks,7 local diamonds and12 terminal paths; four malformed typed payloads are rejected. Result: results/tree-soundness.json. These finite checks support the implementation correspondence but are not the universal proof.

Next: make admission a fail-closed runtime entry point without embedding reference flattening into the evaluator. Separate the typed validator from the semantic observer, test atomic failure before mutation, and retain the Agda crosswalk/formalization as a distinct branch.
