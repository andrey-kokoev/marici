# Hard-flux dynamics with conserved exterior leads — iteration 2

## Correction to the electrostatic dynamics

Freshly reading `spinor-orbit-dynamics.md` and the source matter/link and magnetic actions reveals a missing dynamical distinction. The source-face constraint has rank three on the internal K4. The electron block including its four exterior leads has six cycles. Thus constraining the source faces does **not** constrain all exterior-loop holonomies.

The existing model has no matter hopping on the exterior leads and no magnetic action involving those leads. Each oriented exterior-to-site electric flux ell_i is therefore conserved. Gauss fixes sum ell_i=-1 for this unit negative-charge sector.

The static electric minimum remains correct. Re-minimizing lead flux at every instant, however, is not the dynamics of this action. Iteration 1's electrostatic flow is a separate reduced-model assumption, not its full constrained reduction.

## Internal constraints and unique electric field

Write B for the four-by-six internal incidence, with -1 at the source and +1 at the target. The exact integer identities are

    B B^T=4I-ones,
    B C^T=0,
    B^T B+C^T C=4I.

Hard internal flux C A=0 requires C E=0 under the electric kinetic law. Gauss is

    B E+ell=-rho.

Together these fix

    E=B^T(-rho-ell)/4,
    ||E||^2=||rho+ell||^2/4.

There is no omitted internal electric circulation. For charge -1 the internal current/reaction equation is

    E_dot=J-C^T C J/4=B^T B J/4,
    rho_dot=-B J,
    ell_dot=0.

This agrees identically with the derivative of the reconstructed field. The checker tests these equations on independent normalized complex states, not just at equilibrium.

## State space and symplectic reduction

Choose the internal flat relative connection gauge A_internal=0. The source spinor connection Q is unchanged. The four remaining lead angles have three gauge-independent differences. Use x_i=A_lead,i-A_lead,3 for i=0,1,2, with ell_3=-1-sum_(i<3) ell_i. The common lead angle is gauge; after fixing the charge its canonical one-form contribution is a total derivative.

On this gauge slice the internal E dA term vanishes. The surviving canonical one-form consists of the original matter term and sum_(i<3) ell_i dx_i. Thus locally the physical reduced state space is

    CP^3 x T* T^3

for compact link angles, with phase lifts retained for histories. If link angles are treated as real covering coordinates, replace the torus by its cover. This describes the electron block with inactive graph blocks held at zero field. It does not count independent excitations in other blocks.

In ground-orbit coordinates psi=B_ground a, the CP^3 part retains the overlap metric G from iteration 1; it must not be replaced by four orthogonal address states.

The reduced Hamiltonian is

    H_ell(psi)=<psi,K psi>
       +beta ||ell||^2/2+beta ||rho+ell||^2/8+eta/2.

It is independent of the three x coordinates, so their momenta ell are conserved. At fixed ell the matter equation is

    i psi_dot=K psi+(beta/4) diag(rho+ell) psi

up to the common phase convention on the fixed-norm sphere. In orbit coordinates substitute psi=B_ground a and multiply by B_ground^dagger, with i G adot on the left.

The cyclic coordinate velocities are

    xdot_i=[beta ell_i+(beta/4)(rho_i+ell_i)]
           -[beta ell_3+(beta/4)(rho_3+ell_3)].

They can drift even though they do not enter the matter Hamiltonian. Keeping their conjugate momenta explains why a static electric elimination does not generally commute with time evolution.

## Relation to the static four-ray orbit

Completing the square on sum ell=-1 gives

    H_ell=H_electrostatic
          +(5 beta/8)||ell+(rho+1)/5||^2.

Hence the static optimal assignment is ell*(rho)=-(rho+1)/5. Each of the four ground rays b_i carries a different optimal ell^(i). Its matter equation at that assignment agrees with the electrostatic stationary equation up to a constant phase shift. Its cyclic velocities vanish because all four unconstrained lead derivatives equal -beta/4.

The full minima include the three arbitrary cyclic angles over each matter/lead assignment. They are not merely four points of the complete reduced state space.

Each fixed assignment ell^(i) has exactly one of the four previously classified rays as its global matter minimum: H_ell is bounded below by the electrostatic minimum, and equality requires both a minimizing ray and its matching lead assignment. Source rotations permute these four invariant momentum sectors rather than generate time evolution between them.

At beta=3/5, eta=1/5, fixing ell to its first-ray value gives

    first ray energy: 0.1798077094008586,
    each other orbit ray: 0.1828896072692989.

No transition between different conserved lead assignments is possible under this action. A bath, lead hopping, or magnetic terms on exterior cycles would be additional physical input, not a consequence of the orbit construction.

## Verification

    uv run --with numpy --with scipy python research/voevodsky/checkers/check_spinor_constrained_leads.py

Results: `results/spinor_constrained_leads.json`.

Integer incidence identities are exact. Numerical tests separately check Gauss reconstruction, reaction/current compatibility, completion of squares and all four own-sector stationary residuals. A perturbed fixture requires a nonzero instantaneous-optimum lead velocity (norm about 0.000588), contradicting the exact conserved-lead law if that optimum were enforced throughout its motion.

Fixed-lead Hamiltonian splitting over duration 2 has energy errors 2.81e-8 and 7.02e-9 at steps 0.02 and 0.01, with norm and reversal errors below 2e-14.

## Next

Completed in `spinor-tangent-dynamics.md`: numerical tangent spectra, the coupled Hamiltonian blocks and cyclic-coordinate Jordan chains. The remaining finite-amplitude validation is listed there.

Original next step: compute the tangent Hamiltonian and stability frequencies around each fixed-lead minimum, including how the cyclic coordinates and momenta enter the linearization. Quantization or inter-sector dynamics must be specified independently; this construction does not invent hopping between conserved sectors.
