# Degenerate-pairing radical repair: Lean packet

Source: `research/grothendieck/degenerate-pairing-radical-repair-obstruction.md`
(epistemic-graph event 1345).

The formal carrier types are arbitrary additive commutative groups `Source`
and `Target`. A right radical is an `AddSubgroup Target`; defects and
corrections are additive homomorphisms `Source →+ Target`; the abstract Hom
differential is an additive endomorphism of this homomorphism group.

Lean keeps two conditions distinct:

- `RadicalValued radical defect`, the quotient/projection obstruction;
- `RadicalHomExact radical δ defect`, the existence of a radical-valued
  correction whose Hom coboundary cancels the defect.

Assuming explicitly that `δ` preserves radical-valued maps,
`hasRadicalRepair_iff_projected_zero_and_exact` proves that a repair exists
exactly when both gates hold. `hasRadicalRepair_bot_iff` proves the
perfect-pairing specialization: zero radical collapses repairability to
`defect=0`.

The integer hostile takes the whole target as radical, the Hom differential
to be zero, and the defect to be the identity. Its quotient projection
vanishes, but no correction can cancel it. This proves that the first gate
does not imply the second.

This minimal core does not construct graded chain complexes, prove the defect
Bianchi identity, identify Hom-complex degrees, construct target pairings, or
evaluate the five-site physical radical. Those convention-fixed objects must
come from the sector. In particular, declaring a large radical cannot supply
a missing physical pairing.

Verification boundary: Nima's active no-build instruction remains in force.
Only bounded static scans are run, and this module remains outside
`MariciFormal.lean`.
