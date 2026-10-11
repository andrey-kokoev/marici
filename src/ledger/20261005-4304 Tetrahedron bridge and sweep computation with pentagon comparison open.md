# 4304 — Tetrahedron bridge and sweep computation with pentagon comparison open

## Checked result

The fixed-boundary tetrahedron comparison now preserves all four independently translated triangular faces. `TetrahedronPresentationBridge.FixedBoundaryTarget.equivalence` is proved for the original triangle comparison, rather than for a fourth face chosen retrospectively to make the comparison commute.

Its `equivalence-route-computation` and `equivalence-sweep-computation` theorems identify the forward map with an explicit route formula and then with the corrected direct sweep of the supplied filler. The general square `PathSweepCoherence.mapped-pathover-pasting` removes the canonical-transport and residual-endpoint-path bookkeeping. These are computation laws for the existing map, not replacement choices of equivalence.

`FourSimplexEquationBridge` supplies the induced four-cell comparison. Separately, `MarkedFourSimplexCoherence` gives the independent five-tetrahedron pentagon relation and unique missing-face completion.

## Exact stopping point

`FourSimplexPentagonBridge` applies the proved computation law to all five tetrahedron witnesses. Its `sweep-pentagon-normalization` identifies the translated canonical-completion obligation with the pentagon evaluated on explicit sweep expressions.

`flag-sweep` constructs a cube of paths from vertex 0 to vertex 4 from any filled Cubical four-simplex. Five boundary formulas carry the tetrahedron witnesses; the sixth carries the collapsed 234 triangle. The terminal corner is the right-associated composite of the four edges.

The remaining route/coherencer compatibility obligation is to normalize this cube's corrected boundary to the independent pentagon's long and short routes. `GeneratedRouteCoherence`, `CenterCoherence`, and the independent pentagon comparison `Goal` are not inhabited. Contractibility of the two completion spaces separately does not identify their computed centers.

**Scope.** This entry records the checked fixed-boundary tetrahedron bridge, induced four-cell comparison, independent pentagon completion, and sweep computation. It does not assert the comparison with the independent pentagon, a geometric interpretation beyond the declared path types, or a physical readout. The operator stopped proof development at this boundary and requested this milestone record.

## Durable verification

Packets:

- `research/nima/tetrahedron-presentation-bridge.md`
- `research/nima/four-simplex-pentagon-bridge.md`

Fresh checks used `research/nima/checkers/check_cubical_agda.ps1 -Module <Module> -Fresh`, with safe Cubical options, ignored interfaces, and stable inputs. Recorded receipts:

- `research/nima/results/agda-PathSweepCoherence.json`: completed 2026-10-05T12:52:18Z; source SHA-256 `11b6cac8a98eb62ca791ae11de859d05268c9446434338b6cc4f97138f0f63f8`.
- `research/nima/results/agda-TetrahedronPresentationBridge.json`: completed 2026-10-05T12:56:30Z; source SHA-256 `140984c2dcd6fa9f70855b2bf8b8bd485dfa81ba25e95848ef3b034bea14817c`.
- `research/nima/results/agda-MarkedFourSimplexCoherence.json`: completed 2026-10-05T12:56:52Z; source SHA-256 `6a973e6e3b2ea7504120a9b2dd89391b669a40cb760bc080347dcf2114658e6e`.
- `research/nima/results/agda-FourSimplexPentagonBridge.json`: completed 2026-10-05T13:02:25Z; source SHA-256 `94b0f4abb8dc6315f881f7347bfea45ac6f316fd7b1697da69baa69008f84d18`. This fresh check includes the induced four-cell dependency closure.

Both `research/nima/checkers/check_tetrahedron_presentation_bridge.py` and `research/nima/checkers/check_four_simplex_pentagon_bridge.py` passed their receipt audits. The latter retains classification `independent_pentagon_checked_comparison_coherence_open`. These are the recorded proof checks, not a claim of a new Agda run during ledger preparation.

Site validation: `pnpm run build` passed with exit code 0 via structured-command execution `structured_command_execution:e_32876_1791206762269404700_1`. The current package builds VitePress and Pagefind; the repository instruction's Astro description is historical. The owner-local SCC manifest classification has been corrected to `fixed_boundary_tetrahedron_bridge_checked`; no new SCC compiler run is claimed.

Sequence allocation: `seqclaim-fd1bcffbea3a017fea144c46`, value 4304. Epistemic graph admission: proposal `ep_62c84161-46f8-438e-90b2-eab360338bee`, event `ev-000000015789-12b76bfa-c9cb-4a6c-8795-0d5a1ab1818c` (ledger head `c58c8435c90ac93b37796e30bdfe61e87bb62848722c778458894ac943a00dd7`). Admission records provenance and does not certify mathematical truth. This entry and its admission remain uncommitted; no push is claimed.
