# Nitrogen compositions: fixed-footprint completion through origin 3

## Question and scope

Following the operator's request to compare conjectured nuclear layouts, test the D2 atlas selections with 7P/7N and their immediate 7P/8N extensions. Preserve the reference-construction rules; do not import physical assumptions from the literature.

A complete **packet universe** through D3 contains 87 packets and 123 allowed operations. This is not a complete enumeration of D3 configurations. An attempted unrestricted D3 Boolean-family compilation hit its explicit 250,000-node resource guard; no unrestricted D3 completeness claim follows.

## Results

| Test | N14-composition parents | Immediate N15-composition extensions |
|---|---:|---:|
| Cases examined | 256 | 464 parent/extension incidences |
| Already exit-certified | 0 | 0 |
| Cases with individually unavailable contact witnesses at D3 | 0 | 0 |
| Exit-certified fixed-footprint completions through D3 | 0 | 0 |
| Independently blocked even in relaxed candidate-union exit graph | 256 | 464 |

248 of the 256 N14 parents permit at least one immediate additional neutron. Every one of the 464 additions is an NN-phase-advance to origin3. Each new neutron has **exactly one nuclear face contact**: it is a branch tip, not a bridge between existing nuclear bodies. Other immediate neutron targets encounter 352 occupied-cell/species conflicts. These are incidences, not distinct final geometries.

The original N14 cases have 2–3 unwitnessed contacts each: 360 PN and 256 NN contact incidences overall. Every missing contact has a compatible source/target witness pair in the D3 packet universe when considered individually. This alone does not establish rooted simultaneous completion.

The N15 extensions retain unresolved PN/NN contacts and can introduce NE contact obligations (1268 missing-contact incidences total: 628 PN, 464 NN, 176 NE). All of these likewise have individually compatible witnesses.

## Exact conditional completion test

For each of the 720 cases, require:

1. All original selected records remain selected.
2. Nuclear bodies remain at precisely their original cells with their original species. Additional records on those bodies are allowed.
3. Compatible electron bodies and their records are unrestricted within D3; there is **no neutral-electron-count requirement**.
4. All selected records are reachable from the seed, all required contacts have selected witnesses, and every selected record can reach a selected E exit.

The reduced Boolean diagram includes pairwise compatibility, rooted support on the verified acyclic PN-component condensation, dual exit support, and all contact-witness clauses. Every one of these conditional families has zero models.

An independent necessary-condition test confirms all 720 rejections: take the union of **every** individually seed-compatible packet on the permitted nuclear footprint, together with all individually compatible electrons, ignoring incompatibility between those additions. Even this optimistic graph leaves original selected records without any route to an E exit. Any actual completion is a subgraph, so cannot repair that failure.

Blocked original records occur at origins1 and2, not solely at the newly added neutron. Adding one more neutron does not resolve the older branch obligations.

A positive control on the root PN/NE construction has 23 completions under the same D3 fixed-footprint compiler. All 23 were independently reconstructed from the seed with compatible prefixes and checked using the original whole-state contact/exit inspector. This guards against an accidentally always-empty completion compiler.

## What the literature contributes

Search used `pnpm pdf:search` with nitrogen, nuclear/tetrahedron, and coordinate/symmetry queries. The following observations are from indexed text and captions; no geometric equivalence to the atlas was proved.

- **Jozsef Garai, The double tetrahedron structure of the nucleus**, `references/0309035v2.pdf`: pp2–3 discuss FCC sphere packing, tetrahedral layers and preferential symmetric occupancy; p8 Fig4 describes proposed nuclear layouts; p9 FigS1 layers; pp12–15 TableS1 gives coordinates. Useful hypothesis: compare contact connectivity, shell placement and symmetry rather than composition alone. A tetrahedral cluster of spheres is not our marked tetrahedral-body primitive.
- **Migal and Bondarev, Computer visualization of the spatial structure of the atomic nucleus**, DOI 10.18413/2518-1092-2022-7-2-0-1, search alias `72-1-iqfyd1k`: PDF p4 permits proton, neutron or deuteron cell occupancy; pp11–13 distinguish paired, binding and additional neutron roles. Useful hypothesis: distinguish a neutron that bridges existing substructures from a neutron at a terminal site. Their cell/co-occupancy conventions are not our occupancy rules.

These conjectured layouts do not supply a validated Hamiltonian, binding proof, or permission to bypass reference witnesses. In our tested extensions the additional neutron has the terminal role, not the proposed bridge role.

## Interpretation and next discriminating tests

The obstruction is **not** that D3 lacks any individual PN/NN witness, nor merely that electron counts are too low. The selected histories and fixed nuclear placement leave branches with no admissible exit route even in a relaxed graph.

This does not exclude other N14/N15 structures at D3. Next tests should separate:

- a different arrangement of the same nuclear counts, generated from the seed rather than retrofitted onto these D2 footprints;
- more origin depth while retaining these footprints;
- a different retained history on the same geometry, if independently justified by the intended observer semantics. The present certificate explicitly retains historical records; do not silently discard them.

No new physical stability, global coupled-field sewing, isotope exclusion, or atom-neutrality conclusion is established. No base construction rule or existing atlas was changed.

## Reproduction

```sh
node research/nima/checkers/check_nitrogen_contact_extensions.mjs
```

[Checker](checkers/check_nitrogen_contact_extensions.mjs) · [Full receipt, witness candidates and registry](results/nitrogen-contact-extensions/verification.json)

Receipt includes atlas/checker/generator source hashes, each original selection, each missing-contact witness candidate and rejection reason, extension placement, exact completion counts, and independently blocked records. The headless checker completed successfully after the final source changes.
