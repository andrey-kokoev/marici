# Stable carbon targets: C-12 and C-13

Both targets pass the unchanged phase/compiler rules as **separate extensions
of the selected B-11**. C-13 is not obtained by adding a neutron to the selected
C-12. Empirical stability is a target-selection fact, not derived here.

## C-12: retained B-11 plus P/e

- Counts: **6P / 6N / 6e**, 18 carriers.
- Retains B-11 cells, species, C/M roles, native readers and transport edges.
- Adds proton cell **24** and electron cell **6** (geometric cell IDs).
- Nucleus: `0, 7, 13, 15, 16, 24, 25, 26, 54, 55, 296, 315`.
- Electrons: `6, 14, 295, 297, 316, 318`.
- Reader assignment **2713**, 57 history-bearing certificate states, all
  18 carriers covered and every entered state has an exit witness.

The retained search finds one typed nucleus and two admissible electron
placements. All 8,192 reader assignments were tested; two pass, both preserving
B-11 readers. The viewer selects the first in the existing deterministic order,
not by an energetic or stability score.

## Why direct C-12 → C-13 is blocked

Each proton has two MCM faces. All six protons in the selected C-12 have both
occupied by PN contacts. Under the existing requirement that every neutron
have a native proton reader, another neutron has no available PN port without
changing retained carriers.

The explicit retained search examines 13 connected nuclear extensions and
finds zero typed nuclei and zero geometry candidates. This is an obstruction
for the selected retained assembly under this ansatz, not a physical
impossibility claim for carbon-13.

## C-13: a different retained-B-11 branch

A search from B-11, adding P/N/e together, succeeds without changing any rules:

- Counts: **6P / 7N / 6e**, 19 carriers.
- Retains B-11 cells, species, roles, native readers and transport edges.
- Adds proton **44**, neutron **6**, and electron **5**.
- Nucleus: `0, 6, 7, 13, 15, 16, 25, 26, 44, 54, 55, 296, 315`.
- Electrons: `5, 14, 295, 297, 316, 318`.
- Reader assignment **1353**, 47 history-bearing certificate states, all
  19 carriers covered and every entered state has an exit witness.

The retained-B-11 search has prefix counts `1, 13, 28`, four typed nuclei and
eight geometry candidates. All 16,384 reader assignments were tested. Exactly
one passes and preserves the old readers. This is not uniqueness over all C-13
geometries: no unrestricted whole-domain C-13 search was required or claimed.

Cell 6 has different species assignments in the two *separate* carbon
references. It is not an electron-to-neutron conversion law. Neither reference
changes the species of any retained B-11 carrier. No dynamical rearrangement
mechanism, neutron capture process or cross-isotope display-prefix history is
asserted.

## Viewer and checks

Both isotopes are available in both selectors with 18/19 looping steps,
shared transparency and labels, and paired own-center rotation. Only stable
targets are added to the viewer; unstable targets remain internal controls.

```sh
node research/strominger/checkers/check_carbon_assemblies.mjs
node research/strominger/checkers/check_phase_assembly.mjs
node research/strominger/checkers/prepare_particle_overlap_viewer.mjs
node research/strominger/checkers/check_fiber_space.mjs
```

The phase suite covers nine reference isotopes and 81 character/phase inputs,
all five coefficient slots, all face modes, reversible display, and corruption
controls. Browser checks include each carbon isotope, B-11/C-12 comparison,
and both C-12/C-13 comparison orders. The existing interface and phase laws
were not relaxed; only the explicit carbon target wrapper and selector entries
were added.

Evidence: `results/carbon-assembly/verification.json`,
`results/phase-assembly/verification.json`,
`results/fiber-space/verification.json`, and
`results/fiber-space/carbon12-carbon13-comparison.png`.

These are compatible reference assemblies, not binding-energy calculations,
stability proofs, decay predictions, or physical growth laws.
