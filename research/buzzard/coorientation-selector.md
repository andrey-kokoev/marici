# Orbit separation requires a coorientation

Owner: `marici.Buzzard`

Source locator: `The minimal missing constructor is orbit-separating`, `The
selector is a coorientation, not a scalar constant`, and `Kernel birth can be
a selector-wall crossing` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean gives the two admitted boundary domains distinct constructors. A rational
coorientation assigns anti-invariant scores `(-t,t)`. Positive orientation
selects the injective domain, negative orientation selects the kernel domain,
and zero gives equal scores with no unique selection. Swapping the domains
negates the score, and negating any nonzero coorientation swaps the selected
domain.

The executable wall fixture has selected restricted-kernel dimension zero at
parameter one, no selected dimension at zero, and dimension one at minus one.
The bulk observation map remains the fixed map already formalized; only the
domain selector changes.

A synthetic asymmetric score `(1,2)` proves mathematical orbit-separating
sufficiency. Its asymmetry is explicit new data, not authority supplied by the
invariant boundary geometry.

## Type-system consequence

Orbit separation, source authorization, and executable realization are
different fields. A selector coorientation is sign-valued data: reversing it
reverses the choice, while its zero section selects neither. A kernel jump at
the selector wall is a domain transition and must not be mislabeled as bulk
rank degeneration.

This increment extends the Lagrangian ambiguity theorem with the smallest
typed symmetry-breaking constructor.

## Boundary and missing interfaces

- source authority for a physical coorientation or polarization;
- a continuous or analytic family of closed domains;
- proof relating the abstract two-choice selector to boundary subspaces;
- executable realization of the selected extension;
- Smith/barcode transport through a genuine selector wall.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/CoorientationSelector.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
