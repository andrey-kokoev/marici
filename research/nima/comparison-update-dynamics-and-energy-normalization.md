# Comparison update dynamics and energy normalization

## Starting rule

The mass-comparison prototype has six coordinates q and 153 comparison rows r.
Its deterministic update is P_r q, where P_r = I - rr^T/(r^T r).
Every P_r annihilates r. The update loses information and has no inverse.
Its squared-norm decrease is (r^T q)^2/(r^T r). The traversal budget counts
attempts independently of this decrease.

## Generator fixed by the row normalization

For a weak update I - gamma rr^T/(r^T r), summing over a sweep gives
I - gamma A + O(gamma^2), with A = sum_r rr^T/(r^T r).
The expansion applies near gamma=0; the full projections use gamma=1.
For uniformly sampled rows, the conditional mean single-step update is exactly
(I - gamma A/153)q.

Exact summation gives diagonal entries 51/2, within-carrier off-diagonal
entries -7, and cross-carrier entries -1/2. The eigenvalues are
10, 13, 65/2, 65/2, 65/2, 65/2.
Thus weak mean dynamics gives decay rates, with a rate scale supplied by the
update clock. The unnormalized equal-storage matrix H instead has spectrum
24, 30, 99, 99, 99, 99. These are different choices of comparison weighting.

## Reversible extension

Introduce a conjugate variable p and dimensionless step eta:

    p_next = p - eta A q
    q_next = q + eta p_next

This symplectic update is an added dynamical assumption. Its exact invariant is

    I(q,p) = (p^T p + q^T A q - eta q^T A p)/2.

For each eigenvalue lambda, positivity and oscillatory stability require
0 < eta^2 lambda < 4. The mode phase per step satisfies

    cos(theta_lambda) = 1 - eta^2 lambda/2.

Given a physical step duration tau, the mode frequency is theta_lambda/tau.
The small-step limit gives omega_lambda = (eta/tau) sqrt(lambda).
The checker uses eta=1/10 solely to test a stable instance.

## Exact memory lift of the projection

For one comparison set n = r^T r, a = r^T q/n, and introduce a scalar
record z with the same coordinate units as a. Define

    q_next = q + r(z - a)
    z_next = a.

This exchanges the longitudinal carrier coordinate a with the stored record z;
the transverse coordinates remain unchanged. Applying the operation twice
returns the input. Its conserved budget is

    q_next^T q_next + n z_next^2 = q^T q + n z^2.

For an initially empty record, z=0, the carrier output is exactly P_r q.
The projection's discarded squared norm n a^2 moves into the record.
One scalar is sufficient to store the one-dimensional kernel of a single
projection; a reversible linear extension reproducing that projection requires
at least that much extra information.

A bank of 153 initially empty records reproduces the whole original sweep.
Applying the lifted comparisons in reverse order restores q and empties every
record. Reusing a populated record instead gives r^T q_next = n z: the previous
mismatch returns to the carrier. Repeated projection-only sweeps require fresh
records or a reset process whose resource budget must also be accounted for.
A 153-record bank is a direct local construction, not a minimal global dilation.

This derives a reversible record mechanism from the projection rule. It does
not identify the records with the six conjugate momenta of the symplectic
extension. A local lift is a reflection (determinant -1); its record-plus-carrier
space has seven coordinates. The full bank has 159 coordinates. Neither space
admits a nondegenerate symplectic form. Obtaining Hamiltonian dynamics requires
additional structure, a different extension, or an appropriate reduction.

The conserved record budget can be multiplied by any positive scale without
changing the update. Thus memory conservation alone leaves physical energy
normalization free.

## Reusing the records: closed back-action

Reuse the same bank without resetting or injecting noise. In coordinates
w_r = sqrt(r^T r) z_r, every lifted comparison is an orthogonal reflection.
A sweep is therefore an orthogonal map U on 159 real coordinates. It preserves
pairwise distances and total squared norm. Its eigenvalues have modulus one;
its dynamics consists of fixed, sign-alternating, and rotation components.
The closed system has no attracting settled state. Repeated sweeps can return
stored mismatch to the carrier, with recurrence in the finite-dimensional
rotation dynamics. Carrier observables can fluctuate while the total is fixed.

A deterministic experiment starts with unit covariance on the six carrier
coordinates and empty records. The conserved total trace is 6. In the existing
row order the carrier trace is:

| Sweep | Carrier trace |
|---:|---:|
| 1 | 0.0000345975866705 |
| 2 | 0.000966757161855 |
| 12 | 0.192712910498 |
| 100 | 0.219139336853 |
| 1000 | 0.178749640824 |

Over sweeps 101 through 1000 the carrier trace ranges from 0.0917299307379
to 0.670486600401, with mean 0.237500047309. These are finite-window statistics
for the specified seed covariance and update order. Scaling initial covariance
scales all these budgets; zero input remains zero. Reversing all 1000 sweeps
restores the initial carrier to maximum coordinate error about 1.05e-15.

This realizes deterministic back-action through retained comparison records.
A stationary open-system description requires an explicit environment, reset,
or coarse-graining rule. The finite-window mean is neither a universal floor
nor a particle mass correction. Absolute time and energy normalization remain
free under this closed update law.

## Full sweep rotation spectrum

Numerically diagonalizing the normalized 159-dimensional orthogonal sweep gives
six +1 modes, one -1 mode, and 76 conjugate rotation pairs. The first five
positive phases and periods are:

| Phase (radians/sweep) | Period (sweeps) |
|---:|---:|
| 0.176540974539 | 35.5905212576 |
| 0.188656635885 | 33.3048730446 |
| 0.196361752323 | 31.9980099630 |
| 0.213138025810 | 29.4794196545 |
| 0.316287401076 | 19.8654302568 |

For initial covariance P equal to the carrier projector, the infinite-time
Cesaro mean of carrier trace is sum_g ||P E_g P||_F^2, where E_g are spectral
projectors grouped by equal eigenvalue. Numerical grouping at tolerance 1e-8
gives 0.237673530614. An independent 20000-sweep mean is 0.237521853596.
The mean depends on the initial covariance and the specified schedule.
It does not imply convergence of instantaneous carrier trace.

There is a continuous-time obstruction: a sweep comprises 153 reflections,
so det(U)=-1. A real autonomous norm-preserving linear flow exp(t B), with
B skew-symmetric, has determinant +1. Consequently this one-sweep map cannot
be that flow on the existing real state space. A two-sweep map U^2 has an
orthogonal rotation interpolation, with logarithm branch choices, but loses
the one-sweep sign alternation. A clock or additional state is another option.

A rotation phase specifies a frequency only after choosing a sweep duration
and phase branch. Hamiltonian or quantum identification additionally requires
an action/symplectic structure. These phases do not by themselves determine
particle energies.

## Hamiltonian embedding of two sweeps

Choose the principal rotation angles phi of U^2 and construct its real
skew-symmetric logarithm B. The seven fixed directions comprise the original
six +1 modes and the squared -1 mode. On each rotating plane factor B=JK,
with J a signed quarter-turn and K=|phi| times the identity.

Add one stationary coordinate and pair the resulting eight fixed directions
into four canonical planes with K=0. This gives 160 coordinates, J^T=-J,
J^2=-I, K positive semidefinite, and exp(B)=diag(U^2,1). The extra coordinate
and fixed-sector pairing are embedding choices. They are not identified
carrier degrees of freedom. A degenerate Poisson structure on the original
159 coordinates is another option, retaining the fixed coordinates as Casimirs.

For a chosen two-sweep duration T and action scale S, define

    H(x) = (S/(2T)) x^T K x,
    Poisson tensor = J/S.

Hamilton's equation is dx/dt = Bx/T. Thus it reproduces two sweeps at time T
and conserves H. This makes the normalization freedom explicit: changing S
rescales H and the Poisson tensor inversely, leaving the classical trajectory
unchanged. Changing T rescales its physical rate.

There is also spectral aliasing: replacing every nonzero principal phase phi
by phi + 2*pi*sign(phi) gives a different positive-semidefinite Hamiltonian
with exactly the same sampled two-sweep map. The discrete schedule alone
therefore does not select a unique continuous energy spectrum.

In canonical quantization of the chosen rotating planes, excitation spacings
are hbar*|phi|/T. S fixes the coordinate-to-action normalization and cancels
from those harmonic spacings when the commutators are scaled consistently.
The remaining frequency choices are T and the phase branch. No GeV value is
fixed by this embedding.

Verification:

    uv run research/nima/checkers/check_comparison_hamiltonian_embedding.py

The checker tests the logarithm exponential through spectral reconstruction,
J^2=-I, B=JK, positivity, conservation, and a distinct phase branch yielding
the same sampled map. It uses numerical tolerances of 1e-8.

## Continuous path through individual comparisons

Normalize the record coordinate as w = sqrt(r^T r) z and put
u = r/sqrt(r^T r). A comparison exchanges u^T q and w. In the joint
carrier-record space its reflecting direction is d=(u-e_record)/sqrt(2).
Introduce one auxiliary coordinate e_c perpendicular to this space and define

    G = e_c d^T - d e_c^T,
    R(theta) = exp(theta G).

At theta=pi, both d and e_c change sign; all other directions stay fixed.
Thus R(pi) implements the comparison reflection and an auxiliary sign flip.
With the auxiliary initially zero, it is zero at every comparison endpoint.
During the update it carries a sin(theta) multiple of the difference amplitude.
The same auxiliary can be reused for all 153 comparisons. The final map is
exactly diag(U,-1), which has positive determinant. This supplies a continuous,
norm-preserving path through the full one-sweep schedule on 160 coordinates.

This path uses a prescribed generator for each comparison. The schedule and
angle parameter are external controls. The auxiliary stores an intermediate
amplitude; it is not an autonomous clock. In particular zero amplitude carries
no readable phase, while the prescribed update can still advance.

A shortest plane rotation has angle pi, with two possible orientations.
Choosing it excludes extra full turns by a minimal-path assumption. The
endpoint rule itself also permits 3*pi and any other odd multiple of pi.
For any positive comparison duration tau, the generator (pi/tau) G reaches
the same endpoint at tau. Nonuniform angular speed gives further paths with
the same endpoints. No endpoint or norm-budget constraint fixes tau.

This exposes an exact scale freedom: t -> a*t and every dynamical rate ->
rate/a preserves all sampled comparisons. Under E=hbar*omega, excitation
energies scale as 1/a. An absolute energy in GeV therefore requires a physical
time or equivalent dimensional input. Examples are a specified carrier length
with a derived propagation law, a gravitational scale with a derived descent,
or one measured reference frequency. The present comparison rule supplies
none of these dimensional inputs.

Verification:

    uv run research/nima/checkers/check_comparison_continuous_path.py

All 153 endpoint rotations, orthogonality, intermediate auxiliary excursion,
full-sweep reconstruction, and the pi/3*pi branch equivalence are checked.
This is a continuous orthogonal embedding; a common canonical symplectic
structure for its time-dependent generators has not been constructed.

## Physical normalization still required

Multiplying I by any positive energy coefficient preserves the discrete
invariant. The comparison rule does not fix that coefficient. Nor does it
fix tau, eta, or the physical symplectic/action normalization of q and p.
Relating phase frequency to quantum excitation energy requires specifying
that normalization and quantizing the resulting dynamics. In a canonically
normalized continuous harmonic limit, spacings are hbar omega_lambda.

The calculation supplies a normalized restoring spectrum and a consistent
reversible extension. Particle assignments, the Higgs coefficient 125, and
an absolute GeV scale are not outputs of this calculation.

## Verification

Run:

    python research/nima/checkers/check_comparison_energy_spectrum.py
    python research/nima/checkers/check_comparison_update_dynamics.py
    python research/nima/checkers/check_comparison_memory_lift.py
    python research/nima/checkers/check_comparison_reused_records.py

The first three use exact integer or rational arithmetic. The second checks the normalized
spectrum, projection information loss, and the invariant and inverse of twelve
reversible steps. The third reproduces a full projection sweep with empty
records, checks exact budget transfer, reverses the full sweep, and checks
feedback from a reused record. The fourth uses floating-point arithmetic to
check 1000 closed sweeps, their budget conservation, and their reversal.
No measured constants enter the checkers.

The spectral calculation uses NumPy in an isolated uv script environment:

    uv run research/nima/checkers/check_comparison_sweep_spectrum.py

It checks orthogonality, eigenvalue moduli, eigenvector residuals, completeness
of grouped spectral projectors, and agreement with the long-window average.
