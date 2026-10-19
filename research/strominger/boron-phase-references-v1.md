# Stable boron targets: B-10 and B-11

Both stable isotopes now have phase-coherent reference constructions under the
existing PN, NE, NN and reader-phase-advance rules. Stability is an empirical
target-selection fact, not a conclusion of the compatibility check.

## Important change at B-10

The **currently selected Be-9 cannot be retained** when adding a proton and an
electron in this bounded ansatz. Enumerating its connected ten-nucleon
extensions yields two typed nuclei, but neither can supply five admissible
electron cells while retaining the old cells/species/roles. There is no candidate
to submit to phase compilation. This is not a statement about every Be-9
reference or about physical nuclear reactions.

A separate whole-assembly search succeeds without changing any rules. Thus
B-10 is not displayed or claimed as a monotone extension of the selected Be-9.
The fixed-root 343-cell search finds 180 geometry candidates and tests all
61,440 PN reader assignments. Thirteen assignments pass; the deterministic
selector uses the first admitted candidate in the established enumeration order.
This ordering is not an energy minimization or a physical uniqueness law.

Selected B-10:

- Counts: **5P / 5N / 5e**, 15 carriers.
- Nucleus: `0, 13, 15, 16, 25, 26, 54, 55, 296, 315`.
- Electrons: `14, 295, 297, 316, 318`.
- Reader assignment: **338**.
- **40** history-bearing certificate states; all 15 carriers covered and every
  entered state has an exit witness.

## B-11 retains B-10

B-11 adds neutron cell **7** to the selected B-10 without changing its existing
cells, species, C/M roles, native readers or transport edges. All five electron
cells remain unchanged. The additional neutron has a PN contact with root
proton cell 0.

The retained search examines 11 connected nuclear extensions. One typed
geometry survives, and exactly one of its 1,024 reader assignments passes.

- Counts: **5P / 6N / 5e**, 16 carriers.
- Nucleus: B-10 nucleus plus `7`.
- Reader assignment: **677**.
- **53** history-bearing certificate states; all 16 carriers covered.

This uniqueness is scoped to retaining the selected B-10 in the fixed domain.
It is not a claim about all B-11 assemblies or a physical neutron-capture law.
The full certificate is recomputed, so preservation of cells and transport does
not imply an unchanged display-prefix history.

## Implementation and verification

The existing geometry enumerator now accepts an optional retained nucleus,
starting enumeration from that connected set and excluding its electron cells
from nuclear additions. It retains the same typing, contact, port-budget,
nonadjacent-electron and native-proton-reader requirements. No phase acceptance
rules were relaxed. B-10 uses a root-only search; B-11 uses the retained search.

Both isotopes are available in both viewer selectors, with 15/16 looping steps,
shared labels/transparency and paired rotation. No unstable isotope was added.

Checks:

```sh
node research/strominger/checkers/check_boron_assemblies.mjs
node research/strominger/checkers/check_phase_assembly.mjs
node research/strominger/checkers/prepare_particle_overlap_viewer.mjs
node research/strominger/checkers/check_fiber_space.mjs
```

The phase suite now covers seven reference isotopes and 63 character/phase
inputs, full five-slot transport, all three face modes, reversible display,
and corrupted phase/context/map/coverage controls. Browser checks cover each
boron isotope, Be-9/B-10 comparison and both B-10/B-11 comparison orders.

The four lithium discrimination sweeps were rerun after the enumerator change;
all prior accepted geometry/reader fingerprints and counts remain unchanged.
Unstable lithium isotopes remain internal controls only.

Evidence: `results/boron-assembly/verification.json`,
`results/phase-assembly/verification.json`,
`results/fiber-space/verification.json`, and
`results/fiber-space/boron10-boron11-comparison.png`.

These are compatible reference assemblies, not binding-energy calculations,
stability proofs, decay predictions or dynamically derived rearrangements.
