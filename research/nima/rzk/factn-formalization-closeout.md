# `Fact_n` Rzk formalization: tested closeout

## Checked constructions

The headless Rzk 0.11.3 suite checks the following modules against pinned sHoTT source digest `b396523107ce51d24fb8e248c6f8409f2e1efd402854843791356d29a07566a8`:

1. `01-factn-refinement-face-interface.rzk.md`: refinement, face-product, and naturality interfaces.
2. `02-fact5-single-diagonal-face.rzk.md`: three-element face/quadrilateral equivalence.
3. `03-fact5-dissection-exhaustion.rzk.md`: explicit eleven-element pentagon fixture and exhaustive face-13 classification.
4. `04-fact5-face-order-isomorphism.rzk.md`: directed refinement-graph isomorphism.
5. `05-fact5-nondegenerate-segal-two.rzk.md`: equivalence of the ten nondegenerate two-spines and ten filled triangles.
6. `06-fact5-nested-cut-naturality.rzk.md`: object-level two-step naturality through face 13.
7. `07-fact5-biadjoint-residue-support.rzk.md`: channel-13 cubic residue support.
8. `08-fact5-all-channel-residue-incidence.rzk.md`: all 25 channel-term incidences.
9. `09-fact5-formal-rational-residue-values.rzk.md`: formal sums of inverse propagators.
10. `10-fact5-algebraic-residue-interpretation.rzk.md`: evaluation in any supplied additive carrier with inverse-propagator values.

## Exact demonstrated scope

At five points, the finite constructor model verifies:

- the face above one diagonal is the dissection type of the residual quadrilateral after suppressing a contractible triangle factor;
- this equivalence preserves all refinement arrows in that height-one face;
- every nondegenerate length-two refinement chain has one retained triangle constructor;
- direct and nested inclusions agree for the two refinements through face 13;
- planar cubic residue support and the five formal values `1/X_a + 1/X_b` agree with the residual quadrilateral diagrams.

## Unclosed requirements

### Genuine simplicial type

No genuine directed type with these objects and refinement homs has been constructed. The finite `TwoSpine`/`Triangle` equivalence is not an inhabitant of `is-segal Fact_5`. Identity degeneracies have not been represented as simplicial degeneracy maps. Rezk completeness has not been proved.

Pinned sHoTT supplies predicates and consequences for already-given Segal/Rezk types but no located nerve or Rezk-completion constructor from a strict finite poset. An ordinary inductive dissection type is discrete and therefore cannot realize nonidentity refinement homs.

### Generic polygons

No generic `Fin(n)`, finite subset, list/vector, pairwise noncrossing family, or region-component construction has been defined. The eleven pentagon objects are enumerated constructors. Hence no theorem currently quantifies over `n`, and no finite-to-generic promotion is licensed.

### Algebraic amplitudes

The residue values are syntax interpreted in an arbitrary supplied carrier. There is no constructed multivariate rational-function field, no channel-variable algebraic independence theorem, and no Laurent coefficient/residue operator. Consequently the formal identities are not yet analytic residue theorems.

## Blocking object and reopening condition

The first blocking object is a checked directed nerve constructor for finite posets,

```text
nerve-poset : Poset -> U
```

with hom identification, Segal structure, identity degeneracies, and Rezk completeness. No further enumeration can substitute for it.

Reopen this branch only when either:

1. an Rzk/sHoTT extension supplies such a constructor with a checked contract; or
2. a permitted foundation change provides a formal simplicial-object/nerve library and an explicit interpretation back into Rzk.

After that transition, finite-family infrastructure and generic region decomposition become executable. Without it, claims of a genuine `Fact_n` simplicial type would be assumptions presented as constructions.
