# Grothendieck universal rank-one determinant no-go

## Source mapping

Source:
`research/grothendieck/theta-rank-one-fredholm-realization-no-go.md`.

For a scalar observation `o`, Lean defines the one-dimensional defect matrix
and action by multiplication with `1-o`.

## Lean results

- `rankOneDefect_det` proves that the determinant is exactly `1-o`.
- `rankOneDefect_has_nontrivial_kernel_iff` proves that a nonzero kernel vector
  exists exactly when `o=1`.
- `every_vacuumMinusObservation_has_rankOneDeterminant` packages the universal
  construction for every scalar observation over a field.

The `tautologicalProposal` hostile has exact determinant zero and a nontrivial
kernel while its `independentSourceLaw` field is false.
`determinant_match_does_not_supply_sourceLaw` therefore keeps determinant
matching, transversality loss, and source-derived dynamics as distinct types.

## Scope

This is the finite algebraic determinant lemma, not a construction of a useful
Fredholm family. A substantive theta operator still needs an independently
derived energy, transport, locality, cocycle, or index law from which the
determinant follows. Holomorphic dependence and trace-class typing are not
inferred from the scalar encoding.

## Verification

No build was run under Nima's instruction. The module remains outside the root
import and elaboration is unverified.
