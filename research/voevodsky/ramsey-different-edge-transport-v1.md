# Actual different-edge four-facet transport

## Kernel-checked bindings

The complementary action is now bound to the actual four-facet diagram, rather than only to triples sharing a single edge:

-12 actual directed edge transport cells;
-24 actual vertex-triple transport cells;
-72 different-edge AB/BC/AC route cells;
-72 endpoint-side transport cells;
-72 coherence cells comparing direct route transport with the generic restriction-naturality proof;
-24 transported middle-source index seams and48 bindings to the target route indices.

The original24 target native middle-derivation seams are rechecked through explicitly typed aliases. This verifies that the transported indices land at the intended target diagram with its retained native seam; it does **not** construct a map transporting the source native derivations.

All actual routes are bound to their explicit endpoint bits in the owning four-facet examples. A wrong-side control on the reversed edge23 is rejected. A second hostile control replacing the middle facet by an outer facet is also rejected.

## Boundary

This closes the common-edge-only limitation of the preceding naturality result for the actual indexed four-facet routes. Path coherence remains at the common-index level. Rechecking target derivations is distinct from transporting derivations, and neither step supplies complementary inputs from the default local seed.

The scoped independent-input correspondence remains valid and parent descent remains open. No new native operation or fixed-vertex identity claim is introduced.

## Next executable obligation

Audit the constructor-level lift: specify a P/E derivation comparison that transports prerequisite indices and leaf payloads explicitly, then compare its middle-premise behavior with these source-bound index seams. Do not infer that such a lift exists merely from occurrence equivalence or from the existence of target proofs. Alternatively consolidate these two new naturality/route receipts without changing the parent verdict.

## Verification

- `fixtures/ramsey-different-edge-transport/RamseyDifferentEdgeTransport.agda`
- `checkers/check_ramsey_different_edge_transport.py`
- `results/ramsey-different-edge-transport-v1.json`
- passing freeze `scc-freezes/ramsey-different-edge-transport-v1.820950741218cd1b.json`

Fresh safe Cubical positive and hostile checks passed with `--ignore-interfaces`. Local net revision26 and external admission revision19 remain unchanged. No owning signature, scientific verdict, graph event or Git checkpoint changed; this receipt awaits consolidation.
