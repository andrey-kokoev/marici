# Joint spinor-density and electric relaxation with source flux retained

Successor: `spinor-ground-orbit.md` now exhausts the stationary families, proves the global minimum and checks the minimizing orbit's binary rotation transport. The bounds below remain valid as the earlier independent certificate.

## Result

With the exact source face-flux constraint and the existing beta=3/5, eta=1/5 fixture, the global pure-state matter/electric minimum lies in

    0.17940817039929 < E_min < 0.17980770940086

before adding a particle-sector charging offset. The bare coherent spinor costs 0.18. Explicit source-derived deformed states lie strictly below it, so retaining the native flux does not freeze the charged matter density in the bare doublet.

The interval is a certified GLOBAL bound over all normalized pure spinor amplitudes, not just the minimum of the trial family. The upper endpoint is attained by a feasible trial state; it is not claimed to be the exact global minimum.

## 1. Keep source holonomy, eliminate the field exactly

The exact relative flux law is C*A=0 modulo 2pi. On the four-vertex tetrahedral graph the relative connection is pure gauge, so choose A=0 while retaining the intrinsic +/-i source Wilson phases.

Use the actual reduced four-line kinetic operator from the spinor adapter. In normalized coordinates

    K_e=2(I-N_e), spectrum (0,0,2,2).

The four positive-polarization spectators in the raw eight-coordinate carrier remain at energy three and are not included as fabricated charged negative-face modes. This calculation relaxes the checked negative-face sector; extending populated phase-orthogonal sectors remains separate.

The existing common exterior graph has one lead per electron vertex. Its grounded electric Laplacian is

    L=5I-ones,
    L^-1=(I+ones)/5.

For a unit negative-charge density rho, the minimizing potential is phi_i=-(rho_i+1)/5. The checker reconstructs all six internal electric links and four exterior leads and verifies Gauss including exterior charge +1. Their full energy is

    H_E=beta*(1+sum rho_i^2)/10+eta/2.

Inactive proton and belt graph blocks remain present with zero minimizing charge and field. No background is changed to obtain this formula.

The complete fixed-flux functional is therefore

    F(psi)=<psi,K_e psi>
           +(beta/10)*(1+sum_i |psi_i|^4)+eta/2,
    ||psi||=1.

This is the joint matter/field minimization: electric energy responds to the deformed state, rather than being evaluated only on the original coherent spinor.

## 2. Explicit source-derived relaxation

Choose any face address and let e be its normalized line vector. Define w=(I-K_e)e. Source operator identities give

    <e,w>=0, ||w||=1,
    K_e e=e-w, K_e w=-e+w.

The three other face densities of w are exactly 1/3. This two-direction subspace is derived from the original operator, not an independently chosen two-level fit.

The normalized trial state (r*e+w)/sqrt(1+r^2) has

    t=r^2/(1+r^2) on the selected face,
    (1-t)/3 on each other face,
    H_matter=(r-1)^2/(1+r^2).

Writing c=beta/10, its exact energy is

    F(r)=(r-1)^2/(1+r^2)
         +c*[1+(r^4+1/3)/(1+r^2)^2]+eta/2.

The stationary scale satisfies

    3r^4+6c*r^3-2c*r-3=0.

Equivalently, the t-functional is strictly convex on 1/4<t<1/2, so there is one minimum in that interval. An exact rational bracket and midpoint give a feasible upper-bound state. The same construction is checked at all four source-equivalent face addresses.

For the retained fixture:

- selected-face density: 0.490386324555405;
- other-face density: 0.169871225148198 each;
- excited/dark carrier fraction: 0.000092431299099;
- energy: 0.179807709400859, below coherent energy 0.18.

The state keeps the source holonomy. Its lowering comes from density redistribution and a small positive kinetic deformation cost, not flattening the spinor connection.

## 3. Global certificate, not an assumed symmetric minimizer

For every pure normalized psi, form the symmetric tensor-square state psi tensor psi. The exact operator

    T=(K_e tensor I+I tensor K_e)/2
      +c*sum_i |ii><ii|

has expectation equal to H_matter+c*sum_i rho_i^2 on that tensor square. Its lowest energy on the WHOLE symmetric two-copy space is therefore a lower bound on the original pure-state functional. Allowing non-product vectors can only lower this certificate; no such vector is misidentified as an admissible single particle.

The checker constructs T in the inherited source-column basis on Sym^2(C^4), with metric m_i*m_j on diagonal pairs and 2*m_i*m_j on off-diagonal pairs. All entries lie in Q(sqrt(3),i). Weighted complex LDL positivity at an exact rational test energy certifies the lower bound, without a floating eigensolver.

Independent exact tensor-square fixtures verify the expectation identity. Adding c+eta/2 gives the certified lower endpoint 0.179408170399292. The feasible one-axis state gives the upper endpoint 0.179807709400859.

The certificate does not identify the global minimizing pure state or prove that the four-address trial family is exhaustive.

## 4. Common-sector comparison

With the preceding one-unit elementary occupation offset, the relaxed elementary energy is between 1.17940817039929 and 1.17980770940086 clock units. This is a separate charged matter/link branch, not a correction silently added to the neutral-oscillator model.

At the same beta and eta, the existing signed electric action gives:

    proton source/field correction = beta/24+eta/2 = 0.125,
    neutral belt source/field correction = 0.

These are corrections relative to their own unsourced particle baselines. Signed electromagnetic loading alone does not supply positive neutron nuclear rest energy or deuterium binding.

## Next state-level task

Determine the global pure-state minimizer and its rotation transport after density deformation. Retaining the source flux preserves the native K_e spectrum up to gauge, but the nonlinear charged ground is not automatically a fixed linear doublet.

The exact flux constraint also needs its physical implementation: the previous finite cosine-stiffness action does not enforce it exactly. Neither task is replaced by scaling the energy interval to a measured electron mass.

## Verify

    python research/voevodsky/checkers/check_spinor_fixed_flux_relaxation.py

Results: `results/spinor_fixed_flux_relaxation.json`. Exact tests cover source reduction, electric inverse and complete lead flux, four-address trial identities and stationarity, symmetric tensor expectation, and the global positive-operator certificate. No masses select beta, eta or the trial state.
