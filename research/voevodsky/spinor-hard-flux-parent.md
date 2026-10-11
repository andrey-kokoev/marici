# Parent action and quantum boundary of hard source flux — iteration 2

## Result

An ideal constrained parent action reproduces the classical fixed-lead reduction. The three independent coordinate-flux constraints and their three electric tangency constraints are **second class**. Reducing them changes the link brackets; they cannot both be imposed as annihilation conditions on a normalized state in the ordinary unconstrained quantum link Hilbert space.

This supplies a consistent mathematical parent and structural implementation, not a finite-resource physical device. The conditional quantum model in `spinor-quantum-leads.md` remains a quantization of the reduced system, not a proven exact sector of the finite-stiffness parent.

## 1. Explicit local parent action

Let B be the internal incidence and D any three independent rows of the sourced face incidence C. Use the inherited phase-dependent matter Hamiltonian H_m(psi,A), six internal pairs (A,E), four lead pairs (a,ell) and charge -1. In a local unwrapped chart near relative face flux zero, take

    S=integral dt [ (i/2)(psi† psidot-psidot† psi)
          +E dot Adot+ell dot adot
          -H_m(psi,A)-beta(E^2+ell^2)/2-eta/2
          -lambda^T D A-alpha^T(B E+ell+rho) ].

The exterior Gauss condition fixes sum ell=-1 at unit matter norm. The alpha terms generate site gauge transformations. Their signs here give Adot=beta E+B^T alpha and adot=beta ell+alpha. The source hopping phases are fixed data inside H_m; D A constrains only relative dynamical flux.

Variation of lambda enforces D A=0. Globally use compatible charts of the compact flat subtorus C A=0 modulo 2pi, or parameterize that subtorus structurally. A bare real multiplier times a globally undefined angle is not a global compact action.

Tangency gives

    D Adot=beta D E=0.

Preservation of D E=0 fixes the reaction multiplier. Since E_dot=J-D^T lambda for charge -1,

    lambda=(D D^T)^-1 D J,
    E_dot=P J,
    P=I-D^T(D D^T)^-1 D=B^T B/4.

This works for every current, not just the coherent circulation. B P=B, so the reaction preserves Gauss. Its power E^T D^T lambda vanishes on the constraint surface.

## 2. Constraint classification and reduced brackets

For chi=D A and pi=D E, the Poisson matrix is

    Omega=[[0,W],[-W,0]], W=D D^T.

For the selected three tetrahedral faces, W has diagonal 3 and off-diagonal -1. Its determinant is 16; det Omega=256. Thus all six constraints are second class for nonzero beta. They remove three canonical cycle pairs, not six gauge symmetries. The site Gauss constraints commute with these face constraints and remain first class.

The Dirac bracket is

    {A,E}_D=P,
    {A,A}_D={E,E}_D=0.

After fixing the internal pure-gauge connection A=0, Gauss and tangency uniquely give

    E=B^T(-rho-ell)/4.

Their electric energy is beta||rho+ell||^2/8, reproducing iteration 2 of the classical construction. The four leads remain, with three independent holonomies and conserved momenta. No missing exterior constraints have been supplied by this action.

## 3. Structural exact implementation

An alternative definition of the ideal configuration space is

    A=B^T u modulo 2pi,
    U_ij=U_source,ij exp(i(u_j-u_i)).

Every relative face Wilson loop is identically one because C B^T=0. The intrinsic source +/-i phases remain. Substituting this parameterization into the canonical one-form and quotienting the site gauge redundancy gives the same constrained configuration model. Any electric circulation in the unreduced parameterized action has no canonical velocity partner and is eliminated by its quadratic stationarity equation.

This is a way to **define** a system without independent internal cycle coordinates. It is not evidence that a network of independent physical links acquires that identity at finite stiffness. A physical constructor would have to realize shared endpoint phases and the required hopping coefficients without adding independent loop modes, or justify their elimination quantitatively.

## 4. Why naive quantum projection fails

On a local canonical core, quantizing the unreduced pairs gives

    [chi_a,pi_b]=i hbar W_ab.

In particular W_aa=3. A normalized vector cannot satisfy chi_a|state>=0 and pi_a|state>=0 simultaneously on the common operator domain: the expectation of their commutator would be both zero and 3i hbar.

Compact-angle operators require global care, but the coordinate-flatness obstruction has a separate global form. In L2(T^6) with Haar measure, the relative-flat configuration subtorus has codimension three and measure zero. A square-integrable wavefunction supported exactly there is zero. Delta-supported states are distributions, not normalized vectors in that Hilbert space.

The reduced quantization uses the induced measure on a different configuration space and the reduced brackets. It does not evade the uncertainty principle by hiding a delta-function state in the parent Hilbert space. Group averaging gauge constraints is also not a substitute: these face/tangency constraints are second class, not additional gauge generators.

This rules out an ordinary common-kernel implementation in the stated continuous-link representation. It does not rule out a structurally constrained system, an appropriate limiting theory, a different finite-group model, or approximate flux localization.

## Verify and next gate

    uv run --with sympy python research/voevodsky/checkers/check_spinor_hard_flux_parent.py

Receipt: `results/spinor_hard_flux_parent.json`. Exact matrix tests cover incidence, the constraint Poisson matrix, Dirac brackets, arbitrary-current reaction and complete internal Gauss reconstruction. The measure-zero argument is analytic, not a finite-grid test.

Next quantify a finite-stiffness parent: cycle-flux variance, electric energy and zero-point cost. Determine which subtraction and limiting prescription, if any, can approach the reduced theory. Until that or an actual structural constructor is supplied, physical implementation remains open rather than being declared complete by a multiplier alone.
