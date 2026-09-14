# qg2 ramified ringed Q map

```rzk
#lang rzk-1
#data NimaQG2RamifiedQAlgebra
  := nima-base-Q-ring-localized-at-p-and-kappa-squared-minus1
  | nima-adjoin-d-with-d-squared-equal-conductor-discriminant
  | nima-quadratic-cover-finite-over-base
#define nima-qg2-ramified-Q-algebra : NimaQG2RamifiedQAlgebra
  := nima-adjoin-d-with-d-squared-equal-conductor-discriminant
#data NimaQG2ConductorBranchInCover
  := nima-xi-plus-equals-minus-B-plus-d-over2A
  | nima-xi-minus-equals-minus-B-minus-d-over2A
  | nima-both-branches-annihilate-restricted-kernel
#define nima-qg2-conductor-branch-in-cover : NimaQG2ConductorBranchInCover
  := nima-both-branches-annihilate-restricted-kernel
#data NimaQG2RamifiedQDeckLaw
  := nima-d-to-minus-d-exchanges-conductor-branches
  | nima-deck-character-on-branch-difference-minus1
  | nima-branch-difference-is-log-primitive-orientation-candidate
#define nima-qg2-ramified-Q-deck-law : NimaQG2RamifiedQDeckLaw
  := nima-deck-character-on-branch-difference-minus1
#data NimaQG2RamifiedFilteredLaw
  := nima-discriminant-has-x-order-one
  | nima-d-has-half-x-order
  | nima-x-equals-h-squared-gives-integral-h-filtration
#define nima-qg2-ramified-filtered-law : NimaQG2RamifiedFilteredLaw
  := nima-x-equals-h-squared-gives-integral-h-filtration
```
