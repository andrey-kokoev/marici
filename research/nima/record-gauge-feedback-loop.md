# A closed matter/link feedback trial

## State and action

Extend the four-state transport trial with a real phase A_e on each of six
oriented links and its canonical conjugate E_e. Let U_e=exp(i A_e). Let B be
the vertex-link incidence matrix and C the oriented triangle-link matrix.
The four triangles obey B C^T=0. They are an explicit choice of filled loops
for this trial; fibration alone has not supplied a cell complex.

In model units choose

    H = sum_e kappa_e |psi_b - exp(i A_e) psi_a|^2
        + (beta/2) sum_e E_e^2
        + mu sum_f (1-cos((C A)_f)).

All coefficients are declared inputs. Canonical complex matter dynamics and
{A_e,E_f}=delta_ef give

    i dot(psi) = dH/d(conjugate psi),
    dot(A) = beta E,
    dot(E) = -J - mu C^T sin(C A),
    J_e = 2 kappa_e Im(conjugate(psi_b) exp(i A_e) psi_a).

Thus matter drives the link field, which changes the phase used by subsequent
matter transport. This closes an explicit finite Hamiltonian feedback loop.
The action is a lattice gauge-inspired trial, not derived from the137 records.

## Continuity and constraint

The matter equation gives dot(rho)+B J=0 for rho=|psi|^2. Since B C^T=0,

    d/dt [B E - (rho-rho_background)] = 0

for a static background. The closed graph has zero total divergence, so positive
matter norm needs an equal total background for this Gauss constraint. The
fixture uses uniform rho_background and initializes E=B^T(rho-background)/4.
Introducing multiple signed charge species would be another construction.

The dynamics is in temporal gauge. Time-independent local phases transform
psi_v by exp(i chi_v), A by A+B^T chi, and leave E unchanged. The Hamiltonian,
Gauss constraint and trajectories transform consistently. A full time-dependent
gauge presentation would restore the temporal potential as a constraint multiplier.

## Numerical method and checks

The checker uses exact subflows: electric drift, magnetic kick, and individual
matter-link hopping steps. A hopping step integrates the two-amplitude unitary
rotation exactly and updates its link E by the target density change, preserving
Gauss. A symmetric composition is reversible and second-order accurate; it
preserves Gauss and matter norm to numerical tolerance rather than conserving
the full Hamiltonian exactly at finite step size.

Over one model time unit, max energy errors are7.90767855e-6 at dt=.01 and
1.97679691e-6 at dt=.005, giving the expected factor-four improvement. The electric
link vector changes by norm1.38737652 and phase vector by0.466641681. Gauge-related
initial conditions yield gauge-related trajectories. Reversing100 steps restores
the input within1e-10. All current/force finite-difference checks pass.

## What remains to connect

The previously scalar source/field interface now has an explicit dynamical
return path and a conserved constraint. This supplies a concrete test fixture
for feedback. It does not determine its coefficients, physical time or electric
charge unit. The137-comparison model still requires an adapter identifying its
record variables, mismatch observable and evolution with this matter/link action.
No1/r continuum law or electromagnetic coupling value has been derived.

The next substantive synthesis is that adapter or a source-derived alternative
to this trial Hamiltonian. Repeatedly choosing additional gauge-theory structure
would not establish the carrier origin of the action.

## Verification

    uv run research/nima/checkers/check_record_gauge_feedback.py

Tests the cell boundary identity, Hamiltonian current derivative, Gauss constraint,
total matter norm, time-independent local gauge covariance, second-order energy
error, nontrivial field feedback, and reversible stepping. Model coefficients
are fixed before tests; no measured constants enter.
