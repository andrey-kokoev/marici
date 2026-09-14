# Conormal trace extension and mixed obstruction

```rzk
#lang rzk-1
#data NimaConormalTraceDifference
  := nima-beta-eta35-tensor-retained-normal-line
  | nima-explicit-rank-two-module-extension
  | nima-extension-splits-at-beta-zero
#define nima-conormal-trace-difference : NimaConormalTraceDifference
  := nima-beta-eta35-tensor-retained-normal-line
#data NimaConductorExtRanks
  := nima-Ext1-rank-6
  | nima-Ext2-rank-24
  | nima-Ext3-rank-92
#data NimaEta35Continuation
  := nima-right-multiplication-rank-5
  | nima-right-multiplication-kernel-A-eta35
  | nima-rank-one-continuation-only-same-direction
#define nima-eta35-continuation : NimaEta35Continuation
  := nima-rank-one-continuation-only-same-direction
#data NimaMixedNormalObstruction
  := nima-reflected-04-normal-composition-nonzero-obstruction
#define nima-mixed-normal-obstruction : NimaMixedNormalObstruction
  := nima-reflected-04-normal-composition-nonzero-obstruction
#data NimaConormalObstructionPhysicalStatus
  := nima-ordinary-module-test-not-universal-physical-obstruction
#define nima-conormal-obstruction-physical-status
  : NimaConormalObstructionPhysicalStatus
  := nima-ordinary-module-test-not-universal-physical-obstruction
```
