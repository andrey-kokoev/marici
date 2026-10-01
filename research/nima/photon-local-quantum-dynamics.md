# Gap and photon-number audit (iteration 8, completed during iteration 9)

The implementation begun in iteration 8 has now been checked against fresh mutable state and the preceding construction chain.

## Include the source gap inside the conserved-current construction

For source lowering, replace the polarization envelope by

    M_ge^{0i}=d_i f(t,x) exp(-i Omega t),
    j_ge^mu=partial_nu M_ge^{nu mu}.

Consequently

    j_ge^0=-d.grad(f) exp(-i Omega t),
    j_ge^i=d_i(partial_t f-i Omega f) exp(-i Omega t).

The raising transition is the complex conjugate. Both currents are conserved. Multiplying the OLD current by exp(-i Omega t) without differentiating the phase in M omits the -i Omega d_i f term and fails conservation. The checker includes this negative control.

The full Fourier current still has reduced polynomial J=(k_vec.d,omega*d), not (k_vec.d,(omega-Omega)*d). The scalar Fourier envelope is shifted by the gap. The Ward identity remains off shell.

## Number versus parity

The effective bilinear source-field interaction contains

    V_R = sigma_- A_g^dagger + sigma_+ A_g,
    V_CR= sigma_+ A_r^dagger + sigma_- A_r.

The first term conserves Q=N_gamma+|e><e|. The full interaction generally does not. It does conserve (-1)^Q: counter-rotating terms change Q by two.

Starting in |e,0>, a source-ground outcome therefore selects ODD photon number, not necessarily one photon. With the circular seed on the +z ray, the lowering and raising creation coefficients occupy opposite helicities, g=(0,1), r=(1,0), after removing a common scale.

A two-mode, untruncated-Fock witness gives leading short-time probabilities

    P1=(lambda*t)^2+..., P2=(lambda*t)^4/4+...,
    P3=(lambda*t)^6/18+....

The three-photon term has the source in its ground state and survives source-only heralding. The maximal-photon-number Taylor coefficients are unchanged by adding a positive-gap free Hamiltonian. These coefficients demonstrate the absence of an exact number-protection rule; they are NOT continuum Gaussian multiphoton probabilities.

The checker also verifies Hermiticity, parity commutation, the rotating excitation commutator and a nonzero full excitation commutator. It uses finite-support polynomials without an occupation cutoff; creation into higher photon sectors is retained.

## A scoped Gaussian suppression certificate

For a Gaussian envelope and an isotropic spatial width, angular/helicity integration gives common positive factors for d and its conjugate. The remaining first-order channel weights are proportional to

    I_lower=integral_0^infinity omega^3 exp[-tau^2(omega-Omega)^2-ell^2 omega^2] domega,
    I_raise=integral_0^infinity omega^3 exp[-tau^2(omega+Omega)^2-ell^2 omega^2] domega.

The ratio of these radial integrands is exp(-4*tau^2*Omega*omega). This is not a comparison of individual fixed-helicity intensities for complex d. It approaches one as omega approaches zero, so a band-only suppression claim is not a uniform continuum bound.

An integrated bound follows with a=tau^2+ell^2 and 0<delta<Omega:

    I_raise <= exp(-tau^2 Omega^2)/(2 a^2),
    I_lower >= 2 delta (Omega-delta)^3
               exp[-tau^2 delta^2-ell^2(Omega+delta)^2].

For Omega=1, tau=5, ell=1/5 and delta=1/5,

    I_raise/I_lower <= (390625/100320256)*exp(-14964/625) < 10^-12.

The final inequality is certified using an exact rational positive Taylor lower bound on exp(14964/625) through order 32. No floating-point quadrature is treated as a proof.

IMPORTANT: this compares first-order weights from DIFFERENT initial source states: excited-source emission versus ground-source counter-excitation. It is not a bound on all-orders three-photon contamination after an excited-source pulse, nor a proof of high-fidelity pi/2 transfer. Interpreting these weights as leading probabilities also requires weak coupling.

Ground/vacuum excitation during switching draws energy from external control. It is not spontaneous emission from the stationary interacting vacuum. A time-independent full Hamiltonian can conserve its total energy while not conserving its bare free-energy operator.

## Verification and remaining gate

    python research/nima/checkers/check_photon_local_quantum_dynamics.py

Implementation: `checkers/photon_local_quantum_dynamics.py`.
Report: `results/photon-local-quantum-dynamics.json`.

The next note, `photon-coherent-herald.md`, supplies an exactly solvable all-orders CONTROL model with explicitly different source assumptions. The positive-gap circular-source continuum dynamics remain unresolved; they are not replaced silently by that control.
