# A faithful quotient charge for the collective rotor

## New external-symmetry hypothesis

The preceding action assigned the SAME microscopic external phase rotation to
all1836 rotors. Its primitive collective mode then carried charge1836. That
calculation remains correct. This test constructs a DIFFERENT external symmetry
assignment on the physical gauge quotient and includes the elementary reference
in that assignment. It is not a redefinition of the old observable charge.

The previous rotor/action and path-incidence checks are freshly rerun. The
connected comparison graph and declared Gauss constraints remain conditional
physical inputs. No measured mass or charge selects any numerical coefficient.

## The quotient and its primitive character

Let T^N be the microscopic angle torus and B the connected graph incidence.
The internal gauge subgroup is

    K = image(B:T^edges -> T^N) = kernel(product:T^N -> U(1)).

Connectivity and the primitive integer incidence lattice give

    T^N/K = U(1),
    Phi = sum_s theta_s modulo2*pi.

The primitive physical character exp(i Phi) has charge1 under THIS quotient
circle. An external phase lambda may be lifted to the microscopic torus by any
vector q with sum_s q_s=1:

    theta_s -> theta_s+q_s*lambda.

Different lifts differ by internal gauge transformations. The checker constructs
explicit rational/integer incidence flows for those differences on a spanning
tree; it does not infer equivalence from numerical proximity.

Three equivalent presentations are:

- charge1 on one slot, zero on the others;
- charge1/N on every slot;
- charge1/3 on each member of one three-slot rooted symmetry orbit.

At lambda=2*pi the fractional presentations need not return each microscopic
angle separately. They return modulo the internal gauge group, so their action
on every physical state is periodic. There is no physical freely accessible
fractional-charge excitation inferred from these gauge-dependent lifts.

The first presentation does not physically distinguish its chosen slot: changing
that slot adds an integer gauge vector. A strict integer lift invariant under
the simultaneous rooted S3 action cannot sum to1, because the actual slot orbits
have sizes3 and6 (ten and301 orbits respectively). A symmetric three-slot lift
exists with thirds. This is representation/gauge data, NOT a derivation of quark
charges, color or a three-quark bound state.

## Why this differs from the old diagonal action

The microscopic diagonal circle has q_s=1 and hence sum q_s=N. Its map to the
quotient circle has degree N and kernel Z_N. It is NOT gauge equivalent to the
primitive degree-one map above. Choosing the faithful quotient as the physical
external symmetry is a new physical identification that must ultimately be
sourced. It cannot be made silently after a charge measurement.

Add an independent elementary rotor theta_e transforming by theta_e->theta_e-lambda.
On physical charge states |k,n_e>, the JOINT charge is

    Q = k-n_e.

This is integer and2*pi periodic for all k,n_e in Z. The collective k=1,n_e=0
state and elementary k=0,n_e=1 state have opposite charges of equal magnitude.
No additional core rotor or bare core energy has been introduced.

## Effective action and energy

For any degree-one lift, integrating the declared internal gauge fields gives

    L_collective = C_eff/2 * (dot(Phi)-A_0)^2,
    C_eff^(-1) = sum_s C_s^(-1).

The elementary term is C_e/2*(dot(theta_e)+A_0)^2. At zero external field,

    E(k,n_e) = (k^2/2) sum_s 1/C_s + n_e^2/(2 C_e).

Equal microscopic and elementary inertias give energy ratio N=1836 with the
correct unit charge. The charge mismatch is therefore repairable in a coherent
candidate action, without an extra massive core and without changing a coordinate
period illicitly.

But the SAME external quotient and Gauss law permit C_s=1 on arrow channels,
C_s=1/2 on state channels, and C_e=1. The ratio then becomes1944 while charges
remain exactly+1 and-1. Charge consistency does not select equal inertias.

## Unit charge is not a protected particle identity

The elementary rotor includes n_e=-1, an antiparticle-like state with Q=+1 and
energy1/(2 C_e). It is lighter than the proposed collective state. The operator

    exp[-i(Phi+theta_e)]

maps (k,n_e)=(1,0) to (0,-1), preserving Q and internal gauge invariance. Its
Hermitian sum is an allowed mixing term unless a further sector law forbids it.
The free quadratic action separately conserves k and n_e; retaining that extra
conservation in interactions is an additional obligation. Charge conservation
alone is insufficient. Actual decay would also need energy-carrying final modes;
this finite rotor test establishes an allowed mixing channel, not a decay rate.
No fermionic statistics, baryon number or relativistic mass pole has been derived.

## Verification and residual

    python research/nima/checkers/check_mass_primitive_quotient_charge.py
    python research/aspect/scc/scc.py check nima-mass-primitive-quotient-charge

All charge lifts, incidence-flow identities, orbit counts and energy ratios are
checked with exact arithmetic. Report:
`results/mass-primitive-quotient-charge.json`.

Progress: a joint primitive external U(1) representation repairs the previous
charge obstacle conditionally. The remaining source obligations are its physical
identification, a common charging law and particle-sector protection. The count
1836 still does not fix those ingredients by itself.
