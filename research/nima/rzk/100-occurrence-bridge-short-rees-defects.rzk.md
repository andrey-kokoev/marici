# Occurrence bridge and short-Rees defects

```rzk
#lang rzk-1
#data NimaOccurrenceBridgeCorrection
  := nima-six-occurrences-preserved-over-common-base
  | nima-earlier-rank-one-nonfactorization-not-applicable
#data NimaOccurrenceBridgeDefect
  := nima-degree-two-comparison-cokernel-rank-9
  | nima-auxiliary-normalization-has-higher-Tor
  | nima-bridge-is-quotient-not-equivalence
#define nima-occurrence-bridge-defect : NimaOccurrenceBridgeDefect
  := nima-bridge-is-quotient-not-equivalence
#data NimaShortReesSupportedChannel
  := nima-six-first-conormal-zero-defect-channels
  | nima-eight-higher-wedge-supported-defect-channels
#data NimaShortReesCentralValue
  := nima-complete-defect-sources-have-primitive-central-extensions
#define nima-short-Rees-central-value : NimaShortReesCentralValue
  := nima-complete-defect-sources-have-primitive-central-extensions
#data NimaShortReesCapBehavior
  := nima-six-quadratic-channel-cap-images-zero
  | nima-two-cubic-channel-short-support-images
  | nima-all-defect-cap-generic-Q-projections-zero
#define nima-short-Rees-cap-behavior : NimaShortReesCapBehavior
  := nima-all-defect-cap-generic-Q-projections-zero
#data NimaShortReesPhysicalStatus
  := nima-supported-defects-not-full-physical-comparison
#define nima-short-Rees-physical-status : NimaShortReesPhysicalStatus
  := nima-supported-defects-not-full-physical-comparison
```
