# Physical normal Cech partial completion

```rzk
#lang rzk-1
#data NimaPhysicalNormalCechAtlas
  := nima-three-gradient-pivot-charts
  | nima-three-normal-directions
  | nima-nine-pairwise-overlaps
#define nima-physical-normal-Cech-atlas : NimaPhysicalNormalCechAtlas
  := nima-nine-pairwise-overlaps
#data NimaPhysicalNormalCechCoherence
  := nima-nine-overlap-differences-tangent
  | nima-nine-responses-Cartan-exact
  | nima-three-triple-cocycles-zero
  | nima-no-new-support-from-gradient-pivots
#define nima-physical-normal-Cech-coherence : NimaPhysicalNormalCechCoherence
  := nima-three-triple-cocycles-zero
#data NimaPhysicalWallResidueTransition
  := nima-three-pairwise-Cech-components-zero
  | nima-reverse-order-residue-sign-minus-one
  | nima-pairwise-residue-denominators-coprime-to-Q
#define nima-physical-wall-residue-transition : NimaPhysicalWallResidueTransition
  := nima-reverse-order-residue-sign-minus-one
#data NimaPhysicalCechCompletionScope
  := nima-frozen-marked-complement-class-glues
  | nima-full-signed-minor-chain-boundaries-unchecked
  | nima-Gauss-Manin-or-higher-localization-gluing-open
  | nima-not-yet-road-Cech-completion-witness
#define nima-physical-Cech-completion-scope : NimaPhysicalCechCompletionScope
  := nima-not-yet-road-Cech-completion-witness
```
