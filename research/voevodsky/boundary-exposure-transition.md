# How much boundary exposure reverses the common-vacuum ordering?

## Result

The positive belt–proton energy difference in `open-flux-common-vacuum.md` depends on shielding the belt's six middle modes from exterior flux. It does not require perfect shielding, but it fails once their exterior electric conductance is sufficiently large.

For the inherited illustrative electric coefficient beta=3/5, the sign changes at

    lambda_critical approximately 0.252446898910.

Here outer-mode leads have conductance one and middle-mode leads have conductance lambda. Thus a middle lead at about one quarter of the outer lead's conductance reverses this candidate's ordering. These conductances are coefficients of a declared finite electric network, not measured electromagnetic couplings.

## One continuous boundary family

Keep the same internal source graph, zero background, exterior charge coordinate and exterior charging energy. Add leads at the six previously unconnected middle modes, with cost

    beta E_middle^2/(2 lambda).

Outer leads retain cost beta E_outer^2/2. At lambda=0 the middle leads are absent; at lambda=1 all mode vertices are exposed equally. For every lambda>0, empty and occupied states use exactly the same graph and Gauss law. Varying lambda is a comparison of physical boundary laws, not a coordinate change.

The exterior charge remains -1 in either unit norm-charge sector. Its common eta/2 energy cancels from the difference but is retained in the total sector energies. Internal norm-charge is still not identified with electric charge.

## Exact relaxed energy

Let y be the belt's middle-mode density fraction. The eliminated electric energy coefficient is

    C(y,lambda)=[(lambda+2)(1-y)^2+4y]/[48(lambda+1)].

This formula is checked against exact inversion of the full eighteen-vertex grounded Laplacian and the energy of its internal and exterior fluxes, including their different lead coefficients.

With A=2099/3292 and B=1193/1646, the belt–proton difference is

    min_(0<=y<=1) {
        [sqrt(A(1-y))-sqrt(B y)]^2
        + beta [C(y,lambda)-1/24]
    }.

The full density functional is strictly convex for positive electric coefficients. As in the preceding construction, the outer/middle solution satisfies the full vertex stationarity equations; it is not merely a minimum inside an assumed symmetric ansatz.

## A unique sign transition

At fixed y,

    partial C/partial lambda
       =-(1+y)^2/[48(1+lambda)^2] < 0.

Consequently the optimized belt energy decreases strictly as middle-mode exposure increases; the proton energy is unchanged. There is exactly one sign transition for every beta>0.

The coherent belt fraction is y0=2099/4485. Its unrelaxed field energy equals the proton's at the exact conductance

    lambda0=4405801/17268727 approximately 0.25513.

But that coherent profile is not stationary there. Allowing its density to relax lowers its energy, so the true sign transition is strictly below lambda0.

Exact rational brackets give:

| beta | Critical lambda |
|---|---:|
| 3/5 | 0.252446898910 |
| 1 | 0.250690512408 |
| 6 | 0.230794330132 |

These values quantify boundary sensitivity, not a fit to a mass. The checker also records controls at lambda=0, 1/10, 1/4, 1/2 and 1, with rigorous energy intervals. It uses convex supporting tangents to bracket global minima rather than trusting a numerical optimizer.

## Consequence for the physical construction

The common-vacuum model now supplies a precise necessary gate for its proposed positive ordering: the physical exterior interaction must select sufficiently weak access to the belt's middle modes under the same rule applied to the proton.

The source geometry distinguishes these modes through the cross-face contact addresses, but we have not derived their electric lead conductances from an interacting field. Choosing lambda below its threshold because that yields the desired ordering would be fitting the boundary condition.

The next source question is therefore the exterior coupling map: does an existing field/current construction attach only to cross-face endpoints, or also to the middle modes, and with what inherited kinetic/flux metric? This must be answered before calibrating an energy scale. Additional fitted gaps or bare offsets would not answer it.

## Reproduction

    python research/voevodsky/checkers/check_boundary_exposure_transition.py

Results: `research/voevodsky/results/boundary_exposure_transition.json`.

The existing classical selected-mode scope is unchanged. No quantum excitation quantization, physical particle charge or neutron mass is derived.
