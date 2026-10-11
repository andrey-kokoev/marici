# Prior field/action search after the all-face contact construction

## Scope and verification status

This was a document and implementation search, primarily in `research/nima` and `research/voevodsky`, for existing interactions, field actions, source bindings and normalization work relevant to the remaining mass bridge. No mathematical checker or proof root was rerun in this search. Existing documents' reported tests are not fresh verification.

## Strongest recovered result: a closed field feedback model already exists

`research/nima/record-gauge-feedback-loop.md` and its inspected implementation `research/nima/checkers/check_record_gauge_feedback.py` already provide

    H = sum_e kappa_e |psi_b-exp(i A_e)psi_a|^2
        + beta/2 sum_e E_e^2
        + magnetic sum_f [1-cos((C A)_f)].

It includes canonical link variables, a matter current, backreaction on the field, temporal-gauge evolution, a conserved Gauss constraint, reversible numerical subflows and a gauge-covariance test. This is much more than a passive phase decoration.

Its predecessor `record-charge-and-phase-transport.md` supplies the explicit current and continuity interface. The feedback successor closes the return path that the predecessor still lists as open.

The existing implementation uses a four-vertex/six-link graph, a supplied neutralizing background, chosen hopping/electric/magnetic coefficients and selected filled triangular loops. It explicitly lacks an adapter from the retained comparison dynamics. Its existence does not identify its U(1) charge with measured electric charge or fix its energy unit.

**Consequence:** constructing another generic lattice gauge Hamiltonian would duplicate prior work. The useful next task is a source-preserving adapter from the actual proton/belt mode operators to this existing matter/link interaction.

## Other directly reusable results

### Source-addressed reversible interaction

`seed-port-exchange-binding.md` binds actual native arrow occurrences to the prior carrier/record exchange, retains histories and source/target attachments, and checks the operation against the original full model. This is an existing executable conditional adapter, not a missing interaction to invent again.

`source-exchange-deliverable.md` consolidates its source-to-instrument chain, preparation, phase standard, measurement and resource accounting. It explicitly leaves the native current/field identification and absolute coupling unresolved. A normalized response fraction is not a coupling calibration.

### A scalar action with its kinetic term retained

`comparison-kinetic-readout.md` derives a tangent metric from the chosen overlap readout and constructs a conditional scalar action

    L = F^2/2 (partial theta)^2 - U A(theta).

It checks coordinate-invariant interactions including derivative vertices. The spacetime identification and scales F,U are supplied. This is a viable method for transporting kinetic and potential data together, not an already normalized neutron action.

### Existing mechanics, with a completed follow-up

`original-interaction-versus-current-rotor-reconciliation.md` shows that an older charge/mass/recoil whole already has kick/drift Hamiltonians, momentum balance and work accounting. The missing step is identifying those operative maps with the current source, not supplying yet another clock.

`canonical-polarization-and-recoil-prior-clues.md` points to the completed successor `shared-recoil-cotangent-binding.md`. The latter supplies a common generalized-body representation of the six-port exchange and rejects a simpler three-dimensional collision architecture. Its header also records a later obstruction to combining that representation's momenta with the old spatial reader. The old proposed comparison must not be treated as still unexecuted.

### Field kinematics is not yet field coupling

`photon-maxwell-adapter.md` constructs an exact conditional polarization adapter, field strengths and Ward pairing for a supplied conserved current. It supplies the spacetime/null frame and allows different energies for the same seed coefficients. It does not fix the matter-field coupling or source current.

`137-curved-overlap-extension.md` admits genuine holonomy and metric-compatible transport but explicitly does not choose a field trajectory or backreaction. It cannot replace the stronger closed feedback model above.

### Nonlinear retained response already exists

`mean-fluctuation-transport-and-context-policy.md` derives the covariance correction to actual same-slot residual composition while retaining all records. `inner-face-localized-mode.md` already tests a separate trial specialization of this response on the AB/BA contrast and distinguishes it from the geometric projector cycle. This is a candidate nonlinear response bridge, not an automatically bound auxiliary particle.

### Geometry called “potential” is not an action

`research/voevodsky/retained-potential-realization.md` supplies the finite folded/pullback realization and its annular collar. It explicitly says its parameter is a geometric deformation, not physical time or an interaction equation. Reinterpreting that completed construction as a potential-energy law would add a new physical identification.

## Specific connection to our current carrier

The belt's derived seam energy already has the form

    H_seam(a) = sum_(i,j) gamma_ij |a_i-a_j|^2,
    gamma_ij = n_i n_j/(n_i+n_j),

with inherited amplitude metric diag(n_i). This has the same quadratic-difference structure as the existing matter/link action at zero link phase.

There is therefore a concrete adapter candidate: transport the source amplitude metric and use the derived gamma_ij instead of guessing new hopping coefficients. The canonical equation must use that metric,

    i n_i dot(a_i) = partial H / partial conjugate(a_i),

or an explicitly equivalent orthonormal frame. Copying the old unweighted stepping rule would not preserve the present operator.

This structural match is not yet a checked adapter. In particular:

1. Include the native alignment terms as well as the within-sector seams; a seam-only graph is not the full retained Hamiltonian.
2. Derive the charged-current and link incidence on those actual operations, retaining their transports and histories.
3. Supply only source-justified filled loops, or explicitly declare new magnetic structure. A graph alone does not choose the magnetic action.
4. Address the closed-graph Gauss constraint and its background/boundary flux. Positive amplitude norm cannot silently be identified with both a neutral belt and a charged proton.
5. Preserve the physical interpretation of the common vacuum and kinetic normalization. The earlier direct electron-gap calibrations failed and are not revived by writing a gauge-covariant action.

## Recommended continuation

Reuse the existing matter/link feedback construction and test an exact weighted source adapter on the actual selected-mode carriers. The initial acceptance gate is equality of the zero-field Hamiltonian and its current response, not a new fitted mass ratio. Only after that should field backreaction and vacuum energies be compared under the same action and boundary conditions.

The search found a substantial existing interaction framework, but did not find an already completed proton/belt-to-that-field-action adapter or a selected physical energy normalization. This is a bounded search result, not a claim that no other relevant research exists anywhere in the repository.
