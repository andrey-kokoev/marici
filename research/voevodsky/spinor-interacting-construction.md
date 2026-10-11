# Interacting four-ray construction: classical state space and dynamics

## Completed scope

The existing hard-source-flux matter/link model now has an explicit classical interacting state space, Hamiltonian flow, symmetry action, observable contract and checked local/finite-amplitude dynamics. This is not a quantum four-level system, a retained linear ground doublet, or a derivation of tunneling.

The construction is conditional on beta=3/5, eta=1/5, fixed negative unit matter norm, hard constraints on the internal source faces, no matter hopping on exterior leads and no magnetic terms on exterior cycles. Inactive common-graph blocks remain at zero field. The physical implementation of the hard constraint is still open.

## State space

Locally the reduced phase space is CP^3 x T* T^3. Use normalized matter psi modulo its common phase, three exterior-loop angles theta and three independent lead fluxes ell; sum_i ell_i=-1. Retain lifted matter phases and angle histories when needed for spinorial signs and winding.

The four minimizing matter vectors are columns of

    B_ground=(r I+Q)/sqrt(1+r^2), K=I-Q,
    3r^4+6c*r^3-2c*r-3=0, c=beta/10.

They form a nonorthogonal coordinate basis:

    psi=B_ground a,
    a†G a=1, G=I+2r Q/(1+r^2).

They must not be declared orthogonal address states. Each minimizing ray has its own conserved optimal lead assignment ell=-(|psi|^2+1)/5. The full minimum set consists of four three-dimensional angle tori, not four isolated states. Its energy is 0.1798077094008586 before the separately chosen occupation baseline.

## Hamiltonian and evolution

Let rho_i=|psi_i|^2. The actual reduced Hamiltonian is

    H=<psi,K psi>+beta ||ell||^2/2
      +beta ||rho+ell||^2/8+eta/2.

The equations, modulo common matter phase, are

    i psi_dot=K psi+(beta/4)diag(rho+ell)psi,
    ell_dot=0,
    theta_dot_i=f_i-f_3,
    f_i=beta ell_i+(beta/4)(rho_i+ell_i), i=0,1,2.

Internal electric fields are reconstructed by

    E=B_internal^T(-rho-ell)/4.

Gauss, hard-flux tangency and signed current/reaction feedback agree with this reconstruction. The Hamiltonian conserves charge and energy. Source rotations act on matter with the retained binary phases and permute lead data; the central full rotation is -I on lifted matter. These symmetry maps exchange the ground sectors but are not inter-sector time evolution.

A crucial correction to the first electrostatic model is

    H=H_electrostatic+(5 beta/8)||ell+(rho+1)/5||^2.

The static electric optimum is valid for minimization. Imposing it anew along an arbitrary trajectory would violate ell_dot=0. Accordingly, `spinor-orbit-dynamics.md` remains a checked alternative electrostatic flow, not the final constrained dynamics.

## Dynamics checked

- Three numerically stable matter modes at each fixed-lead minimum: frequencies 0.00611206580804, 2.00611206580804 and 2.04974201753714 in model clock units.
- Three cyclic-angle zero directions with conjugate conserved-momentum Jordan chains. Momentum perturbations produce angle drift, not exponential matter growth.
- Fixed-lead reversible splitting has second-order energy-error scaling.
- Nonlinear trajectories checked over a complete linear slow period (1027.997 clock units) and a momentum-drift fixture. Deviations from tangent predictions scale quadratically with amplitude; tighter integration tolerances resolve those deviations.

Numerical spectra and trajectories are not exact spectral certificates or quantum excitation energies.

## Observable contract

Density, energy, retained lead flux and reconstructed internal field are ordinary reduced observables. Source-dressed coherences and currents require consistent gauge transport. Exterior-loop observables are exp(i theta), with lifted theta additionally recording winding. Common matter phase is not an observable on CP^3; phase-lift histories preserve the source rotation sign under the chosen convention. A small nonlinear angle displacement after one *linear* period is not by itself a closed-orbit Berry phase.

## Evidence map

1. `spinor-ground-orbit.md`: stationary-family classification and exact binary source rotation transport.
2. `spinor-orbit-dynamics.md`: nonorthogonal ground coordinates; initial electrostatic model and its explicitly stated limitation.
3. `spinor-constrained-leads.md`: full fixed-lead reduction and sector distinction.
4. `spinor-tangent-dynamics.md`: canonical tangent Hessian, coupled lead blocks and zero-mode structure.
5. `spinor-finite-dynamics.md`: nonlinear validation and detailed observable/history contract.

Fresh construction-chain verification:

    uv run --with numpy --with scipy --with sympy python research/voevodsky/checkers/check_spinor_interacting_construction.py

Receipt: `results/spinor_interacting_construction.json`. All nine stages run as fresh child processes in dependency order. The receipt records checker/result hashes and verifies downstream bindings. Three upstream receipts are retained and hashed, not re-proved; this is not repository-wide closure.

## Boundary of completion

The requested classical interacting construction is complete within the admitted model. No inter-sector hopping exists in that action. Quantization, physical charge/time normalization and any boundary interaction enabling transitions are distinct additional constructions requiring explicit input. The four-ray orbit alone supplies none of those choices.
