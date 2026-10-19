# Body-coherent PE materialization — net iteration11

## Macro definition

For a compatible rooted selection A, choose an unoccupied neutron body B used as reference support by at least one active terminal-PE shortcut. Collect **all** active shortcuts whose reference neutron body is B. Add their retained intermediate neutron reader packets as one atomic planner step. Each reader carries its original chart, origin and map; do not merge readers merely because their body is shared.

Reject incompatible results. For a certificate-to-certificate macro, separately require the full final audit, including native witnesses for newly occupied faces. Native transfer and terminal-PE rules themselves are unchanged.

## Conditional preservation theorem

Assume the result is compatible, all factors are in the source universe, and every native outgoing edge from a shortcut's P source to a neutron targets that shortcut's reference body (the current source rule shape).

Every native edge of A remains selected and active. Every PE edge using B is replaced by its original PN→NE path through a newly added neutron reader. A PE edge using a different reference body stays active: B does not violate its vacancy guard; nor can an added neutron be its native successor by the rule-shape assumption. Thus every old active edge either remains or has an active two-edge replacement.

Replace edges along the old root paths to obtain root paths for all old packets. Each new neutron is reached from its old P endpoint. Hence the result is rooted. If every old packet could reach an E exit, replace edges along those exit paths as well; each new neutron also exits through its retained NE factor to an old E. Thus exit reachability is preserved.

This does **not** prove full final certification: occupying B creates additional triangular-face obligations. Each such face still needs a selected native witness. Compatibility and face witnessing are explicit separate audit gates.

## Exhaustive bounded test

The checker tests every reference-body group on all698 D2 certificates. For each compatible result it verifies rootedness, all-reader exit reachability, exact disappearance of the affected shortcuts, preservation of all unaffected shortcuts, and both native factors for each replacement. Every certified result must occur in the independently verified complete D2 live graph.

Validated macro edges are added only from certified starts. Reverse target-bitset propagation then compares target-specific reachability before and after augmentation over all216,531 live-state/certified-superset pairs. The receipt records repaired and residual blocked pairs, candidate failure causes, macro sizes and complete macro witnesses.

**Result:**265 candidates (231 one-reader and34 two-reader batches) are all compatible and preserve root/exit reachability.70 fail newly occupied native-face obligations;195 are certified macros. Adding those195 edges repairs **all1,803 previously blocked target pairs**, leaving0 unreachable pairs among216,531 certified-superset pairs.

The previous two-reader counterexample is explicitly replayed: adding either reader alone loses rootedness, while the grouped macro reaches its certified target.

## Next frontier

Classify the70 face-witness failures using the existing source obstruction certificates and targeted source completion search. Determine which need additional selected native face witnesses and which are impossible at D2. This should turn the remaining post-audit rejection into an explicit support-selection condition; do not mistake root/exit preservation for complete contact validity.

## Scope

These are atomic planning transitions, not claims that the otherwise invalid singleton intermediates become valid. Exhaustive results concern D2 and this particular macro family; the preservation argument states its source-rule hypotheses explicitly.

```sh
node research/nima/checkers/check_body_coherent_materialization.mjs
```

[Implementation](body-coherent-materialization.mjs) · [Checker](checkers/check_body_coherent_materialization.mjs) · [Receipt](results/body-coherent-materialization/verification.json)
