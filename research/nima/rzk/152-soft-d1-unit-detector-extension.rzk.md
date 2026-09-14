# Soft D1 unit detector extension

```rzk
#lang rzk-1
#data NimaSoftD1UnitExtension
  := nima-adjoin-constant-monomial-one
#define nima-soft-D1-unit-extension : NimaSoftD1UnitExtension
  := nima-adjoin-constant-monomial-one
#data NimaSoftD1UnitPairing
  := nima-alternating-detector-pairs-one-with-one
#define nima-soft-D1-unit-pairing : NimaSoftD1UnitPairing
  := nima-alternating-detector-pairs-one-with-one
#data NimaSoftD1TargetSplitting
  := nima-f-equals-f-minus-lambda-f-times-one-plus-lambda-f-times-one
  | nima-first-summand-lies-in-detector-kernel
  | nima-target-is-kernel-plus-free-unit-line
#define nima-soft-D1-target-splitting : NimaSoftD1TargetSplitting
  := nima-target-is-kernel-plus-free-unit-line
#data NimaSoftD1UnitExtensionConsequence
  := nima-free-cokernel-killed-in-all-degrees
  | nima-integral-torsion-unchanged
  | nima-geometric-road-Cech-realization-still-required
#define nima-soft-D1-unit-extension-consequence : NimaSoftD1UnitExtensionConsequence
  := nima-free-cokernel-killed-in-all-degrees
```
