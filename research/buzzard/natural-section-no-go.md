# Split quotient versus natural section: Lean packet

## Source boundary

This increment formalizes the finite controls in Grothendieck's
`no-natural-section-transfer.md` and
`equivariant-transfer-selection-nogo.md`. It is a hostile about canonical
selection, not a construction of Betti transfer or physical lift data.

## Formal objects and coefficient types

`C2` is represented by `Bool` with `Bool.xor`. The split quotient
`C2 × C2 → C2` is first projection. The base-preserving shear is
`(a,b) ↦ (a,a xor b)`. A section is first a plain set-theoretic right
inverse; `PreservesXor` separately records the group-homomorphism law.

## Theorems and hostile

- `splitQuotient_has_two_xorSections` constructs the zero and diagonal
  homomorphic sections.
- `shear_preserves_splitQuotient` proves that the shear lies over the base.
- `shear_exchanges_sections` proves that it swaps the two displayed splits.
- `no_shearInvariant_section` proves the stronger hostile: no set-theoretic
  section is invariant under the shear, so no homomorphic section can be
  natural under every base-preserving symmetry.
- `uniformTransfer_leftInverse` and `uniformTransfer_kernelInvariant` prove
  that averaging is a deck-invariant split over rational coefficients.
- `uniformTransfer_dilutes_identitySelector` proves that averaging sends the
  frozen identity selector to weight `1/2`, not weight `1`.
- `chosenLiftTransfer_leftInverse` and
  `chosenLiftTransfer_preserves_identitySelector` prove that a chosen lift
  splits pullback and preserves the selector.
- `chosenLiftTransfer_breaks_kernelSymmetry` proves that the same chosen lift
  is not deck-invariant.

## Missing interfaces

A canonical section can only be recovered from extra source data that breaks
the shear symmetry: a marking, framing, orientation, chamber, or typed lift.
Transport of a command, existence of some split, or equality of quotient
coordinates supplies none of these. Any sector-specific transfer still needs
its own source and target objects and preservation law.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/NaturalSectionNoGo.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
