# Iteration 4: conditional one-photon creation-state map

## Explicit packet-to-creation formula

Keep the six original two-endpoint packets and the iteration-1 plane

    g_plus=u+i sqrt(3) w,
    g_minus=u-i sqrt(3) w.

For any nonzero v=a*u+b*w define

    beta  = (a+i*b/sqrt(3))/2,
    alpha = (a-i*b/sqrt(3))/2,
    v = alpha*g_plus + beta*g_minus.

In an explicitly declared normalized bosonic two-helicity mode fixture, set

    C(v) = beta*a_+^dagger + alpha*a_-^dagger,
    |gamma(v)> = C(v)|0>/sqrt(|beta|^2+|alpha|^2).

The helicity order is (+1,-1). The incidence-eigenvalue labels have the opposite assignment under the previously declared active-rotation convention:

    C(g_plus)|0>  = a_-^dagger|0>,
    C(g_minus)|0> = a_+^dagger|0>.

This is an explicit conditional one-photon state constructor from the two-packet vector. It is not a derivation of quantization, a physical source coupling or an executed emission.

## Bosonic algebra without a false finite-cutoff CCR

The implementation represents finite-support Fock polynomials in two creation variables. The monomial

    z_+^n z_-^m

means (a_+^dagger)^n(a_-^dagger)^m|0>, with squared norm n!m!. Multiplication is creation and differentiation is annihilation. This avoids square roots in the raw occupation coefficients while preserving their correct adjoint relation.

There is NO occupation cutoff. A polynomial with finite support can always be raised to the next occupation. Exact checks establish the bosonic commutators on occupations through four in both modes, mixed-field superpositions, and an explicit occupation-20 boundary control that raises to 21. A truncated matrix representation is not being mistaken for an exact CCR representation.

The vacuum, factorial inner product and bosonic algebra are added physical-model assumptions. They are not inferred from the seed's finite incidence spectrum.

## Photon number and normalization

The numerator C(v)|0> obeys

    N C(v)|0> = C(v)|0>,
    <N>=1, <N^2>=1, Var(N)=0.

The normalized helicity density matrix is

    rho_ij = c_i conjugate(c_j)/n,
    c=(beta,alpha), n=|beta|^2+|alpha|^2.

It is Hermitian, positive, rank one and trace one in the tested exact model. The packet-plane/Maxwell norm and the raw Fock norm satisfy

    ||v||_G^2 = -epsilon^dagger eta epsilon = 6*n.

Normalization is retained symbolically as numerator/sqrt(n). The implementation stores exact n and computes density matrices and expectations by division by n; it does not pretend that every square root of an exact field element lies in Q(sqrt(3),i).

A superposition of both helicities can have <h>=0 while <h^2>=1. This is not a spin-zero particle. Repeated application of C produces two photons and the expected norm 2*n^2, rather than silently returning another normalized one-photon state.

## Gauge and helicity compatibility

Creation coefficients are obtained by pulling the transported polarization back through its retained reference frame and applying the gauge-class decoder. Therefore:

- changes of gauge representative give the same coefficients and density;
- null little-group translations give the same state in a fixed reference frame;
- a fixed-frame rotation multiplies the helicity amplitudes by exp(-i*h*theta);
- co-transporting the reference frame preserves the coefficient coordinates;
- an incompatible reference momentum/frame is rejected.

The registered creation record retains its exact transported-wave parent, reference frame, raw creation coefficients and norm. Substituted records and foreign ledgers are rejected.

## Retained amplitude is not recoverable from the normalized state alone

Scaling a seed by a nonzero complex scalar changes the raw creation numerator and norm but leaves its normalized density matrix unchanged. A test using the scalar 2+i verifies this explicitly.

The original seed amplitude can be reconstructed here only because the record retains the raw coefficients and provenance. It is not an observable obtainable from the one-photon density alone. In particular the raw packet amplitude does not determine a photon emission rate merely by appearing in this formula.

## Momentum and normalization boundary

The current implementation uses a DECLARED normalized two-mode oscillator fixture labelled by the supplied momentum and polarization frame. Within that fixture P^mu=k^mu*N gives a one-photon momentum label k and P^2=0, using the already supplied null k.

An exact sharp-momentum state in infinite volume is distribution-normalized, not a normalizable one-photon wavepacket. The oscillator fixture must not be presented as resolving that issue. Boost comparisons in this checker are identifications between relabelled abstract mode fixtures, not a proof of boost covariance for a fixed finite box or a continuum momentum measure.

The next construction must replace this fixed-mode normalization assumption with an explicit normalizable momentum profile.

## Creation is not an apparatus protocol

A creation operator is not a unitary operation on the full Fock space: a^dagger takes the vacuum to a norm-one state but a normalized one-photon input to a vector of norm sqrt(2). Its algebraic application does not specify a trace-preserving laboratory process, a success probability or an energy reservoir.

What has been constructed is the conditional state expression and its consistency checks. An emission source, source-field interaction and preparation probability remain missing. No electromagnetic coupling constant is extracted from the packet coefficients.

## Verification

    python research/nima/checkers/check_photon_creation_state.py

Fresh exact checks pass for the creation map, untruncated CCR, adjointness, one-photon number, normalized density, gauge/helicity action, the two-photon factorial control and provenance/invalid-input tests. The command reruns the iteration-3 Lorentz checker and the earlier source/Maxwell closure.

Implementation: `checkers/photon_creation_state.py`.

Report: `results/photon-creation-state.json`.

## Next executable iteration

Construct a normalizable momentum-profile one-photon wavepacket, with an explicit one-particle measure, profile support and polarization-frame convention. Audit its norm and gauge/frame transport before proposing an emission mechanism. Keep the new profile/measure inputs separate from information actually selected by the seed.
