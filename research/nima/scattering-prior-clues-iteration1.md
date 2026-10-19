# Prior scattering clues — iteration1 of10

## Question

Can existing source research identify an executable obligation closer to physical scattering than another response fit?

Operator direction: search prior research for actionable clues; allocate one bounded iteration. This is a search constraint, not evidence. The [v17 assessment](../conjecture_net/contracts/high-energy-scattering-explanation-status.v1.json) remains `physical_scattering_not_yet_explained`.

## Claim boundary

The [reuse guide](../strominger/high-energy-research-reuse.md) points to autonomous positive contact forms: retain the diagonal terms and derive boundary equations instead of inserting a pulse. The [neutron construction](../strominger/neutron-autonomous-rim-scattering.md) supplies a form-domain/self-adjointness template and raw-field verifier, not transferable neutron operators or physical scales. The [pentachoron predecessor](../scattering/high-energy/pentachoron_autonomous_contact_note.md) already inherits native operators, has a native threshold √5ε, and explicitly supplies its kinetic choice. Its archived kinetic controls already show sensitivity at K=2.30ε; that observation is not new here.

### Frozen source and types

[Contract](contracts/scattering-clues-iteration1.v1.json) fixes the rival families, probes and tolerances before the initial execution. Active SCC obligation: **readout descent under a common energy-unit change**, not identification of physically equivalent parameter laws. [Owner-local model](scc-models/scattering-prior-clue-iteration1-v1.json) records the conditional numerical stratum. SCC registration followed the initial experiment; it is not a retrospective prospective freeze.

The archived local model has carrier `[L²(R)⊗C²⁰]⊕C²⁰`, form domain `[H¹(R)⊗C²⁰]⊕C²⁰`, frozen ABE geometry and standard Hermitian coordinate metric. All20 continuum and20 core coordinates, including closed channels, enter the boundary solve. This does not assert that these retained records exhaust a physical scattering Hilbert space. No physical-time map is supplied.

Preparation is the source's equal incoherent mixture of its four lowest native modes, ρ₀=Π₀/4, not an identified physical unpolarized beam. Readout is outgoing **excited native-record flux**, not a particle-production probability. Matching dimensions with the neutron carrier or later2+8 product sectors provides no comparison map.

In dimensionless ξ=x/ℓ coordinates, use the declared form

\[
q_{\nu,\eta}(u,\chi)=
\int[\nu\|u'\|^2+u^*H_Ou]d\xi+
\chi^*H_C\chi+\eta\|P(u(0)-\chi)\|^2.
\]

Here ν=κ/(εℓ²)>0 and η is contact coefficient/ε. Source values are ν=1, η=2. Varying η explicitly changes the source's uniform defect-strength assumption; it is a rival contact law, not an allowed gauge transformation of that source. Native H_O,H_C,P and the preparation are held fixed. All sampled rivals retain positivity and conservative boundary structure.

For total E, k_j²=(E−e_j)/ν, open-channel v_j=2νk_j and unit-flux incident amplitude v_j⁻¹ᐟ², the full boundary operator is

\[
M=\begin{pmatrix}
2i\nu\operatorname{diag}(k)-\eta B&\eta B\\
\eta B&E I-C-\eta B
\end{pmatrix},
\qquad C=V^*H_CV,\quad B=V^*PV.
\]

Solve in one fixed native eigenframe V, compose reflected/transmitted amplitudes into the two-direction S matrix, test the boundary/core equations and S* S=I, then scalarize. The common energy-normalization control multiplies E,e_j,C and the numerical kinetic/contact coefficients νε,ηε by factor3. Ratios ν,η and K/ε stay fixed; no source operator or channel is discarded. This stationary readout test supplies no physical-time or velocity calibration. The [full packet](results/scattering-clues-iteration1-full-packet.npz) retains the frame, fields, full S matrices and analytic S tangents.

### Explanatory test

- **Problem:** a missing dynamical-source law can be mistaken for an overall units-calibration gap.
- **Bold conjecture:** native spectral operators plus conservative contact structure select the dimensionless scattering curve up to an energy-unit choice.
- **Rivals:** independent kinetic ratio; independent contact-strength law; mere units/frame/solver artifact.
- **Risky consequence:** units changes preserve full S, but ratio changes need not; three source-selected probes can distinguish the two ratio directions locally.
- **Strongest falsifier:** independent full boundary assembly, archived full/Schur solver comparison, true units control, and analytic versus central-difference log-parameter derivatives at K/ε=2.30,3.00,4.00.

No experimental data or target masses enter the test. NumPy and SciPy share numerical infrastructure: independent equation assembly is not an independent floating-point backend. This is a new stationary local-model solve, not a latest strained-model solve or a wavepacket/convergence certificate.

## Disposition

[Checker](checkers/scattering_contact_scale_clue.py) and [result](results/scattering-clues-iteration1.json):11 checks passed. Archive manifest verification covers all8 listed members; the archived source class is executed without its main, packet generation or symbolic reconstruction. Original archives, notes and owner receipts are unchanged.

At K=2.30ε and source η=2, excited flux is0.121556,0.118282,0.106347 for ν=0.5,1,2, reproducing the historical controls. At ν=1, changing the contact-law coefficient η to1 or4 gives0.066534 or0.082088. Native threshold remains2.2360679775ε. Conservation/boundary residual is at most9.16×10⁻¹⁵; full S changes by at most5.84×10⁻¹⁴ under true common units rescaling.

**New discriminator:** the3×2 Jacobian of excited flux with respect to(logν,logη) has singular values0.201565 and0.029064. Analytic derivatives agree with central differences within6.26×10⁻¹⁰. Thus both directions are numerically distinguishable locally at the fixed source fixture. Flux at K=4ε is nonmonotonic in the sampled ν controls; this is not a global uniqueness or branch-selection theorem.

The governing conjecture fails in this conditional model: conservation and native geometry alone do not select the dimensionless scattering law. Source threshold, mathematical form consistency and local discrimination survive. Physical scattering remains unexplained; programme/root outcomes stay null.

### Actionable clue and existing gap attachment

This packet supports the existing `physical-source-justification` gap (`autonomous-conservative-model`, `conditional-full-spinor-switch`): independently substantiate the kinetic-to-native ratio and the use of the uniform native defect coefficient at continuum contact. Positivity is not that substantiation.

It also sharpens `physical-preparation-calibration-and-identification` (`physical-calibration-and-species`): conditional on independently justified species, preparation and detector maps, the native excitation threshold could fix ε, while an independently measured/derived kinetic coefficient and sampling length fix ν. Multiple calibrated flux probes could then test η=2 without using one flux value to hide a free kinetic ratio. The present Jacobian only supports local discrimination with the other inputs fixed; unknown preparation or detector efficiencies can introduce additional ambiguity.

**Falsifier for this clue:** a source-derived relation fixing these ratios without readout fitting would remove the highlighted freedom. Alternatively, independently calibrated multi-energy records incompatible with the source η=2 law after independent ν determination would reject that contact-law hypothesis in its declared domain. Neither object is currently supplied; defer that physical branch rather than create a waiting leaf.

The [omitted-mode note](../scattering/high-energy/omitted_mode_estimate_note.md) concerns fixed-grid, frozen-source omitted residence, not self-consistent packet/product-current error. It therefore cannot promote this predecessor discriminator to the latest high-energy calculation. Next executable research: trace the inherited uniform defect-energy rule and any independently sourced kinetic/preparation constructor in prior source work; do not substitute a neutron matrix, new fitted factor, or latest-model convergence assertion.

Reproduce through the admitted structured-command binding:

```text
uv run --with scipy python research/nima/checkers/scattering_contact_scale_clue.py
uv run --with scipy python research/aspect/scc/scc.py check scattering-prior-clue-iteration1-v1
```

SCC manifest validation passed with `python research/aspect/scc/scc.py validate research/nima/scc-models/scattering-prior-clue-iteration1-v1.json`. An initial model-ID argument failed path resolution; the corrected file-path invocation passed. Full-packet array count68 and result/source hashes were checked independently.

Report admission: `ev-000000015901-bfe1d8ed-30f1-4497-9311-b3943ba85af6`, proposal `ep_ab397756-f118-4b5b-87b3-ad0ae5f44909`; this iteration's admitted-but-uncommitted interval is[15901,15901]. Communication admission certifies neither the scientific claims nor physical authority. Git checkpoint and push are not authorized; this packet is local uncommitted research, not a proof-outcome export or physical apparatus certificate.
