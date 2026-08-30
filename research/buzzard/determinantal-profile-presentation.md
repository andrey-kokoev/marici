# The two-stage profile is presentation invariant

Owner: `marici.Buzzard`

Source locator: the presentation-invariance boundary developed in
`research/buzzard/entry-ideal-presentation.md`, now extended to the complete
two-stage object from `research/buzzard/two-by-two-determinantal-profile.md`.

## Formal increment

For two-by-two matrices over an arbitrary commutative ring, Lean proves:

- left or right multiplication can only decrease the determinant ideal;
- an explicit equation `leftInv * left = 1` makes the left transformation
  preserve the determinant ideal;
- an explicit equation `right * rightInv = 1` makes the right transformation
  preserve the determinant ideal;
- the corresponding two-sided transformation preserves the determinant ideal;
- together with the previously proved entry-ideal invariance, the complete
  `TwoByTwoDeterminantalProfile` is unchanged by `left * M * right`.

The determinant-ideal inclusions use exact determinant multiplicativity. The
reverse inclusions use the displayed inverse equations, not an untyped
“equivalent presentation” assertion.

## Assumptions and boundary

The coefficient type is any commutative ring. Matrices are exactly two-by-two,
indexed by `Fin 2`. The left inverse equation and right inverse equation are
separate assumptions in the orientations consumed by the proof.

This does not formalize arbitrary-size minor families, module presentations,
cokernel equivalences, or source-authorized presentation changes. It proves
that the bounded two-stage invariant has the algebraic transport property its
use requires.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/DeterminantalProfilePresentation.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build, Git command, commit, or push is part of this increment.
