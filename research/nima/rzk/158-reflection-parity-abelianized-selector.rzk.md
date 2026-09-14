# Reflection parity from an abelianized physical readout

```rzk
#lang rzk-1
#data NimaNativeStrictReflectionLaw
  := nima-sW-equals-minus-W-plus-r11-r00-commutator
#define nima-native-strict-reflection-law : NimaNativeStrictReflectionLaw
  := nima-sW-equals-minus-W-plus-r11-r00-commutator
#data NimaPhysicalReadoutCondition
  := nima-physical-readout-kills-r11-r00-commutator
  | nima-physical-readout-keeps-W-nonzero
#define nima-physical-readout-condition : NimaPhysicalReadoutCondition
  := nima-physical-readout-kills-r11-r00-commutator
#data NimaAbelianizedReflectionParity
  := nima-readout-of-sW-equals-minus-readout-of-W
  | nima-odd-reflection-parity-selected
#define nima-abelianized-reflection-parity : NimaAbelianizedReflectionParity
  := nima-odd-reflection-parity-selected
#data NimaPhysicalParityTransportGate
  := nima-prove-commutator-killing-under-physical-readout
  | nima-prove-W-survives-physical-readout
  | nima-then-transport-native-group-homotopy
#define nima-physical-parity-transport-gate : NimaPhysicalParityTransportGate
  := nima-prove-commutator-killing-under-physical-readout
```
