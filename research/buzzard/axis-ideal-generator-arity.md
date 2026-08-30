# The coordinate ideal needs exactly two displayed generators

Owner: `marici.Buzzard`

Source locator: bounded generator-count sharpening of
`research/buzzard/nonprincipal-axis-ideal.md`.

## Formal increment

Lean defines the explicit family

`axisGeneratorFamily : Fin 2 → Q[u,v]`

with values `u` and `v`, and proves its range is exactly `{u,v}`. Therefore
its ideal span is `axisIdeal`.

Lean also proves that every family indexed by `Fin 1` has singleton range. If
such a family generated `axisIdeal`, the ideal would be principal, contradicting
the previously proved `axisIdeal_not_principal` theorem.

The combined theorem records that two explicit generators suffice and no
one-element indexed family suffices.

## Audit disposition

“Generator arity two” here has only this bounded meaning. The increment does
not define a global minimal-generator cardinal, compute a cotangent-space
dimension, invoke Nakayama's lemma, or generalize to arbitrary ideals. Those
would be stronger interfaces requiring additional independent motivation.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/AxisIdealGeneratorArity.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build, Git command, commit, or push is part of this increment.
