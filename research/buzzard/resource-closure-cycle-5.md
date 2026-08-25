# Descendant-closed resource removal — cycle 5

## Independent sources

- Kitaev, `dpc-bounded-audit-framework.md`: removing a factory label while
  retaining its distilled state and compiled gate is not a counterfactual
  resource restriction.
- Figueiredo, `flavor-dpc-bounded-audit-framework.md`: deleting a UV source
  label while retaining derived fitted coefficients is descendant leakage.

## Lean increment

`ResourceClosure.lean` defines the descendant closure of a set under a typed
directed derivation relation. It proves that roots lie in their closure and
that the closure is removal-closed. A hostile three-stage model proves that
label-only deletion is not removal-closed and that the compiled capability is
included by the correct closure.

The Kitaev and Flavor resource types and derivation relations remain distinct.
Each has an executable theorem showing that removal of its source resource
includes the terminal descendant.

## Disposition

**Generalized operation, specialized resource ontology.** Reachability closure
is common; sector nodes and derivation edges are not identified.

## Missing convention-fixed inputs

1. Complete, source-derived dependency edges for each real resource graph.
2. Treatment of cyclic derivations and jointly required hyperedges.
3. A distinction between causal production, compilation dependency, and mere
   evidential correlation before those edges can coexist in one graph.
4. A capability/monotone theorem proving that the closed removal actually
   destroys the bounded capability in each sector.

## Build

From `research/buzzard/marici_formal`, run `lake build`.

Result: `Build completed successfully (8715 jobs).` Lean/mathlib version:
`v4.33.1`.
