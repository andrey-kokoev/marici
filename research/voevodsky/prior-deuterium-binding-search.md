# Prior-research search for the missing deuterium interaction

## Search result

Searched Markdown in the research tree for deuterium/deuteron/nuclear binding, attractive interactions, mediator exchange and cross-carrier binding. Inspected the relevant Nima, Voevodsky and flavor sources below. No tests were rerun during this search.

The recovered work contains an executable **binding benchmark**, a **connected-energy discriminator**, and a specific **source-port nonlinear-interaction failure**. It does not provide a completed source-derived proton–belt nuclear binding law in the inspected material.

## Reuse these before constructing another model

### Actual binding below a breakup threshold

`research/nima/hminus-nested-orbitals.md` already demonstrates variational binding in a supplied Coulomb Hamiltonian. A symmetrized compact/diffuse orbital trial gives energy approximately -0.5133027718 against the hydrogen-plus-electron threshold -0.5. The equal-orbital trial is above threshold.

Its important reusable feature is the test architecture: preserve species/exchange type, relax the joint state, and compare with a threshold from the same Hamiltonian. Retaining a parent record does not freeze the parent's orbital in the composite. We should reuse that architecture rather than present a positive gluing penalty as binding.

Successor `hminus-recoil.md` includes finite-nucleus kinetics, a mass-polarization control and exact radiation/recoil accounting. It also shows that calibration must be transported when nuclear mass changes. Neither supplies a nuclear force.

### Calculate connected energy, not an added pair constant

`binding-composition-coherence.md` isolates

    E(12)-E(1)-E(2)+E(empty).

It proves that source composition coherence and single-electron calibration do not select this interaction contribution. Its source audit also permits exact energy cochains without breaking the route squares.

`helium-coulomb-variational.md` then computes the connected contribution in a supplied Coulomb model, including both repulsion and orbital relaxation. `helium-correlated-variational.md` improves that result by retaining explicit pair-separation dependence, without fitting the helium reference.

For our next deuterium test, the connected-energy subtraction must use identical boundary and reservoir data. A new attraction must be computed from an operator and a joint state, not inserted as an isotope-specific deficit.

### The proposed nonlinear port operation was already tested

`inner-face-response-port-binding.md` is directly relevant to our triangle ports. The existing proton stage algebra reduces to span(I,M) on the selected amplitudes. The state-dependent diagonal gate needed for the earlier covariance-response proposal is outside that algebra; actual native comparison composition does not supply its numerical interaction or schedule.

The two proposed schedules yield M/6 and zero only after adding that missing gate. Their difference is not evidence that the present source circuit already generates a binding force. Repeating this proposal without a new source binding would duplicate a completed failed branch.

### An attractive shell trial already exists, with a structural failure

`research/voevodsky/hydrogen-attachment-candidate.md` adds a radial law A/rho^2-B/rho and produces a negative shell energy. Its point-site position reader has a fixed nonzero cubic moment on every state, so the simplest spherical hydrogen interpretation fails. Adding a Coulomb-like attractive term to the same sites is not a new source derivation and does not fix that obstruction.

### Mediator support does not select a nuclear interaction

`research/flavor/flavor-charged-scalar-messenger-descent-nonselection.md` constructs a charge-compatible mediated portal and derives its mixed loop curvature. Its value still depends on vertex products, masses and renormalized counterterms. This offers a typed mediator-elimination method, not a transferable numerical nuclear force or sign.

`charge-mass-recoil-triangle.md` and the previously searched interaction pipeline already supply signed impulse/recoil laws for selected charges, masses and an external kernel. They test compatibility, not a source-selected attractive potential or bound state.

## Consequence for the current construction

The current spinor rim lift solves a port-representation issue. The current exterior-flux model solves a zero-background Gauss issue. Neither contains the cross-carrier interaction that these prior binding benchmarks explicitly require.

The next substantive construction should reuse the connected-energy and relaxed-threshold tests above. Its upstream input is a source-authorized constituent-preserving cross-carrier vertex, with an accompanying kinetic/relative-motion sector. The inspected prior material supplies acceptance tests and conditional examples, but not that proton–belt vertex. This is a bounded search conclusion, not an exhaustive absence claim.
