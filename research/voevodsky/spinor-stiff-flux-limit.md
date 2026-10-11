# Quantum cost of finite flux stiffness — iteration 3

## Scope

Continuing the freshly read hard-flux parent action, quantify its local cycle modes rather than claiming that a large cosine coefficient implements an exact constraint. The formulas below are exact for the harmonic normal-mode model; the quartic correction is first-order oscillator perturbation theory. They do not establish a global convergence theorem for the compact interacting parent.

## Three massive cycle modes

The source face incidence obeys C^T C=4 P_cycle, where P_cycle is a rank-three orthogonal projector. Choose orthonormal cycle coordinates x_a and conjugate momenta p_a. With hbar retained, the local field Hamiltonian is

    H_cycle=sum_(a=1)^3 [beta p_a^2/2+2 kappa x_a^2].

Each frequency is omega=2 sqrt(beta kappa). Its vacuum variances and total vacuum energy are

    <x_a^2>=(hbar/4)sqrt(beta/kappa),
    <p_a^2>=hbar sqrt(kappa/beta),
    E_vac=3 hbar sqrt(beta kappa).

The product of variances is hbar^2/4. Localizing flux does not also suppress cycle electric fluctuations: the latter diverge in the stiff limit.

Since C C^T=4I-ones, every face has

    Var[(C A)_f]=(3 hbar/4)sqrt(beta/kappa).

Every internal edge has cycle-projector diagonal 1/2. The Gaussian vacuum therefore gives

    <exp(i(C A)_f)>=exp[-(3 hbar/8)sqrt(beta/kappa)],
    <exp(i A_cycle,e)>=exp[-(hbar/16)sqrt(beta/kappa)].

The second factor suppresses a frozen source hopping amplitude. It tends to one but is not exactly one at finite stiffness. These vacuum averages are not already the full matter-relaxed effective Hamiltonian.

## Tolerance versus cost

In the harmonic model, demanding face RMS flux at most epsilon requires

    kappa >=9 beta hbar^2/(16 epsilon^4),
    E_vac >=9 beta hbar^2/(4 epsilon^2).

These are harmonic-model resource relations, not certified engineering tolerances for the complete cosine model. At beta=3/5, hbar=1, kappa=10000 the face RMS is still about 0.07622 radians while cycle zero-point energy is 232.379 clock units. The kappa=1 table entry in the receipt is only an algebraic illustration, not a claim that the small-angle approximation is accurate there.

The earlier classical current-driven shift also remains relevant: frozen coherent matter gives a displacement proportional to 1/kappa. Quantum RMS fluctuations fall only as kappa^(-1/4). Cancelling a mean displacement would not remove these fluctuations.

## A finite energy correction survives subtraction of the harmonic divergence

The first anharmonic cosine term is

    V4=-(kappa/24)sum_f (C A)_f^4.

Using the oscillator Gaussian fourth moment gives

    <V4>=-9 beta hbar^2/32.

This does not tend to zero with stiffness. At the retained fixture it is -0.16875. Thus subtracting only 3 hbar sqrt(beta kappa) does not even remove the full field-vacuum correction through this perturbative order.

The reduced model's energy 0.472191444 cannot be equated with an unsubtracted stiff-parent absolute energy. A common vacuum prescription could remove field-only terms, but must specify the same reference across sectors. Compact topology, Gauss constraints, higher corrections and matter-induced terms must be controlled before asserting convergence of spectra or unitary dynamics. No such theorem is claimed by this calculation.

## What is and is not implemented

Finite stiffness supplies approximate flux localization, not a normalized state of exactly sharp flux. Infinite stiffness has a singular electric and energy cost; it is not a finite-resource physical constructor. The previous structural model, with relative links built solely from shared endpoint phases, avoids these independent cycle oscillators by changing the underlying degrees of freedom.

The next useful construction is therefore an explicit quantum endpoint-phase architecture, with its charging metric and source hopping operators, rather than another declaration that kappa is large. Its exact algebra can be tested even while its physical realization remains conditional. Alternatively, a finite-stiffness design must declare tolerances and prove error bounds.

## Verify

    uv run --with sympy python research/voevodsky/checkers/check_spinor_stiff_flux_limit.py

Receipt: `results/spinor_stiff_flux_limit.json`. Exact symbolic checks cover cycle rank, covariances, uncertainty saturation, Gaussian moments, the first quartic shift and harmonic tolerance/cost identities. This is not a numerical solution of the complete parent Hamiltonian or an experimental implementation.
