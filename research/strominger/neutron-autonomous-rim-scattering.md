# Autonomous neutron two-rim scattering

## Implemented result

The two-rim interaction now runs as a time-independent continuum contact, rather than a prescribed temporal pulse or a finite off-diagonal dressing matrix. A moving two-channel field exchanges amplitude with the existing 24-coordinate neutron/bank core. Incoming flux, reflected/transmitted flux, virtual closed channels and the full core state are retained.

Nine checks pass over a 201-energy scan. A separate verifier reconstructs the contact equations and flux from the saved raw fields without importing the solver.

## Model and explicit inputs

The state space is

    [L2(R) tensor C2] direct-sum C24.

Use the previously verified native collective operator

    K=H_native/4+sum seam projectors.

Whiten the inherited metric without changing its pairing. The two columns of W are the normalized actual lower/upper collective rim modes, so W†W=I2. In these coordinates the form is

    E = integral [kappa ||psi'||² + psi† H_lead psi] dx
        + chi† K chi
        + eta ||sqrt(ell) psi(0)-W†chi||².

Both contact diagonals and the transfer terms are retained. This is the positive contact completion recovered from the high-energy branch, not the previous bare off-diagonal Hamiltonian and not an autonomous sum of canonical pulses.

The principal numerical fixture supplies

    kappa=1, eta=2, ell=1, hbar=1,
    H_lead=diag(1/2,1/2).

The lead threshold and these coefficients are explicit model inputs; none is inferred from neutron mass. The incoming state is unit-flux incidence in either rim port with no incoming bound/dark component.

## Conservative boundary equations

Continuity and variation of the form give

    kappa[psi'(0+)-psi'(0-)]=eta sqrt(ell)(sqrt(ell)psi(0)-W†chi),
    E chi=(K+eta W W†)chi-eta sqrt(ell)W psi(0).

The one-dimensional H1 trace makes this a lower-bounded closed contact form and hence a self-adjoint time-independent model. Numerical checks supplement that conservation argument; they do not establish it solely by sampling.

Every propagating channel uses amplitude 1/sqrt(v), v=2 kappa k/hbar. Closed lead channels have imaginary momentum, remain in the equations and carry no asymptotic flux. The solver rejects evaluation exactly at a threshold rather than dividing by zero velocity.

## Exact accessible reduction, with all other records retained

Exact rational Krylov generation from the two actual rim columns yields a five-dimensional core subspace. It intertwines K exactly. The other 19 core directions are retained through their complementary basis and operator.

Thus the primary boundary solve has 26 unknowns (two lead boundary values plus 24 core values), while an independent accessible solve has seven. Both are compared to core elimination. At a decoupled dark eigenvalue, the specified scattering preparation selects the zero-bound-component solution; the dark spectrum is not erased.

Six of the dark directions are zero-energy source-bank modes. Their continued presence is another reason not to call a contact bound-state energy the neutron's rest mass.

## Representative scattering results

Incident port 0; probabilities sum over both spatial directions:

| Total model energy | Reflection | Transmission | Flux into other rim port |
|---:|---:|---:|---:|
| 0.80 | 0.74557149 | 0.25442851 | 0.14092687 |
| 1.13 | 0.14680813 | 0.85319187 | 0.02788415 |
| 2.00 | 0.42103017 | 0.57896983 | 0.01336435 |
| 3.00 | 0.99806464 | 0.00193536 | 0.00283262 |

Other-port flux is a subdivision of reflection/transmission, not an extra probability to add to them. Core residence is reported separately as norm per incoming flux, with dimensions of time in the selected units; it is not permanent occupation probability.

Because the principal two thresholds are equal, its asymptotic port conversion is elastic. A separate supplied unequal-threshold control diag(1/2,3/2) verifies nonzero evanescent-channel amplitude below the upper threshold and actual kinetic-to-internal energy transfer once that channel opens. No physical interpretation is inferred from that control threshold choice.

## Accessible bound levels

The positive contact model has two computed localized levels below the supplied lead threshold 1/2:

| Energy | Binding below threshold | Core norm | Exterior norm |
|---:|---:|---:|---:|
| 0.239564867092 | 0.260435132908 | 0.8201300021 | 0.1798699979 |
| 0.406258480176 | 0.093741519824 | 0.5616888037 | 0.4383111963 |

Their decaying exterior tails are included in normalization and the integrated energy form. These are numerical levels, not interval-certified neutron masses. The scattering preparation does not populate them: bound levels alone do not demonstrate capture from infinity.

## Controls and residuals

- Full S unitarity: maximum residual about 1.94e-15.
- Energy ledger: maximum residual about 1.78e-15.
- Full versus accessible core/flux solves: maximum about 1.80e-13.
- Full versus eliminated scattering matrix: maximum about 1.89e-15.
- Zero contact: perfect transmission and zero core excitation.
- Independent core-basis and lead-phase changes preserve the scattering operator covariantly.
- Altering only kappa from 1/2 to 1 to 2 changes port conversion at E=1.13 from approximately 0.04261695 to 0.02788415 to 0.01626967. The kinetic scale has not been secretly selected by geometry.

These are implementation residuals, not measured uncertainty or rigorous spectral error bounds. No time-dependent packet has been calculated in this step.

## Reproduction and retained outputs

Cached dependencies are available through uv; no network access was required:

```sh
uv run --offline --with numpy --with scipy python research/strominger/checkers/check_neutron_autonomous_rim_scattering.py
uv run --offline --with numpy --with scipy python research/strominger/checkers/verify_neutron_autonomous_rim_scattering.py
```

Outputs under `research/strominger/results/`:

- `neutron-autonomous-rim-scattering.json`: model, exact accessible basis, full scan, controls and bound levels;
- `neutron-autonomous-rim-scattering.npz`: full core matrices, all 201 scattering matrices, boundary/core fields and retained complements;
- `neutron-autonomous-rim-scattering-audit.json`: independent raw-field audit.

No shared scattering or neutron source backend was modified.

## Next distinct task

Derive the energy-bearing memory operator from the actual neutron comparison residual, using the exit-encoder construction recovered from the new high-energy research. That question is not answered by giving the current source bank an arbitrary gap. The present autonomous contact supplies the conservative dynamical setting for testing such an encoder once its stored comparisons are specified.
