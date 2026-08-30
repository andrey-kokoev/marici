# Finite-part extraction does not preserve positivity

Owner: `marici.Buzzard`

Source locator: `Relative detector exists; relative positivity does not` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

`SymmetricLaurentWindow` records coefficients of the regulated expression

`pole / epsilon^2 + constant + tail * epsilon^2`.

Its finite part is the constant coefficient. The exact hostile window has
coefficients `(1,-2,1)`. Lean proves that for every nonzero real `epsilon`, its
evaluation equals

`(epsilon⁻¹ - epsilon)^2`

and is therefore nonnegative. Lean also proves its finite part is `-2`, hence
strictly negative.

The resulting existential theorem states directly that pointwise positivity
of every regulated value does not imply positivity of the extracted finite
part.

## Type-system consequence

Finite-part extraction supplies a scalar value but not an order-preserving
map. A detector constructed by subtraction and finite-part regularization
therefore has no positivity or nonvanishing authority unless a separate
ordered structure and preservation theorem are supplied.

## Boundary and missing interfaces

This is a three-term real Laurent window, not a formal Laurent-series or
asymptotic-expansion library. A faithful regulator theorem still needs:

- the regulator family and normalization condition;
- the derived boundary-current subtraction;
- existence and uniqueness of the asymptotic expansion;
- a typed finite-part operator on the admitted expansion class;
- regulator-universality of the constant term;
- a separately justified order cone if positivity is later required.

The theorem does not challenge existence of the relative detector or equality
of its finite part with a source scalar. It rejects only the unauthorized
transport of positivity through finite-part extraction.

The abstraction generalized the order failure and specialized its proof to
the exact literal-square hostile.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/FinitePartPositivity.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without warnings or diagnostics. No site build
or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/FinitePartPositivity.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/finite-part-does-not-preserve-positivity.md`
