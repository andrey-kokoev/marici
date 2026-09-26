# A source adapter for the defect-indexed Newtonian spatial toy

## Outcome

The existing Machian point-source model supplies an explicit adapter once its
particle positions, masses, observation point and gravitational law are
retained. Its charge-selected centroid and spatial-fiber presentation agree,
and the original Newtonian jet is invariant under the corresponding change
of origin. The adapter is implemented and tested against the live fixture.

A decisive limitation is also explicit: even the COMPLETE particle momentum
measure does not determine the position mass measure. Two sources with the
same particle momentum distribution can have different local tidal tensors.
Fourier duality supplies a coordinate carrier, not missing source-state data.

## Declared source model and adapter

Use the Newtonian weak-field point-source model already stated in
`research/nima/marici-machian-gravity-direction.md`, section 'First
source-to-local localization map', and implemented in
`research/nima/checkers/check_machian_newtonian_localization.py`.

At one instant, supply positive masses m_a, affine spatial positions r_a,
zero velocities and an observation point o. This is instantaneous data, not
a claim that mutually attracting particles remain at rest for all time.
For the kinematic charge comparison only, take c_light=1 and the leading
rest-mass four-momenta p_a=(m_a,0,0,0); binding-energy corrections are outside
this approximation. G=1 is the original toy's separate supplied convention.

The source adapter is

    labelled particles -> mu=sum_a m_a delta_{r_a}
                       -> Phi(x)=-G integral 1/|x-y| dmu(y)
                       -> (Phi,grad Phi,Hess Phi) at o
                       -> tidal Hessian.

The first arrow is a positive finite measure by the supplied positive masses.
It is not a smooth density. As a distribution rho in Euclidean coordinates,
it satisfies rho=sum m_a delta(x-r_a). Projection to this measure can forget
particle labels and merge coincident masses; retain the particle table if
exact provenance recovery is required.

The Newtonian kernel and acceleration readout are supplied physics. The first
arrow does not derive them. The adapter is supported by the already-declared
Machian model, NOT by an identification with the cosmological defect source.

## Charge-selected rest direction and origin

Let M=sum m_a. The leading total four-momentum is P=(M,0,0,0), timelike.
It selects the same spatial hyperplane as any positive multiple of it. Mapping
P to its normalized future direction is a declared realization into the base
of the earlier spatial family. It does not identify its magnitude or physical
role with the cosmological nonconservation defect D.

With x_a=(0,r_a), define J=sum x_a wedge p_a. Then J^{i0}=sum m_a r_a^i,
and the earlier centroid formula gives

    X^i = J^{i nu} P_nu/P^2 = sum m_a r_a^i/M = c^i,
    X^0 = 0.

This agrees with the ordinary Newtonian center of mass. The centroid convention
chooses the transverse origin; time along its worldline remains unspecified.
Axes are retained from the fixture, not derived from a spinless charge packet.

For the actual fixture,

    (m_1,r_1)=(2,(3,0,0)), (m_2,r_2)=(1,(0,4,0)), o=(0,0,0),
    M=3, c=(2,4/3,0).

The centroid-relative source table and observer are

    r'_1=(1,-4/3,0), r'_2=(-2,8/3,0),
    o'=(-2,-4/3,0).

Since r'_a-o'=r_a-o, the full jet is unchanged:

    Phi=-11/12,
    grad Phi=(-2/9,-1/16,0),
    E=diag(-229,74,155)/1728.

Shifting sources without the observer would change the observation problem.
Retaining c reconstructs the original affine coordinates; erasing c retains
relative geometry but does not recover that absolute presentation.

## Fourier duality: what it does and does not supply

For the position measure mu, its Fourier-Stieltjes transform is

    mu_hat(k)=sum_a m_a exp(-i k(r_a)).

It retains positional phases and determines the finite measure, using the
standard uniqueness theorem. The frequency k is dual to displacement; a
physical momentum convention k=p/hbar additionally requires the phase scale.
The finite measure need not have an L2 density; the point-source problem must
not be passed silently through an L2 Plancherel theorem. Its bounded transform
and uniqueness belong to finite-measure Fourier analysis.

This transform is NOT the particle momentum distribution

    nu=sum_a m_a delta_{p_a,spatial}.

In the present zero-velocity fixture nu=M delta_0, which cannot specify any
of the r_a. For an exact counterexample, use two unit masses at (+/-2,0,0),
or two unit masses at (0,+/-2,0), both observed at the origin. Both have
nu=2 delta_0, total P=(2,0,0,0), centroid zero and J=0, but

    E_x=diag(-1/2,1/4,1/4),
    E_y=diag(1/4,-1/2,1/4).

Therefore a physical adapter from momentum marginals alone to position density
cannot recover both source states. A wave amplitude with its phases, a full
phase-space state, or explicit position data would be additional sufficient
kinds of input in their respective models; choosing one is physical modeling.
We have selected explicit positions because that is what the existing toy uses.

## The cosmological scale is not silently dropped

The recovered cosmological source supplies the spatial metric

    dl^2=a(eta)^2 d x_comoving^2.

At one fixed epoch, a positive scale s=a(eta) maps comoving displacements to
proper ones, r_proper=s r_comoving. For the same mass weights, the pushed-forward
measure preserves total mass. Coordinate densities obey

    rho_proper(x)=s^-3 rho_comoving(x/s)

in the distributional sense. It is incorrect to multiply every atom's MASS by
s^-3; that factor belongs to density relative to coordinate volume.

If the SAME numerical source coordinates are instead interpreted as comoving
ones and physically dilated by s while G is fixed, the evaluated fields obey

    Phi -> Phi/s, grad_proper Phi -> grad Phi/s^2, E_proper -> E/s^3.

These scaling laws compare different physical source separations. A mere
coordinate change for an unchanged physical configuration preserves geometric
observables and transforms their components instead. The checker tests the
first, explicitly stated interpretation at s=2. No FRW evolution equation or
cosmological Newtonian limit is proved by that fixed-epoch scaling test.

## Fibration interpretation

The full retained source package contains the direction, metric, masses,
positions, observer, centroid and frame. It admits several projections:

- to rest direction, with a Euclidean spatial fiber;
- to momentum/charge data, whose fibers still contain different position states;
- to position mass measure, forgetting labels/coincident decomposition;
- to local jet and then its affine-invariant Hessian.

The nontrivial fibers of the momentum/charge projection are precisely why
source information is still required. Totalizing retained fibers recovers
that information; choosing just a momentum readout does not select its lift.
This is a concrete use of fibration language rather than a new dynamics axiom.

## Verification

Run:

    python research/voevodsky/check_particle_source_spatial_adapter.py

All 19 exact Fraction checks passed. The checker extracts ONLY the pure jet
evaluator and `sources_a` assignment from the existing source AST, avoiding
its module-level result-writing side effects. The extraction interface is
count-checked, source-hashed and compared with the saved original jet receipt.
No owner implementation was modified.

Checks cover positive mass and total mass, centroid reduction, recentering of
both sources and observer, recovery using retained origin, full jet translation
invariance, proper-scale response, mass-measure conservation, and identical
momentum/charge data with different tides. Receipt:
`research/voevodsky/particle-source-spatial-adapter.json`.

This reuses the existing arithmetic evaluator and is not an independent
validation of Newton's law, universal PDE uniqueness, Fourier inversion or
source dynamics. Universal identities above are written mathematics.

## Disposition

The source adapter is now explicit for the existing Machian/Newtonian model.
There is no need to posit a missing formal position-space carrier. What cannot
be recovered from the momentum defect alone is the POSITION STATE on it.

The cosmological-to-Newtonian source identification remains unproved. Further
progress there requires a declared physical state/localization map, not another
reversible change of presentation or a Fourier transform of a momentum marginal.
