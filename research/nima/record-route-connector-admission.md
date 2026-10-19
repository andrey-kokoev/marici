# Connector provenance from existing record routes

## Fresh advance

The explicit connector interface now has witnesses constructed from ACTUAL directed routes in the existing137-record endpoint graph, rather than only hand-declared frame bridges.

This is conditional on interpreting those record routes as connector operations. The records already supply route syntax and typed attachment maps, but a route is not automatically an admitted physical pulse. The source-role interpretation remains explicit.

## Reachability is not common-target collapse

The actual graph has32 ports:

-16 arrow-sector ports form one strongly connected component;
-16 state-sector ports are isolated from one another and from the arrow sector (each has its original loop record).

There are272 reachable ordered port pairs:256 in the arrow sector and16 state diagonals.240 are cross-port routes, each with retained original record labels.

Their induced leaf-pair support is

    121^2 + 16 = 14657.

This includes the977 original common-target pairs and adds13680 pairs. It is still4112 pairs short of the common-target candidate's18769 pairs:

    2*121*16 + (16^2-16) = 4112.

Those missing pairs require arrow/state cross-sector connections or connections between distinct state ports. No route in the existing graph supplies them. Available flat frames do not repair that missing source syntax.

## A graph-derived third structural candidate

Assign first-family successor keys by the graph's reachable components, then use the ORIGINAL second incoming promotion. This yields17 final records: one arrow-sector family and16 state families.

The checker verifies exact original leaf retention, unchanged weighted J4 and a final leaf-pair relation EXACTLY equal to the route-reachability relation.

This is a source-graph-derived context candidate, more constrained than arbitrary partitions. It is not declared intended T9: the choice to close contexts under graph routes, and the response interpretation of those routes, remain additional operation contracts.

The candidate profiles are now:

| Context task | Final families | Leaf-pair support |
|---|---:|---:|
| original same-target domain |32|977|
| closure under existing directed record routes |17|14657|
| global common target |1|18769|

All three retain the supplied J4. Their DIFFERENT operational domains are what distinguish them.

## Two route interpretations, kept separate

For each actual directed route, compute separately:

1. the product of existing REFERENCE attachments;
2. the product of actual COMPARISON maps.

Reference attachments in the declared flat frame stratum telescope to P_end P_start^-1. Using that as a connector produces the familiar decoded product C_b r C_a.

Actual comparison routes generally do not telescope that way. Their connector inserts a nontrivial response between the operands. The checker retains a concrete actual-route witness for which passive-reference and actual-comparison interpretations produce different decoded values.

It also uses an existing two-record carrier loop, without inserting a shear or changing any source matrix. The reference loop is identity, while the actual comparison loop is not. Thus route endpoints alone cannot replace actual response history.

These are distinct operations on the SAME retained route syntax. Choosing the passive interpretation merely because it reproduces the desired aggregate would conceal the operation-binding question.

## Admission controls

The checker constructs reference and actual-comparison connector declarations for all240 reachable cross-port pairs, with explicit route labels in provenance. It retains their direction and does not invent reverse events by numerical inversion.

The original record route is validated edge-by-edge for endpoint composition. A numerical map at two ports is not accepted as evidence of a missing route.

The route declarations are mathematical controls, not physical instrument authorization. They do not identify fixture record arrows with seed primitive occurrences or construct higher fillers.

## Remaining exact source decision

If intended T9 creates contexts, there is now a concrete choice to test:

- Does it close the comparison domain under EXISTING record routes? Then the17-component-key candidate realizes that structural contract.
- Does it use actual comparison-route responses or reference transports along those routes? These have checked distinct readouts.
- Does it connect different state ports or the state and arrow sectors? Then it needs additional source events beyond this graph; common-target collapse cannot stand in for their provenance.

The original T9 organizing specification selects none of those contracts. This result identifies available and missing source witness syntax without promoting it to an intended physical generator.

## Verification

    uv run research/nima/checkers/check_record_route_connector_admission.py

806 exact checks pass. Dependencies freshly rebuild the full geometric record/flat-attachment chain. No new Agda theorem or physical experiment is claimed.

Artifacts:

- `checkers/check_record_route_connector_admission.py`
- `results/record-route-connector-admission.json`

Fresh prior-source reading also recovered the constraint in `recovered-reference-return-response-chain.md`: reference flatness audits must not be mistaken for source admission. This step tests actual graph reachability and route response interpretation, not another invented flatness law.
