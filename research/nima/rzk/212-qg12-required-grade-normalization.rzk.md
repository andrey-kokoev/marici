# Required qg12 grade normalization

```rzk
#lang rzk-1
#data NimaQG12NodeResidueData
  := nima-qg1-collision-residue-minus-kappa-minus3-over64p4kappa-minus1-squared
  | nima-qg2-endpoint-residue-minus1-over16p3kappa-minus1-squared
#define nima-qg12-node-residue-data : NimaQG12NodeResidueData
  := nima-qg2-endpoint-residue-minus1-over16p3kappa-minus1-squared
#data NimaQG12RequiredNormalization
  := nima-opposite-residue-factor-minus-kappa-minus3-over4p
  | nima-normalized-qg1-plus-qg2-node-residue-zero
#define nima-qg12-required-normalization : NimaQG12RequiredNormalization
  := nima-opposite-residue-factor-minus-kappa-minus3-over4p
#data NimaQG12NormalizationStrength
  := nima-unique-necessary-node-factor
  | nima-derived-from-cancellation-not-source-authorized
  | nima-falsifier-for-parent-Jacobian-candidates
#define nima-qg12-normalization-strength : NimaQG12NormalizationStrength
  := nima-unique-necessary-node-factor
#data NimaQG12NormalizationNextGate
  := nima-recover-factor-from-parent-normal-coordinate-Jacobian
  | nima-recover-grade-shift-from-regulated-chain
  | nima-reject-road-comparison-if-source-factor-differs
#define nima-qg12-normalization-next-gate : NimaQG12NormalizationNextGate
  := nima-recover-factor-from-parent-normal-coordinate-Jacobian
```
