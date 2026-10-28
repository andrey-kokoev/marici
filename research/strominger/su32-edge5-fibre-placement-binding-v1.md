# Edge-5 candidate fibre and placement domains

## Constructed

The first explicit candidate binding now retains:

- **80 named fibre identities**, indexed by the actual native P cells;
- a reflected E presentation for each identity;
- all **320 actual face occurrences per presentation side**;
- the same 80 logical fibre occurrences at the entry and exit N-body boundaries;
- four actual passage-face choices at each boundary;
- **eight eligible global-middle placement triples** extending the native-edge condition.

These are concrete domains for a later simultaneous assignment, not completed paths.

## Fibre identities and the reflected presentation

The identity is `edge5-fibre:<P-cell-id>`. Its opposite presentation is the E cell obtained by middle-plane reflection for the fixed reading. Each of its four source faces maps to an actual face of that E cell; the exact cell-face occurrence identities and coordinate-axis correspondence are retained.

This is an **explicit candidate presentation convention**. Geometry makes the association precise and reversible, but does not prove that the paired cells are physically connected by a fibre. No period-four closure or lexically selected target is imported from the earlier candidate.

The 320 face occurrences on each side are incidences of 80 fibres, not 320 newly independent contents.

## Boundary domains

The entry boundary is the selected incoming N body; the exit is its reflected N body. Both expose the same complete fibre inventory. These are logical bundle occurrences at a shared-body attachment, not eighty invented physical faces.

All four actual entry-forward shared faces and all four exit-backward shared faces are recorded. Individual fibre-to-face allocations remain variables. The map from the external bundle to the body-wide P/E presentations is not supplied by merely assigning their identities.

## Scope of the incidence placement condition

The proposed first edge-5 extension uses **one global middle-plane readout triple**, rather than assigning an independent edge-3 pattern to every comparison cone.

The middle plane contains 25 N cells and four transverse tips. Each transverse tip T has exactly two middle-plane N neighbours sharing actual native edges with it. Assigning those two neighbours the ordered roles U=P/P and V=E/E yields two triples per tip, hence eight in total.

Every triple retains its two actual shared edges and T's opposite-tip group. A later routing must still establish that both tip-group members are active, the selected records are available at T,U,V, and the remaining cross-pair placements are specified. No candidate triple is selected yet.

This scope is a declared extension hypothesis, not a result derived from the edge-3 census. It remains compatible with retaining all 44 edge-5 cones as contextual obligations; those cones are not replaced by eight independent routing copies.

## Reference names are not face-axis names

The two P references, two E references and four entry joint pairings are also enumerated at binding `[0,0]`. Their directional labels are not equated to the four coordinate face axes. The signed-record-to-fibre-occurrence map remains a separate binding.

## Verification

Contract: `contracts/su32-edge5-fibre-placement-binding-v1.json`.

```sh
node research/strominger/checkers/check_su32_edge5_fibre_placement_binding.mjs
```

Fresh execution checked all 80 identity associations, 640 face occurrences, actual boundary-face correspondence, exact presentation reversal, preservation of the boundary inventory, and all eight native-edge triples. The receipt is losslessly serializable and pins the prior contract and source hashes.

Receipt: `results/su32-edge5-fibre-placement-binding-v1/verification.json`.

Remaining route obligations are explicit: fibre-to-boundary-face allocation, paths to the body-wide presentations, signed-reference binding, internal junctions, boundary closure and contextual operations/fillers. No route or native dynamics is claimed by this deliverable.
