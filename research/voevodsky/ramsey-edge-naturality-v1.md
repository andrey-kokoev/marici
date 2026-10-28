# Full edge-permit transport commutes with endpoint restriction

## Result

Fresh safe Cubical checking constructs12 full edge-permit equivalences for charts0/7 and the six edges, with arbitrary-witness inverse laws and12 canonical agreement cells.

There are24 restriction naturality laws: for every valid edge permit, transporting its chosen vertex restriction agrees with transporting the edge permit and then restricting at the correctly transported endpoint. The proof reuses the existing full vertex-permit maps, so this is a compatibility theorem between the two constructions, not a second unrelated vertex map.

The involution reverses endpoint order on edges01 and23. The remaining four edges transport their endpoint order unchanged. Twelve endpoint transport cells are checked. A hostile test omitting the order reversal on edge01 is rejected.

Two edge-permit types are empty (chart0/edge02 and chart7/edge13); four of the24 restriction laws consequently have empty domains. The other laws and the12 canonical edge witnesses supply nonvacuous cases.

## Boundary

The theorem transports the endpoint choice explicitly. It does not prove that one fixed global endpoint bit commutes with the symmetry. In particular, the existing native restriction interface takes a fixed Boolean side, whereas the symmetry reverses sides on only two edges.

No local operation was added and no complementary input generated. The independent-input scope, retained-correspondence verdict and open parent descent remain unchanged.

## Next executable obligation

Audit endpoint-selection policies: construct the transported edge-dependent selector and test whether any deterministic selector can be invariant under this involution. Edges01 and23 are fixed as unoriented edges but their endpoints exchange, so they provide concrete tests against a silently fixed endpoint selector. Retaining both endpoints and transporting a chosen endpoint are distinct policies and must not be conflated.

## Verification

- `fixtures/ramsey-edge-naturality/RamseyEdgeNaturality.agda`
- `checkers/check_ramsey_edge_naturality.py`
- `results/ramsey-edge-naturality-v1.json`
- passing freeze `scc-freezes/ramsey-edge-naturality-v1.b858ede30f55abff.json`

The positive and hostile checks passed fresh with `--ignore-interfaces`. Owning definitions are unchanged and pinned. Net revision25 and external admission revision19 remain unchanged; this receipt awaits consolidation. No graph event or Git checkpoint occurred.
