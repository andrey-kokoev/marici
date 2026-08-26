# Finite Hermite entropy packet

## Grothendieck source

This formalizes the implication layer of
`research/grothendieck/newman-hermite-relative-entropy.md`.

## Formal objects

- `finiteHermiteRelativeEntropy ref obs = log(ref/obs)` is the normalized
  finite discriminant entropy.
- nonnegativity is proved from positive observed discriminant and the explicit
  Hermite extremal premise `obs<=ref`.
- zero entropy is equivalent to saturation `ref=obs` for positive inputs.
- `centeredRepulsionDissipation` is four times the finite sum of squared
  centered electrostatic defects.
- a supplied flow identity `E'=-dissipation` implies `E'<=0`.
- zero dissipation is equivalent to vanishing of every finite defect.

## Assumptions and coefficient type

Entropy and dissipation use real coefficients. The defect index is any finite
type. No zero configuration, ordering chamber, or differential flow is built
into these generic implications.

## Hostile and missing interfaces

`finiteHermiteRelativeEntropy 1 2<0` shows that the logarithmic definition
does not imply nonnegativity without the extremal discriminant inequality.

The source must still provide the all-rank probabilists-Hermite discriminant
and radius formulas, the constrained global maximizer/uniqueness theorem,
and the derivative identity along the correctly normalized finite Newman
flow. The checker verifies ranks 2 through 8 and the symbolic equilibrium
coefficient, but finite regression is not an all-rank Lean proof.

Xi-window convergence, edge control, collision-barrier limits, infinite-rank
renormalization, and the Newman constant remain gated. Sharing Hermite local
profiles with another heat equation does not identify the two sector flows.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
