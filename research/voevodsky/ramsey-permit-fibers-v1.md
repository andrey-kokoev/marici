# Vertex permits: unique witnesses within a fixed facet

Fresh local state is revision24. This result addresses the proof-representation gap left by the canonical external-support involution.

## Kernel result

Fresh safe Cubical checking proves:

1. The four-element vertex type is a set, using a retraction into natural numbers.
2. Each three-slot face inclusion is injective, using an explicit left inverse.
3. `InFace v f` is a proposition: two slot/equality witnesses of membership in the same face are equal.
4. The native chart permit is an equality of natural numbers, hence a proposition.
5. Consequently the fiber of `VertexPermit c v` over a fixed facet is a proposition. Two vertex permits are equal exactly when their facet projections are equal.

Twelve source-bound normalization cells show that any permit with the facet of one of the actual canonical `vp-f-v` witnesses equals that witness. This covers arbitrary equality-proof representations, not just generated reflexivity terms.

## What is not collapsed

The facet itself remains retained data. A hostile equation between the valid chart0/vertex3 permits from facets0 and2 is rejected. Propositional membership witnesses do not make the whole vertex-permit type a proposition.

## Next obligation

Construct a total canonical classification of the valid facet choices, eliminate impossible facet/vertex cases, and lift the involution through these fibers to full dependent occurrence types. The present theorem supplies uniqueness within each choice, not yet that full occurrence equivalence.

No additional native operation, source-generation claim or parent descent verdict follows. The scoped retained-correspondence theorem is unchanged.

## Verification

- `fixtures/ramsey-permit-fibers/RamseyPermitFibers.agda`;
- `checkers/check_ramsey_permit_fibers.py`;
- `results/ramsey-permit-fibers-v1.json`;
- passing freeze `scc-freezes/ramsey-permit-fibers-v1.9ae77c1df51038a4.json`.

The positive and hostile checks were run fresh with `--ignore-interfaces`. Owning definitions and actual canonical witnesses are directly pinned. Net revision24, external admission revision19 and all scientific verdicts remain unchanged; this receipt awaits consolidation. No graph event or Git checkpoint occurred.
