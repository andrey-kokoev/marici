# Native common-edge attachments with retained parent faces

Fresh inspection confirmed that the existing native span constructor is generic in its attachment index and permit type. This turn specializes that constructor to actual edge attachments rather than inventing a new comparison rule.

## Typed attachment domain

An edge is one of the six unordered pairs of distinct tetrahedral vertices. Its permit retains:

1. a chosen parent face;
2. that chart's PN permit on the chosen face;
3. an explicit face-slot witness for the first endpoint;
4. an explicit face-slot witness for the second endpoint.

The underlying packet is the complete validated parent-face record. The native selected-span index retains the full edge permit, including the parent choice and both memberships. Therefore the two eligible parents of an MM edge are not collapsed.

The generated instance binds all24 charts and48 full port records from the already checked request interface. All144 face-induced edge attachments have actual native input proofs. A concrete triple composition uses charts q0, q2, q0 on the same geometric edge, with different first/final parent-face choices. The full middle attachment is shared by the composed routes through the existing native triple constructor.

## Endpoint restriction

Restriction to either endpoint preserves the same parent face, PN certificate and full packet, retaining the relevant face-slot witness. A typed admission map sends edge-policy seeds to vertex-policy seeds, and a structural recursive map transports every native derivation along that admission map without changing its package.

Separately, the restricted vertex selected spans are constructed from the restricted common indices. These are not falsely identified with the unchanged edge package transported between admission policies.

Kernel equations show that the AB, BC and AC common-index restrictions commute with the corresponding projections of a retained triple. Native vertex composition is instantiated on the restricted concrete triple.

## Hostile control and scope

A hostile equality identifying two distinct parent-face choices on the same MM edge is rejected. Matching geometric support alone does not erase that retained data.

This proves native common-edge spans, their existing declared-domain composition, and endpoint restriction/admission cells. It does not provide a total edge-domain map between different role partitions, an interpretation of scalar field restrictions, or a complete four-facet descent theorem.

The next missing connection is the four-facet cover: choose an independently admitted parent port for each facet, then compare the restrictions to a triple-intersection vertex along its different incident edges. Those paths must preserve the same parent packet and agree on their endpoint membership, rather than merely agree on a vertex label. The current common-edge triple is not silently substituted for that different-edge vertex diagram.

## Verification

- Contract: `contracts/ramsey-native-edge-attachments-attempt.v1.json`.
- Generic module: `agda/RamseyNativeEdgeAttachments.agda`.
- Complete instance/hostile: `fixtures/ramsey-native-edge-attachments/`.
- Checker: `checkers/check_ramsey_native_edge_attachments.py`.
- Receipt: `results/ramsey-native-edge-attachments-v1.json`.
- Passing freeze: `scc-freezes/ramsey-native-edge-attachments-v1.f8e55e1064b71021.json`.

Fresh safe Cubical checks pass with ignored interfaces and stable input/compiler inventories. The first frozen attempt encountered unresolved implicit chart arguments in the concrete vertex instance; supplying those arguments explicitly fixed the elaboration error. That failed attempt remains in SCC history and is not a mathematical refutation.

The net remains local revision21 with no scientific verdict changes, graph mutation or Git checkpoint.
