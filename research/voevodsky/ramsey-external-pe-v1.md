# Externally indexed P/E realization of the retained diagram

Fresh inputs are the checked four-facet vertex compositions and the native P/E span signature. This turn adds an owner-local construction witness rather than changing raw native package equality.

## External tree and native compilation

The source indices form a fixed external type. An external tree has three constructors:

- a leaf carrying a source index;
- a product of an indexed family of trees;
- an E-selection retaining the indexed family and selected index.

Every tree compiles to an actual native package and a native P/E derivation. Compilation uses the existing native rules, not a new opaque admission result.

An occurrence in a product identifies a branch and an occurrence within it. An occurrence in E does the same over the **whole prerequisite family**, not just its selected branch. A located occurrence therefore has a fixed source-index readout outside the universe-varying native package. Equality of located occurrences preserves any fixed observation of that source index.

The raw native seed predicate remains path-closed. The extra guarantee belongs to the explicit compiler tree and its located occurrences; it is not claimed for every inhabitant of the raw native resolution type.

## Binding to the existing four-facet diagram

A generic traced-span constructor builds external trees for the existing selected spans and triple compositions. Kernel compiler cells identify their encoded packages with the existing native span/composition packages.

The actual24 four-facet vertex triple compositions are instantiated. Each has an external tree, a compiled native derivation, a package-agreement cell, and a full-source middle-occurrence equation identifying its actual chart, vertex, parent face, PN permit and membership witness.

These are external construction witnesses for the same checked diagram, not a claim that arbitrary native proofs can be reconstructed uniquely from their endpoints.

## Erasure control

A concrete two-source example gives both Boolean source indices the same literal payload. Their compiled native leaf packages are definitionally equal, but their located external leaves cannot be equal: projecting the fixed source index would give false = true. The impossibility theorem is kernel checked, and a hostile equality assertion is rejected.

Thus even literal endpoint equality does not erase external source provenance. This handles a stronger erasure control than merely relying on unequal packet strings.

## Next source-policy test

The construction still uses independently admitted target ports. Now that external leaves are available, test a restricted source policy on them: define what leaf indices are allowed, propagate that predicate through P/E, and inspect the concrete complementary-chart occurrences. This can establish precisely whether the existing retained diagram needs an independently supplied target, without confusing native package paths with fixed source identity.

Any resulting obstruction will concern this declared external P/E compiler and source policy, not arbitrary native rules, all physical paths, or the broader descent conjecture.

## Verification

- Contract: `contracts/ramsey-external-pe-attempt.v1.json`.
- Generic module: `agda/RamseyExternalPE.agda`.
- Actual instances/hostile: `fixtures/ramsey-external-pe/`.
- Checker: `checkers/check_ramsey_external_pe.py`.
- Receipt: `results/ramsey-external-pe-v1.json`.
- Passing freeze: `scc-freezes/ramsey-external-pe-v1.c6119c0b31d18b59.json`.

Fresh safe Cubical checks pass with ignored interfaces and stable source/compiler inventories. The owning native signature is unchanged. Net revision23 and the scoped retained-correspondence verdict remain unchanged; broader descent stays open. No graph mutation or Git checkpoint occurred.
