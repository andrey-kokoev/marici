# Registered native-whole fixture test: inventory and pair admission are distinct

## Registration

This executes `pb208-native-whole-fixture-attempt`, registered before execution in
net revision26. The frozen contract is
`contracts/pb208-native-whole-fixture-attempt.v1.json` and the pre-execution net is
`contracts/persistent-seam-pe-conjecture-net.snapshot.rev26.json`.

Its criteria were intentionally separate: a grounded whole-inventory reader,
and admission of both actual NE/NN alternatives into that same retained whole.

## Grounded inventory criterion

The original native fixture exporter was freshly replayed from its source
holonomy histories, followed by the exact whole-field sewing checker. The source
histories construct2P/2N/1E,14 retained packets and18 witnessed interfaces. No Pb
layout or isotope quota is an input. All18 field-sewing checks pass again.

An active chart is a pointer into the retained assembly record, not the whole
record. Compute inventory from the distinct occupied primitive bodies in that
record. This same computation returns2P/2N/1E at every one of its14 packet readers
and across all18 interfaces, despite their different P/N/E reader species.
Removing all E packets changes the computed inventory to2P/2N/0E. Thus the count
is grounded in the constructed record, not a fitted constant.

This is a positive example of separating an active reader from a whole inventory.
It requires the retained assembly descriptor alongside the field and history;
the44 amplitudes alone have not been shown to encode arbitrary particle inventory.

## Actual conflicting pair: common-frame binding test

Reconstruct the original PN-to-NE and PN-to-NN alternatives independently. For
every retained P packet in the fixture, its ordered C0/M0/C1/M1 vertices determine
one affine map from the source unit seed. Use that SAME map for the common PN
prefix and both targets. Check full reference aliases, absolute origins relative
to the root, five-slot permutations and actual occupied geometry/species.

Both alternatives refer to the same source primitive, so their transformed cell
keys remain identical in every common frame. A fixed occupied fixture primitive
has one species. It cannot simultaneously match both target species. The exact
bindings therefore admit no common NE/NN pair. The test also verifies genuine
root/PN-prefix bindings, avoiding a vacuous failure from having no relevant root.

The bounded search covers7 retained P-root frames. Five admit the exact root/PN
prefix, two also admit the E target, and none admits the NN target. No common
pair is admitted. These are frame-binding counts, not a census of all possible
future assemblies.

Independent relocation of the two targets would evade this test by discarding
their shared-source geometry; it is not an admitted comparison.

## Criterion-linked disposition

**Inventory grounded, pair not admitted.** The first criterion succeeds; the
second fails for this existing fixed-species fixture and its marked P-root frames.
Whole-field sewing and chart-independent inventory are not substituted for the
missing pair admission. This is not a refutation of all whole-reader models.

The result locates the necessary change more precisely: under the current grammar,
a chart's species is also the species of its occupied primitive. The fixture
separates "which body reads" from "the whole inventory," but does not permit two
species-readers on one occupied primitive. A broader reader/carrier distinction
would require a source-backed extension with occurrence, geometry and field maps,
not silently relaxing the validator or relabeling a neutron as an electron.

The Pb construction remains open. Any next extension must be registered and tested
as an explicit change of carrier interpretation, not credited to this fixture.

## Reproduce

```sh
node research/strominger/checkers/export_joint_field_sewing_fixture.mjs
python research/strominger/checkers/check_joint_field_assembly_sewing.py
node research/strominger/checkers/check_native_whole_inventory_fixture.mjs
```

The attempt, all marked-root mappings and receipt are in
`results/native-whole-inventory-fixture/`. The source fixture and its unchanged
field result are replayed, not replaced with new matrices.
