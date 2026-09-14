# L2 Bockstein to log-primitive rank reduction

```rzk
#lang rzk-1
#data NimaL2BocksteinRanksForLogComparison
  := nima-ranks-8-14-18-22-26-through-D28
#define nima-L2-Bockstein-ranks-for-log-comparison
  : NimaL2BocksteinRanksForLogComparison
  := nima-ranks-8-14-18-22-26-through-D28
#data NimaLogNormalLinkPrimitiveRank
  := nima-relative-log-orientation-line-rank-one
#define nima-log-normal-link-primitive-rank : NimaLogNormalLinkPrimitiveRank
  := nima-relative-log-orientation-line-rank-one
#data NimaL2LogComparisonRankConsequence
  := nima-any-map-to-log-line-has-kernel-rank-at-least-7-13-17-21-25
  | nima-full-Bockstein-image-cannot-embed-in-log-primitive-line
  | nima-physical-map-must-select-scalar-quotient
#define nima-L2-log-comparison-rank-consequence : NimaL2LogComparisonRankConsequence
  := nima-physical-map-must-select-scalar-quotient
#data NimaL2LogComparisonNextDatum
  := nima-functional-rho-on-Bockstein-cokernel
  | nima-proof-physical-residual-is-detected-by-rho
#define nima-L2-log-comparison-next-datum : NimaL2LogComparisonNextDatum
  := nima-functional-rho-on-Bockstein-cokernel
```
