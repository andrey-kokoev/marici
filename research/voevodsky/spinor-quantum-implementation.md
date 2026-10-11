# Quantum construction and physical acceptance contract — iteration 5

## Status

**Completed:** an explicit conditional quantization and an exact ideal endpoint-rotor architecture implementing relative hard flux, with a unitary equivalence between their physical Hamiltonians.

**Not completed:** a platform-specific physical realization, measured calibration, or microscopic derivation identifying this model with the original physical particle. No physical platform has been selected or tested. An algebraic Hamiltonian specification cannot certify those missing facts.

This distinction supersedes any reading of “implementation” as a completed experimental device. The endpoint architecture changes the independent degrees of freedom rather than deriving exact pinning from finite cosine stiffness.

## Completed mathematical construction

The chosen model uses hbar=1, periodic lead rotors, one matter occupation and operator-square electric energy. Its Hilbert space is

    C^4 tensor l2({ell in Z^4 : sum ell=-1}).

Its exact blocks are

    H_ell=K+(beta/4)diag(ell)
           +[5 beta||ell||^2/8+beta/8+eta/2]I.

At beta=3/5, eta=1/5 the global ground energy and first excitation gap are

    E0=(59-sqrt(1609))/40 = 0.4721914439934211,
    gap=(sqrt(1609)-37)/40 = 0.0778085560065790.

The ground multiplicity is four. An analytic lower bound excludes all other integer-flux blocks without a cutoff. These are model-unit energies, not physical mass predictions.

The endpoint parent uses gauge generators G_i=n_i+ell_i+N_i, assisted transfers |j><i|R_i R_j^dagger and charging coefficients beta/8 for endpoint momenta and beta/2 for lead momenta. Relative loops telescope identically; intrinsic source Wilson phases remain. The physical basis |i;-ell-e_i;ell> is unitarily identified with the reduced basis |i>|ell>.

The independent-link parent instead has second-class face/tangency constraints. It does not contain a normalized exact-flat state in its ordinary continuous-link Hilbert space. Its harmonic stiff limit has shrinking flux uncertainty but diverging electric/zero-point energy, and a finite first anharmonic vacuum shift. No full strong-coupling convergence theorem was proved.

## Exact finite encoding for a concrete simulation target

Because lead flux is conserved, the direct sum of the four ell=-e_i blocks is an exact invariant 16-dimensional subspace. It contains the global ground and first excited energy, and can be encoded in four qubits: two for the flux label and two for matter.

This is not an arbitrary truncation error estimate: states initially in these four blocks remain there under the exact Hamiltonian. It does **not** represent the whole rotor theory or observables that shift to other flux sectors. A simulator of this finite restriction would validate encoded dynamics, not establish a microscopic physical U(1) constraint mechanism. No device circuit or experimental gate fidelity is supplied here.

## Physical acceptance tests

| Obligation | Required evidence | Failure control | Current status |
|---|---|---|---|
| Endpoint factorization | Identify physical shared endpoint variables; show that links have no independent cycle coordinate within the stated operating domain | Add an independent phase on one link; its face product changes | Unverified physically |
| Assisted hopping | Derive or calibrate all six charge-compensated transfers, source phases and onsite terms | Bare matter hopping changes two G_i values | Unverified physically |
| Charging metric | Obtain endpoint/lead quadratic coefficients and any cross-capacitance terms from the actual platform; state physical time/action units | Change coefficients while retaining gauge symmetry; spectrum changes | Unverified physically |
| Sector preparation | Prepare sum n=0, sum ell=-1 and G_i=0 with stated fidelity; report preparation/measurement resources | Gauge-breaking perturbation leaves the admitted sector | Unverified physically |
| Error and extra-mode control | Bound parasitic modes, imperfect transfers and evolution error over a declared duration | Independent-link mode defeats the structural flatness identity | Unverified physically |

The first two algebraic failure controls are included in the new checker. They do not substitute for physical measurements.

For a bounded Hamiltonian error V with ||V||<=delta_H on an admitted invariant space, Duhamel's formula gives

    ||U_actual(t)-U_ideal(t)|| <= |t| delta_H/hbar.

If the ideal dynamics preserves a projector P and the initial state lies in P, the leakage probability is at most (|t|delta_H/hbar)^2 (capped at one). This is a conditional acceptance bound, not a numerical error budget until delta_H is established. For unbounded rotor perturbations one needs an energy-domain estimate instead of asserting an operator-norm bound.

If three implemented unitary relative edge operators differ from their ideal factors in norm by at most delta_U each, the triangle product differs from I by at most 3 delta_U, by a telescoping product estimate. Nonzero tolerance certifies approximate—not exact—flatness. Independent scalar source phases must be compared separately with the sourced Wilson target.

## Fresh verification

    uv run --with sympy python research/voevodsky/checkers/check_spinor_quantum_implementation.py

Receipt: `results/spinor_quantum_implementation.json`.

All four quantum-stage checkers were freshly run. The runner verifies result bindings, the invariant finite encoding, exact gap, and algebraic failure controls. The classical construction receipt is retained and hashed, not re-executed by this quantum runner. No laboratory or repository-wide closure is claimed.

Detailed sources:

- `spinor-quantum-leads.md`: representation, ordering and full-lattice ground bound.
- `spinor-hard-flux-parent.md`: multiplier action, Dirac reduction and quantum obstruction.
- `spinor-stiff-flux-limit.md`: harmonic localization cost and first anharmonic correction.
- `spinor-endpoint-constructor.md`: structurally flat quantum parent and exact intertwiner.

## Nonredundant continuation

Choose and justify a physical platform, or construct an explicitly labelled digital simulation of the invariant 16-dimensional model. Then derive its actual Hamiltonian and test the acceptance conditions above. This requires new physical/design inputs; rerunning the ideal algebra cannot complete the physical claim. Quantization of this stated candidate is complete, while physical implementation remains an open task.
