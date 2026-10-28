# Edge-5 global routing witness under an explicit corridor contract

## Result

A simultaneous integer-flow solve produced **80 labelled entry-to-exit routes covering all 245 cells**. Every route uses actual shared faces, has 17 cell occurrences and 16 face crossings, and reverses exactly while retaining its fibre identity.

This is a complete witness for the declared **anchor-only, multiplexed geometric-corridor problem**. It is not a completed native full fibration or a selected-pair interaction law.

A separate stronger interpretation has a concrete obstruction: requiring each fibre to visit its P presentation anchor **before** its reflected E anchor is impossible for 40 fibres under the fixed monotone reading.

## Contract fixed before solving

`contracts/su32-edge5-global-routing-witness-v1.json` specifies:

- the existing 80 fibre identities and N-body boundaries;
- P/E presentation sites as reference anchors, not compulsory ordered waypoints;
- strictly forward shared-face hops across the 17 layers;
- a candidate internal passage between any distinct entering/exiting faces of a whole convex cell;
- multiplexing: several distinct fibre instances may use the same face or corridor;
- at least one passage through every cell;
- exact identity, payload and path retention under reversal.

The arbitrary-cell-turn and multiplexing policies are explicit assumptions. They are not inferred native junction rules. The finite per-arc bound of 80 only bounds this problem and is not a physical capacity estimate.

Requiring every cell to be active is stronger than the previous retention-only condition. It guarantees geometric visits to all eight eligible middle triples and their partner tips, but does not assign the intended record pairs to those deliveries.

## Global construction, then path extraction

The solver builds the entire carrier network at once:

- split each cell into incoming/outgoing flow vertices;
- give its throughput arc lower bound 1 and upper bound 80;
- insert all 560 directed shared-face arcs, each with bounds 0–80;
- impose total flow 80 using a fixed exit-to-entry bookkeeping edge.

The bookkeeping edge is not a physical seam or return passage. Lower-bound circulation is reduced to integral maximum flow. The resulting complete flow is independently checked for integer bounds and conservation at every split vertex.

Only after that solve is the flow decomposed into eighty labelled paths. Decomposition order chooses one witness, not a source-selected matching or an optimal solution. No local reader grows the wiring.

## Witness inventory

- **80** distinct retained fibre identities;
- **245** covered cells;
- **366** used shared faces out of 560;
- **1,280** individual face traversals;
- **41** distinct geometric cell paths carrying the 80 named fibres;
- all **8** eligible middle triples reached, including both members of each required tip group.

Forty-one geometric paths do not mean forty-one fibres. Distinct named occurrences share paths under the explicit multiplexing policy. Conversely, their common route does not permit merging their payload records.

The receipt supplies each route, its reverse, exact entry/exit face allocation, per-cell flow, per-face flow and per-cell corridor support. At an interior cell, the candidate corridor runs from the entering face's barycentre through the cell centre to the exiting face's barycentre. These points are convex combinations of the native vertices, so the segments lie in the whole convex cell.

This verifies centreline support, not disjoint finite-width strands. It also does not establish dense coverage of every triangle edge or native interaction/filling laws on the 44 cones. Unused geometry remains retained in the source carrier.

## Conservation and reversal

Each route has one occurrence of its fibre at each layer. It never branches, merges with another fibre identity, or repeats a cell. Its successive faces are independently checked against the actual two cell owners.

Reversing every route recovers the same cell and face occupancies in the opposite orientation. Reversing twice recovers the exact labelled assignment. A tagged opaque payload bank is delivered and recovered without content changes; payloads are carried per identity rather than summed at shared sites.

This is reversibility of the stated path/payload convention, not native time-reversed evolution or reversal of the original preparation history.

## Ordered-waypoint obstruction

Middle-plane reflection sends layer L to layer 18−L. Forty P anchors lie in layers 10,12,14,16; their paired E anchors lie in layers 8,6,4,2.

A strictly layer-increasing path cannot visit those P anchors before their E partners. The receipt lists all forty conflicts by fibre ID and actual cell/layer.

This rules out that **ordered P-then-E waypoint contract**. It does not rule out visiting the anchors in layer order, nonmonotone routing, another endpoint association, or the anchor-only convention used for the successful witness.

## Remaining semantic boundary

Geometric visits to T,U,V are established, with the exact visiting fibre IDs retained. The signed-record-to-fibre map remains unbound, so the visits are not yet certified delivery of the intended P/P and E/E contents or execution of their comparisons.

No middle triple is selected. Because the stronger all-cell coverage condition implies visits to all triples, the eight reachability checks are not an independent selector.

The result advances beyond inventories to an actual whole-carrier route assignment. Further claims must identify which additional native passage, finite-width, fibre-content or comparison constraints this witness satisfies or violates.

## Verification

```sh
node research/strominger/checkers/check_su32_edge5_global_routing_witness.mjs
```

Fresh headless execution passed complete-flow conservation, full path reconstruction, all actual face hops, boundary domains, cell coverage, exact reversal, payload retention and four negative controls. The latter reject duplicated fibre identities, a false face hop, incorrect direction and an independently infeasible lower-bound circulation.

Receipt: `results/su32-edge5-global-routing-witness-v1/verification.json`.

All input contracts and source receipts are hash checked. No geometry, previous candidate or native operation was changed.
