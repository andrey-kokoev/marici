# The coordinate ideal in `Q[u,v]` is nonprincipal

Owner: `marici.Buzzard`

Source locator: the non-PID coefficient-ring boundary in
`research/strominger/distinction-preserving-completion.md`, and the missing
interface explicitly recorded in `research/buzzard/fitting-rank-strata.md`.

## Formal increment

Lean works in the concrete commutative domain
`MvPolynomial (Fin 2) Rat`, with coordinate variables `u = X 0` and `v = X 1`.
It defines `axisIdeal = Ideal.span {u,v}` and proves:

- `axisIdeal` is proper, using evaluation at the origin;
- `u` does not divide `v`, using evaluation at `u = 0, v = 1`;
- no polynomial generates `axisIdeal` as a singleton ideal;
- equivalently, `axisIdeal` fails Mathlib's native
  `Submodule.IsPrincipal` predicate;
- the first determinantal ideal of `diag(u,v)` is exactly `axisIdeal`.

The contradiction is structural. If a generator `g` existed, then `g` would
divide both `u` and `v`. Properness makes `g` a nonunit. Since `u` is prime,
Mathlib's irreducibility divisor theorem makes `g` associated to `u`, forcing
`u` to divide `v`, contrary to the explicit evaluation countermodel.

## Assumptions and boundary

The coefficient type is exactly `Rat`; there are exactly two variables indexed
by `Fin 2`. Primality of a multivariable coordinate uses Mathlib's theorem for
polynomials over a cancel-multiplication nontrivial coefficient ring.

This proves one concrete ideal is nonprincipal. It does not install a global
`Not (IsPrincipalIdealRing Q[u,v])` instance, formalize higher Fitting ideals,
or prove module-presentation invariance. No geometric or physical source
interpretation is inferred from the algebraic obstruction.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/NonprincipalAxisIdeal.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build, Git command, commit, or push is part of this increment.
