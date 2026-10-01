# Rotor action: obtaining1836 energy units is not obtaining a unit-charged particle

## Forward-realization scope

The finite path-incidence graph is freshly reconstructed. It is connected, so an
explicit action can now be tested on it instead of adding another controller.
The rotor variables, action and external coupling below are candidate physical
inputs, not consequences already established by the carrier. Their reductions
are derived, and no observed mass value fixes a coefficient.

Take N=1836 compact angles theta_s with integer conjugate momenta n_s, and positive
charging inertias C_s. Use hbar=1. An isolated reference rotor has C_e=1 and
first excitation energy1/2. "Capacitance" below means the coefficient in this
rotor action; conversion to an electrical capacitance and physical units would
require the microscopic coupling and normalization.

## Phase locking: a connected Josephson-type action

Consider

    L = (1/2) sum_s C_s (dot(theta_s)-A_0)^2
        - J sum_(s,t) [1-cos(theta_s-theta_t)].

Every rotor has one unit of the same external U(1) charge normalization as the
reference. In the IDEAL phase-rigid reduction theta_s=phi, the action becomes

    L_eff = (sum_s C_s)/2 * (dot(phi)-A_0)^2.

The common phase has period2*pi, so its conjugate total charge Q is integer.
At A_0=0 its charging energy is

    E_Q = Q^2/(2 sum_s C_s).

For equal C_s=C_e, the first unit-charge energy is1/N times the elementary gap,
not N times. Inertias add for a common phase. This is the constrained rigid
limit, not a claim that finite-J phase slips and relative-mode zero-point effects
have been computed or vanish exactly.

## Charge locking: a different gauge action

Let B be the vertex-edge incidence matrix, with one +1 and one -1 per edge.
Introduce auxiliary temporal gauge fields a_e and instead use

    L = (1/2) (dot(theta)-B a-A_0*1)^T
              C (dot(theta)-B a-A_0*1).

Varying a enforces B^T n=0. On the connected graph, integer momenta satisfy
n_s=k for every s. This is the previously sought equality constraint, now as
the Euler-Lagrange/Gauss equation of an explicit action. But introducing the
auxiliary gauge fields is still a new physical law, not inferred from the graph.

The gauge-invariant compact coordinate is Phi=sum_s theta_s modulo2*pi. Its
primitive character is exp(i Phi), and

    C_eff = 1/(sum_s 1/C_s),
    L_eff = C_eff/2 * (dot(Phi)-N*A_0)^2,
    E_k = (k^2/2) sum_s 1/C_s,
    Q_external = N*k.

For equal inertias and k=1 this gives precisely N elementary energy units.
It ALSO gives N elementary units of external charge. The same common U(1)
rotation which shifts each theta_s by lambda shifts Phi by N*lambda.

## Energy and charge must be tested together

| Candidate | First nonzero energy/reference gap | External charge magnitude |
|---|---:|---:|
| Phase-rigid collective rotor |1/1836|1|
| Gauss-locked collective rotor |1836|1836|
| Desired proton-like identification |approximately1836|1|

Thus these two simple actions do not supply both quantities under the common
external-coupling assumption. The sign of charge does not repair the magnitude.
A charging excitation has not otherwise been shown to be a relativistic rest-mass
pole, fermion or baryon.

Writing Phi/N does not by itself repair the charge. On the original rotor torus,
exp(i Phi/N) is not single-valued under shifting just one theta_s by2*pi. Changing
the external action to assign each microscopic rotor charge1/N would give a
unit-charged collective mode, but changes the coupling relative to the elementary
reference. It is new charge-assignment data, not a coordinate convention.
A quotient global symmetry could motivate such assignments, but its joint action
on the elementary sector would need to be constructed too.

There is an important alternative: neutral internal comparison channels plus a
separate unit-charged core. This is not excluded by the test. It returns the open
problems of the core's dynamics, the internal energy law and its normalization
relative to the elementary charged excitation. The comparison channels cannot
be assumed charged and neutral at different steps of the same argument.

## Coefficient hostile

Keeping the Gauss law and all typed relabellings, choose C=1 on arrow channels
and C=1/2 on state channels. The primitive energy ratio becomes1944 while its
external charge is still1836. Gauge invariance does not fix the charging form.
Common charge locking therefore does not yet protect the proposed numerical
energy ratio even before the particle-charge mismatch is addressed.

## Verification and residual

    python research/nima/checkers/check_mass_rotor_action_charge.py
    python research/aspect/scc/scc.py check nima-mass-rotor-action-charge

All energy ratios and finite integer-charge windows are checked exactly. The
continuum action reductions follow the displayed variational constraints;
finite checks regress their algebra, not a laboratory realization or a finite-J
approximation. Report: `results/mass-rotor-action-charge.json`.

Progress: an explicit variational mechanism now yields the equality constraint
and its collective energy law. Remaining: SOURCE the action and microscopic
external charges together, rather than selecting whichever normalization yields
the target mass. Static carrier incidence alone does not make that selection.
