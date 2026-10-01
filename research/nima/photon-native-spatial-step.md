# Native clock-compatible two-packet continuation and spatial readout

## Question and result

Use the already constructed phase clock to advance the retained seed, then test its image in the existing tetrahedral S4 realization. Do not import Maxwell/Fock emission or assume a translational step.

The result separates three facts:

1. The existing unit-rate rotor clock can be attached explicitly to the seed's three-cycle, with the rotor/adjoint factor of two checked.
2. The endpoint-based spatial amplitude contrast cycles, but is NOT the circular rigid-rotation readout used in the earlier response.
3. Full retained continuation branches along actual seed edges. Some paths remain spatially open when the coefficient summary returns. No unique translating excitation follows from that summary.

## Existing inputs, kept distinct

- `retained-rotor-history-clock.md`: T-T0=theta on the chosen real rotor lift, with unit rate dT/dtheta=1 under C=kappa. History and winding are retained.
- `photon-two-packet-construction.md`: the actual six-record order (AB,BC,CA,BA,AD,DB), the seed v=u=(1,-1,1/2,-1,1,-1/2), and w=(0,0,1/2,0,0,-1/2).
- `checkers/check_whole_seed_occurrence_spectrum.py`: prefix extension retains endpoint-bearing paths; aggregation by final occurrence gives K.
- `twenty-four-triangle-shared-seed.md`: tetrahedral coordinates A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1), with the contrast and area representations distinguished.

No new physical clock, seconds calibration, photon detector or external propagation speed is inserted here.

## Attach the existing clock, rather than rename the discrete counter

On seed-plane coordinates (a,b), the checked continuation is

    C=[[-1/2,1/2],[-3/2,-1/2]].

In the existing Clifford adjoint module use q=sqrt(3)*a, p=b and Q=q*e1+p*e2. Its rotor U(theta)=exp(theta J) gives

    a(theta)=a(0) cos(2 theta)+b(0) sin(2 theta)/sqrt(3),
    b(theta)=b(0) cos(2 theta)-sqrt(3)*a(0) sin(2 theta).

At theta=pi/3 this is exactly C. Therefore the specified positive rotor segment attaches one K update to

    Delta T=pi/3,
    spatial/adjoint phase increment=2*pi/3.

The unit-rate clock remains T, not an independently fitted timestamp. The integer update count n is related by T_n-T_0=n*pi/3. If displayed ticks are desired, n=3(T-T0)/pi is just a rescaled reading.

This attachment uses a stated lift segment. Adding full windings can preserve endpoint matrices while changing the retained clock; the seed endpoint alone does not remove that freedom. It does not assign execution durations to arbitrary odd S4/frame operations.

After three updates the seed coefficients and adjoint return, but U(pi)=-I and the clock has advanced pi. After six updates U(2*pi)=I, but the clock has advanced 2*pi and the histories are still different. The lift sign belongs to this retained rotor construction; it is not a new photon-spin assignment.

## Actual clocked update retains paths before aggregation

Initialize six formal paths of length one with the supplied seed coefficients. The initial primitive is part of preparation; each timed update APPENDS one admissible primitive:

    (p_0,...,p_n;c) -> {(p_0,...,p_n,p;c): target(p_n)=source(p)}.

No preceding record is deleted. Coefficients are copied to every admissible extension; only a separate reader sums them by their last packet. That reader satisfies

    aggregate(extend(history))=K*aggregate(history).

The successive path counts are 6,10,16,26,42,68,110. They do not reset with the three-cycle. These are formal retained histories, not detector events or a probability distribution. In particular, prefix extension is not unitary in the retained counting norm: the seed norm 9/2 becomes 7 after one extension. No Born or path-selection law has been inserted.

## Correct the earlier spatial identification

The earlier response chose the compatible adapter

    J(a,b)=a(1,-1,0)+(b/3)(1,1,2),
    J*C=R_(ABC)*J.

That identity is correct. It gives a circular three-step orbit, and J^T J=(2/3)diag(3,1). But it does NOT establish that J is the packet endpoint readout.

Use the actual target-incidence reader instead:

    y_i=sum_(packet.target=i) c_packet,
    x_read=sum_i r_i*y_i.

This is a SIGNED AMPLITUDE CONTRAST in the existing tetrahedral coordinates. It is not a photon position, a normalized centroid, or a Born-probability mean. A common factor 1/2 would merely change its coordinate normalization.

On the selected seed plane this reader is

    E(a,b)=(0,-3a+b,a+b),
    E^T E=[[10,-2],[-2,2]].

Its explicit evolution is

| Update n | (T-T0)/pi | Target amplitudes (A,B,C,D) | Spatial amplitude contrast |
| --- | --- | --- | --- |
| 0 | 0 | (-1/2,1/2,-1,1) | (0,-3,1) |
| 1 | 1/3 | (-1/2,1/2,1/2,-1/2) | (0,0,-2) |
| 2 | 2/3 | (1,-1,1/2,-1/2) | (0,3,1) |
| 3 | 1 | same as n=0 | (0,-3,1) |

The squared Euclidean lengths are 10,4,10. Thus this update is not a rigid orthogonal S4 rotation of that readout. The continuous interpolation supplied by the attached rotor is a closed ellipse in the x=0 plane:

    x_read(theta)=(0, -3 cos(2theta)-sqrt(3) sin(2theta),
                      cos(2theta)-sqrt(3) sin(2theta)).

The circular adapter and the endpoint contrast cannot be substituted for one another silently. This corrects the spatial interpretation in the earlier conversational example.

## What actually changes location in the retained paths?

At clock zero, an initial AB record ends at B. Its next extensions include

    AB -> AB,BC: B -> C,
    AB -> AB,BA: B -> A.

There are different endpoint displacements at the SAME update and clock increment. After three continuations, both of these records are present with coefficient one:

    AB,BC,CA,AB: B -> B, net displacement (0,0,0),
    AB,BC,CA,AD: B -> D, net displacement (-2,0,2).

They coexist while the aggregate coefficient vector has returned to v_seed. It would be wrong to infer that all endpoints returned, or that the state specifies a unique travelling trajectory.

For any retained path on this fixed carrier, successive displacements telescope to final target minus initial target. Both endpoints are among four fixed vertices, so squared net displacement is always 0 or 8, at any depth. In contrast, n appended edges have total geometric path length 2*sqrt(2)*n. Increasing path length and history depth do not establish unbounded spatial displacement.

## S4 transport check

All 24 relabellings transport the entire endpoint registry and its spatial reader covariantly. In the transported six-role ordering, the incidence matrix remains the same. Only two relabellings preserve the original directed six-arrow support as a set.

For the standard contrast action R_sigma, the transported endpoint reader is R_sigma*E. The alternative area action is det(R_sigma)*R_sigma, which is proper and sends odd-labelled branches to the complementary tetrahedral placement. Neither finite action alone supplies translations to new spatial cells.

This test attaches the clock to one even cyclic update and checks its relabelling covariance. It does not equate spatial determinant with the orientation cocycle of every possible clock lift.

## Verification

    uv run --with sympy python research/nima/checkers/check_photon_native_spatial_step.py

The command freshly reruns the original seed audit and the retained-clock checker, then verifies the symbolic adjoint bridge, full retained continuation through six updates, endpoint readouts, open/closed path controls, norm distinctions and all 24 relabellings. The arbitrary-depth displacement bound follows from telescoping endpoints in the fixed four-vertex carrier, not from extrapolating six samples.

A bare `python` run requires SymPy to be installed; the displayed uv command supplies it and passes.

Implementation: `checkers/photon_native_spatial_step.py`.
Report: `results/photon-native-spatial-step.json`.

## Productive next gate

Determine whether the native spatial construction gives distinct spatial placements to retained extensions or keeps them in this fixed tetrahedron. If a larger carrier is already supplied, attach the same clocked continuation to that carrier and compute net transport there. Do not invent a drift vector, replace the endpoint reader by the convenient circular adapter, or turn copied path coefficients into probabilities without a supplied rule.
