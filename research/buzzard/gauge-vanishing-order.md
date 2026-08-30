# Regular gauge preserves vanishing order

Owner: `marici.Buzzard`

Source locator: `The observability divisor includes multiplicity` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean models a local rational polynomial germ's seam order by
`Polynomial.natTrailingDegree`. It proves generally that multiplication by a
character germ with nonzero constant coefficient preserves the vanishing
order of every nonzero determinant germ.

It also proves that multiplication by `X^2` adds exactly two to the order.
For the stated fixture

`D = X^4 * (1 + 2*X^2)` and `c = 3 + X^2`,

both `D` and `c*D` have order four. The singular factor `X^2` changes the
product order to six. An existential hostile packages the failure when the
regularity premise is omitted.

## Type-system consequence

The vanishing locus and its multiplicity transport only through chart factors
that are units at the seam. A presentation factor vanishing at the seam is not
an admissible gauge and can manufacture a false exceptional depth.

This increment generalized the determinant nonvanishing theorem to local
multiplicity while making regularity an explicit independent premise.

## Boundary and missing interfaces

- analytic or formal-power-series germs beyond polynomial fixtures;
- a typed local-unit predicate for the physical gauge category;
- the source-derived observability matrix or determinant-line section;
- comparison between polynomial trailing degree and analytic zero order;
- local Smith data beyond aggregate determinant order.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/GaugeVanishingOrder.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
