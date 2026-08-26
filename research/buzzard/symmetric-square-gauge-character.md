# Symmetric-square gauge character

Owner: `marici.Buzzard`

Source locator: `The jet determinant is a relative gauge invariant` and `The
determinant lives in an orientation line` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean defines the symmetric-square representation of a rational `2 x 2` chart
change in the basis `(x^2,y^2,2xy)` and proves by exact determinant expansion
that its determinant is the cube of the original determinant.

For independent even and odd parity charts, the design-determinant character
is therefore the product of their determinant cubes. Lean verifies the exact
fixture with determinants six and thirty-five: the character is `9261000`,
and a local determinant four transports to `37044000`.

The orientation-reversing fixture has character `-1`, carrying four to minus
four. It preserves nonvanishing while reversing positivity. Lean packages this
as an existential hostile against chart-independent determinant positivity.

## Type-system consequence

The observability determinant is a relative invariant. Its nonzero locus is
stable under invertible chart transport, but its coordinate value and sign are
not intrinsic. A positivity claim requires an independently supplied
orientation of the determinant line or an orientation-preserving gauge group.

The abstraction generalized the even-jet rank test while preserving the
distinction between nonvanishing and positivity.

## Boundary and missing interfaces

- a typed determinant-line object rather than its rational coordinates;
- source authorization of parity-sector chart changes;
- a physical orientation or proof that admissible charts preserve one;
- the analytic feature germ whose local determinant is being transported;
- complex Hermitian chart transformations and their real determinant character.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/SymmetricSquareGaugeCharacter.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
