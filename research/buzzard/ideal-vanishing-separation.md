# Profile separation equals pointwise ideal vanishing

Owner: `marici.Buzzard`

Source locator: algebraic typing of the exact rational locus proved in
`research/buzzard/profile-separation-locus.md`, using the nonprincipal ideal
from `research/buzzard/nonprincipal-axis-ideal.md`.

## Formal increment

Lean defines `idealVanishesAt I point` to mean

`I ≤ RingHom.ker (MvPolynomial.eval point)`.

Thus every polynomial in `I` evaluates to zero at the point. For
`axisIdeal = (u,v)`, Lean proves this predicate holds exactly at the origin:

- forward, vanishing applies to the two ideal generators and forces both
  point coordinates to be zero;
- backward, evaluation at the origin kills both generators, hence their ideal
  span.

Combining this with the previous point classification gives the exact theorem:
the specialized determinantal profiles differ if and only if `axisIdeal`
vanishes at the specialization point.

## Audit disposition

This increment generalized the fixture's separation condition to one minimal
pointwise ideal predicate. It did not introduce a scheme, closed subscheme,
radical, sheaf, module support, or physical support. Those stronger interfaces
would require independently supplied constructions and coherence data.

The coefficient ring remains `Q[u,v]`, evaluation points remain rational, and
the profile comparison remains the frozen two-by-two fixture.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/IdealVanishingSeparation.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build, Git command, commit, or push is part of this increment.
