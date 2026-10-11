# Prior clues for the collective active sector, charge and recoil

## Strongest directly relevant findings

### 1. The multiport mechanical obstruction was already partly known

`multiport-mechanical-binding-gate.md` tests ONE common scalar carrier body
and six scalar partners under one metric-preserving linear map. Collision
normals would require off-diagonal overlaps C_ij=v_i*v_j, hence zero tetrads.
The actual bound ports AB,BC,AD,DB give -5/29282, ruling out that architecture
for every positive mass assignment.

Fresh rerun: 35 exact checks pass, including the original source adapter.
Our newer six-dimensional irreducibility result extends the understanding;
it should not be presented as the first discovery that local collision
readings fail to assemble into a global mechanics.

### 2. The real-phase obstruction and its complex extension already exist

`137-gauge-adapter-and-complex-lift.md` proves that any real norm-preserving
continuous symmetry commuting with all labelled reflections vanishes on
the active comparison space. It then supplies a complex lift with global
phase symmetry and Hamiltonian pulses for those SAME comparisons.

This is a clear clue for charge: the absence of a common real linear scalar
or a second real quadratic invariant does not settle the complex phase
question. Complexification adds real degrees of freedom and canonical
structure; it is not a concealed property of the original real six-space.

The same note rejects a product-of-two-vectors carrier because even one
comparison raises its tensor rank. Retaining the full tensor state is a
prior positive design requirement, not a new option to invent now.

### 3. Local endpoint phase covariance has a precise metric obligation

`137-local-endpoint-phase-adapter.md` keeps the full complex tensor and
uses x_ab -> exp(i(chi_B[b]-chi_A[a])) x_ab. Features AND the Gram transform
with it; record amplitudes are neutral in that adapter. Holding the
non-diagonal Gram fixed fails covariance.

Time-dependent transport has the connection term

    H' = S H S^-1 + i dot(S) S^-1.

Crucially, this frame change preserves Gram loop phases. It is not itself
physical curvature or a new interaction force.

### 4. A collective state/phase backreaction Hamiltonian is already built

`137-comparison-phase-backreaction.md` puts the original comparison
mismatches and a dynamical overlap phase in ONE action:

    H=(kappa/2) sum_i |delta_i|² + beta p²/2 + mu(1-cos(theta)),
    delta_i=w_i-u_i(theta)^dagger q.

Its comparison contribution drives the conjugate phase momentum through

    dot(p)_comparison = -partial_theta[(kappa/2) sum_i |delta_i|²].

The changing phase in turn changes the comparison features. H and the
global complex-phase norm charge are conserved. This is an existing
whole-system backreaction example, not six independently chosen body masses.

Fresh rerun passes. At dt=.01 its maximum energy error is about 1.29e-10
and global norm error about 5.07e-11. Those are numerical convergence checks,
not exact formal analysis. The action, square-root frame, one-phase reduction
and kappa,beta,mu are declared choices. Its theta changes an overlap holonomy;
it has not been identified with the current Hamiltonian witnessing angle.
It is also not the original ordered reflection schedule, so its dynamics
must not silently replace that schedule.

### 5. Collective charge can be a quotient character, not a slot sum

`mass-primitive-quotient-charge.md` constructs a faithful collective U(1)
character on a connected rotor gauge quotient. It distinguishes that
primitive quotient action from the degree-N diagonal microscopic action.
Together with an elementary opposite character it gives joint charge
Q=k-n_e. Mass/inertia normalization and particle-sector protection remain
separate in that model.

This supplies a positive structural clue: decide which symmetry acts on the
whole and its quotient before identifying a coordinate sum with charge.
It belongs to the declared many-rotor/Gauss model, not yet our six-direction
exchange sector. The checker was not rerun during this search.

## A composition warning that matters for witnessing

`exchange-shared-leg-composition-gate.md` and
`labelled-exchange-experiment-compiler.md` distinguish native path composition
from chronological addressed exchange. The exchanges fail strict shared-leg
factorization on rooted rectangles, while preserving ordered event histories.
The existing compiler deliberately retains native witnesses AND instrument
events rather than equating every native face with an identity pulse.

Thus a nontrivial exchange response around a returned witnessed reading is
not automatically a contradiction. But the actual native witness and the
attached event action must both remain present; endpoint agreement does not
identify their composition laws.

## Best next use, without inventing another model

The closest positive lead is the EXISTING comparison-state/overlap-phase
backreaction model, together with its full tensor and endpoint-phase adapter.
Before importing its force law, compare its phase with the present retained
witnessing phase:

- Is the latter only a frame rotation transporting fixed overlaps?
- Or does a source operation change an invariant overlap/holonomy that can
  enter the existing mismatch Hamiltonian?

This distinction matters: pure phase-covariant re-presentation and independent
curvature are explicitly different in the prior work. Identifying them by the
common symbol theta would manufacture a coupling rather than recover one.

The task is therefore an actual phase/operation identification using those
existing constructions, not a new oscillator, per-port mass assignment or
external measurement model.

## Fresh commands

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_multiport_mechanical_binding.py
    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_137_phase_backreaction.py

Both pass. Other listed sources were inspected, not all independently rerun.
