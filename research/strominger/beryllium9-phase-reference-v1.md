# Be-9: stable-isotope reference retaining Li-7

## Result

Be-9 (4P/5N/4e) passes the existing phase compiler and entry/exit audit while
retaining the selected Li-7 cells, species, C/M roles, native readers and all
existing transport edges. No new interface law or acceptance relaxation was
introduced. The existing NN outside-context reference assumption still applies.

Added carriers (numbers are geometric cell IDs, not phase indices):

- Neutron **6**, joined to retained neutron **7** through NN/MCC.
- Proton **44**, joined to neutron **6** through PN/MCM.
- Electron **5**, joined to neutron **6** through NE/MCC.

The selected nucleus is `0, 6, 7, 13, 16, 25, 44, 55, 296`; electrons are
`5, 15, 295, 297`. Reader assignment 81 yields 29 history-bearing certificate
states covering all 13 carriers, with every entered state able to reach an exit.

## Search scope

The existing enumerator was generalized from three protons/electrons to four,
using the same domain, role constraints and native-proton-reader requirement.
Electron triples became combinations of the specified electron count. The
unchanged port-budget rule reserves one MCC incidence per electron and consumes
two per NN contact. For Be-9, five neutrons supply ten MCC incidences; reserving
four permits at most three NN interfaces during enumeration.

Complete geometry enumeration in the 343-cell domain produced:

- Prefix counts: `1, 4, 18, 82, 381, 1788, 8099, 27152, 51216`.
- 1,376 typed nuclei and 2,976 geometry candidates.
- 12 candidates retaining the selected Li-7 geometry, species and C/M roles.
- All 1,536 reader assignments for those 12 candidates tested.
- Exactly one phase-compatible assignment; it also retains all old readers and
  transport edges.

The uniqueness claim is restricted to this retained-Li-7 search, not all Be-9
assemblies. Non-retaining phase assignments were not exhaustively classified.
Display prefixes come from the recomputed certificate: preserving the old cells
and transport does not assert an unchanged display history or physical growth
process.

## Verification and viewer

Be-9 is available in both selectors as a **phase reference**, with 13 looping
items, shared opacity/labels and paired own-center rotation. New viewer targets
remain restricted to stable isotopes; Li-5/Li-8 remain test controls only.
Empirical stability is a target-selection fact, not inferred from this audit.

```sh
node research/strominger/checkers/check_beryllium9_assembly.mjs
node research/strominger/checkers/check_phase_assembly.mjs
node research/strominger/checkers/prepare_particle_overlap_viewer.mjs
node research/strominger/checkers/check_fiber_space.mjs
```

The phase suite checks all five slots, all face modes, nine character/phase
inputs per isotope (45 total), reversible display and corruption controls.
Browser checks include Be-9 alone and both orders of Li-7/Be-9 comparison.

After generalization, the four complete lithium discrimination sweeps were
rerun. `check_beryllium9_search_regression.mjs` verifies identical candidate and
acceptance counts and SHA-256 fingerprints of **all accepted geometry/reader
records**, against the pre-Be-9 results. The original stable/unstable conclusion
is unchanged; no new stability rule was fitted.

Evidence:

- `results/beryllium9-assembly/verification.json`
- `results/beryllium9-assembly/lithium-regression.json`
- `results/phase-assembly/verification.json`
- `results/fiber-space/lithium7-beryllium9-comparison.png`

This is a bounded compatible assembly, not a calculation of binding energy,
stability, lifetime, or a reaction mechanism.
