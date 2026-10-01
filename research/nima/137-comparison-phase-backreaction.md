# Phase backreaction from the137 comparison mismatches

## Trial action directly on comparison variables

Retain a complex carrier q in C16 and137 complex records w_i. Let one independent
overlap phase theta vary in G_A(0,1)=exp(i theta), with its conjugate entry,
and let G_B=10I+J remain fixed. The positive tensor metric is
K(theta)=conjugate(G_A(theta)) tensor G_B.

Choose the positive square-root frame and set

    u_i(theta)=sqrt(K(theta))*v_i / sqrt(v_i^dagger K(theta) v_i),
    delta_i=w_i-u_i(theta)^dagger q.

Introduce one canonical rotor momentum p and the trial Hamiltonian

    H=(kappa/2) sum_i |delta_i|^2 + beta*p^2/2 + mu*(1-cos(theta)).

This puts the actual137 comparison records and curved metric in one dynamical
model. The simultaneous quadratic comparison penalty, canonical frame, single
phase reduction, and constants kappa,beta,mu are explicit choices. The rotor
potential uses a triangle holonomy phase in this one-edge fixture. They are not
selected by the fibration architecture or by the137 normalization argument.

## Coupled equations

With U having rows u_i^T and canonical complex dynamics:

    dot(q) = i*kappa*U^T delta/2,
    dot(w) = -i*kappa*delta/2,
    dot(theta) = beta*p,
    dot(p) = kappa*Re[delta^dagger (dU/dtheta)^* q] - mu*sin(theta).

Here delta=w-conjugate(U)q and star in the derivative term denotes entrywise
conjugation, matching the row convention. The comparison term is exactly
-minus the phase derivative of mismatch storage. Thus comparison state drives
the phase; the phase changes the comparison directions and later state updates.

Hamiltonian dynamics conserves H and the global phase charge ||q||^2+||w||^2.
The latter is distinct from H. No full local gauge constraint is asserted for
this single-phase canonical reduction. It is not the earlier externally selected
sequence of reflection exchanges; their stationary1/137 result cannot simply
be transferred to this coupled Hamiltonian.

## Numerical fixture

Use kappa=.3, beta=.7, mu=.2, theta(0)=.4, p(0)=.1, initially empty records,
and a seeded complex carrier vector. The initial comparison force is
-0.00723394143802 and rotor force -0.0778836684617. After one model time unit,
theta=0.439384847737, p=0.0124910033769, and record norm=0.195076296875.

An RK4 test at dt=.02 and .01 gives maximum Hamiltonian errors4.14446e-9 and
1.29113e-10, and global norm errors1.61704e-9 and5.06740e-11. The phase derivative
uses centered differences of the normalized feature frame. An independent
finite difference of total H confirms the force. The action has no explicit
time dependence, so its exact equations conserve H; the quoted errors concern
the numerical integration and derivative approximation.

## Incremental result

The comparison model now has a concrete closed phase/state backreaction fixture.
Previously, curved phases were static parameters and the closed gauge dynamics
lived in a separate four-site transport trial. This construction uses the137
mismatch variables directly. It still leaves action selection, full local gauge
completion, physical charge and clock, and coefficient normalization open.
In particular changing kappa relative to beta or mu changes the interaction
without altering the count137. No physical alpha or decimal tail is fixed here.

A next verification should compare dynamical outcomes under those independent
coefficients and test whether any proposed long-time normalized readout is
robust. That would test a conjecture about this action rather than import the
old fixed-metric equilibrium result.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_137_phase_backreaction.py

Checks phase force against energy differentiation, global norm conservation in
the vector field, numerical energy/norm convergence, nontrivial phase and record
evolution, and global phase covariance. No measured constants enter.
