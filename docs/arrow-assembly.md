# Arrow assembly: proton, electron and assembly measures

Start here to choose an existing constructor, reproduce its assembly cycle, or interpret an arrow count. This is the implementation-navigation guide; the linked research packets own the mathematical claims.

**Verification status:** fresh documentation replay passed the three common geometric cycles, the proton source frontend and input controls, and an isolated run of the electron coefficient producer. All 17 replay checks passed. The electron prerequisite receipt was reused, not regenerated. Browser, energy-bridge and Agda workflows were not rerun by this audit.

## Choose the operation

All paths are relative to the repository root.

| Task | Existing entrypoint | Required input | Result and measures |
|---|---|---|---|
| Common geometric assembly for proton, neutron or electron examples | `research/voevodsky/checkers/assemble_relative_geometry.py` | Rational metric, proper affine isometry generators, seed points and roles | Generated vertices, supporting facets, interfaces, center cones and counts |
| Full scheduled geometric cycle, with reverse recovery | `research/voevodsky/checkers/evolve_relative_geometry_modes.py` | Same source schema | Calls the common assembler; returns geometry, exact facet modes, every scheduled centroid state, reverse checks, generator orders and return-step count |
| Proton-style coefficient network from directed triangles | `research/nima/checkers/check_twelve_triangle_positive_geometry.py --source ... --output-dir ...` | Directed endpoint pairs **and** rational 3D coordinates | Dispatches to `assemble_triangle_arrow_source.py`; writes network manifest, stage counts and return-cycle measures |
| Existing electron spinor coefficient network | `research/voevodsky/checkers/check_electron_tetrahedral_spinor.py` | Declared four-face spinor fixture and prerequisite receipt | Writes rank-two return, 144-transfer manifest, stage supports and positive-cycle checks |
| Labelled path/coherence tetrahedron | `research/nima/agda/RetainedTetrahedralPackage.agda`, `Cells.build` | Typed vertex/edge paths and a compatible three-face horn | Retained surface and filler, recoverable request; no coefficient-network count |

The common geometry and cycle scripts do not dispatch on particle names. Their source records differ. The coefficient protocols have different declared carriers and operators; a common geometric shape does not choose those operators.

## Common three-carrier coefficient and energy assembler

`research/strominger/checkers/assemble_metric_coefficient_protocol.py` accepts
a coordinate metric and commuting local/alignment projectors, then derives
`N=GL` and the common projector-defect energy `H=(pi/4)(2I-L-G)`.
It has no particle branches. Explicit native import adapters are exercised by:

```sh
python research/strominger/checkers/check_common_three_carrier_protocol.py
```

Twenty checks reconstruct the proton/neutron/electron native returns exactly.
Transfer totals are 1836/1836/144; return ranks are 1/1/2; energy traces in
pi/4 units are 57/57/10. All return-state constraint energies are zero.
Proton and neutron have the same spectrum under this rule. Transfer count
is separately shown to change under an orthonormal basis change, so it is
not an intrinsic mass measure. The remaining unification target is the
vacuum-relative occupation layer, not a fitted weight assigned to a stage.
See [results and contract](../research/strominger/common-three-carrier-protocol.md).

A [common signed endpoint-rotor parent](../research/strominger/common-endpoint-charging.md)
now transports the actual selected source kinetic operators into one charging
interface with graph-derived internal resistance and a common empty reference.
Run `python research/strominger/checkers/check_common_endpoint_charging.py`.
At the inherited fixture it gives proton/electron/belt ground energies
approximately `0.549172153 / 0.472191444 / 0`. It recovers the prior spinor
parent and preserves its Wilson phases, but the external-charge-only law leaves
the neutral belt at zero. Neutral internal interactions are the next energy
input, not an identification of positive norm with electric charge.

The [neutral-record continuation](../research/strominger/common-parent-neutral-records.md)
now attaches all 21 inherited seam controls to that parent, with the same record
pool and inactive vacuum subtraction in every sector. Run
`python research/strominger/checkers/check_common_parent_neutral_records.py`.
The zero-mixing fixture gives belt energy `21/4`, preserving its native return;
proton/electron energies stay unchanged. Seven checks verify the exact native
attachment and joint ground bound. This fixes the missing neutral energy term,
but not the failed proton/electron ratio.

## Dimension-independent retained coefficient networks

`research/strominger/checkers/retained_coefficient_network.py` now accepts
labelled ports and exact sparse staged operators without a spatial-dimension
restriction. It returns retained transfers, the composed return operator,
rank, cycle measures and exact input recovery. It does not infer operators
from bare arrows or geometry.

```sh
python research/strominger/checkers/check_retained_coefficient_network.py
```

Ten checks reproduce the native 1836/rank-one and 144/rank-two protocols from
stored manifests. An explicitly declared five-cell direct-sum extension also
passes, with 720 transfers and rank ten. Its identity fiber transports are
new chosen data, not a derived five-cell spinor law or a new electron count.
See [implementation and scope](../research/strominger/retained-coefficient-network.md).

A stronger [intrinsic five-cell calculation](../research/strominger/diagonal-spin-networks.md)
reuses the prior geometric spin frames and fold transports. All five admitted
diagonal actions preserve both prior doublets. Its explicitly declared global
`L, G=N=J P J*` protocol has supports `80+1520+1520=3120`, for either doublet
or their rank-four sum, in both chiralities. These are conditional full-cell
protocol counts, not native 144 replacements; geometric transport operations
remain separately retained. Run
`python research/strominger/checkers/check_diagonal_spin_networks.py`.

## Real-plus-complex arrow input for the neutron candidate

The candidate can now be supplied as two directed triangles in `R ⊕ C`, with
explicit real separation and complex endpoint coordinates. A particle-independent
frontend infers their common affine action, then calls the unchanged shared
geometry assembler and cycle wrapper. It does not infer the metric or scale
from graph incidence.

```sh
python research/strominger/checkers/assemble_real_complex_arrows.py --source research/strominger/inputs/neutron-real-complex-arrows.json --output research/strominger/results/neutron-real-complex-assembly.json
python research/strominger/checkers/check_neutron_real_complex_arrows.py
```

Twenty checks reproduce the existing neutron source and complete assembly/cycle
in an explicitly permuted coordinate basis: six vertices, eight supporting
facets, six moving facets, two fixed caps and three scheduled return steps.
The same frontend handles pure-complex and pure-real controls. No coefficient
protocol or physical neutron identification is inferred.
See [definition and scope](../research/strominger/neutron-real-complex-arrows.md).

The [native coefficient/energy continuation](../research/strominger/neutron-arrow-native-bridge.md)
passes this inferred source through the prior bridge with its native adapter
inputs retained. Run `python research/strominger/checkers/check_neutron_arrow_native_bridge.py`.
It reconstructs the eighteen modes and the existing intrinsic protocol:
`432+108+1296=1836` transfers, rank one. Native constraint energy vanishes
on the return; the separate existing occupation law gives `21/4` at its
zero-mixing fixture. These are different measures, not quantities to add
or a calibrated neutron mass.

## Phase-input adapter for the neutron geometry

The optional `research/strominger/checkers/assemble_cubic_phase_source.py`
adapter accepts complex seeds instead of explicit upper/lower coordinates.
It calls the unchanged shared geometry and cycle constructors, retaining the
source phase record, decoded source and affine cell-height moments.

```sh
python research/strominger/checkers/assemble_cubic_phase_source.py --source research/strominger/inputs/neutron-phase-source.json --output research/strominger/results/neutron-phase-assembly.json
python research/strominger/checkers/check_cubic_phase_source.py
```

The fixture uses phase seeds +1 and -1, an order-three multiplier and supplied
`height_scale=7/20`. The explicit decoder is Y=h*Re(u^3) on admissible seeds;
cell interiors retain the separate affine height moment. All 15 regression
and rejection checks passed, including exact equality of the old/new geometry
and complete cycle. It returns six vertices, six active side facets, two fixed
interfaces and a three-application return. It removes coordinate input, not
the separation parameter or third real degree of freedom. The legacy source
remains supported and is not overwritten.

Details: [complex-plane encoding](../research/strominger/neutron-complex-plane-encoding.md).

## Common assembly cycle: proton and electron

The cycle wrapper directly imports `assemble_relative_geometry.assemble`. Its sequence is:

1. Generate point orbits and supporting facets from the supplied metric and affine actions.
2. Encode each centered facet centroid in exact cyclotomic modes for each generator.
3. Retain fixed modes; classify moving facets by nonzero-frequency support.
4. Apply the supplied generator list repeatedly, re-encoding at each step.
5. Return the full scheduled trace and verify every reversed step recovers its prior centroid state.

Run from the repository root with Python (standard-library arithmetic). These examples write new audit outputs rather than replacing the established shared receipts:

```sh
python research/voevodsky/checkers/evolve_relative_geometry_modes.py --source research/voevodsky/inputs/relative-proton.json --output research/strominger/results/assembly-guide/proton-cycle.json
python research/voevodsky/checkers/evolve_relative_geometry_modes.py --source research/voevodsky/inputs/relative-electron.json --output research/strominger/results/assembly-guide/electron-cycle.json
python research/voevodsky/checkers/evolve_relative_geometry_modes.py --source research/voevodsky/inputs/mode-neutron.json --output research/strominger/results/assembly-guide/neutron-cycle.json
```

The `research/strominger/results/assembly-guide/` destination belongs to this documentation audit; other consumers should select their own output directory.

Freshly reproduced results:

| Source | Moving / fixed facet-centroid channels | Generator orders | Scheduled applications to word return |
|---|---|---|---|
| Proton | 4 / 0 | 3, 3 | 6 |
| Electron geometry | 5 / 0 | 5 | 5 |
| Neutron | 6 / 2 | 3 | 3 |

Read these JSON fields:

- `geometry`: coordinates, metric, selected facets, interface and attachment records, cone cells and `counts`.
- `facet_states`: retained centered centroids, exact encoded modes, active/fixed classification and energy/orthogonality checks.
- `centroid_motion_trace`: every state under the generator-list schedule.
- `scheduled_atomic_steps_to_word_return`: applications in that schedule, not physical time or a coefficient-arrow count.
- `reverse_history_recovers_every_centroid` and `fixed_modes_retained`: the precise recovery guarantees.

This recovers centroid states, not an arbitrary source presentation from a final shape. The mode wrapper changes external-interface roles to ordinary carriers before assembly and then selects interfaces by fixed centroid modes. Attachment-pole roles remain. Its selection rule is supported at canonical supporting facets, not arbitrary subdivisions.

Details: [source constructor](../research/voevodsky/relative-geometric-source-constructor.md), [reversible cycle](../research/voevodsky/relative-geometric-reversible-mode-motion.md), [selection](../research/voevodsky/relative-geometric-complex-mode-selection.md), [subdivision counterexample](../research/voevodsky/centroid-admission-refinement-counterexample.md).

## Proton coefficient assembly: the 1836 count

```sh
python research/nima/checkers/check_twelve_triangle_positive_geometry.py --source research/nima/inputs/proton-six-arrows.json --output-dir research/strominger/results/assembly-guide/proton-coefficients
python research/nima/checkers/check_triangle_arrow_source_input.py
```

The first command writes `assembly.json` and `arrows.json`. The second constructs the same network in memory, compares every typed endpoint and coefficient against the existing historical manifest, tests each single-arrow deletion, and rejects empty-cycle or incompatible geometric input. It prints its result without writing a new receipt.

Pipeline: directed three-cycles -> permutation closure -> proper geometric rotations -> centroid-edge triangle orbit -> cyclic local selection -> frame alignment -> dense collective feedback.

The established fixture has twelve triangles and **1836 distinct stage-typed coefficient transfers**. Inspect `arrows_per_stage`, `unique_directed_arrows`, `closed_three_step_cycles`, `return_cycle_union_measure`, `closed_walk_union_covers_every_arrow`, `boundary_chain_zero` and `signed_volume`.

The source contains six directed occurrences forming two triangles, plus explicit coordinates. A bare three-star has no directed triangle and is rejected. Cubical path completion is a different input type; do not silently turn derived inverse paths into new primitive rows to satisfy this frontend.

`--regression` runs the historical fixed fixture and writes historical artifacts; it is not the source-driven mode above. Details: [twelve-triangle construction](../research/nima/twelve-triangle-positive-geometry.md).

## Electron coefficient assembly: the 144 count

Producer: `research/voevodsky/checkers/check_electron_tetrahedral_spinor.py`.

It reads `research/voevodsky/results/electron_charge_spin_frontier.json` and requires `verification_passed`. That prerequisite is produced by `check_electron_charge_spin_frontier.py`, whose entrypoint reads `results/smaller_negative_flux_carrier.json`. These are stored-source dependencies, not a CLI accepting an arbitrary arrow list.

The producer declares four tetrahedral normals, builds Pauli face projectors, constructs the tight-frame return, and checks the binary tetrahedral action. The stages are `L=diag(P_i)`, `G=N`, and return `N`; their supports are **16 + 64 + 64 = 144**, on eight raw complex coordinates with a rank-two logical carrier. Every transfer participates in a positive closed three-step cycle; the cycle trace sum is two.

It writes, at fixed locations:

- `research/voevodsky/results/electron_tetrahedral_spinor.json`: checks and measures.
- `research/voevodsky/results/electron_tetrahedral_spinor_store.json`: normals, face projectors and stage-labelled transfers with exact weights.

The producer has no output-directory flag. Its direct invocation is `python research/voevodsky/checkers/check_electron_tetrahedral_spinor.py`; coordinate ownership before regenerating those shared stores. The documentation checker below instead imports the unchanged producer, temporarily redirects its `BASE` to an isolated directory, copies the existing prerequisite receipt verbatim and calls `main()`. That replay passed every producer check, exactly reproduced the stored manifest and confirmed all three shared electron receipts/stores remained unchanged. It does not regenerate the upstream prerequisite chain.

The spinor encoding admits reconstruction on its encoded logical subspace; this is not disassembly into arbitrary original arrow inputs. The **four-face spinor attachment** is not the entire **five-cell electron geometric pentachoron**.

Details: [support comparison](../research/voevodsky/electron-proton-assembly-relation.md), [construction routes](../research/voevodsky/particle-construction-routes.md).

## Bridges, displays and unresolved interfaces

[The geometric phase/energy bridge](../research/voevodsky/geometric-phase-energy-bridge.md) reconstructs proton/belt native modes using explicit ordered corners, character, frame and grouping adapters. Its checker reads stored native geometry/energy artifacts. It explicitly reports that the electron five-cycle moves the attachment tetrahedron: source-compatible spinor transport over all five boundary cells is not supplied by that bridge.

`research/voevodsky/checkers/check_unified_assembly_page.mjs` tests the combined browser display, retained phase guides, geometry stages and spinor-store agreement. Its unified presentation is not a general raw-arrow backend. `check_storage_branch_comparison.py` imports only the cycle script's `Cyclotomic` arithmetic; that import does not establish an end-to-end assembly caller.

For path completion, see [retained tetrahedral packages](../research/nima/retained-tetrahedral-package.md) and [three-spoke shared path assembly](../research/strominger/rooted-spoke-shared-assembly.md). The latter preserves three primitive occurrences while returning six edge-path slots, four faces and a filler; it does not return 1836-style measures.

The inspected interfaces establish neither a direct raw-star-to-coefficient adapter nor a common full five-cell electron coefficient protocol. This is a bounded interface finding, not a claim that all repository machinery has been exhaustively searched.

## Counting and recovery vocabulary

| Term | Counted or recovered object |
|---|---|
| Primitive arrow | Supplied occurrence with source, target and identity |
| Path edge | Typed equality witness, possibly constructed by inverse/composition |
| Affine generator | Supplied action on a metric coordinate space |
| Geometric cell/channel | Facet, cone or retained centroid mode at a stated resolution |
| Coefficient transfer | Nonzero matrix entry with explicitly typed port stages |
| Scheduled return | Repeated supplied action word, not necessarily the shortest unqualified return |
| Recovery | Specify table unpacking, horn recovery, spectral decoding, logical decoding or reversal of a recorded schedule |

Do not compare counts across rows as if they measured the same resource. Neither 1836 nor 144 is established here as a minimum or a mass.

## Verification and maintenance

```sh
python research/strominger/checkers/check_assembly_guide_examples.py
python research/strominger/checkers/check_assembly_guide_discovery.py
```

The example checker replays the commands above and the isolated electron producer. Its receipt is `research/strominger/results/assembly-guide/verification.json`; logs and generated outputs are alongside it. Navigation checks write `research/strominger/results/assembly_guide_discovery.json`. Source hashes bind the inspected implementations; these are local-checkout replays, not clean-install certification.

The discovery checker requires Python and `rg` (ripgrep). It runs bounded searches
across `docs`, root instructions/README and the matter index; each of the four
search terms must return this guide. It also validates guide links, documented
command/input paths and replay-source hash freshness. This is not a public-site
search ranking test.

When changing this guide:

- Replay the common-cycle commands into isolated outputs; verify traces and expected measures.
- Replay the source-driven proton command and historical-manifest control.
- Verify the electron producer in an isolated output setup without rewriting shared stores.
- Check links from agent instructions, repository/research indexes, specialized scripts and older notes.
- Confirm searches for **arrow assembly**, **electron**, **proton** and **assembly measures** reach this guide.

Audit provenance and verification boundaries: [assembly discoverability audit](../research/strominger/assembly-discoverability-audit.md).
