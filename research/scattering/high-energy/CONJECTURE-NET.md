# High-energy scattering conjecture net

[Durable replay cache, full-receipt checks and budget accounting](REPLAY-MAINTENANCE.md)

## Current mathematical successor: v2

[Sharpened propositions](contracts/high-energy-scattering-conjectures.v2.json) · [validator](check_high_energy_net_v2.py) · [live shared workbench](../../conjecture_net/HIGH-ENERGY-WORKBENCH.md) · [scope review](../SCATTERING-WITNESS-SCOPE-REVIEW.md)

The registered v1 below remains frozen history. This local v2 successor separates **ten testable propositions** from three deferred source/physical/assembly obligations. No historical scientific outcome is imported and no central registry version is silently replaced.

| ID | Fixed proposition |
|---|---|
| H1 | **Established in the supplied model:** full-spinor projectors, switch involutions and positive defect energies satisfy the exact identities at both endpoint poses, with selected-line complements retained. |
| H2 | **Established at both endpoint poses:** independently assembled ordered-path products and the switching graph's third-order block agree on C20. The six orders remain distinct. |
| H3 | **Established in the supplied model:** the complete memory encoder is unitary and transports its declared energy continuation. Equality with the independently supplied outgoing Hamiltonian is **not** inferred. |
| H4 | **Established by analytic proof:** the specified open-hinge form on its H1/finite-record domain is closed, nonnegative and self-adjointly realized. No infinite-coupling trace constraints are introduced. |
| H5 | **Established for exact downstream finite equations:** all-time residual-aware continuity proof, with fresh pilot and response128 source-binding audits. Response128 truncation acts on the entrance forcing, not the retained downstream coordinates. |
| H6 | **Open, numerically supported:** completed 17-to33 comparison changes peak transport by 0.1135%, packet transport by 0.1439%, and product probability by 0.06784%. Exact moment preparation and peak movement are propagated through stored kernels; certified upper changes are 0.1608%, 0.1439%, 0.06784%. Source-preconditioner powers 1–8 fail numerical contraction tests. The six-cycle attempt ended inconclusively; a costed successor is needed for solver/kernel/reference bounds. |
| H7 | **Open, partial progress:** a sufficient uniform Schur certificate is derived. The corrected 548-direction state has a nonzero omitted native term, which an interaction-only residual misses. The positive solver norm and a conditional Bessel envelope for the closed radial Green block are now fixed. Central low-sector/downstream matching rows now pass numerical checks; the omitted-sector envelope is conditional. The binary-reference factor residual is ball-enclosed, but no source gap or coupled inverse is certified. VF1 certifies full linked binary native inertia (130 negative, no zero), but original source/frame bridges and coupled inverse remain open. VF1/RB1 ended inconclusively. VB1 now certifies exact radical vertices/centering and native-source assembly inertia. Ground/frame identity and full-band coupled inverse remain missing. Gap/frame certification, bandwise residual coverage and coupled inverse bounds remain missing. |
| H8 | A common retained continuum realization supports state-norm packet convergence and unique diagnostic limits under cofinal refinements, with separate current/denominator/peak controls. |

| H9 | The actual exit encoder intertwines the independently supplied native Hamiltonians. **Refuted:** exact source traces are 136 and 120, so no invertible intertwiner exists at the same energy reference. |
| H10 | **Refuted under its explicit constructor-admission clause:** chirality is hard-coded by slot, not transported with the owner. The exact retained-seam defect has squared norm 25/9 at both endpoints. No general exchange impossibility is inferred. |

[H9 proof and fixed H10 exchange prescription](EXIT-AND-EXCHANGE-CONJECTURES.md). Three propositions are open; each has quantifiers, a falsifier, source references and a bounded test protocol with explicitly subjective effort/outcome forecasts. H1–H5, H9 and H10 are excluded from forecasting. [H10's obstruction](PARTICIPANT-EXCHANGE-OBSTRUCTION.md) is a source-constructor admission failure with a fresh exact local witness, not a full exchanged-Hamiltonian comparison. [H4's analytic proof](OPEN-HINGE-FORM-PROOF.md) supplies trace bounds, positivity, form-norm equivalence and the representation-theorem argument. [Its source-binding audit](check_open_hinge_form.py) is not a machine verification of that functional-analysis proof. [H2's checker](check_ordered_composition.py) builds the 160-dimensional graph independently of path enumeration and verifies the C4 block and zero C16 complement. [Its receipt](results/ordered-switch-composition.v1.json) includes exact defects for collapsing six orders, deleting an order, and reversing one order; no classical measurement of paths is introduced. [H3's proof](RETAINED-ENCODER-PROOF.md) covers both endpoint poses by the arbitrary-unitary-link path theorem; [its exact checker](check_retained_encoder.py) independently reconstructs the archived source encoder and verifies the energy identity. The negative endpoint's transported geometry is covered by the theorem, not claimed as a fresh matrix replay. [H1's exact checker](check_local_switches.py) reconstructs both endpoint geometries and checks sixteen local blocks, including the initial ABE face. [Its receipt](results/local-full-spinor-switches.v1.json) binds the nested archive and checker hashes. H9's source-bound trace obstruction is recomputed by the net validator. Source-authorized dynamics, physical species/calibration and the overall explanation remain separate obligations. Histories that interfere are not turned into measured classical records.

```sh
uv run --with sympy python research/scattering/high-energy/check_local_switches.py --check
uv run --with sympy python research/scattering/high-energy/check_retained_encoder.py --check
uv run --with sympy python research/scattering/high-energy/check_ordered_composition.py --check
python research/scattering/high-energy/check_high_energy_net_v2.py
python research/scattering/high-energy/check_high_energy_net_v2.py --check
python research/voevodsky/checkers/check_conjecture_workbench.py --programme high-energy
python research/voevodsky/checkers/check_conjecture_workbench.py --programme high-energy --check
```

H1–H5 are established within their declared model scope. H5's [residual-aware proof](PACKET-CONTINUITY-PROOF.md) now has both a [pilot audit](results/packet-continuity-pilot.v1.json) and [response128 audit](results/response128-continuity.v1.json). All 17 stored downstream stationary equations and five reconstructed packet ledgers pass the latter's declared floating test. The analytic identity is for exact equations; rounded arrays retain their measured residual. This does not certify entrance-response or continuum accuracy. H7's [full linked binary inertia](VERIFIED-BINARY-INERTIA.md), [verified leading inverse factor](VERIFIED-INVERSE-FACTOR.md), [verified binary D blocks](VERIFIED-D-BLOCKS.md), [ball-factor residual and attempt closure](BALL-FACTOR-RESIDUAL.md), [inverse-factor reconstruction](INVERSE-FACTOR-RECONSTRUCTION.md), [arithmetic propagation screen](INERTIA-ROUNDOFF-SCREEN.md), [bounded lower-threshold search](INERTIA-THRESHOLD-SEARCH.md), [inertia robustness attempt](INERTIA-MARGIN-ATTEMPT.md), [central matching residual audit](CORRECTED-MATCHING-RESIDUAL.md), [source radial-envelope and solver-norm derivation](RADIAL-RESOLVENT-ENVELOPE.md), [corrected native-leakage audit](CORRECTED-RESIDUAL-NATIVE-TERM.md), [full-resolvent certificate](FULL-RESOLVENT-CERTIFICATE.md) and [partial audit](results/resolvent-certificate-attempt.v1.json) explicitly separate a closed-sector gap from full coupled stability. Exact controls refute gap-only and finite-scan shortcuts, not H7 itself. Its remaining-work estimate is revised; the shared planner selects **H7 VB1**, the explicitly budgeted [exact vertex/frame bridge](H7-VERTEX-FRAME-BRIDGE.md). Native geometry is now bridged to the pinned exact radical coordinates, not a certificate of ground/frame identification or coupled inverse. H6's successor remains unspecified. H6's solve is complete: [independent review and explicit acceptance-error budgets](QUADRATURE-REFINEMENT-REVIEW.md). Its [stored-kernel peak localization](PEAK-ENCLOSURE.md) is now certified. [Readout intervals](READOUT-ENCLOSURES.md) now include the bracket variation. [Exact moment-root enclosures](PREPARATION-ENCLOSURE.md) now bound the stored-grid preparation. [Prepared readout propagation](PREPARED-READOUT-ENCLOSURES.md) now includes those intervals and peak movement. The [polynomial screen and attempt closure](POLYNOMIAL-PRECONDITIONER-SCREEN.md) reject the tested contraction leads numerically. A successor needs an explicit new protocol and budget for a different finite-response solver/kernel/reference-error certificate, not another quadrature run. No numerical result has been promoted to an error-certified proposition. Its ranking concerns bounded-test efficiency, not physical importance.

## Historical registered v1 and source context

Related, separately scoped [low-energy proposition net](../low-energy/CONJECTURE-NET.md): conditional models, no shared calibrated energy regime or imported physical outcome.

Question: can the retained conditional model produce convergence-controlled coherent scattering readouts? Boundary: source-model geometry, explicitly extended switching and model-unit packet calculations; no physical species/calibration or continuum certificate. Disposition: registered source-pinned dependency net with an executable saved-kernel replay; scientific claims remain open.

## Explanation assessment

[Machine-readable status](../../conjecture_net/contracts/high-energy-scattering-explanation-status.v1.json): **physical scattering not yet explained**. Three gap groups are linked to the existing conjectures: numerical error/completion, physical source justification of the switching/contact rules, and preparation/calibration/particle-detector identification. Ledger4320 closes software transport only. This assessment is a versioned overlay; the frozen model contract is unchanged.

## Strominger research update — 2026-10-13

[Research attachment](../../nima/scattering-strominger-update.md) · [machine-readable11-node overlay](../../nima/contracts/scattering-strominger-update.v1.json).

The last24-hour review adds conditional autonomous rim scattering, source-generated local clocks, typed reference/raw-response and ideal joint-bank constructions, plus the interface-preserving Hamiltonian and retained energy observer. The latter already transports energy through complete retained T9 data; outer means alone remain insufficient. The old cycle-law closure obstruction is preserved. A new explicit scattering–Hamiltonian operation-map obligation remains open: none of these results identifies the coefficient Hamiltonian with this model's scattering generator or amplitudes. Source reports are pinned references, not imported proof outcomes. Physical explanation and the three gap groups remain unresolved; the frozen model and historical assessment are unchanged.

## Source-matrix core bridge audit — 2026-10-13

[Exact audit](../../nima/scattering-core-bridge-spectrum-v1.md) · [current local bridge work net](../../nima/contracts/scattering-core-bridge-work-net.v7.json) (v1–v6 retained as history).

The latest local bridge decomposition is [v7](../../nima/contracts/scattering-core-bridge-work-net.v7.json). This is a scoped research overlay; the registered 11-node historical net and pinned explanation assessment are not silently revised or promoted. The [positive-contact classification](../../nima/scattering-positive-contact-class-v1.md) proves that the balanced rank-one rule is not forced by positivity: coupled coordinate orbits carry three invariant combinations, while decoupled contacts hide the core. The [finite coherent contact inverse](../../nima/scattering-finite-contact-inverse-v1.md) recovers the three coupled invariants from three distinct actual source values; two allow an explicit positive alias. Native-operation obstruction synthesis is the next executable conceptual frontier. The [inverse-conditioning analysis](../../nima/scattering-inverse-conditioning-v1.md) supplies finite regular-domain bounds and exact failure families: source contrast decays as E^-4, and separated positive models have on-shell amplitude gaps shrinking as E^-9/2. The [observation-scoped parameter inverse](../../nima/scattering-parameter-inverse-v1.md) is now constructed: generic phase or augmented-probability inputs identify positive continuum parameters, but parity-probability-only aliases and the exact blind energy 5391/3292 remain. Quantitative inverse conditioning is now constructed at its explicit regular-domain scope; no uniform-global stability is claimed. The [operation audit](../../nima/scattering-contact-source-audit-v1.md) separates inherited core/ports from supplied continuum inputs and gives exact conservative rivals with distinguishable fluxes. Native operation selection remains separately deferred; parameter inference does not select a native law.

The [exact two-port response](../../nima/scattering-two-port-memory-v1.md) remains constructed with five minimal linear memory coordinates and nineteen retained dark directions. Its even/odd responses have two/three visible poles. Source selection remains open; contact response poles are not bound-state energies or physical species.

The unchanged coefficient law cannot cover the principal two-rim contact-generated core through a contact-complete linear generator map, even with a common time rescaling and scalar energy shift. Its five natural-complexification frequency bands are equally spaced; the actual five distinct bright-core bands are not. This is an exact source-matrix candidate exclusion, not physical scattering refutation or identification with the strained pentachoron model. The broader bridge remains open. The inherited-versus-supplied operation audit and observation-scoped identifiability are now constructed; source-internal native-operation obstruction synthesis remains executable without external delivery. The historical overlay's observer pin is stale relative to the current note and is not silently repinned.

## Wiring

- `contracts/high-energy-scattering-conjecture-net.v1.json`:11 conjectures, prerequisite DAG, evidence pointers, deferred physical-map branch and executable action.
- `contracts/high-energy-source-pins.v1.json`: hashes of original notes, scripts, historical results and all original source archives; four individually pinned replay members.
- `high_energy_scattering_net.py`: adapter to shared `research/conjecture_net/graph_metrics.py`, source/graph/programme validation, safe selective archive preparation and replay.
- `research/conjecture_net/registry.json`: registered as `scattering.high-energy.v1`, a conjecture-net contract.
- `research/conjecture_net/contracts/programme-hierarchy.v15.json`: candidate testbed link to physical-sector realization and empirical recovery, not an admitted proof import.
- `research/nima/scc-models/high-energy-scattering-net-wiring-v1.json`: forward-realization obligation at planning/evidence stratum.

The dependency chain is native endpoint realization -> conditional full-spinor switch -> conservative model -> asymptotic record flux -> packet current readout. The readout feeds separate transport-sign, energy-quadrature and omitted-response obligations; quadrature and omitted response feed spatial/continuum control. The target also needs a physical calibration/species map. Dependency arrows express obligations, not identity of different source grids, kinetic conventions or preparations.

Original results are historical evidence pointers, not automatically assigned ++ outcomes. In particular, selected-line overlaps7/9,7/9,1/9 do not supply exact sewing; the full-spinor extension remains explicit. Four prepared columns are not a full scattering matrix. Product2+8 record sectors are not independently identified particles.

## Execute

From the repository root:

```sh
python research/scattering/high-energy/high_energy_scattering_net.py
python research/conjecture_net/test_high_energy_scattering_net.py
uv run --with scipy python research/scattering/high-energy/high_energy_scattering_net.py --replay
```

Run those commands through the admitted structured-command MCP binding. SciPy's ephemeral uv environment supplies NumPy; no system environment modification is needed.

Default execution verifies integrity, dependency typing and the v15 attachment only. `--replay` extracts just the comparison script, two small complex kernels and saved reference JSON into `.ai/tmp/high-energy-scattering-replay`, then runs the existing comparison in process. No solver or full archive extraction is involved. It recomputes both17- and9-energy-node readouts, compares them against saved values using declared numerical tolerances and retains actual residuals in `results/high-energy-net-replay.json`. Workspace input collisions are rejected.

The source archives stay at their original paths. Textual source/evidence snapshots are registered incrementally; unrelated inventory pins and collection copies are not refreshed. Integrity replay verifies implementation/provenance, not experimental accuracy.

## Executable frontier and missing map

The localized numerical follow-up remains17-to33 energy samples with128 response directions fixed; the corrected-residual response hierarchy is a distinct omitted-tail test. Existing nine-node subsampling changes the128 peak rate by14.244725%, so64-to128 agreement cannot certify quadrature convergence. Fresh stationary solves for these follow-ups are not run by this wiring command.

Physical identification is deferred once: the missing object is an independently sourced dimensional preparation/instrument/species map. It reopens only when that map is supplied and checked against the actual model records; it is excluded from the executable frontier. Registry admission, graph metrics and kernel replay cannot discharge it.
