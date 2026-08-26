# Finite refinement correspondence packet

## Grothendieck source

This covers the convention-fixed finite algebra in Sections 20--22 of
`research/grothendieck/theta-cubic-bilinear-companion.md`: coefficient
pullback, packet pushforward, the fiber norm, and seam-kernel preservation.

## Formal objects

- `coefficientPullback q c` is `q^* c`.
- `packetPushforward q v` is the finite fiber sum `q_! v`.
- `fiberNorm q c` records multiplication by each fiber cardinality.
- `SeamCovariant q bFine bCoarse` is the exact interface
  `(b_fine)^* q^* = (b_coarse)^*`.
- `seamCompatible_pullback` proves preservation of the seam hyperplane.
- `nonuniform_fiber_norm_is_not_uniform` is the hostile capped-chart example.

## Typing and scope boundary

The pull--push theorem needs finite index types and an additive commutative
monoid. Seam evaluation is stated over a commutative semiring.

This does not formalize theta convergence, seam derivatives, positivity,
physical descent, or the paired moment inequality. Those need independent
analytic inputs. `SeamCovariant` is exposed as an assumption rather than
inferred from the existence of a refinement map.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is not claimed
because Nima's active instruction prohibits builds.
