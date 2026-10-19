# Prior scattering clues — iteration3 of10

## Question

Can the prior source's K/ε=5 probe recover coupling discrimination after retaining unknown shared preparation?

Fresh mutable [explanation status](../conjecture_net/contracts/high-energy-scattering-explanation-status.v1.json) remains unresolved. [Iteration2](scattering-prior-clues-iteration2.md) showed that three probes retain preparation rank2 and only one coupling direction. Operator direction allocates this bounded continuation; it is not scientific evidence.

## Claim boundary

The archive behind the [autonomous-contact note](../scattering/high-energy/pentachoron_autonomous_contact_note.md) already samples K/ε=5. The checker verifies all four chosen energies against that pinned historical list before calculating. No energy is selected by searching for a favorable sensitivity.

### Frozen operation and type

[Prospective contract](contracts/scattering-clues-iteration3.v1.json); [owner-local SCC model](scc-models/scattering-prior-clue-iteration3-v1.json). Active obligation: forward realization of the effect family, then passive native-ground-frame readout descent.

Use only the archived fixed-ABE20+20 contact predecessor. Its carrier is `[L²(R)⊗C²⁰]⊕C²⁰`; all open/closed native and core modes remain in the boundary solve. The prepared ground sector has dimension4. At each energy, compose the full two-direction S matrix and form F_E=A_E* A_E from all excited outgoing rows. Then evaluate p_E(ρ)=Tr(F_Eρ). Different open-channel counts are retained separately; no S matrices at different energies are identified or composed with each other.

Couplings are ν=1,η=2 at the fixture. The local density evaluation point is ρ₀=I₄/4, but all15 traceless Hermitian perturbations of one energy-independent density remain available. This is a model-state neighborhood, not a physical beam assumption. Ground-frame changes conjugate both effects and their derivative packets. No physical-time, preparation, detector or species map is supplied.

For an orthonormal traceless Hermitian basis Q_a, construct

\[
N_{Ea}=\operatorname{Tr}(F_EQ_a),\qquad
J_{Ej}=\operatorname{Tr}(\partial_{\log\theta_j}F_E\,\rho_0),
\quad\theta=(\nu,\eta).
\]

Use one absolute SVD threshold10⁻⁹ to select the image of N and project J onto its orthogonal complement. Full effects and analytic derivative operators are retained before scalarization. This is local nuisance analysis, not a density fit or physical parameter estimate.

### Explanatory test

- **Problem:** three flux probes cannot separate both source-law directions when shared preparation is unknown.
- **Bold conjecture:** the inherited fourth probe preserves preparation rank2 and restores two local coupling directions at the source fixture.
- **Rivals:** a genuinely informative fourth probe; growth of preparation directions; repeated-data or coordinate artifacts.
- **Risky consequences:** both projected singular values exceed the frozen10⁻⁵ floor; repeating K/ε=4 instead does not create a direction; passive Fourier frame changes preserve the result.
- **Strongest falsifier:** full-effect analytic/central-difference comparison, historical-source replay, duplicate probe, frame transport and normalized dark-density null tests.

The two source contrast rows L are the left-nullspace basis of N. Their full operator relations are checked directly, not inferred solely from scalar rank. This is a consequence of the frozen nuisance projection, not an additional selected probe.

## Disposition

[Checker](checkers/scattering_four_probe_clue.py), [result](results/scattering-clues-iteration3.json), [full packet](results/scattering-clues-iteration3-full-packet.npz). SCC check and manifest validation passed. The conjecture survives at the declared fixture:

| Probe set | Preparation rank | Coupling rank after nuisance projection | Projected singular values |
|---|---:|---:|---|
|2.30,3,4|2|1|0.0289795,7.63×10⁻¹⁷|
|2.30,3,4,5|2|2|0.126746,0.0219038|
|2.30,3,4,4|2|1|0.0290209,1.12×10⁻¹⁶|

The extra source flux at5 is0.0454217 for ρ₀, reproducing its historical result. Source/conservation residual is at most8.39×10⁻¹⁵; full-effect derivative error2.51×10⁻⁹; passive-frame singular-value error5.65×10⁻¹⁷. Dark-density excitation is numerically zero within5.21×10⁻¹⁸, so no all-preparation identification claim survives.

### Actionable source-derived readout

The two contrast rows, stored in the result and full packet, satisfy

\[
\sum_E L_{rE}F_E\simeq0,
\qquad Lp(\rho)\simeq0.
\]

The maximum full-operator residual is1.18×10⁻¹⁵. Since every F_E annihilates the same dark sector, a contrast annihilating all traceless preparation directions cannot leave a nonzero identity term. Thus these numerical operator relations apply to **any shared ground density** at the fixed couplings, not just to ρ₀; no scalar-only cancellation hides a retained response. A common overall multiplicative detector gain also cancels in Lp. Energy-dependent detector gains or energy-dependent preparations do not.

The contrast coupling Jacobian at ρ₀ is

\[
LJ\simeq\begin{pmatrix}
-0.0221022&-0.1225054\\
0.0261150&0.0191388
\end{pmatrix}.
\]

It has the two nonzero singular values above. This supplies a conditional four-energy test of the source law without fixing its shared preparation: compute contrasts from independently specified native operators/couplings, then compare calibrated record fluxes. No experimental fluxes, fitted masses or retrospectively adjusted source coefficients enter this packet. The construction uses full effect matrices, not inverse reconstruction of a source from desired readouts.

Existing gaps remain: `physical-source-justification` requires the kinetic/contact law, and `physical-preparation-calibration-and-identification` requires the native-record measurement map, energy scale, controlled shared-preparation condition and relative detector calibration. The new discriminator supplies none of those objects. Euclidean singular values are numerical conditioning diagnostics, not experimental uncertainty bounds. No full strained-model, packet-quadrature, omitted-mode or continuum-completion claim is made; physical scattering remains unexplained and root outcome null.

### Nonredundant continuation

The contrast identities do not imply preparation-independent **coupling sensitivity**: J depends on the density. Next executable test: use the retained derivative operators to derive the2×2 contrast-Jacobian determinant over the source's two-dimensional bright sector, retaining its Bloch-ball positivity constraint. Locate rank-deficient bright preparations or establish a scoped bound; do not extrapolate the ρ₀ result to every non-dark beam.

Reproduce through the admitted structured-command binding:

```text
uv run --with scipy python research/nima/checkers/scattering_four_probe_clue.py
uv run --with scipy python research/aspect/scc/scc.py check scattering-prior-clue-iteration3-v1
python research/aspect/scc/scc.py validate research/nima/scc-models/scattering-prior-clue-iteration3-v1.json
```

Independent result/source hash and full-operator closure checks passed for all37 retained arrays. Report admission: `ev-000000015905-66bd3ab9-e6f8-4559-82c1-cab59f94f05a`, proposal `ep_7d1dcacd-655d-49cd-a85e-5f2342edbbba`; this iteration's admitted-but-uncommitted interval is[15905,15905]. Communication admission does not certify scientific truth. Four source/contract/manifest/packet files are untracked; numerical outputs are ignored. Original source artifacts and earlier iteration results are unchanged. No programme proof export or physical calibration is asserted; Git commit/push remains unauthorized.
