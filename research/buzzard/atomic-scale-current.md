# Atomic scale-current packet

## Grothendieck source

This formalizes the finite-cutoff incidence core of
`research/grothendieck/theta-primitive-and-square-incidence-are-atomic-scale-currents.md`.

## Formal objects

- a labelled source is a finitely supported function `Label ->₀ R`;
- `atomicScalePushforward` is the pushforward along the source scale map;
- weights with the same scale are added;
- `currentReadout` pairs a finite current with a test function;
- `currentReadout_atomicScalePushforward` proves exact finite-cutoff
  evaluation before or after incidence pushforward;
- `finiteSineReadout_pushforward` specializes to the odd sine character;
- `ExponentialScaleCurrent` and `TemperedScaleCurrent` keep primitive and
  square completion targets as distinct types;
- the collision hostile gives a nonzero two-label packet whose pushed current
  vanishes when both labels share one scale.

## Assumptions and coefficient types

The general finite theorem uses decidable label/scale equality and a
commutative semiring. The sine specialization uses real coefficients. The
collision hostile uses exact integers.

## Missing source and completion interfaces

The sector must still instantiate labels `(p,k)`, scales `k*log p`, and
weights `(1/k)*p^(-k/2)`, including primality and finite cutoff conventions.
The finite theorem does not establish the infinite growth estimates:
primitive current requires an exponential/Laplace test rigging, whereas the
square current is tempered but not finite. No coercion between those wrapper
types is provided.

The undamped sine character is outside both asserted completed pairings at
the critical boundary. Archimedean/modular relative completion must supply
that readout. Label-scale injectivity or a richer graded current is required
to exclude the collision hostile. Infinite scalar compression and RH remain
gated.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
