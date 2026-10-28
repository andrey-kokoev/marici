# Pb-208 as a target for a representation trace

## Proposed object, not an established construction

The operator proposes four retained 28-step traces, arising from four binary levels 1,2,4,8, assembled into esd7 with a central-cell start and E-vertex end: 1 -> [4 x 28] -> 1. Four tree levels have 14 links; a complete tree contour traverses 28 links with multiplicity. This counting fact supplies neither the actual transport schedule nor its tetrahedral assembly map.

Here test the proposal against a whole Pb-208 representation, rather than assume a trace is a sequence creating independent particles. The terminal E presentation is not automatically one physical electron. No particle species is assigned merely from a chart label.

## Expected trace structure

Let A denote the retained whole assembly. A candidate trace is a diagram of presentations X_s with transport/comparison witnesses, not just a word of endpoint involutions. Each presentation should retain enough data to recover A, or explicitly retain witnesses for what a readout forgets. The four branch traces must agree on specified shared interfaces; their joint assembly must retain the face and higher coherence data, not only a list of occupied coordinates.

Required test readouts:

- A nuclear composition readout gives 82 P and 126 N roles.
- If a neutral-atom realization is additionally claimed, its distinct electron readout gives 82 electrons. Internal E-labelled presentations are not counted as electrons without a binding.
- Branch and chart changes preserve these readouts under the declared equivalences.
- Differently ordered routes with the same readout are compared with retained witnesses; endpoint equality alone does not erase history.
- The central-cell and E-vertex presentations refer to the same retained assembly through an explicit binding, not an asserted equality of cell and vertex.

These are proposed conformance requirements, not newly verified facts about a Pb trace. They do not select a unique assembly or explain stability.

## What prior work actually supplies

The existing esd7 envelope has layer-item counts 1,4,44,126. The legacy construction matches 44 inner items to 44 distinct outer witnesses, then labels the remaining 126-44=82 outer items P. It adds 82 N connectors and 82 electron endpoints, giving 44+82=126 N. Thus the count readout is 82 P,126 N,82 e by a supplied assignment policy. This is not a trace-derived isotope selection.

Moreover, the earlier source audit reports that none of those 82 legacy chains preserves the marked edge required by the recovered window protocol. Matching counts and non-overlapping geometry therefore do not establish a coherent native realization. The matched outer locations also depend on traversal/tie-breaking conventions even when the count stays 44. These prior checks were inspected, not freshly rerun here.

## A useful conditional falsifier

The existing native growth grammar creates at most one body per individual operation. From one seed, 112 such operations give at most 113 bodies, below a 208-body nucleus or a 290-body neutral-atom loadout. Thus the four-28 proposal cannot be interpreted as that particular sequential one-body growth program.

This is NOT an obstruction to a collective or representation-changing trace. A step that reindexes a retained assembly can preserve many roles simultaneously. It is also not a claim that a supplied assembly has been generated: re-presenting an input does not explain its origin.

## Next discriminating construction

Construct one actual presentation change carrying an entire retained assembly, together with its projection/reconstruction or comparison witness. Test interface preservation and the composition readout before prescribing 28 steps. Then determine whether four such histories admit the proposed esd7 assembly and central-cell/E-vertex endpoint bindings. Do not replace missing witnesses with a count-matching assignment or a preferred matching order.

Sources inspected:
- [Pb formation gate audit](pb208-formation-gate-audit-v1.md).
- [Explicit legacy loadout](lead208-outward-chains-v1.md).
- [Native assembly grammar and its individual-operation bound](../nima/generative-phase-assembly-v1.md).
- [Retained-total fibration kernel](../nima/label-from-to-fibration-tower.md): an example of representation change with reconstruction, not an established binding to Pb-208 or the proposed 28-step trace.

Disposition: target clarified; no Pb trace, new evolution law, 28-step realization, isotope derivation or stability result constructed.
