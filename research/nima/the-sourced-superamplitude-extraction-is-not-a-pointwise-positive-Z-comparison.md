# Sourced superamplitude extraction is not pointwise comparison at positive real Z

## Question

Can the exact fermionic `χ_1^4 χ_5^4` component traced at the frozen positive nine-point moment-curve target be compared directly with the numerical traced eight-form density there?

## Source-derived map and exact obstruction

No direct same-external-point map exists. In the primary source `research/sources/nima/papers/six-point-nmhv/1312.2007/amplituhedron.tex`, section `The Superamplitude` (lines 625–675), extraction is explicitly **evaluate the GLOBAL rational target form at `Y0` after formally replacing the last `k=2` external entries by `(φ_1·η_a, φ_2·η_a)`, then Berezin-integrate over all eight `φ` variables**. It is not projection of one ordinary positive-real external `Z` point to a fermion coefficient.

The body of every product `φ_r·η_a` is zero. Thus the six-column external bosonized body has rank at most four and EVERY six-bracket body vanishes. The frozen numerical moment-curve data have rank six, with exact first-six-column bracket `34560`. Nonvanishing of that maximal minor is preserved by any invertible frame transformation, including a transformation taking the observed plane to `Y0`. For retained eight columns the ordinary-real external kernel has dimension TWO; its bosonized body kernel has dimension FOUR. Moreover the source's `Y0` lies along the last two coordinate axes, whereas every body-level `CZ_body` has both last coordinates zero, so its fixed-target source fibre has NO ordinary-body lift.

The checker reproduces these rank and determinant assertions from the primary-source extraction formula, including a deliberately rank-four truncated control. The numerical positive cell and the sourced superamplitude component are individually legitimate but inhabit DIFFERENT input domains. Neither a nonzero numerical source-component trace nor a numerical target-form trace can be equated or compared by scalar ratio without introducing a map that the source does not define.

## Disposition

The old pointwise comparison route is rejected at its first typed datum. The executable successor is to derive the GENERAL rational two-sheet target form where six-brackets are invertible, prove that the full traced expression admits the relevant nilpotent specialization (cancellation of any would-be six-bracket inverse poles), perform the source's `Y=Y0` and Berezin extraction, and compare its complete fermion component and residues to the sourced ψ invariant. Direct substitution into the existing fixed-target two-kernel fibre algorithm is invalid on the rank-four body; the algebraic target form must be continued FIRST. This does not refute equality after that source-derived operation and does not identify a nine-point generalized-R history.

Checker: `research/nima/checkers/check_four_mass_bosonization_source_domain.py`; result: `research/nima/results/four-mass-bosonization-domain-gate.json`.
