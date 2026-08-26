# Grothendieck reciprocal-double seam flag

## Source mapping

Source:
`research/grothendieck/theta-reciprocal-double-acquires-an-invariant-flag-exactly-on-the-seam.md`.

The centered spectral parameter is `z : ℂ`. The direct and reciprocal sheet
weights are `-z` and `star z`. The two visible covector coefficients are
`a,b : ℂ`, and their common invariant eigenvalue is `alpha : ℂ`.

## Lean statements

- `conjugate_eq_negative_iff_realPart_zero` proves that `star z = -z` is
  equivalent to `z.re = 0`.
- `reciprocalInvariantWeights_force_seam` cancels the two nonzero sheet
  coefficients in their eigenvalue equations and forces the seam.
- `sharedForcing_cancel_iff_antisymmetric` identifies cancellation of the
  shared forcing channel with the antisymmetric sheet relation `b = -a`.
- `offSeam_forbids_twoSheetInvariantWeights` is the finite hostile: away from
  the seam no common invariant covector can keep both sheet coefficients
  nonzero.

## Scope

This formalizes the finite scalar invariant-weight obstruction. It does not
prove zero confinement, construct the completed theta operator, or claim that
the invariant flag exists in either open half-plane. Extra source channels may
change the equations only when their incidence is independently supplied.

## Verification

Per Nima's instruction, no Lean build was run. The module is intentionally not
imported by `MariciFormal.lean`, so elaboration remains unverified.
