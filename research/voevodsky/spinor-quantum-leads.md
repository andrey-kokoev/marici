# Conditional quantization of the reduced hard-flux model — iteration 1

## Explicit choices, not inferred physical facts

Freshly read `prior-quantization-and-hard-flux-search.md`. Reuse its compact-rotor conventions, but distinguish a quantization prescription from a physical derivation.

Choose hbar=1 in the supplied model units, periodic untwisted lead-angle wavefunctions, and one matter occupation in four orthonormal source modes. This is a level-one choice for the matter projective carrier. Single-occupation bosonic and fermionic constructions agree here; no multiparticle statistics is selected. Use the electric energy as a square of charge operators. Quantize the already reduced Hamiltonian, not an as-yet-proved quantum parent reduction.

Neither the classical ground-ray basis nor the spinorial full-turn sign forces these choices. In particular a twist of the rotor boundary conditions, a different action normalization or a different ordering would define a different candidate.

## Hilbert space and self-adjoint Hamiltonian

The Hilbert space is

    H=C^4 tensor l2({ell in Z^4 : sum ell=-1}).

Using ell_0,ell_1,ell_2 as independent momenta identifies its rotor part with L2(T^3), with ell_3=-1-ell_0-ell_1-ell_2. The site number operators are N_i=|i><i|, so sum N_i=I and N_i^2=N_i.

Quantize the reduced electric expression without discarding charge fluctuations:

    Hhat=K+(beta/2)sum ell_i^2
         +(beta/8)sum(N_i+ell_i)^2+eta/2.

Each Fourier sector is an exact four-dimensional block

    H_ell=K+(beta/4)diag(ell)
          +[5 beta ||ell||^2/8+beta/8+eta/2]I.

All ell commute with Hhat. Its domain consists of sequences for which sum_ell ||H_ell psi_ell||^2 is finite; the finite-support Fourier vectors form a core. Hermitian finite blocks with uniform positive quadratic growth in ell define a bounded-below self-adjoint direct sum with compact resolvent. Time evolution is the direct sum exp(-it H_ell), not a nonlinear wavefunction equation and not a four-state hopping ansatz.

Sector superpositions are allowed. Conserved flux does not by itself impose a quantum superselection rule for every possible observable. Nevertheless this Hamiltonian supplies no transitions between its flux sectors.

## Why classical density squared is not a one-particle operator square

For a sharp lead assignment and a normalized matter vector with density rho,

    <sum N_i^2>=1,
    sum <N_i>^2=sum rho_i^2.

Consequently

    <Hhat>-H_classical(psi,ell)
       =(beta/8)[1-sum rho_i^2].

The difference is the retained charge variance, not an adjustable baseline. Replacing N_i^2 by the normal-ordered N_i(N_i-1) would remove all single-occupation self terms and change the prescribed electric Hamiltonian. The old nonlinear four-ray minima are not automatically eigenstates of this quantum model.

## Global ground space without a rotor cutoff

Take beta=3/5, eta=1/5. On the integer lattice sum ell=-1, the norm square ||ell||^2 is a positive odd integer. Its minimum one occurs precisely at the four assignments ell=-e_i. Every other assignment has ||ell||^2>=3.

Since K is positive and min ell_i>=-||ell||^2 for integer ell,

    H_ell >=(3 beta/8)||ell||^2+beta/8+eta/2.

Every nonminimal flux block therefore has energy at least 17/20=0.85. This excludes the entire infinite complement analytically; no finite flux cutoff is used.

In a minimal block define v=beta/4. After subtracting its scalar offset, the operator is K-v|i><i| with characteristic polynomial

    x(x-2)[x^2-(2-v)x-v].

Its lowest eigenvalue is simple. The ground matter vector is proportional to

    (r_q I+Q)e_i,
    r_q=(v+sqrt(v^2+4))/2.

The common ground energy is exactly

    E0=(59-sqrt(1609))/40
       =0.4721914439934211...

before any occupation baseline. The selected-face probability is approximately 0.5373949741, not the classical 0.4903863246.

The full ground vectors are these matter vectors tensor |ell=-e_i>. They are orthogonal because their lead Fourier states are orthogonal, even though their matter factors overlap. The ground multiplicity is four. Source rotations permute both factors and retain their binary matter phases. This construction does not produce a preferred quantum ground doublet.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_spinor_quantum_leads.py

Receipt: `results/spinor_quantum_leads.json`. Exact symbolic checks verify the source conference algebra, all four block characteristic polynomials and ground vectors, ordering examples and the strict global energy comparison. The infinite-lattice exclusion follows from the integer norm bound above. No measurement or empirical mass sets a coefficient.

## Remaining hard-constraint implementation

This completes one explicit candidate quantization of the reduced model, not the requested physical implementation. Next construct a parent action with face-flatness multipliers, classify its constraints and compare its reduction with this Hilbert space. In particular exact coordinate-flatness states in an ordinary continuous-link L2 space require care: one cannot insert a formal delta-function state and call it a normalized quantum ground state. Finite stiffness and reduction-before-quantization must be compared rather than equated.
