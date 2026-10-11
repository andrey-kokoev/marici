# Harmonized proton / neutron / electron visualization stages

Date: 2026-10-09
Status: Visualization proxy, not a new common generating law

At the operator's request, the main viewer now uses one eight-stage geometry sequence for all three constructions. The electron is no longer presented in a separate “pentachoron trial” assembly section.

| Stage | Shared purpose | Electron representation |
|---|---|---|
| 1 | Separate labelled segments | Ten detached labelled edges |
| 2 | Identify vertices | Five-vertex K5 skeleton |
| 3 | Form faces | Ten separated triangular faces |
| 4 | Group constituent pieces | Five exploded tetrahedral boundary-cell records |
| 5 | Identify shared interfaces | Ten shared triangular interfaces, each present in its two incident cells |
| 6 | Approach matching faces | Rigid translations of the projected cell records toward coincidence |
| 7 | Glue matching interfaces | One copy of each of the ten triangular faces |
| 8 | Inspect completed constructions | Complete projected pentachoron with its attachment cell retained |

The proton and neutron retain their earlier geometry procedures, explained under the shared stage headings. The stages are intentionally harmonized explanatory proxies rather than assertions of identical underlying algorithms. In particular, the electron's five projected boundary cells are not five disjoint spatial volumes.

Selecting or replaying either isotope runs the shared eight-stage constituent sequence first, then the verified attachment motion. The hydrogen-1 shared-face match and hydrogen-2's two belt-rim matches are unchanged.

Projection and four-face spinor diagnostics are available in a collapsed inspection section. They no longer constitute a competing top-level geometry sequence. The spinor operator remains a calculation on the retained ABCD cell, not on the entire five-cell carrier.

Verification: `node research/voevodsky/checkers/check_unified_assembly_page.mjs` checks all eight stages on both source and public asset, including the electron's 0/0/10/20/20/20/10/10 displayed triangle counts, five intermediate cell records, final interface coincidence, isotope replays, source spinor identities, standardized vertex markers, and mobile resizing. A first run exposed a negative initial animation timestamp relative to performance.now(); the phase index is now clamped at zero.
