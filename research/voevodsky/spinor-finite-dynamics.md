# Finite-amplitude dynamics and retained observables — iteration 4

## Fresh-state continuation

This continues the freshly read tangent checker and the fixed-lead Hamiltonian. The numerical experiment uses the first ground sector; the checked source rotations relate the other three. No bath, hopping between lead sectors, or quantization is added.

## Nonlinear validation

Integrate the full normalized projective vector field and cyclic angle velocities, keeping the three independent lead momenta exactly constant. Use an adaptive DOP853 integrator and compare with the independent matrix-exponential solution of the analytic tangent generator.

Two fixtures are tested at amplitudes 0.002 and 0.001:

1. A real direction in the slow matter eigenspace, with unchanged lead flux. Duration is one linear slow period, **1027.99699881** clock units.
2. A lead-momentum perturbation with matter initialized at its linearly displaced center -H^-1 M delta ell. Duration is 100 clock units.

| Fixture | Maximum tangent error, amplitude 0.002 | Amplitude 0.001 | Ratio |
|---|---:|---:|---:|
| Slow matter mode | 1.87523e-4 | 4.68512e-5 | 4.00252 |
| Momentum-driven drift | 9.66819e-4 | 2.41585e-4 | 4.00198 |

Errors are Euclidean norms in the documented local canonical/projective and unwrapped-angle coordinates, not invariant distances between states. Their quadratic scaling is the relevant check. Tenfold tighter solver tolerances change the smaller-amplitude trajectories by at most 8.53e-11 and 9.98e-12, respectively. Norm is imposed by the projective chart, not tested as an independently integrated conservation law here; the earlier splitting tests supply that check. Computed energy variation is at roundoff in these small fixtures, which is not an exact conservation certificate.

## A nonlinear angle displacement survives a slow matter cycle

For the slow fixture, the tangent prediction returns the lead angles to their starting values after one linear period. The nonlinear trajectory instead accumulates first-angle displacements approximately

    -0.000187522 at amplitude 0.002,
    -0.0000468512 at amplitude 0.001.

This is a second-order accumulated cyclic-angle response, not a change of the conserved flux sector. The evolution was stopped at the linear period; an exactly closed nonlinear matter orbit is not established. Therefore this observation must not be advertised as a Berry phase of a proved closed orbit.

For the momentum fixture, the first-angle displacement at amplitude 0.001 is 0.09617294, compared with the tangent prediction 0.09631586. The discrepancy scales quadratically with amplitude as expected.

## State and observable contract

The classical state consists locally of:

- normalized matter amplitudes modulo common phase, or their nonorthogonal ground-coordinate representation a with a†G a=1;
- three cyclic lead holonomies theta modulo 2pi (or retained real lifts);
- three independent conserved lead fluxes ell, with the fourth fixed by sum ell=-1.

Observables and retained histories must be distinguished:

- **Site density:** rho_i=|psi_i|^2, invariant under common phase and independent of the chosen ground basis.
- **Internal electric field:** E=B_internal^T(-rho-ell)/4, determined by density and the retained lead assignment.
- **Lead electric field:** ell itself, not its instantaneous static optimizer.
- **Energy:** the fixed-lead Hamiltonian; its electrostatic lower envelope is not the trajectory Hamiltonian.
- **Relative matter coherences and currents:** computed with the intrinsic source connection. Their gauge-fixed component values must be transported together with that connection under changes of gauge.
- **Exterior-loop holonomy:** exp(i theta_i), gauge invariant for the corresponding closed lead/internal path. The real theta_i history additionally retains winding information.
- **Common matter phase:** absent from CP^3. A lifted amplitude history is required for the source binary rotation sign; absolute dynamical phase depends on the fixed-charge Hamiltonian extension and gauge convention. Neither density nor a cyclic lead angle should be substituted for it.

The lead angles do not affect the current Hamiltonian because there is no coupling on exterior cycles. They remain physical cyclic coordinates; deleting them loses trajectory information and their conjugate conserved fluxes.

## Verify

    uv run --with numpy --with scipy python research/voevodsky/checkers/check_spinor_finite_dynamics.py

Results: `results/spinor_finite_dynamics.json`. This is numerical finite-amplitude evidence, not a global dynamical theorem or a quantum spectrum.

## Remaining construction work

Consolidate the state-space, Hamiltonian, symmetry and observable contracts into one entry point and run the complete dependency/checker chain freshly. Any subsequent proposal for inter-sector transitions must identify an actual new lead or boundary interaction; it cannot arise by relabeling the four classical minimizing rays as orthogonal quantum states.
