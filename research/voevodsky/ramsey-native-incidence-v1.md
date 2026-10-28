# Native retained incidence packages with coherent reindexing

## Actual native construction

`agda/RamseyNativeRetainedIncidence.agda` uses the existing `NativeTableRules` and `NativeTableResolution`, not an imitation constructor calculus. Its declared input policy admits only full typed parent-port values:

    (port identity, its Permit proof, literal full source-bound record).

The record includes the prior actual PN source/target packets, named references, cell data, operation, history positions and parent-triangle certificate. The permit is also carried as a typed component, not only embedded in a string. No edge, selected incidence, restriction or comparison result is seeded.

For an indexed family of parents, native P constructs the full retained family. Its common-support type is

    Common(I,parent) = Sigma vertex ((i:I) -> Inside(parent i,vertex)).

Native E selects only an actual inhabitant of that type and retains the P family. The kernel proves exact recovery of the support witness, every indexed full parent value and the corresponding native input derivation.

## Restriction policy and composition

A reindexing r:J->I retains the selected subfamily and pulls back each support certificate. The generic theorem proves that successive reindexings r and s agree with their composite, both on the common-support witness and on the resulting native selected package.

This is reconstruction of the restricted package with actual P/E constructors, not a newly invented native primitive rule named restriction. Reindexing may drop parents outside its selected subfamily; it preserves each retained parent literally. It must not be described as recovering discarded parents from an edge readout.

The theorem accepts general reindexings, including repetitions, so occurrence indices remain explicit. It does not identify unequal role assignments or unrelated proof witnesses.

## Source-bound concrete instances

The generated examples quote the four complete port records from `results/ramsey-lifted-facet-incidence-v1.json`. For each omitted-vertex facet, the kernel evaluates the chart-specific role function and verifies that the parent triangle has exactly two M vertices. The two complementary role contexts are not collapsed into a global role assignment.

The support relation excludes the omitted vertex. The concrete module admits:

-12 selections: each of the six geometric edges at either of its two endpoints;
-4 selections: each triple of facets at its unique common vertex;
-the native family of all four parents, even though their common support is empty.

The kernel proves that no vertex lies in all four facets. A separate hostile module tries to select such a vertex and fails type checking. No common fourfold E selection is fabricated from the existence of the P family.

The examples establish combinatorial support and the source-bound typed permit values. The kernel does not interpret the source JavaScript geometry, operation validation or exact multiradical field matrices. Those remain bound to the prior runtime receipts.

## Verification

The prospective contract, generic source, generated instances and checker were frozen before tests:

`scc-freezes/ramsey-native-incidence-v1.44e2fa1299abebfc.json`.

The frozen SCC challenge passes. Both positive modules pass fresh safe Cubical checking with `--ignore-interfaces`; the empty-fourfold hostile is rejected. The runner records compiler hash and complete source inventories and confirms they remain unchanged during checking.

Artifacts:

- `contracts/ramsey-native-incidence-attempt.v1.json`
- `agda/RamseyNativeRetainedIncidence.agda`
- `fixtures/ramsey-native-incidence/RamseyNativeIncidenceExamples.agda`
- `fixtures/ramsey-native-incidence/RamseyNativeIncidenceBadFourfold.agda`
- `checkers/check_ramsey_native_incidence.py`
- `results/ramsey-native-incidence-v1.json`

## Remaining parent gate

This closes native admission of **retained incidence and support-restriction packages under the stated input policy**. It does not yet install the numerical field comparison as a native equivalence, or provide a source-defined field observable localized on a geometric edge or vertex.

The next nonredundant task is to inspect the actual source interface maps and determine whether any supplies the required geometric edge restriction. If one exists, bind its domain, orientation and lift data and test its commuting squares. If only whole-field/coefficient readouts exist, record that exact missing datum rather than define an arbitrary projector and call it physical descent.

Full face-chart descent and the Ramsey root remain open. No graph verdict, net revision or Git checkpoint was made.
