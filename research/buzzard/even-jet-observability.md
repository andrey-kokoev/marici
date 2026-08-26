# Even-jet observability

Owner: `marici.Buzzard`

Source locator: `Even seam jets are the first viable source test` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean represents a normalized formal jet as a rational sequence. Reciprocity
acts on order `n` by multiplication with `(-1)^n`. Every reciprocity-even jet
therefore has zero coefficients in every odd order.

The model six-component feature germ places coordinate `i` at normalized jet
order `2*i`. Lean proves each component is reciprocity-even and that the six
even orders `0,2,4,6,8,10` form the identity observation matrix. The resulting
observation map on six pairing parameters is exactly the identity and hence
injective.

Truncating at degree eight retains only five coordinates. The isolated
tenth-order parameter is nonzero but invisible to every retained observation,
giving an executable nonfaithfulness countermodel.

## Type-system consequence

Reflection of a reciprocity-even germ cannot manufacture opposite-point or
odd-jet information. A single structured germ can nevertheless supply a
faithful six-row packet when its even jets have full rank. This is an existence
and typing result only; it does not assert that the physical scalar Poisson
section supplies the required vector-valued feature germ.

The abstraction generalized the prior symmetric-square rank criterion to
formal local jets while preserving the missing source-constructor boundary.

## Boundary and missing interfaces

- a source-derived six-component Clark-module feature germ;
- analytic differentiability and convergence beyond formal jets;
- normalization relating derivatives to normalized jet coefficients;
- a proof that physical flux evaluation factors through these feature rows;
- control of even-jet rank throughout the intended spectral domain.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/EvenJetObservability.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
