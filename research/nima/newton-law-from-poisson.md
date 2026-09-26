# Newton's inverse-square law from Poisson data

Next upstream audit: [graph action selection](graph-action-selection-audit.md)
constructs a retained variational comparison, but finds that locality,
composition and shift covariance still permit quartic alternatives. It does
not derive the Poisson assumption used here.

## Result and status

We no longer take the 1/r potential as a physical input to this derivation.
Instead we assume three-dimensional Euclidean space, Poisson's equation for
an isolated point source, and decay at spatial infinity. The mathematical
argument below determines Phi=-GM/r and hence the inverse-square acceleration.

The continuum argument is written mathematics. Agda checks its conditional
algebraic interface and radial coefficient consequences, NOT a real-analysis
implementation of the PDE, distributions, Gauss theorem or uniqueness. The
RRC history is likewise a parameterized implication, not an instantiated
formal proof about a real gravitational field. This distinction is essential.

## Explicit assumptions

Let K=GM, with G a supplied coupling and M a supplied source mass. Require:

1. Flat Euclidean R^3, with its ordinary Laplacian and spherical area 4*pi*r^2.
2. A locally integrable distributional solution Phi, smooth away from the
   origin, satisfying Delta Phi = 4*pi*K*delta_0 on ALL of R^3.
3. Phi(x) tends to zero as |x| tends to infinity, uniformly in direction.
4. To identify a gravitational acceleration, the additional coupling law
   a=-grad Phi. To call m*a a force, supply the inertial mass m and F=m*a.

The pure delta source rules out hidden dipoles or other singular multipoles.
Vacuum harmonicity outside the origin plus a total flux alone would NOT rule
those out. The origin is excluded from the point-particle acceleration formula.

Neither the value of G, Poisson's equation itself, nor the matter/acceleration
coupling is derived from RRC.

## Continuum derivation

### 1. Uniqueness and spherical symmetry

If Phi_1 and Phi_2 satisfy the same full distributional equation, h=Phi_1-Phi_2
is distributionally harmonic on all of R^3. Weyl's lemma makes h a smooth
harmonic function, including at the origin. Apply the maximum principle to
h and -h in balls, then send their radii to infinity. Decay implies h=0.

Every rotation of a solution has the same source and boundary condition, so
uniqueness forces rotational invariance. Write Phi(x)=f(r). This does not
assume spherical symmetry of an arbitrary exterior vacuum solution.

### 2. Vacuum integration: derive the radial form

For r>0, the spherical Laplacian gives

    0 = f''(r) + (2/r) f'(r) = (1/r^2) (r^2 f'(r))'.

Consequently r^2 f'(r)=C and f(r)=A-C/r. The 1/r dependence is therefore an
output of the three-dimensional vacuum equation, not a starting ansatz.

### 3. Source normalization fixes the coefficient

The distributional point source fixes outward flux through every sphere:

    4*pi*r^2 f'(r) = 4*pi*K.

Thus C=K. Equivalently, for f=A+B/r the flux is -4*pi*B, so B=-K. The vacuum
ODE alone could not select this sign or magnitude. The source equation does.

### 4. Boundary condition removes the constant

Decay at infinity forces A=0, giving the unique candidate

    Phi(x) = -GM/|x|.

It also exists: this function is locally integrable in three dimensions and
harmonic off the origin. For a compactly supported smooth test psi, integrate
Phi*Delta psi over |x|>epsilon. The inner boundary contribution is

    integral_{S_epsilon} [K/epsilon * partial_r psi
                         + K/epsilon^2 * psi] dS,

which tends to 4*pi*K*psi(0). This verifies the full distributional Poisson
equation, including the sign of the source. No additional delta derivatives
are introduced.

### 5. Acceleration and force

Using the separately supplied acceleration law,

    a(x) = -grad Phi(x) = -GM*x/|x|^3,
    |a| = GM/r^2                 (G,M nonnegative),
    F(x) = -G*M*m*x/|x|^3.

This derives Newton's point-mass law from the stated field equation,
geometric setting, source and boundary conditions. It is not a derivation
from pure logic or RRC, nor a derivation of the equality of inertial and
passive gravitational mass: the chosen acceleration coupling already embodies
that universality.

## Machine-checked portion

`agda/NewtonFromPoisson.agda` proves, over an arbitrary small commutative ring:

- cancellation of area from area*slope=charge when inverse area is supplied;
- inverse-square slope from normalized spherical Gauss data;
- equality to the negative reciprocal-radius primitive, conditional on a
  derivative/decay interface;
- the corresponding signed acceleration equality;
- an existing RRC `compare-rule` history retaining the boundary data and the
  derived equality to the candidate potential.

Its `Exterior` and `Calculus` records explicitly require reciprocal-radius
and inverse-area identities, a declared regular-function domain, the
reciprocal primitive derivative, decay and derivative-uniqueness facts.
Derivatives are applied only with a witness of membership in that domain.
`BoundaryData.gauss` explicitly supplies normalized Gauss law. These are not
postulates secretly asserted for reals: they are parameters to a safe theorem.
No real-valued instance of those interfaces has yet been constructed.

`agda/NewtonRadialCoefficients.agda` additionally checks the Laurent factor
n(n+1), its values at exponents 0,-1,-2, and the general integer-scaled theorem

    A=0 and -B=K  ==>  (A,B)=(0,-K).

It does not prove that every real vacuum solution is a Laurent polynomial;
completeness comes from the continuum ODE argument above, not a finite search.

## Exact computational checks and connection to the prior bridge

`checkers/check_newton_from_poisson.py` constructs derivative, radial
Laplacian and normalized-flux operations on finite Laurent polynomials. It
selects vacuum modes, applies decay, and solves the flux coefficient. Three
source/coupling cases, including zero mass, are evaluated at five exact
positive radii. These finite checks are not substituted for the ODE proof.

The following hostiles are rejected:

- positive rather than negative potential coefficient: wrong source flux;
- r^-2 rather than r^-1 potential: fails the 3D vacuum equation;
- an additive constant: preserves PDE and flux, violates decay;
- applying the 3D potential to the 2D radial Laplacian;
- evaluation at the singular origin.

Translation and linear superposition give the multiple-point-source potential.
The checker derives the coefficient of each source in the existing two-source
fixture BEFORE passing it to the prior polynomial differentiation route. Its
tidal result remains diag(-229,74,155)/1728. Thus the earlier 1/r input is now
supported by the field-equation derivation, without claiming that the whole
continuum-to-jet chain has been compiler-verified.

## Reproduce and audit

Run through the operator-authorized shell:

```powershell
pwsh -NoProfile -File research/nima/checkers/check_newton_from_poisson.ps1
```

Fresh Agda compilation of `NewtonRadialCoefficients` (including
`NewtonFromPoisson`) passed. Two deliberately false certificates fail with
`[UnequalTerms]`, exit 42: wrong vacuum exponent gives `2 != 0`, and wrong
normalized flux gives `12 != 11`.

Receipts:

- `results/newton-from-poisson.json`
- `results/agda-NewtonRadialCoefficients.json`
- `results/newton-poisson-formal-audit.json`

## Remaining boundary

The next formal obligation is an actual real-analysis/distributional instance
of the declared interfaces and a formal connection to the jet evaluator.
The next physical explanatory obligation is to justify Poisson's equation and
the acceleration coupling from additional principles. Neither obligation is
closed by this algebraic certificate.
