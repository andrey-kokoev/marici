# Endpoint-rotor quantum constructor — iteration 4

## What is constructed

An explicit ideal quantum architecture implements relative face flatness as an operator identity, rather than a large-energy penalty. Its gauge-invariant subspace is unitarily equivalent to the reduced quantum model of `spinor-quantum-leads.md`. Thus quantization and reduction agree for this specifically defined endpoint model.

This is not a proof that the independent-link finite-stiffness parent converges to it, nor a demonstrated physical apparatus. It changes the elementary field degrees of freedom: endpoint phases replace independent internal link phases. The freshly read stiffness audit explains why that distinction matters.

## Degrees of freedom and Hamiltonian

Use four endpoint rotors with integer momenta n_i and bilateral unitary raising operators R_i, and four lead rotors with integer momenta ell_i. Retain one matter occupation with basis |i>, N_i=|i><i|. Restrict the conserved totals to sum n_i=0 and sum ell_i=-1.

The local gauge generators and assisted matter transfers are

    G_i=n_i+ell_i+N_i,
    T_ji=|j><i| R_i R_j^dagger.

A transfer i to j lowers N_i and raises N_j while raising n_i and lowering n_j. Hence every G_i is preserved. The Hamiltonian is

    H_endpoint=sum_ij K_ji T_ji
               +(beta/8)sum_i n_i^2
               +(beta/2)sum_i ell_i^2+eta/2.

For i=j the transfer is simply N_i. Reverse transfers are adjoints and K is Hermitian, so the matter term is Hermitian. The rotor shifts are untruncated bilateral shifts, not finite matrices with a falsely exact phase-number algebra. Charging terms are positive and the assisted hopping is bounded; the usual charging-operator domain supplies a self-adjoint Hamiltonian.

The charging ratio beta/8 versus beta/2 is specified to reproduce the reduced electric metric. It is a physical design input, not selected by gauge symmetry alone.

## Exact relative flatness without independent cycle oscillators

For directed negative-charge transport define its relative link operator by R_i R_j^dagger. Along every closed face the endpoint operators telescope:

    (R_i R_j^dagger)(R_j R_k^dagger)(R_k R_i^dagger)=I.

This holds on the entire endpoint-rotor Hilbert space. It requires neither an infinite penalty nor simultaneous sharp conjugate operators. The intrinsic source factors are separate: the normalized Q_ji coefficients on the chosen oriented faces retain Wilson phases +i; reversing orientation conjugates them. The overall kinetic hopping sign is not mistaken for the intrinsic transport phase.

There are no independent internal cycle coordinates to excite. This is the structural mechanism enforcing the hard relative flux. Adding independent link phases would invalidate the identity and return to a different model.

## Physical subspace and exact reduction map

Impose the first-class site gauge conditions G_i=0. Unlike exact coordinate-flatness in independent-link L2 space, these integer-charge conditions have a nonzero normalizable kernel. They can be defined by compact gauge averaging. Whether a device prepares and preserves that sector is an additional operational question.

A complete physical orthonormal basis is

    |i; n=-ell-e_i; ell>, sum ell=-1.

Define W from the reduced Hilbert space by

    W(|i> tensor |ell>)=|i; -ell-e_i; ell>.

This is a bijection of orthonormal bases and hence a unitary map onto the physical subspace. Assisted hopping sends that basis vector to |j; -ell-e_j; ell> with exactly coefficient K_ji. Moreover

    (beta/8)||-ell-e_i||^2+(beta/2)||ell||^2+eta/2
      =5 beta||ell||^2/8+beta/8+(beta/4)ell_i+eta/2.

Therefore W^dagger H_endpoint W is exactly the previously quantized H_ell, including its number-square term. The identity holds for the whole integer lattice, not only the four ground blocks. Unitary dynamics, conserved flux and the four-dimensional ground space transfer through W.

No claim about the quantization of arbitrary alternative classical extensions is needed: this is a concrete quantum parent for the specific prescription already chosen.

## Implementation obligations not removed by algebra

A physical realization would have to supply:

1. Four shared endpoint phase degrees of freedom rather than six independent internal phases.
2. The six assisted transfers with the source magnitudes, complex phases and diagonal terms.
3. The declared endpoint/lead charging forms and physical action/time units.
4. Preparation in the chosen total-charge and G_i=0 sector, and bounds on gauge-breaking errors.
5. Control of extra device modes and independent-loop phases.

Finite gauge penalties could be added for approximate sector preparation, but they are not automatically exact protection against uncontrolled perturbations. No circuit parameters, hardware measurements or microscopic source construction currently establish these obligations. The result is an exact Hamiltonian specification, not evidence of a completed laboratory implementation or a natural electron model.

## Verify

    uv run --with sympy python research/voevodsky/checkers/check_spinor_endpoint_constructor.py

Receipt: `results/spinor_endpoint_constructor.json`. Exact symbolic tests verify charge-neutral assisted transfers, Hermitian reverse coefficients, telescoping relative loops, retained source Wilson phases and the unrestricted charging/intertwining identity. Integer fixtures include fluxes far outside the ground blocks without truncating the representation.

Completed successor: `spinor-quantum-implementation.md` consolidates the freshly verified quantum chain and physical acceptance contract. The endpoint architecture closes the ideal algebraic implementation; a physical platform still needs evidence, not another rename of the Hamiltonian.
