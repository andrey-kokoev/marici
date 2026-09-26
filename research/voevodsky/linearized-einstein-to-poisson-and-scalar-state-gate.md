# From linearized Einstein to Poisson: the scalar-state gate

## Outcome

The static weak-field dust sector of the already-used linearized Einstein
model gives the Newtonian Poisson equation and the tidal Hessian, with signs
and normalization checked by direct tensor contraction. Poisson need not be
an independent equation if Einstein's equation and this physical regime are
supplied. This is a conditional reduction, NOT a derivation of Einstein's law
from the structural calculus.

The source gate is now sharper: a cosmological scalar state is not automatically
pressureless matter. Its density alone cannot supply the stress tensor needed
for this reduction. Even a homogeneous massive scalar with fixed energy density
has time-dependent pressure; dust behavior requires an averaging regime.

## Recovered starting point

`research/nima/checkers/check_machian_linearized_source_boundary_map.py`
already uses a conserved source, harmonic-gauge trace reversal and independent
homogeneous radiative data. The present checker independently contracts the
linearized Ricci and Einstein tensors to test the static reduction rather
than simply assuming the Poisson kernel.

The preceding cosmology-source audit recovered a fixed-background scalar model
with time-dependent effective mass/couplings, a scale factor, and a choice of
curvature coupling. Those facts do not by themselves provide the backreacting
stress tensor of a selected scalar state or the validity of a dust approximation.
No claim is made that the source has no position-space or matter structure.

## Static weak-field calculation

Admit signature (-,+,+,+), c=1, linearized Einstein's equation

    G^(1)_mu nu = 8*pi*G T_mu nu,

and the static scalar metric sector

    h_00=-2 Phi, h_0i=0, h_ij=-2 Psi delta_ij.

For a nonzero spatial Fourier covector k, direct contraction gives

    G^(1)_00 = -2 |k|^2 Psi,
    G^(1)_0i = 0,
    G^(1)_ij = (Phi-Psi)(k_i k_j-delta_ij |k|^2).

For a pressureless static source T_00=rho, T_0i=T_ij=0, the nonzero spatial
mode therefore forces Phi=Psi and

    -|k|^2 Phi = 4*pi*G rho,

which is Delta Phi=4*pi*G rho. This is the complete linearized tensor equation
for that mode, not only its 00 component. The zero mode requires a separate
boundary/background treatment, as the preceding periodic experiment showed.

The dust source is conserved at zeroth order when it is static. Exactly static
self-gravitating dust need not be a nonlinear equilibrium: this argument is a
linearized or instantaneous approximation, not an all-time static universe.
A Fourier amplitude rho(k) is not itself a nonnegative physical density at
every point; the checker tests mode equations, not a standalone positive
single-mode matter distribution.

Admit geodesic motion of a slow test body. At leading order,

    Gamma^i_00 = partial_i Phi,
    d^2 x^i/dt^2 = -partial_i Phi.

Thus the acceleration coupling follows from the supplied metric and geodesic
principle in this regime. With the declared curvature convention,

    R_0i0j = partial_i partial_j Phi,
    delta a^i = -delta^ik R_0k0j xi^j.

Einstein's equation, universal geodesic coupling and the approximation regime
are substantive physical inputs. Replacing two Newtonian assumptions by those
inputs is a unification/reduction, not an assumption-free dynamics selection.

## A stress counterexample

For a general STATIC conserved source, harmonic trace reversal gives

    hbar_mu nu(k)=16*pi*G T_mu nu(k)/|k|^2,
    h_mu nu=hbar_mu nu-(1/2) eta_mu nu trace(hbar).

Define Phi=-h_00/2. Then

    -|k|^2 Phi = 4*pi*G (T_00+sum_i T_ii).

Density alone is insufficient when spatial stresses matter. An anisotropic
source need not fit the scalar metric ansatz above; the checker uses the full
metric perturbation for this test.

At k=(0,1,2,0), put T_00=3 and T_ij=e_i e_j for e=(2,-1,0).
The source is conserved since the spatial k is orthogonal to e. With
4*pi*G=1, the density-only dust solution would give Phi=-3/5, but the full
stress source gives Phi=-8/5. The direct Einstein residual vanishes only for
the correctly constructed full solution. This is a formal conserved source
example, not a claim that every such stress is realized by the primary scalar.

## Scalar energy does not imply dust

For a separately declared minimally coupled canonical REAL scalar on a local
Minkowski background with L=-1/2 (partial phi)^2 - V(phi),

    rho = (1/2) dot(phi)^2 + (1/2)|grad phi|^2 + V,
    T_ij = partial_i phi partial_j phi
           + delta_ij [(1/2) dot(phi)^2-(1/2)|grad phi|^2-V].

Consequently

    rho+sum_i T_ii = 2 dot(phi)^2 - 2 V.

This is an algebraic stress identity, not permission to insert arbitrary
time-dependent scalar data into the STATIC Poisson formula. Time derivatives
of the metric cannot generally be discarded for those data.

For a homogeneous free massive oscillator phi=A cos(mu t),

    rho=mu^2 A^2/2,
    pressure=-(mu^2 A^2/2) cos(2 mu t).

The same constant rho occurs at positive and negative pressure phases. Over
one oscillation, <pressure>=0 and <rho>=mu^2 A^2/2. This identifies a possible
massive-scalar dust mechanism, but does not establish it for the original
cosmological state or localize it into the two point masses.

In an expanding, spatially varying setting the proposed regime would need
mu much larger than the expansion and envelope-variation rates, small physical
wave number relative to mu, controlled averaging errors, weak metric fields,
and negligible relevant stresses after averaging. The source's massless or
conformally coupled sectors cannot be called this massive dust regime by
renaming their energy as rho. A nonminimal curvature coupling also changes
the physical stress tensor; it must be carried through rather than silently
replaced by the minimally coupled example above.

## Relation to the periodic cosmological toy

The earlier finite-grid equation used a frozen scale factor and supplied
Delta_com Phi=4*pi*G a^2 delta rho. The calculation here proves only the
Minkowski static reduction. Promoting it to expanding FRW perturbations
requires the time-dependent constraint equations, a gauge choice, a source
stress prescription and a controlled quasistatic/subhorizon limit. Those
terms were not computed or bounded by the periodic checker.

Homogeneous gravitational modes and boundary data are still independent in
the general linearized theory, as Nima's prior TT-wave counterexample shows.
The static nonzero-mode sector and a chosen Green operator restrict those
freedoms; they do not prove their physical absence in arbitrary cosmology.

## Verification

Run:

    python research/voevodsky/check_linearized_einstein_poisson_reduction.py

All 16 exact Fraction tests passed: full dust-mode Einstein equation,
normalization, unequal-potential stress, pure-gauge cancellation, electric
curvature/Hessian agreement, a conserved stressed source with a different
potential, scalar pressure ambiguity and homogeneous oscillator moments.

Receipt: `research/voevodsky/linearized-einstein-poisson-reduction.json`.
The oscillator test uses the known cycle moments <sin^2>=<cos^2>=1/2; it does
not numerically integrate a scalar evolution or prove an averaging theorem.
Universal continuum formulas above remain written mathematics, and no new
Agda proof or nonlinear Einstein convergence theorem is claimed.

## Current frontier

The missing physical bridge is now a precise state-and-regime question:

    Does an explicitly selected state of the primary cosmological scalar model
    have a controlled, weak-field, negligible-stress limit whose density and
    boundary data realize the Newtonian source packet?

The existing calculation answers neither by fiat. It supplies the target
stress conditions and counterexamples that any claimed bridge must survive.
