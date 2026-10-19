# Reuse assessment: scattering/high-energy and the neutron rim programme

## Main conclusion

Yes: the new branch supplies two especially useful constructions that go beyond our latest finite internal-channel test:

1. an autonomous, energy-conserving continuum contact driven by incoming motion;
2. an isometric memory encoder with a spectrum derived from the comparison residual being stored.

It does not select physical energy units or identify its pentachoron phase-record spectra as neutron masses. Its matrices must not be copied into our different neutron carrier merely because both have retained records.

## 1. Highest-priority reuse: autonomous contact rather than a scheduled pulse

`pentachoron_autonomous_contact_note.md` replaces a prescribed pulse with a time-independent contact form. Its source implementation `ContactModel` retains open and closed native channels, solves full and eliminated junction systems, uses unit-flux normalization, and computes residence time and bound-state normalization.

The inherited positive mismatch gate keeps both diagonal terms and its off-diagonal transfer. Incoming kinetic energy supplies internal excitation. Residence time follows from the chosen dynamics instead of being a hand-picked pulse duration.

For our actual two-rim map W with metric adjoint T and T W=I2, the corresponding candidate is

    L2(R) tensor C2  direct-sum  C24,

with the same neutron/bank core K and a contact term

    eta ||sqrt(ell) psi(0)-T chi||²_(3 I2).

The continuum's internal threshold, kinetic coefficient, contact length and eta must be declared. This is a new continuum extension, not a claim that the old finite two-auxiliary Hamiltonian already had autonomous encounter motion.

At ell=1 its boundary blocks are

    eta [[I2,-T],[-W,W T]].

Unlike our previous bare off-diagonal contact, this is a positive form. Its diagonal completion changes the model and must not be dropped when comparing energies.

Eliminating the retained core gives

    R(E)=T(K-E)^-1 W,
    V_eff(E)=eta*ell*[I2+eta R(E)]^-1,

away from elimination poles. This reuses the FULL two-rim response already calculated, including its off-diagonal transfer and all visible poles. Near a singular elimination denominator, the full block solve remains the appropriate primary calculation, as in the new source code.

### Fresh compatibility checks

A new dependency-free checker used our current neutron matrices to verify:

- inherited rim normalization and weighted adjoint;
- rank-two positive contact form and all four boundary blocks;
- exact full-core versus two-rim-response elimination at six rational cases.

Thus this is an executable algebraic attachment, not only an analogy. No full neutron continuum scattering calculation was performed in this review.

## 2. Particularly relevant to register spectra: energy-bearing memory

`pentachoron_exit_gate_note.md`, sections 5–7, constructs a residual map D, partial isometry W, retained native projector N and a memory operator M such that

    W† M W=D†D,
    ||Nz||²+||Wz||²=||z||².

The reversible gate acts on native records PLUS memory. For ready memory, the stored energy exactly equals the removed comparisons' quadratic energy. This is much closer to deriving a register spectrum from its actual task than assigning every register an arbitrary elementary gap.

However, the note also computes the energy change of the OTHER native terms after encoding. That change is not generally zero. An autonomous exit coordinate supplies the necessary energy exchange; the memory identity alone is not full energy conservation.

Useful next task for the neutron is therefore to identify its actual comparison residual D, construct an isometric encoder for that residual, and calculate the induced memory operator and remaining native-energy change. Do not copy the pentachoron memory eigenvalues or treat residual storage as a source-selected neutron vacuum gap.

## 3. Kinetic and deformation machinery worth retaining

- `pentachoron_relativistic_kinetics_note.md` implements a genuine spectral square-root kinetic operator, retaining its nonlocal resolvent correction. Replacing only a wave number in a local boundary condition is explicitly rejected. This is reusable if the neutron contact is later given such kinetics, but rho=mc²/epsilon remains supplied.
- `quantum_strain_note.md` carries a single strain coordinate and its metric through every topology. Its unitary measure changes retain both metric potentials and endpoint trace factors. This is a useful template for a deformable neutron interface; its pentachoron strain metric and material connection are not automatically the neutron's.
- The strain and time-resolved diagnostic notes distinguish coherent amplitude interference, signed currents, conditional populations and actual outgoing flux. They rule out multiplying stage probabilities or relaunching a normalized rare subbranch as the entire input.

These are dynamical improvements, not merely alternative numerical values for a register gap.

## 4. Important controls inherited from the new branch

- A bound level below an incoming threshold does not prove capture from an asymptotic scattering state under a fixed self-adjoint Hamiltonian. Additional outgoing resources or a different preparation are needed for permanent formation.
- Transient connected occupation is not an asymptotic product probability.
- Phase-record direct sums are not tensor products of independently occupied physical particles.
- Physical scales remain uncalibrated. The displayed epsilon=hbar=m=ell=1 and rho=1 are model choices. No neutron mass or SI conversion can be imported from them.
- The quantum-strain numerical results still have continuum/high-closed-mode sensitivity; precision residuals are not convergence or experimental error bounds.

## Verification performed here

```sh
python research/strominger/checkers/check_high_energy_contact_reuse.py
```

Four checks passed, including six exact Schur comparisons. The autonomous-contact archive's eight manifest entries and the exit archive's six entries were freshly hash-checked, together with the autonomous model's nested source-script/receipt pins.

Receipt: `research/strominger/results/high-energy-contact-reuse.json`.

The archived contact solver was inspected. It was not executed: NumPy, SciPy and SymPy are absent from the default Python environment. Historical scattering and strain numbers are reported from their notes, not freshly reproduced. No new scattering source file or archive was modified.

## Recommended next implementation

Start with the autonomous two-rim scattering attachment using the existing exact R(E), a full-block solver, all closed modes and a common reference. Test norm flux, energy exchange, frame covariance and full versus eliminated solutions before adding strain or square-root kinetics.

In parallel with that bounded implementation, pursue the exit-memory construction as the most relevant new clue toward a task-derived register energy. It addresses what the bank stores and what energy it must carry, rather than trying to infer a rest offset from recurrence or count.
