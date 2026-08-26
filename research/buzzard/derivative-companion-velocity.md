# Derivative companion velocity packet

## Grothendieck source

This formalizes the exact finite-coordinate content of
`research/grothendieck/theta-derivative-companion-is-defect-velocity.md`.

## Formal objects

- `ComplexCoordinates R` avoids importing analytic structure into the
  algebraic identity.
- `orientedDerivativeCompanion A D` represents `A+iD`.
- `reflectedDerivativeCompanion A D` represents `A-iD`.
- their componentwise sum is `2A`, the division-free symmetric projection.
- `verticalNormVelocity` is the coordinate value of `∂_y |A|²` once the
  analytic source supplies `∂_y A=iD`.
- `derivativeCompanion_norm_difference` proves the exact factor-two identity.
- `oriented_companion_survives_simple_real_crossing` proves that `A=0` does
  not erase a nonzero real derivative direction.

## Assumptions and coefficient types

The algebraic identities hold over any commutative ring. Survival of a simple
crossing additionally needs a nontrivial ring. No order or topology is used.

## Hostile and analytic gates

The integer hostile has vertical velocity `-2` and sector norm difference
`-4`. Thus the canonical construction of `A+iA'` does not imply its required
Hermite--Biehler orientation.

Identifying `D` with a complex derivative requires an entire function and the
Cauchy--Riemann identity `∂_y A=iA'`. Deriving `A'` from a generator insertion
requires the unitary representation, generator domain, and differentiation
under the vacuum pairing. A positive labelled current/Green identity remains
missing. No de Branges positivity, zero confinement, or RH is asserted.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
