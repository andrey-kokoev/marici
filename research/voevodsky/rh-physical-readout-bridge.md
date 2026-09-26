# Conditional physical readout of an off-critical zeta zero

## Question

If the completed arithmetic RH object admitted a faithful passive or unitary apparatus realization, what exact apparatus defect would an off-critical zero force?

## Claim boundary

This packet proves only a coordinate theorem. For a nontrivial zero candidate

\[
\rho=\beta+i\gamma
\]

and the rigid Li coordinate

\[
u(\rho)=1-\frac1\rho=\frac{\rho-1}{\rho},
\]

one has

\[
|u(\rho)|^2-1=\frac{1-2\beta}{\beta^2+\gamma^2}.
\]

Therefore \(|u(\rho)|=1\) exactly when \(\beta=1/2\). Functional reflection gives

\[
u(1-\rho)=u(\rho)^{-1}.
\]

An off-critical reflected pair consequently has reciprocal squared gains: one exceeds one and the other is below one. It cannot be represented by eigenphases of one lossless unitary stage.

The centered spectral coordinate

\[
t=\frac{\rho-1/2}{i}=\gamma-i(\beta-1/2)
\]

is real exactly on the critical line. Thus the same defect appears as a nonreal candidate spectral coordinate for a purported fixed self-adjoint operator.

These identities do not prove that zeta zeros are apparatus modes. They do not turn an arithmetic continuation parameter into physical time, energy, or frequency.

## SCC classification

The active obligation is **readout descent**. The lower arithmetic coordinate calculation is exact, but the upstream route from the theta/Evans source to a positive physical observable is not closed.

The current SCC model `theta-rh-corrected-g4-v2` classifies the source as a `source_typed_partial_interaction_net_not_rh_proof` and retains three missing constructors:

1. the complete prime-shell adjoint residual family;
2. global Fourier–Poisson response intertwining;
3. the Evans-to-conservative-Green chain map.

A physical experiment additionally requires a calibrated apparatus map that sends the conservative Green form to a declared positive power, covariance, or norm readout with error bounds. No reviewed artifact supplies that map.

## Conditional apparatus consequences

Assume, beyond the proved coordinate theorem, that a source-derived map identifies every arithmetic phase \(u(\rho)\) with an eigenvalue of a lossless unitary apparatus stage. An off-critical zero then forces a contradiction because unitary eigenvalues have modulus one.

For a reciprocal two-channel realization, let

\[
g=|u(\rho)|^2,
\qquad g^{\vee}=|u(1-\rho)|^2=g^{-1}.
\]

When \(\beta\ne1/2\), one channel requires gain and the other attenuation. The measurable signature in an engineered realization would be one of:

- failure of norm preservation under repeated apparatus stages;
- a nonzero gain/loss budget;
- an independent reservoir needed to complete a passive colligation;
- a nonreal resonance coordinate rather than a real self-adjoint eigenvalue;
- failure of a reconstructed covariance or power kernel to remain positive semidefinite.

The final item is conditional on the Weil functional being identified with that kernel. Weil positivity implies RH, but that source-to-apparatus identification is itself part of the missing readout descent.

## Relation to existing research

- `research/grothendieck/li-cayley-hilbert-polya-target.md` fixes the conditional Cayley operator after arithmetic positivity.
- `research/grothendieck/hilbert-polya-gap-is-between-exponential-and-resolvent-calculi.md` proves that self-adjointness alone does not constrain zeros of an exponential overlap.
- `research/grothendieck/gaussian-positivity-promotes-to-weil-positivity.md` proves the all-scale Gaussian-positivity-to-RH promotion arrow, not its premise.
- `research/nima/rh-rigging-frontier-after-exact-evans-domain-and-five-port-summability.md` identifies the unresolved adjoint residual and Fourier–Poisson sewing.
- `research/aspect/theta-colligation-output-port-phase-diagram.md` gives finite apparatus realization constraints, not an RH test.

## Finite hostile

`check_rh_physical_readout_bridge.py` checks the exact rational identities on a bounded hostile grid, including very large ordinates where the modulus defect is small but nonzero. It also requires deliberate failure of the false assertions that off-critical phases remain unit modulus and that off-critical centered spectral coordinates remain real.

A finite positive grid does not establish a global theorem. Here the global identities are elementary algebra; the grid checks implementation and sign conventions only.

## Executable-frontier audit

SCC inverse design returns four missing witnesses. The nominal first test is the complete prime-shell adjoint residual family. Prior source audit shows that this test is not executable yet: `research/nima/five-port-prime-shell-source-locator-table.md` records no frozen complete-shell expression for the derivative/wall pairings, no full stratified Fourier–Poisson transport for the reciprocal port, and no polarized two-output metric identity for the linking port. `research/nima/the-scc-prime-shell-cell-has-no-source-formula-for-its-reciprocal-linking-response.md` further records six missing source maps for the ordered-pair response.

The first missing typed object is therefore a source-normalized reciprocal/linking response section on each ordered theta-label pair and consecutive-prime shell. Its acceptance test is an entire source identity, fixed before inspecting Xi zeros, that reproduces the negative ordinary completed logarithmic-half-density Laplace term after the separately typed endpoint contribution is removed, preserves ordered-pair orientation and adjacent-shell concatenation, and supplies every parameter jet required by multiplicity.

No coefficient may be inferred from desired cancellation. This branch is deferred until that section is materialized. The Evans-to-Green, global Fourier–Poisson, and calibrated-apparatus branches likewise lack their declared source objects, so no further physical promotion is executable from the current packet.

## Disposition

The conditional signature is resolved: a faithful lossless/unitary realization would convert off-criticality into reciprocal gain/loss and nonreal spectral coordinates. The physical bridge stops at readout descent, with the reciprocal/linking response section as the first missing typed object. RH violation would falsify that realization; it would not violate physics generally.
