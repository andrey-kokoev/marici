# Prior scattering clues — iteration4 of10

## Question

Does nonzero bright preparation suffice for the four-probe coupling discriminator?

Fresh mutable [explanation status](../conjecture_net/contracts/high-energy-scattering-explanation-status.v1.json) remains unresolved. [Iteration3](scattering-prior-clues-iteration3.md) established two local coupling directions at ρ₀=I₄/4, not at every preparation. The operator requests a bounded prior-research continuation; no scientific premise follows from that direction.

## Claim boundary

The [autonomous source](../scattering/high-energy/pentachoron_autonomous_contact_note.md), section7, already separates dark inputs and keeps a full flux-normalized S matrix. The present question uses that preparation distinction and the retained derivative operators, rather than fitting another response curve.

### Frozen operation, type and transport

[Prospective contract](contracts/scattering-clues-iteration4.v1.json); [owner-local SCC manifest](scc-models/scattering-prior-clue-iteration4-v1.json). Active obligation: state-based forward realization of the contrast Jacobian, then passive bright-frame readout transport.

Use the pinned archived fixed-ABE20+20 local contact predecessor. At ν=1,η=2 and K/ε=2.30,3,4,5, retain the complete ground effects F_E and derivatives ∂_jF_E from iteration3. Source ground matching splits the4-dimensional ground sector into2-dimensional bright/dark supports. This is not a physical spin or particle identification.

With the existing contrast rows L, define full ground operators

\[
T_{rj}=\sum_E L_{rE}\partial_{\log\theta_j}F_E,
\qquad C_{rj}(\rho)=\operatorname{Tr}(T_{rj}\rho).
\]

Compress only after checking dark support vanishes. In the source bright frame B,

\[
\rho_b=\frac{I+\boldsymbol b\cdot\boldsymbol\sigma}{2},\quad
\|\boldsymbol b\|\leq1,\qquad
C(\rho_b)=A_0+\sum_i b_iA_i.
\]

The Pauli matrices are coordinates on this mathematical two-mode density domain. A full ground density with bright weight w has contrast Jacobian wC; its determinant is w² times

\[
f(\boldsymbol b)=d_0+\boldsymbol l\cdot\boldsymbol b+
\boldsymbol b^TQ\boldsymbol b.
\]

Coefficients follow algebraically from the retained2×2 affine Jacobian, not from scalar curve fitting. Preserve the complete operator packet through this contraction. Passive frame changes transport both operators and density; no physical-time map is supplied.

### Explanatory test

- **Problem:** the equal-mixture sensitivity may fail even with substantial bright signal.
- **Bold conjecture:** every positive bright density retains both local coupling directions.
- **Rivals:** only dark occupation loses sensitivity; a non-dark density gives rank loss; the apparent witness is nonpositive or a coordinate/numerical artifact.
- **Risky consequence:** no determinant sign change occurs within the positive Bloch ball.
- **Strongest falsifier:** the frozen center/axis/cube/source-quadratic-eigenvector search brackets a radial root; verify a shared full ground density, nonzero flux, rank loss and passive frame transport.

The sufficient bound `|d₀|−||l||−||Q||₂` was frozen as an alternative survival test. Its failure alone would be unresolved, not a refutation. The root density is a deliberate mathematical hostile, not a source-derived physical preparation or a proposed fit to experimental fluxes.

## Disposition

[Checker](checkers/scattering_bright_robustness_clue.py), [result](results/scattering-clues-iteration4.json), [full packet](results/scattering-clues-iteration4-full-packet.npz). SCC check and manifest validation passed. Prior source and packet hashes are checked; no older result or archive is regenerated.

**Preparation-uniform coupling sensitivity is falsified in this local model.** The frozen search found a strictly positive non-dark shared density:

- Bright weight0.5; Bloch norm0.984558876.
- Full ground eigenvalues0.00386028,0.25,0.25,0.49613972.
- Excited fluxes0.114590,0.024662,0.008332,0.006381 at the four probes.
- Contrast-Jacobian singular values0.05909696 and1.97×10⁻¹⁸; determinant residual1.76×10⁻¹⁹.

This is not a dark-state exclusion, vanishing signal, nonpositive density, or PSD-boundary artifact. Polynomial/direct determinant discrepancy is at most1.05×10⁻¹⁷; derivative dark-support residual3.81×10⁻¹⁶; passive-frame witness error1.66×10⁻¹⁷. It is a numeric local-jet counterexample, not a proven exact finite parameter degeneracy or an all-energy theorem. The four-energy contrast identities from iteration3 remain intact.

### Actionable preparation condition

Secondary algebraic characterization, performed after the primary witness result, numerically reduces the determinant to one bright moment x=n·b:

\[
f(x)\simeq0.0111048978842-0.00960441972533x
-0.00170090336853x^2,
\]

with n approximately(0.97262510,0.02706791,−0.23079807). The quadratic axis-reduction residual is1.99×10⁻¹⁷; the feasible critical coordinate is x≈0.984558876. These are source-frame numerical coefficients, not an exact symbolic reduction or laboratory polarization axis.

The stored mathematical moment operator is M=B(n·σ)B*, with bright projector Π_b. Its conditional density moment is x=Tr(Mρ)/Tr(Π_bρ). A preparation acceptance test must therefore constrain this moment away from the critical value, plus maintain adequate bright signal. Counting bright occupation alone does not certify two-coupling sensitivity. Deriving M does not supply a physical measurement or preparation actuator.

Existing `physical-preparation-calibration-and-identification` gap: independently map and constrain the native preparation moment, shared across energies, before claiming the four-probe law is identifiable. `physical-source-justification` still needs independent kinetic/contact inputs. No species map, uncertainty-complete detector calibration, latest strained-model convergence or physical scattering explanation follows; root outcome stays null.

### Nonredundant continuation

The prior source also retains reflected and transmitted flux separately. Next executable test: add its already defined **total reflected flux at K/ε=2.30** to the four excitation readouts, using the full S packet and the positive rank-loss witness. Test whether this channel-sensitive record restores both coupling directions after retaining all preparation nuisance directions. Do not assume it helps or invent a new physical detector map. This changes the readout family instead of blindly adding energies or fitting a preparation.

Reproduce through the admitted structured-command binding:

```text
uv run --with scipy python research/nima/checkers/scattering_bright_robustness_clue.py
uv run --with scipy python research/aspect/scc/scc.py check scattering-prior-clue-iteration4-v1
python research/aspect/scc/scc.py validate research/nima/scc-models/scattering-prior-clue-iteration4-v1.json
```

Independent source/result closure checked all15 arrays, positive witness density, moment Hermiticity and M²=Π_b. Report admission: `ev-000000015907-c948c9fc-c561-48a6-ac4e-586062004745`, proposal `ep_8f01c126-9651-41d6-8844-27e0d611c47f`; this iteration's admitted-but-uncommitted interval is[15907,15907]. Communication admission does not certify scientific truth. Four source/contract/manifest/packet files are untracked; numerical outputs are ignored. No programme proof export, physical preparation authority or Git commit/push is asserted.
