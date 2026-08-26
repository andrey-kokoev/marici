# Variable count changes the principal-ideal interface

Owner: `marici.Buzzard`

Source locator: the warning that Smith-factor interfaces are
coefficient-ring dependent in `research/buzzard/fitting-rank-strata.md`, now
grounded by `research/buzzard/nonprincipal-axis-ideal.md`.

## Formal increment

Lean compares two exact coefficient types over the rationals:

- `Polynomial Rat`, the univariate polynomial ring `Q[X]`;
- `MvPolynomial (Fin 2) Rat`, the bivariate ring `Q[u,v]`.

Mathlib synthesizes `IsPrincipalIdealRing (Polynomial Rat)`. Lean then proves
that no `IsPrincipalIdealRing` structure can exist on the bivariate ring:
such a structure would make the already formalized coordinate ideal `(u,v)`
principal, contradicting `axisIdeal_not_isPrincipal`.

The combined theorem records both sides of the boundary. Thus a
principal-generator or Smith-normalization interface cannot be transported
between these coefficient rings merely because both are polynomial rings over
`Rat`.

## Claim boundary

This is a coefficient-type theorem, not a general classification of polynomial
rings. It does not construct Smith normal form, higher determinantal ideals,
module Fitting ideals, or a completion functor. It also does not assert that a
particular physical sector uses either coefficient ring; that requires a
source-authorized coefficient choice.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/CoefficientRegimeBoundary.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build, Git command, commit, or push is part of this increment.
