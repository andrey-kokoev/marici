# Full conductor square and D03 support

```rzk
#lang rzk-1
#data NimaFullConductorSquareCompletion
  := nima-nine-coherent-extensions-complete
  | nima-three-invariant-completions
#define nima-full-conductor-square-completion
  : NimaFullConductorSquareCompletion
  := nima-nine-coherent-extensions-complete
#data NimaD03SupportRank
  := nima-marked-D03-gallery-rank-0
  | nima-long-facet-D03-rank-0
  | nima-short-facet-35-rank-2
  | nima-facet-union-rank-2
#data NimaShortFacetSupportBehavior
  := nima-two-short-facet-directions-reflection-odd
  | nima-D25-terms-unavoidable
  | nima-no-invariant-short-facet-direction
#define nima-short-facet-support-behavior : NimaShortFacetSupportBehavior
  := nima-no-invariant-short-facet-direction
#data NimaD03PhysicalConsequence
  := nima-coefficient-family-does-not-realize-marked-D03-gallery
#define nima-D03-physical-consequence : NimaD03PhysicalConsequence
  := nima-coefficient-family-does-not-realize-marked-D03-gallery
```
