# Two Newtonian construction paths, one retained RRC comparison

Successor: [Newton's law from Poisson data](newton-law-from-poisson.md)
derives the previously supplied 1/r potential mathematically from the field
equation and boundary conditions, with a separately scoped conditional Agda
certificate. It does not claim a compiler-checked continuum PDE proof.

## What changed

The first bridge certified a supplied tidal formula. This successor compares
that formula with an independently constructed second-order jet of the
Newtonian potential. Both routes use the existing two-source fixture and G=1.
The result is still diag(-229,74,155)/1728.

## Potential route

For one source at r*n, use dimensionless observer coordinates u=x/r. With
|n|=1, write

    |u-n|^2 = 1+t,   t = -2 n.u + u.u.
    P = 8 - 4t + 3t^2.

`agda/NewtonianPotentialJet.agda` constructs the coordinates, squared distance,
and P by constant, addition, scaling and multiplication of second jets. The
multiplication rule includes both mixed first-derivative terms. It does not
call the direct geometric tensor routine.

`agda/NewtonianTidalRoutes.agda` checks, for BOTH fixture sources:

- P(0)=8, selecting the positive reciprocal-radius branch;
- every value, gradient and Hessian entry of P^2*|u-n|^2 equals that of 64.

Thus P/8 is a verified local inverse-radius jet. Multiplying by -m/r and
converting two u derivatives to x derivatives gives the m/r^3 scale. The
formal output uses common denominator 8*1728=13824; integer arithmetic does
not silently divide coefficients.

The geometric route separately computes m/r^3*(delta_ij-3*n_i*n_j). Agda
checks all nine entries of

    potentialTotal8(a,b) = 8 * tidal(a,b).

This is a fixed-fixture equality of two exact constructions, not a theorem
for all masses and positions. No equivalence of all integer tensors under
multiplication by eight is asserted: both compared outputs already share
the same denominator.

## RRC comparison

The two complete packages have different retained route tags, the actual
source values and the common denominator. Existing `compare-rule` uses the
identity equivalence of their interpreted tensor types and the independently
proved value equality. Existing `Pi-rule` retains the comparison together
with radial normalization, reciprocal checks and the earlier affine-law
witness. `reify-history` retains the combined history, with a checked recovery
identity. Equal outputs do not erase their distinct presentations.

The interpretation of jets as derivatives, their product/chain rules and the
Newtonian potential are explicit mathematical/physical inputs. No real-analysis
formalization proves that the implemented jet operations are derivatives of
arbitrary real functions. No general uniqueness theorem for reciprocal jets
is formalized here. The checked residual and positive branch verify the
chosen local expansion; they do not derive Newton's law or global dynamics.
RRC still receives the constructed proofs rather than inventing them.

## Independent computational route and hostile checks

`checkers/check_newtonian_potential_routes.py` performs truncated multivariate
polynomial multiplication using Fraction coefficients in physical x
coordinates, then extracts the Hessian from polynomial coefficients. It uses
neither the Agda jet product implementation nor the direct geometric formula
in its potential route. It agrees with the existing evaluator on both
`sources_a` and `sources_b`, and on a non-axial (3,4,0) source that exercises
nonzero mixed derivatives. Incorrect quadratic coefficient and potential sign
are rejected. The Python comparisons share Fraction arithmetic.

The formal negative controls reject a wrong tensor entry, wrong reciprocal
normalization, and omission of the second product-rule cross term: the second
derivative of x*x is 2, not 1. These are compiler type mismatches, not import
or runner failures.

## Reproduce

```powershell
pwsh -NoProfile -File research/nima/checkers/check_newtonian_tidal_bridge.ps1
```

The shell runner freshly checks BOTH positive Agda modules and all three
expected-failure modules, and runs the exact Python comparisons. Receipts:

- `results/agda-NewtonianTidalRoutes.json`
- `results/newtonian-potential-routes.json`
- `results/newtonian-tidal-formal-audit.json`

This deepens the existing fixed calculation into a checked local
potential-versus-geometry comparison. General Newtonian equivalence,
continuum differentiation, experimental validation and gravitational
emergence remain outside its scope.
