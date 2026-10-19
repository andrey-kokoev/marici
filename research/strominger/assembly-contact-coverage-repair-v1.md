# Enforce physical-contact coverage and reselect references

## Repair

`phase-assembly-model.mjs` now requires **both carrier coverage and contact
coverage**. The exported `auditAssemblyContacts` reconstructs the actual face
adjacencies from occupied cells, checks species/MMCC roles and the exact declared
ledger, then requires a typed transport edge for every contact. Same-carrier
reader advances cannot witness physical contacts.

The compiler rejects candidates with missing edges using
`unwitnessed-physical-contact`. The independent reference auditor reruns this
check before accepting a certificate, then retains all existing native phase,
permutation, history, origin and terminal-coverage audits. No transport edge or
new contact law is invented.

## Reselection

All ten viewer references survive the stronger gate. Generic selectors now
skip formerly accepted candidates with unwitnessed contacts; affected retained
chains were recomputed from the newly selected B-10 onward.

| Selected reference | New orientation |
|---|---:|
| B-10 | 329 |
| B-11 | 841 |
| C-12 | 1705 |
| C-13 | 841 |
| N-15 | 5801 |

B-11 retains the new B-10 and adds neutron cell 252. C-12 retains B-11 and adds
proton 47/electron 251. C-13 separately retains B-11 and adds proton 112,
neutron 253/electron 254. N-15 retains the new C-13 and adds proton 47,
neutron 295/electron 296. Retention includes native readers and old transport.
The frozen N-15 module was regenerated and is still recompiled/audited on
admission. The nitrogen checker exhausts its retained scope again: four
geometry candidates and 65,536 reader assignments.

The selected C-12 also changed because its retained B-11 parent changed; the
old standalone C-12 remains valid as a contact-coverage regression control.
No isotope option had to be removed from the viewer.

## Capture and diagnostic regressions

Re-running C-13 + proton with the new C-13 yields **two N-14+ references**:
proton 47/orientation 1705 and proton 49/orientation 1865. All 12,288 reader
assignments were tested; both accepted references retain old readers and
transport and pass the stronger independent auditor. The selected first now
has 63 certificate states covering 20 carriers. Old proton 18/24 IDs belong to
the superseded parent geometry, not the current references.

The C-12 → N-13 retained route remains blocked, even after stripping electrons:
there is no adjacent unoccupied proton position. Its conditional O-14 stages
remain unexecuted; the separately completed bounded count searches in
`n13-o14-capture-v1.md` are independent of selector changes.

The nuclear/electron separation and boundary/contact diagnostics were rerun
against the new references. Their conceptual limits are unchanged. Their
current contact reports now have no missing edges; the historical gap is
preserved by fixed legacy regression fixtures rather than a permanently
failing assertion about the current selected C-13.

## Lithium acceptance drift (intentional)

Exhaustive Li-5/6/7/8 sweeps were also rerun. Li-5/6/7 retain their exact
accepted-record fingerprints. Li-8 decreases from **10 to 5** accepted reader
assignments under the stronger gate, but still passes as a radioactive control.
Geometry candidates and total reader assignments are unchanged.

The historical `check_beryllium9_search_regression.mjs` was tried and fails
its frozen Li-8 expectation of 10. It is deliberately not rewritten to claim
unchanged results. Its explicit successor for the repaired gate is
`check_contact_lithium_regression.mjs`, which checks the unchanged Li-5/6/7
fingerprints and records both the historical and new Li-8 fingerprints.
That successor passes. Compatibility is still not sufficient for stability.

## Countercontrols

`check_assembly_contact_coverage.mjs` preserves the former B-10, B-11, C-13,
N-15 and first N-14+ geometry/orientation pairs: each now rejects specifically
for its unwitnessed N13–E14 cell contact. The formerly selected C-12 is a
positive legacy control.

For each current reference, checks independently:
- remove all witnesses for a PN, NE or NN contact, leaving carriers present;
- delete a declared contact, or duplicate a ledger entry;
- invent a self-contact transport edge;
- change a chart's occupied species.

All are rejected. The former hole cannot be restored merely by omitting a
ledger declaration or a certificate edge.

## Verification

Passed fresh headless checks:

```sh
node research/strominger/checkers/check_assembly_contact_coverage.mjs
node research/strominger/checkers/check_lithium_discrimination.mjs 5
node research/strominger/checkers/check_lithium_discrimination.mjs 6
node research/strominger/checkers/check_lithium_discrimination.mjs 7
node research/strominger/checkers/check_lithium_discrimination.mjs 8
node research/strominger/checkers/check_contact_lithium_regression.mjs
node research/strominger/checkers/check_boron_assemblies.mjs
node research/strominger/checkers/check_carbon_assemblies.mjs
node research/strominger/checkers/check_nitrogen_assemblies.mjs
node research/strominger/checkers/check_phase_assembly.mjs
node research/strominger/checkers/check_carbon13_proton_capture.mjs
node research/strominger/checkers/check_n13_o14_capture.mjs
node research/strominger/checkers/check_nuclear_electron_separation.mjs
node research/strominger/checkers/check_boundary_contact_derivation.mjs
node research/strominger/checkers/check_window_construction.mjs
node research/strominger/checkers/prepare_particle_overlap_viewer.mjs
node research/strominger/checkers/check_fiber_space.mjs
```

Receipts are refreshed under their respective `results/` directories, including
`assembly-contact-coverage/verification.json` and the viewer screenshots.

This repairs an admission-checking omission. It does not derive E/E contact,
nuclear binding, stability or a bare-nucleus boundary law. Those remain open.
