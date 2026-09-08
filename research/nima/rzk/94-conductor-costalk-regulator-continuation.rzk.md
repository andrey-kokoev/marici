# Conductor costalk regulator continuation

```rzk
#lang rzk-1
#data NimaCostalkRegulatorModule
  := nima-costalk-free-Lambda-degree-1-rank-1
  | nima-costalk-free-Lambda-degree-2-rank-15
  | nima-costalk-free-Lambda-degree-3-rank-18
#data NimaStableCostalkRank
  := nima-stable-costalk-rank-34
  | nima-stable-counit-kernel-rank-31
  | nima-stable-counit-image-rank-3
#data NimaCounitRegulatorTorsion
  := nima-three-beta-torsion-primary-directions
  | nima-supported-classes-themselves-beta-torsion-free
#define nima-counit-regulator-torsion : NimaCounitRegulatorTorsion
  := nima-three-beta-torsion-primary-directions
#data NimaPrimaryTransferStatus
  := nima-three-explicit-zero-unit-nonzero-transfers
#define nima-primary-transfer-status : NimaPrimaryTransferStatus
  := nima-three-explicit-zero-unit-nonzero-transfers
#data NimaNonzeroRegulatorContinuation
  := nima-all-34-classes-survive-beta-inversion
  | nima-ten-invariant-zero-primary-directions-remain
#define nima-nonzero-regulator-continuation : NimaNonzeroRegulatorContinuation
  := nima-all-34-classes-survive-beta-inversion
#data NimaRegulatorPhysicalStatus
  := nima-continuation-does-not-select-physical-conductor-Morse-class
#define nima-regulator-physical-status : NimaRegulatorPhysicalStatus
  := nima-continuation-does-not-select-physical-conductor-Morse-class
```
