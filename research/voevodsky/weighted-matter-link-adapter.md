# Exact weighted carrier adapter to the existing matter/link feedback law

## Result

The actual phase-selected proton and belt modes now admit an exact weighted adapter to the matter/link interaction already constructed in Nima's `record-gauge-feedback-loop.md`.

| Source sector | Selected amplitudes | Native alignment links | Seam links |
|---|---:|---:|---:|
| Proton | 12 | 24 | 0 |
| Belt | 18 | 18 | 21 |

The zero-field operator is exactly the restriction of the previously retained 36-dimensional Hamiltonian. Native alignment was included; this is not a seam-only replacement model. The remaining 24 proton and 18 belt carrier directions remain identified as the orthogonal complements rather than being asserted absent.

We also tested nontrivial field backreaction with the inherited weighted metric. No fitted hopping coefficient or independent seam occupation register was introduced.

## 1. Prior construction reused

This implements the next adapter identified in `prior-field-action-search.md`. It reuses:

- `research/nima/record-charge-and-phase-transport.md`: phase-covariant matter energy and current;
- `research/nima/record-gauge-feedback-loop.md`: dynamical link variables, Gauss preservation and exact-subflow stepping;
- `research/nima/checkers/check_record_gauge_feedback.py`: the existing feedback algorithm, generalized here to the actual weights.

The old four-vertex fixture is not renamed as a particle. Its interaction law is applied to new source-derived graphs with checked intertwining maps. The closed-graph background limitation was already stated in that prior work and is not claimed as a new discovery.

## 2. Exact zero-field adapter

For each retained triangle mode v_i write its coefficient as a_i. Let V embed these amplitudes in the original carrier, and n_i=||v_i||^2 in the physical metric. The amplitude inner product is diag(n_i).

Using the actual stores, the checker verifies

    V^sharp V=I,
    H V=V K,
    [H,V V^sharp]=0.

The selected sector is therefore invariant. Its coefficient operator is precisely

    K=M^(-1) L, M=diag(n_i),

where L is a symmetric weighted graph Laplacian. Every positive edge weight is recovered from the actual off-diagonal coefficient:

    gamma_ij=-n_i K_ij=-n_j K_ji.

For native-alignment links, n_i=n_j and gamma_ij=n_i/4. For belt seams,

    gamma_ij=n_i n_j/(n_i+n_j).

Reassembling these edges reproduces K entry by entry. These weights are not adjusted to a desired spectrum or mass.

## 3. The reused field extension

Give each oriented graph link a phase A_e, U_e=exp(i A_e), and conjugate electric variable E_e. Use the electric-only specialization of the prior law:

    H_total = sum_e gamma_e |a_b-U_e a_a|^2
              + beta/2 sum_e E_e^2.

The magnetic coefficient is zero. No arbitrary filled loops or magnetic cell structure is inserted.

Because the source amplitude metric is not the identity, the canonical matter equation is

    i n_i dot(a_i) = partial H/partial conjugate(a_i).

It gives density and oriented current

    rho_i=n_i |a_i|^2,
    J_e=2 gamma_e Im(conjugate(a_b) U_e a_a).

For incidence B with -1 at the tail and +1 at the head,

    dot(rho)+B J=0,
    dot(A)=beta E,
    dot(E)=-J.

Thus B E-(rho-background) is conserved for a fixed background. The checker verifies the current as the derivative of the energy with respect to A, the matter continuity equation, Gauss conservation and total instantaneous Hamiltonian power balance using exact arithmetic.

Time-independent gauge changes transform a_i by exp(i chi_i) and U_ab by exp(i chi_b) U_ab exp(-i chi_a). Exact root-of-unity fixtures test energy, current, density and derivative covariance. The general covariance follows algebraically from the displayed difference term. A physical time-dependent gauge presentation would also need its temporal potential.

## 4. Weighted feedback stepping

For one link at fixed U, the nonzero matter-generator eigenvalue is

    lambda_e=gamma_e(1/n_a+1/n_b).

The update uses exp(-i lambda_e dt), not the old unweighted 2*kappa frequency. Its electric update is the change in the target weighted density. This preserves the link's Gauss balance.

Electric drift and forward/reversed half-step link sweeps form the same reversible second-order composition as the prior implementation. Unwrapped link phases are retained. The test schedule is a declared integrator schedule; it is not asserted to reproduce the source's original whole-Tick chronology. No native source history is erased or identified with this new stepping schedule.

The numerical fixture uses beta=0.6 from the prior feedback example and a model duration 0.25. Beta and model time are supplied, not physical calibrations.

| Test | Proton | Belt |
|---|---:|---:|
| Maximum energy error, dt=0.01 | 4.78e-6 | 5.00e-6 |
| Maximum energy error, dt=0.005 | 1.20e-6 | 1.25e-6 |
| Maximum Gauss error | <1e-13 | <1e-13 |
| Reversal error | <1e-13 | <1e-13 |

The factor-four energy-error reduction is consistent with the second-order scheme. Both electric and phase variables change nontrivially. Finite-step energy conservation is not claimed exact. The tests also compare gauge-related trajectories.

## 5. The common-vacuum gate is explicit

The fixture chooses a positive fixed background compatible with its initial matter and electric field. On any closed incidence graph,

    sum_i (B E)_i=0,

so Gauss imposes

    sum_i rho_i=sum_i background_i.

With positive-total background, empty matter cannot satisfy the same constraint for any E. Changing the background between the particle and vacuum would change the model, not calculate a vacuum-subtracted energy in one physical system.

This is the prior feedback model's known limitation, now explicitly checked on the actual particle graphs. A signed-species construction, physical boundary flux, or another source-supported Gauss sector would be needed for a common vacuum. Their charge assignments and energy costs must be retained rather than silently supplied.

In particular, conserved positive amplitude norm is not already measured electric charge. This adapter does not identify a charged proton and a neutral neutron under one electromagnetic field law.

## 6. Scope of the completed step

Completed:

- exact source-selected mode embedding and zero-field operator equality;
- derived graph weights for native alignment and seam terms;
- weighted current/continuity/Gauss identities;
- nontrivial reversible classical matter/link feedback and gauge controls.

Not completed:

- a physical identification of the link field, its normalization or its background;
- a quantum vacuum and particle creation/charge sector construction;
- a magnetic action selected by native filled-loop data;
- the field interaction on populated phase-orthogonal carrier sectors;
- a neutron rest-energy or atomic-mass calculation.

This is a substantive source adapter to an existing field interaction, not another generic Hamiltonian proposal. It advances the missing map while retaining the prior action's explicit physical assumptions.

## Verification

    python research/voevodsky/checkers/check_weighted_matter_link_adapter.py

Results: `research/voevodsky/results/weighted_matter_link_adapter.json`.

Source identities and finite current/gauge controls are exact rational/algebraic calculations. Feedback trajectories use explicitly tolerance-checked complex floating arithmetic. The prior implementation was inspected and its law reused; its original NumPy checker was not separately rerun in this step.
