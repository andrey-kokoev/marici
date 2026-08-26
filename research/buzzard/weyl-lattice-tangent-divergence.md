# Weyl-lattice tangent divergence: Lean packet

## Source boundary

This increment formalizes the universal finite convex core of Grothendieck's
`xi-weyl-lattice-tangent-divergence.md`. It does not specialize to Xi zeros,
because doing so would presuppose the ordered real configuration whose
existence is RH-sensitive.

## Formal objects and assumptions

For a real slope `u` in the logarithm domain `u>-1`, define

\[
\phi(u)=u-\log(1+u).
\]

For any finite family of slopes, the divergence is twice their sum. The index
type and finite set are arbitrary; an ordered configuration supplies the
pair-indexed slopes only after its coordinates are declared.

## Theorems and hostile

- `logarithmicTangentGap_nonnegative` proves `φ(u)≥0` on `u>-1`.
- `logarithmicTangentGap_eq_zero_iff` proves equality exactly at `u=0`.
- `finiteTangentDivergence_nonnegative` proves the finite coupled sum is
  nonnegative.
- `finiteTangentDivergence_eq_zero_iff` proves it vanishes precisely when
  every retained pair slope vanishes.
- `singleton_nontrivial_tangent_divergence_positive` gives a strict finite
  fixture at slope `1`.
- `perturbed_pair_ordered_iff_slope_gt_neg_one` proves that the logarithm
  domain is exactly strict ordering of a pair above a positive base gap.
- `allPairDifferencesZero_iff_common_translation` proves the equality case is
  precisely a common translation of every retained coordinate.

## Missing interfaces

The remaining log-Vandermonde tangent identity needs a concrete finite pair
index, finite products, positivity of ordered differences, and the explicit
harmonic gradient. The Xi formula additionally assumes flattened
ordinates are real and ordered, so it cannot serve as evidence for RH. A
source-side pre-real-rooted extension remains absent.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/WeylLatticeTangentDivergence.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
