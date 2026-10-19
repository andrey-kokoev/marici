# Prior scattering clues — iteration2 of10

## Question

Does the iteration1 coupling discriminator survive releasing the supplied equal ground mixture? Operator direction: search prior research for clues toward physical scattering; perform one bounded iteration using freshly read mutable state. This allocates research, not evidence.

Fresh [explanation status](../conjecture_net/contracts/high-energy-scattering-explanation-status.v1.json) still has unresolved source, numerical-completion and preparation/calibration gaps. [Iteration1](scattering-prior-clues-iteration1.md) identified two locally distinguishable coupling directions **with its preparation fixed**.

## Claim boundary

### Prior source clues

The [native operation-energy lift](../voevodsky/native-operation-energy-lift.md) declares a uniform positive defect constructor; it does not claim a physical clock or unique physical dynamics. The [connected phase-energy source](../scattering/high-energy/pentachoron_connected_phase_energy_note.md), section6, supplies the involution J and the same ε coefficient as native seams:

\[
\epsilon(J-I)^*(J-I)=2\epsilon(I-J).
\]

Its block form therefore fixes η=2 **conditional on that uniform defect rule and the declared matching operation**. It does not independently validate applying the rule to continuum sampling or determine ν. This narrows the source-justification request: test the uniform-rule/contact extension, rather than treating η as an unfixed coefficient inside the original definition.

The [autonomous predecessor](../scattering/high-energy/pentachoron_autonomous_contact_note.md), sections2,7, separately supplies the equal mixture of four ground modes and exhibits dark inputs. Neither an unpolarized physical beam nor a two-particle tensor-product preparation follows from those four retained records. This motivates a full preparation-effect test rather than more equal-mixture response fitting.

### Source operation, type and composition

Reuse only the byte-pinned archived20+20 local contact model: `[L²(R)⊗C²⁰]⊕C²⁰`, fixed ABE pose, all open and closed modes. At each declared K/ε=2.30,3,4, construct the full two-direction scattering matrix in the same native eigenframe. For left incidence restricted to the four ground modes, let A_K select all excited outgoing rows from both directions. The retained ground-sector effect is

\[
F_K=A_K^*A_K,\qquad p_K(\rho)=\operatorname{Tr}(F_K\rho),
\qquad 0\leq F_K\leq I_4.
\]

Preparation domain: one energy-independent positive trace-one4×4 density ρ. It is a mathematical model-state domain, not physically admitted beam control. No physical-time or detector map is supplied. The15 traceless Hermitian directions are retained; no inferred radical is discarded globally. Scalar readout follows full boundary sewing, flux conservation and effect-positivity checks.

Active SCC obligation: forward realization of the full effect family, then test proposed readout descent after forgetting preparation by spectral normalization. Distinct preparations are not assumed equivalent. [Prospective primary contract](contracts/scattering-clues-iteration2.v1.json); [owner-local manifest](scc-models/scattering-prior-clue-iteration2-v1.json).

### Explanatory test

- **Problem:** unknown preparation may imitate a change in coupling law.
- **Bold conjecture:** every energy-independent ground preparation changes excited flux only by one common amplitude, so flux ratios eliminate preparation uncertainty.
- **Rivals:** one scalar bright weight; preparation-dependent spectral shape from retained intermediate dynamics; numerical error or invalid density.
- **Risky consequences:** normalized effects F_K/Tr(F_K) coincide; the two coupling directions survive projection away from preparation-induced readout changes.
- **Strongest falsifier:** compare full effects, retain all15 preparation directions, project the coupling Jacobian off their image, and test one shared positive density against each fixed finite coupling rival.

A supplemental [six-state witness](contracts/scattering-clues-iteration2-preparation-witness.v1.json) was registered **after** the primary effect result, before its own execution. Its states are constructed from the source ground matching operator, not optimized from fluxes: its two bright eigenvectors and their four ±/±i superpositions. Each state is fixed across energies. This is an explicit source-state hostile, not retrospective preregistration of the primary experiment.

## Disposition

[Checker](checkers/scattering_preparation_clue.py), [result](results/scattering-clues-iteration2.json), [full packet](results/scattering-clues-iteration2-full-packet.npz). Numerical equation/effect checks and SCC check passed. Eight archived manifest members are verified; original notes, archives and receipts remain unchanged. Effect/source scalar agreement is within1.39×10⁻¹⁷ and conservation residual within8.39×10⁻¹⁵.

**The scalar-preparation conjecture is falsified in the retained local model.** Maximum normalized-effect difference is0.645677. Two fixed, positive pure preparations, `(b₀+b₁)/√2` and `(b₀−b₁)/√2`, give the following excited fluxes with ν=1,η=2 unchanged:

| Preparation | K/ε=2.30 | 3 | 4 | Flux(4)/Flux(2.30) |
|---|---:|---:|---:|---:|
| Plus |0.229270|0.049134|0.019358|0.084433|
| Minus |0.243856|0.018304|0.458370|1.879671|

Thus curve shape alone cannot be attributed to changed coupling without constraining preparation. These are source-state effects, not empirical particle yields.

The preparation-to-three-flux map has numerical singular values0.431887,0.173523,6.56×10⁻¹⁶: rank2 at these probes. After projecting the coupling Jacobian off that nuisance image, singular values are0.0289795 and6.25×10⁻¹⁷: only one local coupling direction remains distinguishable. This does not retract iteration1's fixed-preparation result; it blocks using that result with unknown preparation. No global degeneracy or all-energy rank theorem follows.

The deliberately fixed **finite** rivals ν=1.00001 and η=2.00002 did **not** exactly match all three baseline fluxes by changing one shared density: residuals1.71×10⁻⁷ and2.34×10⁻⁷ exceed the frozen10⁻¹⁰ threshold, although both densities remain positive. They are failed finite-matching attempts, not exact coupling/preparation counterexamples. The successful finite falsifier is the preparation-only shape change above.

### Actionable clue and continuation

Existing `physical-preparation-calibration-and-identification` gap: independently constrain the incident density before interpreting a normalized spectral curve as contact-law evidence. Dark-state exclusion or an asserted unpolarized beam is insufficient; coherent bright preparations already change shape. Detector efficiency and species identification remain additional missing maps, not supplied by this effect audit.

Existing `physical-source-justification` gap: η=2 is a conditional prediction of the inherited uniform defect rule; positivity alone does not establish that rule physically. Do not fit η or ν to compensate for an unsupported preparation. Physical scattering remains unexplained; root outcome is null. This predecessor result neither transfers to the latest strained model nor bounds its numerical completion.

Next nonredundant executable test: add the prior source's already sampled K/ε=5 probe under a new prospective contract. Test whether preparation rank2 persists and whether two coupling directions survive nuisance projection. The fourth probe is a testable candidate, not an established repair; source/preparation/instrument maps still require independent inputs.

Reproduce through the admitted structured-command binding:

```text
uv run --with scipy python research/nima/checkers/scattering_preparation_clue.py
uv run --with scipy python research/aspect/scc/scc.py check scattering-prior-clue-iteration2-v1
python research/aspect/scc/scc.py validate research/nima/scc-models/scattering-prior-clue-iteration2-v1.json
```

SCC manifest validation and check passed; independent source/result hash closure verified all38 retained arrays. Report admission is `ev-000000015903-ca3ffe91-92d6-4308-9b59-5097779bda13`, proposal `ep_063a3b4f-ff95-4e11-9220-a65adfdff1bd`; this iteration's admitted-but-uncommitted interval is[15903,15903]. Admission preserves communication, not scientific truth. Five owner-local source/contract/manifest/packet files are untracked; numerical results are ignored. No programme proof export, physical preparation authority, Git commit or push is asserted.
