# Interacting amplitudes in the four-ray ground basis — iteration 1

Successor: `spinor-constrained-leads.md` derives the hard-internal-flux reduction. Exterior lead fluxes are conserved, so the electrostatic flow below is not generally the full constrained dynamics. The four static ground rays carry different conserved lead assignments.

## Construction and scope

Starting from the freshly read `spinor-ground-orbit.md`, use its source conference gauge Q, K=I-Q, and minimizing root r. This constructs classical Hamiltonian dynamics for the **electrostatically reduced** functional, not yet a dynamical reduction of the full matter/link action and not a quantum theory.

The normalized ground vectors are the columns of

    B=(r I+Q)/sqrt(1+r^2).

They are independent but not orthogonal. The amplitude space is

    psi=B a,  a in C^4,
    G=B†B=I+2r Q/(1+r^2),
    a†G a=1.

The normalized lifts form a seven-real-dimensional sphere in this metric; quotienting the common phase gives CP^3. Retain lifts when computing spinorial phase histories. The four ground rays are four points in this projective space, not four orthogonal quantum alternatives.

G has two eigenvalues (r-1)^2/(1+r^2) and two (r+1)^2/(1+r^2). At the fixture its condition number is about 10818. Numerically evolve psi rather than repeatedly inverting this poorly conditioned metric. As c tends to zero and r tends to one, the basis becomes singular; it is not a uniform coordinate chart for that limit.

## Hamiltonian and symplectic structure

Pull back the usual complex-amplitude action using psi=B a:

    L=(i/2)(a†G adot-adot†G a)-H(a),
    H=a†B†K B a+c sum_i |(B a)_i|^4+c+eta/2,
    i G adot=B†[K B a+2c diag(|B a|^2)B a].

Here c=3/50, eta=1/5. Constants are extended off the unit sphere as constants; other extensions can change the common phase, not projective dynamics. A physical absolute-phase convention needs the original constrained action.

The equation conserves a†G a and H analytically. It is exactly the coordinate transform of

    i psidot=K psi+2c diag(|psi|^2)psi.

No orthogonalization that changes observables, guessed hopping matrix or fitted tunneling coefficient is introduced.

If T is a retained source rotation, its orbit-coordinate action is B^-1 T B. Since B is a polynomial in Q, it commutes with T, so this equals T in the matched source gauge. The metric and quartic functional are invariant under the source monomial rotations. The central action remains -I. Discrete source rotations map solutions to solutions; this is not a derivation of continuous rotation transport between tetrahedral addresses.

## What dynamics exists on the four rays themselves?

For each column b_i,

    [K+2c diag(|b_i|^2)]b_i=mu b_i,
    mu=<b_i,K b_i>+2c sum_j |b_ji|^4.

All four have the same mu. Thus their lifts evolve as exp(-i mu t)b_i, while each projective ray is fixed. Restricting to precisely the four ground rays yields no inter-address motion. Any proposed hopping or tunneling on that discrete set needs additional dynamics or a quantization prescription.

The surrounding CP^3 supports nontrivial interacting trajectories. For example, the normalized sum of two specified ground columns has energy 0.1801885595084202, above 0.1798077094008586. Classical superposition is allowed in the ambient amplitude space but does not preserve minimal energy.

## Verification

Run:

    uv run --with numpy --with scipy python research/voevodsky/checkers/check_spinor_orbit_dynamics.py

Results: `results/spinor_orbit_dynamics.json`. These are numerical checks, not replacement exact certificates for the preceding ground-state classification.

- Four stationary residuals below 2e-16.
- Twenty seeded amplitude fixtures verify the metric-transformed vector field, norm derivative and energy derivative.
- Exact onsite and kinetic subflows are composed symmetrically. Over duration 2, steps 0.02 and 0.01 give maximum energy errors 2.77e-8 and 6.93e-9: second-order scaling.
- Norm and time-reversal errors are below 1e-14 in these runs.

## Remaining executable work

Derive the constrained symplectic reduction of the complete hard-flux matter/electric action. Static minimization of the electric field alone does not prove that the displayed first-order dynamics is its exact reduction: longitudinal variables, gauge fixing and any remaining cycle electric modes must be accounted for. Then compute tangent stability of the ground rays in the admitted reduced model. Quantization and inter-ray transition amplitudes remain separate questions.
