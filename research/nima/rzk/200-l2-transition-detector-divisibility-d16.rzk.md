# L2 transition detector divisibility at D16

```rzk
#lang rzk-1
#data NimaL2LeftAnnihilatorD16
  := nima-integral-left-annihilator-of-A-has-rank31
#define nima-L2-left-annihilator-D16 : NimaL2LeftAnnihilatorD16
  := nima-integral-left-annihilator-of-A-has-rank31
#data NimaL2TransitionDetectorIdealD16
  := nima-values-on-3a3-plus-3a3b-generate-ideal3
  | nima-no-integral-A-annihilating-detector-pairs-transition-to-unit
#define nima-L2-transition-detector-ideal-D16 : NimaL2TransitionDetectorIdealD16
  := nima-values-on-3a3-plus-3a3b-generate-ideal3
#data NimaL2LogPrimitiveNormalizationD16
  := nima-unit-log-pairing-requires-dividing-detector-by3
  | nima-Z-one-third-normalization-suffices
  | nima-integral-physical-unit-pairing-needs-different-class-or-extension
#define nima-L2-log-primitive-normalization-D16 : NimaL2LogPrimitiveNormalizationD16
  := nima-integral-physical-unit-pairing-needs-different-class-or-extension
#data NimaL2RankOneQuotientCorrection
  := nima-rho-is-on-Bockstein-image-modulo-A-image
  | nima-rho-is-not-on-cokernel-after-full-Bockstein-image
#define nima-L2-rank-one-quotient-correction : NimaL2RankOneQuotientCorrection
  := nima-rho-is-on-Bockstein-image-modulo-A-image
```
