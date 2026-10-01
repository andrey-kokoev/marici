# Iteration 9: exact driven control and a certified one-photon herald

## What has changed

The gap/counter-rotating audit shows why source depletion alone is not an exact one-photon certificate. This iteration constructs a soluble continuum control model in which the ENTIRE photon-number distribution is known, rather than extrapolating first-order emission to probability one.

This is an explicitly changed model: a degenerate control qubit, a real conserved current, and external switching. It does not solve the positive-gap circular-source dynamics or provide a microscopic apparatus.

## An explicit vector on the actual two-packet records

In the retained order (AB,BC,CA,BA,AD,DB), choose

    v_lin=(g_plus+g_minus)/2=(1,-1,1/2,-1,1,-1/2).

This is the a=1,b=0 vector in the same oscillatory plane. It is a linear polarization superposition, not a new incidence eigenmode and not a two-photon state. Each basis record is the original two-endpoint packet primitive.

The declared adapter gives

    d=(sqrt(3),0,0),
    M^{0i}=d_i f, M^{i0}=-d_i f,
    j_real^mu=partial_nu M^{nu mu}.

Take a real Gaussian or compact smooth bump f as in iteration 7. This supplies a real, conserved, smooth current with finite radiation norm. Profile, physical units, field quantization and coupling remain added inputs.

## Exactly solvable quantum source

Let X be a Pauli source operator, X^2=1, and set H_source=0. Declare

    j_hat^mu=X*j_real^mu,
    H_I(t)=lambda*X*integral d^3x j_real^mu(t,x) A_mu(t,x),

up to a common sign convention. X is conserved. The interaction density is local in the field/current coordinate, but the effective control qubit is not a derivation of microscopic relativistic matter or a finite calibrated apparatus.

The commutator of two linear free-field observables is a scalar. Since X^2=1, [H_I(t),H_I(s)] is also a scalar times the identity, and all further nested commutators vanish. The time-ordered unitary is therefore exactly

    S=exp(i Phi)*exp[X*(a^dagger(alpha)-a(alpha))],
    alpha_h(k) proportional to lambda*epsilon_h(k)^*.jtilde_real(k),
    mu=||alpha||^2=lambda^2*N_source.

Phi is a common phase, not a relative phase between the two source branches. Gauge conservation removes gauge-dependent radiative contributions. The smooth envelopes make alpha normalizable. No rotating-wave approximation or photon-number cutoff is used in this model.

For a unit-width Fourier-normalized Gaussian, N_source=pi/2 for this real seed. The normalized wavepacket psi=alpha/sqrt(mu) has the same radiation-profile interpretation as iteration 7. For example, the supplied gain lambda^2=1/(5*pi) sets mu=1/10 in these conventions; the seed does not determine that gain.

## Exact outgoing state and source herald

Prepare a source state |e> that is an equal superposition of X eigenstates, with |g> the orthogonal source-readout state. These are degenerate control states, not an excited/ground energy pair. From field vacuum,

    S|e,0> = exp(i Phi)/2 * [ |e>(|alpha>+|-alpha>)
                                      + |g>(|alpha>-|-alpha>) ].

An ideal source-only readout after the interaction selects the odd coherent superposition

    |odd_alpha>=(|alpha>-|-alpha>)/sqrt(2*(1-exp(-2mu))).

This readout is assumed; its implementation and errors are not supplied. It does not absorb the field in the mathematical instrument, unlike direct destructive photon counting. Gaussian switching is understood asymptotically; a compact smooth bump permits an exactly switched-off source at finite time, with a different profile/normalization integral.

The exact statistics are

    P_flip=(1-exp(-2mu))/2=exp(-mu)*sinh(mu),
    P(n|flip)=mu^n/(n!*sinh(mu)) for odd n, zero for even n,
    F_1=|<1_psi|odd_alpha>|^2=mu/sinh(mu).

Unconditionally, photon counts are Poisson with mean mu. Source heralding eliminates vacuum and EVERY even photon number, but leaves n=3,5,... . For every mu>0, F_1<1. This is a fidelity/photon-number statement; 1-F_1 is not the trace distance, which for these pure states is sqrt(1-F_1).

## All-orders rational certificates, not truncated simulations

Write sinh(mu)/mu=1+T. The first term of T is mu^2/6, and each subsequent-to-previous term ratio is at most mu^2/20. For mu^2<20,

    T <= (mu^2/6)/(1-mu^2/20),
    1-F_1=T/(1+T) <= T_bound/(1+T_bound).

Also, exponential remainder/convexity bounds give

    max(0,mu-mu^2) <= P_flip <= min(mu,1/2).

Thus the model supplies explicit operating points:

| Supplied mean mu | Certified one-photon infidelity | Certified source-herald probability |
| --- | --- | --- |
| 1/10 | <=10/6007 <0.002 | between 0.09 and 0.10 |
| 1/100 | <0.00002 | between 0.0099 and 0.01 |

The first setting therefore gives greater than 99.8% one-photon fidelity conditional on a source herald occurring with at least 9% probability. These are ideal-model bounds, not measured apparatus performance. The certificate rejects a request for exact one-photon output or unsupported fidelity/success targets.

## Energy and omitted reservoirs

The source gap is zero, so it contributes no internal energy loss. With the interaction switched off at the endpoints, the mean radiated field energy is mu*<omega>; it must be supplied by external control. For the unit-width Gaussian,

    <omega>=3*sqrt(pi)/(4*sqrt(2)).

Source preparation, source readout and control apparatus costs are not closed here. This is driven photon production with a quantum herald, not energy generation from the seed vector.

## Verification

    python research/nima/checkers/check_photon_coherent_herald.py

The command freshly reruns the construction chain, including the completed gap audit. Exact checks cover central commutators, displacement/normal-ordering Taylor coefficients, factorial Fock weights, odd-sector selection and rational all-orders tail bounds. The infinite-series solution follows analytically from the central-commutator identity; checking twelve Taylor orders alone is not represented as a proof of an infinite identity.

Implementation: `checkers/photon_coherent_herald.py`.
Report: `results/photon-coherent-herald.json`.

## Next executable iteration

Consolidate an end-to-end output contract that distinguishes:

- the exact ideal normalized one-photon vector and the engineered global transfer model;
- the local-current profile change;
- this driven, approximate-one-photon herald with a certified all-orders error;
- any ADDITIONAL number-selective instrument required for exact one-photon output.

Do not call a source-ground herald a number-one measurement, or a destructive photon detector a nondemolition preparation. An exact available output photon requires those instrument/dynamical assumptions to be stated and checked separately.
