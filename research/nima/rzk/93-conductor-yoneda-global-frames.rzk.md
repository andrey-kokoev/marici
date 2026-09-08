# Conductor Yoneda operations and global frames

```rzk
#lang rzk-1
#data NimaConductorYonedaAlgebra
  := nima-free-product-of-two-exterior-algebras
  | nima-six-last-block-contraction-generators
  | nima-cross-sheet-words-independent
#define nima-conductor-Yoneda-algebra : NimaConductorYonedaAlgebra
  := nima-free-product-of-two-exterior-algebras
#data NimaGlobalFrameAction
  := nima-first-conductor-derivative-translation
  | nima-quadratic-occurrence-tail-kernel
#define nima-global-frame-action : NimaGlobalFrameAction
  := nima-first-conductor-derivative-translation
#data NimaConductorMarkingGroupoid
  := nima-unbounded-higher-marking-groups
  | nima-quadratic-frame-kernel-contributes-loops
#data NimaFramedExtensionGroupoid
  := nima-global-extension-groupoid-is-1-type
  | nima-endpoint-residue-components-remain-distinct
#define nima-framed-extension-groupoid : NimaFramedExtensionGroupoid
  := nima-global-extension-groupoid-is-1-type
#data NimaHigherPathEndpointBehavior
  := nima-higher-conductor-paths-do-not-change-extension-class
#define nima-higher-path-endpoint-behavior : NimaHigherPathEndpointBehavior
  := nima-higher-conductor-paths-do-not-change-extension-class
#data NimaYonedaPhysicalStatus
  := nima-Yoneda-model-not-native-physical-identification
#define nima-Yoneda-physical-status : NimaYonedaPhysicalStatus
  := nima-Yoneda-model-not-native-physical-identification
```
