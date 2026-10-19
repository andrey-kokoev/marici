# Rung symmetry atlas v1: objects before group names

## Main result

There is no justified single group assignment per numerical rung. The useful classification is indexed by **rung, carrier, retained structure, allowed action, and observer**.

A new finite check reuses the actual retained-index constructors. For endpoint-labelled, constant-payload directed-edge records, source-indexing (12→11) and target-regrouping (11→10) commute with all 24 vertex permutations. Each action satisfies all 576 composition pairs on each indexed presentation. The same support stabilizer is recovered at all three presentations. Keeping the folder names fixed while relabelling the records is rejected as a noncommuting control.

The existing seed transport, conditional edge-lift, and 36-component simplex-operation suites were also freshly replayed. Their results are retained at their original scopes; no missing physical or field-to-record adapter is supplied by this atlas.

Machine-readable companion: `rung-symmetry-atlas-v1.json`.

## The actual diagram

```
12 --9--> 6
 |        |
11 --8--> 5
 |        |
10 --7--> 4
```

Here 9, 8 and 7 name horizontal transports. They are not additional state spaces inserted between the other presentations. This is the clarified diagram, not the older eight-successor label/from/to recurrence.

| Rung or role | Object / retained structure | What is checked | What remains unassigned |
|---|---|---|---|
| 12 | Individually labelled records, endpoints, values, masses and available histories | Vertex-relabelling action on support exemplars; existing seed-response encoding | Full symmetry of arbitrary payloads; field-to-record binding |
| 11 | Same complete records in source-indexed families | New exact relabelling/indexing square and group law | No new A4 or V4 assignment arises from indexing |
| 10 | Same complete records regrouped by target | New exact relabelling/regrouping square and group law | Not a quotient or loss of orientation |
| 9 / T9 | Horizontal promotion/generation on a declared input domain | Existing retained promotions and seed response survive transport | Full-field intertwiner and independently selected physical dynamics |
| 8 / T8 | Source-indexed presentation of T9 | Existing upper square commutes | Not an independent new group or dynamical law |
| 7 / T7 | Target-indexed presentation of T9 | Existing lower square commutes | Not an independent new group or dynamical law |
| 6 | Promoted records with members, masses and intermediate provenance | Existing seed response and original leaves retained | Full promoted-payload automorphisms and fresh-label action |
| 5 | Promoted records indexed by source | Existing retained reconstruction and square | No new group selected by indexing |
| 4 | Promoted records indexed by target, with separately specified reference/readout | Existing seed response reaches both routes; moved probes give covariant readings | Physical metric/calibration and observer-selected stabilizer |

The new support tests use the owning `Row`, `indexed`, and `unindex` implementations. Their fixtures are **not** the full original 137-slot numerical/DG source. The existing seed checker provides a different concrete adapter: four column records encoding permutation responses. These different input domains are not silently identified.

## What actually changes symmetry?

All orders below refer to vertex permutations preserving the declared structure, except the separate field row.

| Structure | Group / order | Rung significance |
|---|---|---|
| Complete directed support on four vertices, no orientation restriction | S4 / 24 | Same stabilizer at 12, 11, 10 in the new support tests |
| Same tetrahedron with handedness retained | A4 / 12 | Extra retained structure, not a numerical-rung deduction |
| Four-state support with one distinguished vertex | S3 / 6 | A marked vertex differs from an oriented tetrahedron |
| Complete directed support with one specified directed edge removed | S2 / 2 | Fixes the two ordered endpoints, permits spectator swap; same at 12, 11, 10 |
| Actual six-arrow seed | C2 / 2 | Identity and (AB)(CD); same at 12, 11, 10 |
| That seed with its ordered generator pair retained | Trivial / 1 | Existing seed checker: the swap exchanges the generators and is excluded |
| Declared P-field rotations and projector reflections | A4 × V4 / 48 | Generated group on 36 field components; numerical rung **not assigned** |

The two order-two support stabilizers above have different concrete actions. Equal order alone does not identify structures or maps.

The full S4 acts covariantly on the *family* of relabelled marked seeds even when a particular fixed seed has only a two-element stabilizer. Likewise, carrying a named preparation and reader with the source gives a covariant observation; demanding that a fixed unmarked observer be invariant is a different requirement.

## Why retained indexing preserves the tested symmetry

For a record collection E with source map s, retain each record inside its source family:

```
Index_s(E)[a] = all complete records with source a.
```

An admissible relabelling must move both the source keys and their members. Then

```
Index_s(g E) = g Index_s(E).
```

Unindexing reconstructs the complete original records. In these fixtures, a relabelling fixes the source-indexed presentation exactly when it fixes the original collection. The same applies to target indexing. Nothing here removes an orientation, selects one vertex, projects out a field sector, or creates a new exchange operation.

This preserves the declared relabelling action; it is not a classification of every set-theoretic automorphism or arbitrary linear transformation of the record space. If values, C/M marks, forms, history or a fixed observation are added, their action and preservation conditions must also be checked.

## Existing field result: do not attach it by numerology

The freshly replayed `check_simplex_interface_algebra.py` verifies:

- four orthogonal projector sectors with ranks **1, 11, 2, 22**;
- two commuting projector-derived reflections;
- twelve independently constructed proper tetrahedral actions;
- **48 distinct matrices** forming A4 × C2 × C2.

This is the group generated by those declared operations, not the entire automorphism group of the field. Neither rank 11 nor twelve rotations locates the object at rung 11 or 12. `rotation-realization-square-v1.md` explicitly leaves that assignment open. The two internal involutions are not automatically edge transport or mirror symmetries.

To attach this entry to a rung, the missing object is a typed map from the decorated field to the rung's full record payload/Context, with an intertwining equation for each intended action. Matching twelve directed support labels is useful but does not carry all field amplitudes, projectors or preparation data.

## Prior research consolidated

1. `research/nima/rung-transport-diagram-and-fixed-reference.md`: clarified diagram and retained indexing; two comparison policies in its historical checker.
2. `research/nima/pinned-T9-software-contract.md`: later fixed inherited-key software policy. Replaying both older policies is a control, not a claim that the current software policy is undecided.
3. `research/nima/seed-cycle-response-through-retained-rungs.md`: actual seed permutations, ordered responses, fixed-reference readout, covariant marked probes and seed stabilizers. Freshly replayed.
4. `research/nima/equivariant-edge-lifts-and-spectator-policy.md`: two conditional edge lifts, generating S4 or V4, distinguished by spectator action and triangle holonomy. Freshly replayed; neither becomes a rung assignment.
5. `research/strominger/simplex-interface-algebra-v1.md` and `rotation-realization-square-v1.md`: exact field operations and the missing rung adapter. Simplex suite freshly replayed, including its rotation dependency.
6. `research/nima/label-from-to-fibration-tower.md`: historical proposed gauge-name table; its gauge assignments are not derived and its schedule is different.
7. `research/voevodsky/symmetry-descent-and-complementary-observers-programme-v5.md`: general typed transfer framework. Consulted, not freshly reverified here.

## Follow-up: candidate 36-to-137 field decoration

`field-36-to-137-refibration-v1.md` now supplies a lossless **pair-valued** decoration of the existing 137-leaf generator: eleven arrow roles and four derived source-vertex fibers. All 36 field components reconstruct, and the twelve native proper rotations commute with the construction. Raw/source/target views contain 137 leaves under 137/32/32 outer entries.

This is progress beyond a bare support match, not a completed numerical rung assignment. The chosen source fibers are not yet identified with the old independently supplied state-root preparation. Numerical/DG legs, d, and the full right-rung promotion contract still need a typed adapter. The field action therefore remains unassigned to a numerical rung in this atlas.

## Next precise obligations

- Construct the field-to-actual-record adapter, preserving payload, marked endpoints, coefficients and provenance.
- Specify the action on fresh promoted labels and verify full horizontal equivariance, rather than inferring it from the already checked presentation squares.
- Classify fixed-configuration and fixed-observer stabilizers separately from relabelling covariance.
- Test the declared action on the full 137-slot numerical/DG source, including its excluded edge, supplied roots and context. Support-level S4 covariance is not enough.

## Reproduction and boundaries

```
python research/strominger/checkers/check_rung_symmetry_atlas.py
```

This validates the atlas schema/entries, performs the new finite tests, and freshly runs the existing seed/rung, edge-lift, and simplex-operation checks. Output is the ignored runtime receipt `research/strominger/results/rung-symmetry-atlas/verification.json`, with direct audit-source hashes and replay logs. The owning simplex receipt additionally records its source dependencies. This is not an assertion that the direct hash list is a complete transitive dependency manifest for every old checker.

No website, viewer, group assignment to physical gauge fields, or deployment is changed.
