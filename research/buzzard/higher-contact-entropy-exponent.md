# Higher-contact Hermite entropy exponent: Lean packet

## Source boundary

This increment formalizes the convention-fixed exponent classifier in
Grothendieck's `higher-contact-hermite-negative-mass-law.md`.

## Formal objects and coefficient types

The contact multiplicity is a natural number `m`; its even spatial order is
`2*m`. Exponents are rational. `hermiteNegativeMassExponent m = m + 1/2`, and
`exponentFromContactOrder r = (r+1)/2`.

## Theorems and hostile

- `exponentFrom_evenContactOrder` identifies the two parameterizations.
- `hermiteNegativeMassExponent_injective` proves the exponent determines the
  contact multiplicity.
- The quadratic, quartic, and sextic examples give `3/2`, `5/2`, and `7/2`.
- `distinctSectors_same_contactExponent_hostile` assigns the same quadratic
  contact to two distinct Boolean sectors; their exponent agrees.

The hostile prevents a universal local heat normal form from being promoted to
sector identity or source-selection authority. The exponent classifies an
observed contact; it does not exclude the contact.

## Missing analytic interfaces

The source theorem still needs a smooth finite contact with first nonzero jet
of order `2m`, the backward heat-semigroup action on that jet, the physicists'
Hermite normalization, negative intervals for every positive even Hermite
polynomial, parabolic rescaling of the negative-mass integral, and control of
the little-o remainder. Identifying this local heat profile with a Newman or
theta flow would require an additional sector bridge and is not assumed.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/HigherContactEntropyExponent.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
