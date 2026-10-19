# Li-7: retained-Li-6 phase reference

## Result

A 3P/4N/3e reference assembly passes the existing phase-first compiler and
history-bearing entry/exit audit. It retains the selected Li-6 cells, species,
C/M roles, native readers and existing transport edges, adding neutron cell 7
through the MCM face of proton cell 0. No new interface law was introduced.
The existing NN reference assumption remains part of the retained Li-6 model.

- Nucleus: `0, 7, 13, 16, 25, 55, 296`.
- Electrons: `15, 295, 297` (unchanged).
- Added PN face: lattice vertices `0, 1, 3` (geometric IDs, not phase indices).
- Reader assignment: `41` in the expanded interface ordering.
- All ten carriers have phase-bearing entry-to-exit witnesses.

## Search and limits

The existing whole-assembly enumeration now also supports four neutrons. It
still uses the same 343-cell domain, root proton 0, global MMCC typing, PN/MCM,
optional NN/MCC, and three distinct nonadjacent terminal electron cells. Every
neutron must have a native proton reader. Each NN contact consumes two MCC
ports; at least three remain for electrons.

The seven-cell enumeration has prefix counts `1, 4, 18, 82, 381, 1616, 3863`,
276 typed nuclei and 528 geometry candidates. Exactly one candidate retains
the selected Li-6 cells, species and roles. Of its 64 reader assignments, one
passes the existing phase compiler. The admitted assignment also preserves
every existing Li-6 reader and transport edge (checked independently).

This is a bounded reference result, not global uniqueness, a physical neutron
capture process, or a derivation of binding energy or stability. Display order
comes from the recomputed phase witnesses: it is not asserted that the old
nine-item display history followed by a final neutron is a physical growth law.
Absolute phase origins remain unbounded; coefficient closure does not reset them.

## Viewer and checks

Li-7 is available in both selectors with ten looping display steps, including
comparison with Li-6 and synchronized own-center rotation.

- `node research/strominger/checkers/check_lithium7_assembly.mjs`
- `node research/strominger/checkers/check_phase_assembly.mjs`
- `node research/strominger/checkers/check_fiber_space.mjs`

The phase suite covers all five coefficient slots, three face modes, nine
character/phase inputs per isotope, reversible display prefixes, and corrupted
phase/context/map/coverage negative controls. The browser suite exercises Li-7
alone and both orders of Li-6/Li-7 comparison.

Evidence: `results/lithium7-assembly/verification.json`,
`results/phase-assembly/verification.json`, and
`results/fiber-space/lithium6-lithium7-comparison.png`.
