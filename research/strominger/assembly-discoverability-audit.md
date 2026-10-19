# Arrow assembly discoverability audit

## Objective and status

Operator instruction: document and expose the existing assembly machinery so that a new agent can find the proton and electron workflows, their assembly cycles, retained results and measures without reconstructing the architecture from scattered experiments.

Iterations 1–2 traced the source and produced `docs/arrow-assembly.md`. Iteration 3 added eight Markdown entry links and four script-docstring pointers; executable assembler bodies were not edited. Iteration 4 replayed all three geometric cycles, the proton source frontend and hostile controls, and the isolated electron coefficient producer: all 17 replay checks passed. Proton reproduced 1836 transfers; electron reproduced 144 and the exact stored manifest. Shared electron stores were unchanged; the upstream frontier receipt was reused rather than regenerated. The refreshed guide passed all 17 discovery checks with no broken links.

Navigation verification: `python research/strominger/checkers/check_assembly_guide_discovery.py`; receipt `research/strominger/results/assembly_guide_discovery.json`. It checks links, literal search terms and script pointers, not search ranking. Its executable AST hashes establish a baseline, not a before/after comparison. Replay command: `python research/strominger/checkers/check_assembly_guide_examples.py`; receipt `research/strominger/results/assembly-guide/verification.json`. Iteration 5 adds actual bounded ripgrep searches, command/input path validation and replay-source hash freshness checks to the discovery checker. The guide is the maintained entrypoint; the inventory below records how it was discovered.

## Discovery paths inspected

| Entry | Navigation inspected in iteration 1 | Initial finding / repair target |
|---|---|---|
| Root `AGENTS.md` | Stacks/PDF search, SCC, analytical operating rules, ownership and execution protocols | No assembly-specific starting link. Add a concise link to the canonical guide, not another architectural summary. |
| Root `README.md` | Project map, SCC, extensive Nima ledger map and commands | No direct arrow-assembly workflow entry. Add a guide link near project navigation. |
| `papers/witness-generators/README.md` | Current Cubical WG tutorial and matched comparison | This directory also holds particle assembly pages, but the README is a tutorial index, not their implementation map. Add a separately scoped assembly pointer without redefining the tutorial. |
| `research/matter/README.md` | Common geometric assembly update and retained phase/energy/memory update | Existing research-level discovery route; it already distinguishes geometry from coefficient counts. Link the implementation guide here. |
| `research/voevodsky/relative-geometric-source-constructor.md` | Common source constructor, all three inputs, independent comparison and remaining coefficient obligation | Existing substantive guide; preserve and cross-link rather than duplicate. |
| `research/voevodsky/relative-geometric-complex-mode-selection.md` | Uniform centroid selection and follow-up link | Leads to the reversible-cycle implementation overlooked in the earlier conversation. |
| `research/voevodsky/relative-geometric-reversible-mode-motion.md` | Exact encoding, complete scheduled traces, inverse histories, measures and energy bridge | Principal common-cycle entrypoint for the inspected geometry workflows. |
| `research/voevodsky/assembly-identity-arrow-contract.md` | Explicit proposed structural-arrow interface | A proposed contract, not evidence of an implemented arrow-only frontend. |

Iteration 3 implemented the guide links in the root instructions/README, matter index, tutorial index, source-constructor and reversible-cycle notes, plus the proton coefficient and electron/proton comparison notes. Four implementation docstrings also point to the guide.

No top-level `research/README.md` appeared in the inspected directory listing. Existing research indexes must be used or intentionally supplemented, not described as already covering assembly.

## Implementation map established from source

Paths below are repository-relative.

### Common geometry and reversible cycle (proton AND electron)

- Source: `research/voevodsky/inputs/relative-proton.json` or `relative-electron.json`.
- Constructor: `research/voevodsky/checkers/assemble_relative_geometry.py`, `assemble(source)`.
- Input schema: exactly `metric`, `generators`, `seeds`; not an endpoint-arrow list. The constructor generates orbits, supporting facets, interface records and center cones.
- Cycle wrapper: `research/voevodsky/checkers/evolve_relative_geometry_modes.py`, `evolve(source)`, directly imports and calls `assemble`.
- Steps: remove explicit external-interface roles for the mode experiment; assemble; encode every supporting-facet centroid in exact cyclotomic modes; select active facets by nonzero-frequency support; apply the supplied generator-list schedule; record every centroid state; reverse every step.
- Output: `geometry`, `facet_states`, `generator_orders`, `scheduled_word_order`, `scheduled_atomic_steps_to_word_return`, `centroid_motion_trace`, `reverse_history_recovers_every_centroid`, `fixed_modes_retained`.
- Recovery scope: centroid states under the supplied generator schedule, including fixed modes. Not an inverse reconstructing an arbitrary original generator presentation from a final shape.
- Independent callers: `check_relative_geometry_sources.py`, `check_relative_geometry_mode_selection.py`, `check_relative_geometry_mode_motion.py`.
- Documented fixtures: proton four moving channels, six scheduled applications; electron five moving channels, five applications; neutron six moving and two fixed channels, three applications.
- These counts are not coefficient-network transfers. Centroid admission is restricted to supporting facets; `centroid-admission-refinement-counterexample.md` records failure on arbitrary subdivisions.

### Proton coefficient network

- Frontend: `research/nima/checkers/check_twelve_triangle_positive_geometry.py --source ... --output-dir ...` dispatches to `assemble_triangle_arrow_source.run`.
- Implementation: `research/nima/checkers/assemble_triangle_arrow_source.py`.
- Input: coordinates plus directed endpoint pairs, e.g. `research/nima/inputs/proton-six-arrows.json`.
- Steps: complete oriented three-cycles -> permutation closure -> proper rotations -> centroid-edge triangle orbit -> cyclic local projectors -> alignment -> dense collective feedback.
- Output: `assembly.json`, `arrows.json`; measures include arrows per stage, unique directed transfers, closed three-step cycles, return-cycle union measure, boundary closure and signed volume.
- Documented proton result: 1836 staged coefficient transfers. This is not a count of tetrahedral edges or primitive input occurrences.
- Input/control caller: `check_triangle_arrow_source_input.py` inspected in iteration 2. It compares the entire historical manifest, tests all six single-arrow deletions, rejects empty triangles and incompatible coordinates, and prints JSON without writing a receipt. Fresh run passed in iteration 4; its stdout is retained in `results/assembly-guide/proton-input-controls.log`.
- The historical `--regression` mode is a fixed fixture, not the source-input constructor.

### Electron coefficient network

- Producer located: `research/voevodsky/checkers/check_electron_tetrahedral_spinor.py`.
- Inspected entrypoint reads and requires `results/electron_charge_spin_frontier.json`; constructs four declared tetrahedral normals and local spinor projectors, then the global tight-frame return.
- Stores referenced by callers: `results/electron_tetrahedral_spinor_store.json`.
- Documented result: 144 transfers on the tetrahedral attachment, rank-two logical carrier. This is distinct from the common geometric electron's five-cell pentachoron.
- Producer inspected through its output writes in iteration 2. Stages have supports 16, 64, 64; all transfers participate in positive cycles; trace sum is 2. It writes `electron_tetrahedral_spinor.json` and `electron_tetrahedral_spinor_store.json` at fixed locations with no output flag. Its prerequisite producer reads `smaller_negative_flux_carrier.json`. Isolated replay passed in iteration 4, including exact manifest equality and unchanged shared-store hashes.
- `check_particle_construction_routes.py` reads the proton and electron stores and compares partial routes; it is not evidence that one raw-arrow frontend constructs both protocols.

### Existing geometry-to-coefficient bridge

`research/voevodsky/geometric-phase-energy-bridge.md` points to `checkers/check_geometric_phase_energy_bridge.py`. It documents a checked partial bridge from common generated proton/belt geometry to native modes and energy accounting, with explicit frame, ordered-corner character and grouping adapters. It documents the electron obstruction: the five-cycle moves the tetrahedral attachment to other cells; existing spinor transport across all five cells is not supplied there.

Iteration 2 inspected bridge imports, stored inputs, writes and the explicit missing-map report. `check_unified_assembly_page.mjs` is a browser/display checker consuming the spinor store, not a raw-arrow assembly wrapper. `check_storage_branch_comparison.py` imports only `Cyclotomic`; it does not call the geometric cycle. These bounded findings still do not justify a repository-wide absence claim.

### Path/coherence packages

`research/nima/agda/RetainedTetrahedralPackage.agda` and the new `research/strominger/agda/RootedSpokeSharedAssembly.agda` construct/recover retained tetrahedral requests and typed faces/fillers. Their six edge slots are neither scheduled centroid applications nor coefficient transfers. They must appear as a distinct route in the guide, not as a substitute for numeric assembly measures.

## Terminology corrections for the guide

- **Common assembler exists:** the same relative geometry constructor is called for proton, neutron and electron examples.
- **Common cycle wrapper exists:** `evolve_relative_geometry_modes.py` already returns geometry, full scheduled centroid traces, inverse checks and measures. The earlier suggestion that even this cycle machinery was missing was inadequately investigated.
- **Arrow input** can mean primitive occurrence records, affine generators, equality paths, or coefficient transfers. State which at each interface.
- **Electron** can refer to a geometric pentachoron or a four-face spinor store. Name the artifact, not just the particle label.
- **Disassembly/recovery** can mean table unpacking, horn recovery, spectral decoding, reversing a scheduled trace, or recovering a source presentation. Do not substitute one for another.
- **Missing** must name an inspected interface and scope, not repository-wide absence inferred from one script.

## Disposition

The five-step documentation objective is implemented: audited discovery paths, source-traced implementation map, canonical guide, navigation links and reproducible example/discovery checkers. No new assembler or scientific adapter was introduced.

Verification is bounded to the existing checkout and retained prerequisites. It does not certify a clean installation, public-site search ranking, browser behavior, the upstream electron receipt chain, energy bridges or a new Agda compilation. No commit or publication is claimed.
