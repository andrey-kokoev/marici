# Iteration 2: a conditional Maxwell realization of the two-packet vector

## What is now constructed

The actual seed vector from iteration 1 is retained:

    g_plus=(1,-1,-omega^2,-1,1,omega^2),
    g_minus=conjugate(g_plus),
    packet order=(AB,BC,CA,BA,AD,DB).

Write g_plus=u+i sqrt(3) w with rational six-vectors u,w. On their complex span define the explicit adapter

    Phi(a*u+b*w) = [(0,sqrt(3)*a,-b,0)]

into the transverse gauge quotient at

    k=(E,0,0,E), E>0,
    eta=diag(1,-1,-1,-1),
    epsilon ~ epsilon+alpha*k.

Brackets indicate the gauge class. E and the Minkowski/null-frame data are SUPPLIED parameters in natural units, not derived packet frequencies. The implementation uses exact Q(sqrt(3),i) arithmetic without an external symbolic dependency.

The two vectors map to

    Phi(g_plus)  = sqrt(3)*(0,1,-i,0),
    Phi(g_minus) = sqrt(3)*(0,1,+i,0).

These are unnormalized plane-wave polarizations. They are not by themselves quantized one-photon states or evidence that an apparatus has produced a photon.

## Gauge-invariant inverse

For any transverse representative epsilon at the chosen momentum, epsilon^0=epsilon^3. Subtracting (epsilon^0/E)k gives the representative

    (0,epsilon^1,epsilon^2,0).

Decode it using a=epsilon^1/sqrt(3), b=-epsilon^2 and

    a*u+b*w=(a,-a,(a+b)/2,-a,a,-(a+b)/2).

Thus decoding is independent of the gauge representative and returns the exact original six packet coefficients. An off-plane seed vector is rejected rather than silently projected into a photon-labelled sector.

The gauge quotient includes its zero class. Decoding a pure-gauge vector returns zero; encoding that zero as a nonzero wave candidate is rejected.

## Exact physical-kinematic checks under the declared adapter

For nonzero null k, the Maxwell polarization operator is

    M(k)=k^2 I-k (eta*k)^T.

It has rank one in the tested null frame: a three-dimensional kernel, consisting of two transverse directions and the gauge line. Quotienting by the latter gives dimension two. The embedding columns and the gauge direction form an exact basis of this kernel.

For the reduced Fourier field strength

    F^{mu nu}=k^mu epsilon^nu-k^nu epsilon^mu,

where the common Fourier derivative factor -i is suppressed, checks establish:

- k.epsilon=0;
- F is unchanged by epsilon->epsilon+alpha*k;
- k_mu F^{mu nu}=0;
- the Fourier-space Bianchi identity;
- the free Maxwell equation on both embedding columns, hence on the entire encoded plane;
- nonzero field strength for every tested nonzero encoded polarization.

The pullback of the physical transverse Hermitian form -eta is diag(3,1), exactly the invariant plane metric constructed in iteration 1. The two mapped modes are orthogonal with squared norm six. This is a checked compatibility of the chosen embedding and metric, not an independent derivation of a physical norm from bare packet endpoints.

## Continuous helicity and the added representation

Use active rotations R_z(theta) and the helicity convention U(R_theta)=exp(-i*h*theta). The maps above then give

    g_plus -> helicity -1,
    g_minus -> helicity +1.

The signs are not a contradiction: the original plus/minus labels referred to the incidence eigenvalues omega and conjugate(omega), not to physical helicity labels.

On seed-plane coordinates the imported continuous rotation acts by

    T(theta) = [[cos(theta), sin(theta)/sqrt(3)],
                [-sqrt(3)*sin(theta), cos(theta)]].

At theta=2pi/3 this agrees exactly with the previous seed matrix T. The embedding intertwines T(theta) and the declared spacetime vector rotation. The rotation-generator eigenvalue equations are checked, together with exact rotations at pi/2, pi/3, 2pi/3 and a rational cosine/sine pair, and their composition law.

The spin-four alias still agrees at the C3 angle but fails the additional pi/3 rotation test in this adapter. Therefore spin one has been selected BY THE SPACETIME VECTOR REPRESENTATION, not by information newly extracted from the finite incidence matrix.

## Conditional Ward pairing

For a supplied conserved current j with k.j=0,

    j.(epsilon+alpha*k)=j.epsilon.

Exact checks verify this on a basis of the conserved-current space. A nonconserved-current control changes under a gauge shift. This is a kinematic Ward check conditional on current conservation; no electromagnetic charge, source current or interaction normalization is derived.

## Hostile controls and missing selection

- A timelike momentum fails the null gate and the transverse Maxwell equation.
- Zero momentum, pure gauge as a nonzero wave, an off-plane packet vector and nontransverse representatives are rejected.
- Incorrect packet order, inexact inputs and invalid rotations are rejected.
- The SAME seed coefficients give valid adapted waves at E=1 and E=7/3. The seed therefore has not selected the energy.
- The spin-four C3 alias demonstrates that the continuous spin assignment also needs the adapter's extra representation data.

The adapter adds Minkowski geometry, a momentum/frame, a polarization embedding, a gauge law, the Maxwell target equation and a continuous vector action. Its tests show consistency of those additions with the selected seed plane, not their necessity from that seed.

## Verification

    python research/nima/checkers/check_photon_maxwell_adapter.py

Fresh checks pass, including the iteration-1 candidate audit and its preceding whole-seed closure. Exact field-arithmetic checks cover inverses, conjugation, multiplication, associativity and distributivity on mixed-field fixtures.

Implementation: `checkers/photon_maxwell_adapter.py`.

Report: `results/photon-maxwell-adapter.json`.

## Next executable step

Extend the adapted packet beyond the fixed +z null frame: verify Lorentz transport, the null little-group gauge action and round-trip recovery while preserving the seed packet identities. This tests whether the conditional construction is a coherent photon-polarization family rather than one convenient frame-specific encoding.

Source selection of the adapter, electromagnetic coupling and quantized photon creation/physical preparation remain separate open gates.
