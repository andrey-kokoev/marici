# The transform-to-pullback geometric edge is not serialized

A fresh AST audit separates the valid matrix theorem from its geometric provenance.

`research/voevodsky/check_global_mixed_variance_transform.py` invokes six component `main()` functions only as unbound statements. No component returns a connector object, chain complex, or morphism consumed downstream. The eleven-field transform signature is a literal dictionary, and `unique_connector_signature` is created by copying that same dictionary.

`research/voevodsky/check_physical_derived_pullback_after_transform.py` calls `transform.main()` and then declares `d1`, `d2`, `d3`, and the primitive cycle as literals. Thus execution order is present but dataflow is absent.

This does not refute Entry 435's mathematical construction or the integral homology calculation. It proves only that the repository currently lacks an executable certificate for the edge

`constructed transform -> framed connector chain object -> road homotopy pullback complex`.

## Minimal reopening contract

A noncircular constructor must export:

1. a labelled connector chain object with basis and differential;
2. the normalization-sheet image map into that object;
3. the labelled road-inclusion chain map;
4. the two maps defining the homotopy pullback;
5. a computed pullback differential in a declared basis;
6. a basis comparison showing that computed differential equals the displayed `(d3,d2,d1)` matrices;
7. an independently loaded framed-connector signature rather than a copy of the transform signature.

Only after this contract passes should the normalized `(1,1,1)` class be called geometrically realized. The symbolic target packet remains a coefficient model, and no rank-three geometric family follows from this audit.

Executable evidence: `checkers/check_transform_to_pullback_serialization_gate.py`.
