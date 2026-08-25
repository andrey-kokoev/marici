# Authority composition audit — cycle 2

## Sources and boundary

- Strominger, `authority-grant-composition-interpretation.md` and
  `contracts/authority-grant-composition.v1.json`.
- Grothendieck, `theta-labelled-overlap-moving-seam.md`.
- Strominger hostile fixtures,
  `contracts/authority-grant-composition-hostile-fixtures.v1.json`.

This cycle does **not** introduce a partial category. It introduces only the
typed admission vocabulary whose fields are independently exercised by the
theta and Kitaev sectors.

## Formal objects

- `GrantSignature Obj Domain` records source, target, authority kind, evidence
  domain, and variance.
- `PairwiseTyped g h` requires endpoint, authority kind, evidence domain, and
  variance equality. Thus authority kind cannot increase by composition.
- `CompositionWitness g h` additionally contains an explicit coherence defect
  and a proof that it vanishes.
- `TripleAudit` preserves the hostile distinction between pairwise admission
  and triple coherence.

## Sector tests

- Folded theta is **coherent-only**: its two grants have positive and doubled
  evidence domains. The theorem `theta_needs_domain_extension` proves that the
  strict shared interface rejects them. The missing interface is a typed domain
  extension/transport plus the moving-endpoint seam-current coherence cell.
- Kitaev is **noncomposable**: `kitaev_lift_is_not_admissible` records that a
  logical capability does not preserve authority or evidence typing when
  treated as a five-rail physical lift.
- `pairwise_does_not_supply_triple_coherence` executes the hostile fixture with
  two admitted adjacent pairs and nonzero triple defect.

## Disposition

**Failed to generalize; specialized as an admission audit.** There are not two
independent positive sector constructions with the same domain-composition
operation. Adding `compose` or category laws now would erase the theta domain
extension and the Kitaev authority failure.

## Missing convention-fixed inputs

1. A type of evidence-domain morphisms distinguishing transport, intersection,
   and authority extension.
2. The direction and functorial law for variance under each domain morphism.
3. A source-derived proof that the theta positive domain extends to the doubled
   domain without increasing authority.
4. The exact type and gluing law of the moving-seam coherence witness.
5. A second independently established positive sector composition using the
   same operations, before associativity or partial-category laws are shared.

## Verification

Run from `research/buzzard/marici_formal`:

```text
lake build
```

Result: `Build completed successfully (8712 jobs).` Lean/mathlib version:
`v4.33.1`. This certifies only the Lean statements above, not the sector
assumptions that motivate them.
