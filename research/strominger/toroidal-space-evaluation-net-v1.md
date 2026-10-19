# Toroidal space evaluation: live conjecture net

**Contract:** [toroidal-space-evaluation-net.v1.json](contracts/toroidal-space-evaluation-net.v1.json)  
**Audit:** `checkers/check_toroidal_space_evaluation_net.py`  
**Parent:** [field-realization/instrument net](field-realization-instrument-conjecture-net-v1.md)

This is the maintained owner-local branch for evaluating `{3,6}_{(2,0)}` against our actual problem. The parent net's dispositions and frontier are not changed. This document and the contract expose the research decisions, dependencies and continuation priorities; they are not private reasoning traces or measurements of physical energy.

## Current answer

The torus has an exact positive relation to our declared twelve-channel field: its A4 channel action, explicit tetrahedral realization, field frames B, metric and retained comparison protocol correspond. This is stronger than a symmetry analogy.

The relation has identifiable costs and choices: left-face convention, cyclic mode, coordinate identification, reference, deck information, and source-fiber organization. Different realizations preserve different structures. Those distinctions—not a generic assurance about future work—determine the continuation branches below.

## FCC update (revision 2)

The [FCC test](fcc-toroidal-field-v1.md) adds three supported nodes (`FCC-quotient`, `FCC-refinement-family`, `FCC-pose-field`) and rejects three fixed-structure claims (`rival-FCC-fixed-refinement`, `rival-FCC-fixed-frame`, `rival-FCC-center-star-native`).

The unrefined geometry passes 192 boundary-neighbor covariance checks. Only four of twelve actions preserve the source subdivision. Pose-dependent frames pass all twelve field squares; one fixed frame fails nine. The family of three subdivisions is equivariant, but moving among its members is not thereby a native operation.

This exposed the first discriminator `FCC-refinement-interface`, resolved by the next construction.

## Eight-sector interface (revision 3)

The [eight-sector interface](eight-sector-interface-v1.md) supplies a common comparison space for all three diagonal subdivisions, plus an antipodal cube-to-tetrahedron chart. Retaining averages and differences makes all 16 chart changes invertible and all 64 composition triangles commute.

With both existing phase-aware N bindings, the interface recovers all five coefficients for each of four actual native reader contexts, their absolute origins and full source provenance. A coherent NN-chain fixture and independent-record fixtures both pass. Source N field norms and uniform L/G/corner-cycle operations are preserved. Proper-root sector symmetry and affine pose/deck transport are separately checked.

`FCC-refinement-interface` is **supported for this read-only task**. Two stronger simplifications are rejected: `rival-refinement-average-only` loses information, while `rival-refinement-face-pair-locality` fails because some transported NN channels touch all four target coarse pairs. The source grammar remains unchanged.

At revision 3 there were **27 nodes: 12 supported, 10 rejected, 5 open**. Closing the FCC comparison task returned `P-reader-lift` to first place. The N toroidal-incidence question remains distinct from the completed eight-sector comparison.

## Chamon construction branch (revision 4)

The [Chamon branch note](chamon-conjectures-v1.md) registers five open conjectures from `references/2210.09867v2.pdf`: the FCC stabilizer benchmark, paired spatial/internal symmetry, defect and boundary rules, refinement-compatible observables, and boundary difference fields.

The first task is `Chamon-FCC-benchmark`: construct the 32-spin period-four model, verify commuting signed Pauli generators of rank 24 and a 256-dimensional ground space, and reproduce the trivial period-two collapse as a control. Its small exact calculation provides the operator dictionary needed downstream, so it takes first priority; the existing P-reader task moves to second without changing its verdict.

At registration there were **32 nodes: 12 supported, 10 rejected, 10 open**, with five ready tasks. The subsequent checked construction is recorded below.

## Existing constructions found (revision 5)

The [reuse search](chamon-existing-constructions-v1.md) found a tetrahedral-octahedral gauge model with an explicit polynomial Clifford map to Chamon, entanglement-renormalization circuits, a honeycomb topological defect network with interface rules, and public stabilizer/syndrome code. Targeted primary text and the implementation were inspected after discovery through ask.sciencemadereadable.com.

The benchmark now starts by adapting the existing code as an independent reference. Operator-refinement work starts from the published maps and gluing rules. The 32-node counts and frontier remain unchanged: these are inputs to our local compatibility checks, not substitutes for them.

## Checked Chamon benchmark and polynomial dictionary (revision 6)

The [benchmark](chamon-fcc-benchmark-v1.md) passes on four covers. The actual native octahedra give 32 spins, rank 24 and a 256-dimensional ground space on the period-four cover; all stabilizer phases and class products are checked. Across three noncollapsed covers, all 236 rows agree with the pinned upstream builder after coordinate conversion. Period two collapses to identity stabilizers as predicted.

The published Laurent stabilizer column also matches all 240 generated octahedra through an explicit primitive-coordinate, anchor and Pauli-frame dictionary. Its formal commutation identity passes, and the physical metric and actual primitive periods remain recorded.

`Chamon-FCC-benchmark` and the new `Chamon-polynomial-dictionary` are supported. At revision 6 there were **33 nodes: 14 supported, 10 rejected, 9 open**, with seven ready tasks. The operator-map import was prioritized.

## Checked operator map and refinement observables (revision 7)

The [Appendix B import](chamon-gauge-map-v1.md) passes exact symplectic/stabilizer identities, honeycomb incidence, the supplementary 58-step gate-and-reindexing reduction, and signed tests on 32-, 64- and 256-spin covers. All four existing charts preserve operator records, products, norms and shared-site identities. Ancilla frames, phases and the sublattice translation remain explicit; no quantum-to-neutron-field coupling is inferred.

`Chamon-refinement-observables` is supported. Current totals: **33 nodes: 15 supported, 10 rejected, 8 open**. Six tasks are ready, starting with spatial/internal symmetry. Boundary difference fields now await only defect/boundary rules; `PN-lift` still awaits both reader lifts.

## Evidence-backed initial nodes

| Node | Verdict | What the evidence establishes |
|---|---|---|
| `channels` | Supported | Four classes, twelve directed channels, the specified A4 action. |
| `decorated-field` | Supported | Metric and L/G/C preserved as specified field data. |
| `geometric-B` | Supported | Realized left-face sectors recover B and its metric; H has determinant -1 as a coordinate identification. |
| `comparisons` | Supported | All references and ordered-parent comparison data are equivariant. |
| `rival-surface-isomorphism` | Rejected | Torus and tetrahedral boundary have different topology and cell incidence. |
| `deck-information` | Supported | Reverse-labelled channel returns can retain nonzero deck displacement. |
| `dual-tetrahedron` | Supported | Collapsed dual gives -B, but identifies pairs of dual vertices. |
| `dual-cube` | Supported | Faithful eight-vertex dual realization, full group order 48. |
| `rival-cube-B` | Rejected | The same centroid-edge frame recipe has rank two on the cube/Petrie dual. |
| `dual-operator-map` | Supported | Dual channel permutation preserves metric, named operators and A4. |
| `rival-dual-endpoints` | Rejected | That permutation is not a four-endpoint relabelling. |
| `import-fixed-N` | Rejected | Existing fixed N five-coefficient binding has rank at most three. Phase-dependent bindings are a different, nonunique class. |
| `import-strict-PN` | Rejected | Existing restricted-character obstruction excludes the specified strict geometric C3/role-exchange PN task. |

Every node's exact statement, scope, receipt observations and reopening condition are in the contract. “Supported” does not promote a larger physical or transfer interpretation. “Rejected” applies to its stated candidate class, not to every possible toroidal model.

## Dependency structure

```text
channels ──> decorated-field ──> comparisons
    └──────> geometric-B
    ├──────> deck-information
    └──────> dual-cube ──> rejected cube-centroid-B recipe

geometric-B ──> collapsed dual-tetrahedron
                  + decorated-field ──> dual operator map
                                          └─> rejected endpoint relabelling

geometric-B + comparisons + deck-information ──> P-reader-lift
geometric-B + comparisons                    ──> choice-selection
operator duality + rejected endpoint shortcut
                 + comparisons              ──> dual-comparison-transport
decorated-field + rejected fixed-N binding   ──> N-reader-lift

P-reader-lift + N-reader-lift
              + rejected strict-PN shortcut  ──> PN-lift [blocked]
```

Arrows express readiness requirements with explicit required verdicts. They are not proof implications. A rejected shortcut can enable a differently specified rival without being revived.

## Frontier and expected value of continuation

These priorities are qualitative research judgments, not success probabilities or physical energies. The contract records what a positive or negative result would change.

### 1. `Chamon-spatial-internal-symmetry` — recommended start

**Test:** pair spatial generators with internal Clifford conjugations and verify signed stabilizer images and composition, retaining deck offsets and implementer-phase conventions.

**Value:** high information gain for low-to-medium effort using the checked coordinate and Pauli dictionary.

### 2. `Chamon-defect-boundary-rules`

**Test:** construct syndrome words for ribbons, cages and boundary fusion; compare both layer terminations and their surviving class parities.

**Value:** high information gain for medium effort; supplies the lattice charge target for boundary-field construction.

### 3. `P-reader-lift`

**Proposition:** the selected P reader task has a coefficient-compatible toroidal lift retaining deck displacement and absolute origin.

**Test:** the four-vertex permutation `(2,3,0,1)` is torus translation e2. Use the actual five-slot P advance and the existing five-to-36 field interface. Check one and two advances, with field action, all coefficients, deck displacement and realization origin recorded separately. Two advances may be identity on quotient addresses while retaining origin +2 and chosen lift displacement 2e2.

**Value:** high information gain for low-to-medium effort. It is a concrete bridge test with available source operations. It does not pretend that P success would imply N or PN success. The choice of a planar lift must remain explicit rather than being called canonical by default.

### 4. `choice-selection`

**Proposition:** the task selects the realization/orientation/mode/reference up to admitted equivalence.

**Test:** compare remaining choices under the same task observations and actual admitted symmetry group. A source-defined selector or equivalence classification supports the proposition; indistinguishable inequivalent choices refute uniqueness for that task.

**Value:** high information gain for medium effort. This distinguishes a useful representation from a representation determined by the problem itself.

### 5. `dual-comparison-transport`

**Proposition:** an explicit changed comparison presentation transports the full field through duality while retaining the change of source fibers.

**Test:** decode, apply channel duality, and re-encode with a declared transformed reference and incidence contract. Compare that global re-encoding with the stronger demand for a local typed morphism.

**Value:** medium information gain for low-to-medium effort. It identifies the exact structural cost of duality instead of conflating operator preservation with endpoint preservation.

### 6. `N-reader-lift`

**Proposition:** a phase-aware toroidal representation can retain the specified N reader task and all five coefficients.

**Test:** first retain or explicitly change native N locality: eighteen two-component patches are not P's twelve triples. Test a declared phase-dependent binding family, including the already known nonuniqueness of its seeds. Do not re-run the rejected fixed-binding proposal under a new name.

**Value:** high information gain for medium-to-high effort, with more interface choices than P.

### Dependency-gated Chamon tasks

`Chamon-boundary-difference-fields` requires supported boundary rules. Its operator-refinement prerequisite is now supported.

### Blocked: `PN-lift`

This needs specified P and N interfaces. Its contract must state whether the target C3 is geometric or internal. The already-rejected strict geometric action cannot be silently replaced and then reported as validated.

## Decision trail

The contract retains the public evidential trajectory:

1. Channel and decorated-field correspondence established a concrete representation.
2. The paper supplied explicit realization alternatives.
3. Recovering B strengthened the relation to the actual field geometry.
4. The dual branches separated topology retention from reuse of the centroid frame.
5. The source-fiber counterexample separated operator equivalence from typed transport.
6. Existing coefficient-binding and PN obstructions constrain the transfer frontier.
7. The FCC test separates honeycomb covariance, fixed-refinement failure and pose-dependent field success. It opens the explicitly indexed refinement-interface branch without changing native rules.
8. The eight-sector construction closes that read-only interface task. Full coefficient/context recovery succeeds; averages alone lose information, and transported NN support can expand to four coarse pairs. The remaining frontier is reviewed rather than silently replaced.
9. The supplied Chamon paper opens a concrete quantum-model branch on the FCC support. Five conjectures are registered, starting with the finite stabilizer benchmark and retaining the downstream dependency gates.
10. Online search finds existing honeycomb quantum constructions and source code. Tasks shift from deriving those structures afresh to importing their dictionaries and checking compatibility with our interfaces.
11. The native FCC benchmark passes and the published Laurent column is matched exactly. Register the polynomial dictionary and prioritize the larger operator-map import, retaining metric, periodic quotient and auxiliary-degree accounting.
12. Appendix B and its supplementary reduction pass, including signed operator transport through all four existing charts. Support the scoped operator-refinement node; retain the ancillas, translated wire and phase convention. Spatial/internal symmetry is next; boundary and reader-field coupling claims remain separate.

No expected-positive verdict is attached to an open node. The removed double-helix objective is not a dependency or continuation in this net.

## Maintenance and verification

For every new result:

1. Freeze the task, candidate class and rival before changing a verdict.
2. Link the checker, receipt and decisive observation.
3. Update only the scoped affected nodes; retain rejected alternatives and their reopening conditions.
4. Append the decision trail and recompute the dependency frontier.
5. Review priorities with reasons, rather than inferring importance from whichever check ran last.

Run:

```
python research/strominger/checkers/check_toroidal_space_evaluation_net.py
```

The net audit checks dependency acyclicity, required verdicts, evidence assertions and direct receipt freshness, frontier ordering, parent navigation, recognition by the repository's conjecture-net collector, and mutation controls. Collector recognition is read-only here; no shared collection or parent verdict is rewritten. It writes `results/toroidal-space-evaluation-net/verification.json`. This audit is registration/evidence validation, not a new scientific proof or a run of the open frontier tests.
