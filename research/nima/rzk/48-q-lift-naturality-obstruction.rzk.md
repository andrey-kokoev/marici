# Q-lift coefficient-naturality obstruction

The primary lifting ideal and the secondary naturality obstruction have
different annihilators.  This module keeps their generators in different
 types and records the six common-to-branch relation defects.

```rzk
#lang rzk-1

#data NimaNaturalityAnnihilatorGenerator
  := nima-naturality-annihilator-common-rees
  | nima-naturality-annihilator-X13
  | nima-naturality-annihilator-X15
  | nima-naturality-annihilator-X35
  | nima-naturality-annihilator-X02
  | nima-naturality-annihilator-X04
  | nima-naturality-annihilator-X24

#data NimaNaturalityAnnihilatorMode
  := nima-naturality-common-tau-plus-times-tau-minus
  | nima-naturality-positive-occurrence
  | nima-naturality-negative-occurrence

#define nima-naturality-annihilator-mode
  : NimaNaturalityAnnihilatorGenerator -> NimaNaturalityAnnihilatorMode
  := \ g -> match g
       (nima-naturality-annihilator-common-rees =>
          nima-naturality-common-tau-plus-times-tau-minus
       | nima-naturality-annihilator-X13 => nima-naturality-positive-occurrence
       | nima-naturality-annihilator-X15 => nima-naturality-positive-occurrence
       | nima-naturality-annihilator-X35 => nima-naturality-positive-occurrence
       | nima-naturality-annihilator-X02 => nima-naturality-negative-occurrence
       | nima-naturality-annihilator-X04 => nima-naturality-negative-occurrence
       | nima-naturality-annihilator-X24 => nima-naturality-negative-occurrence)

#data NimaQLiftRelationDefect
  := nima-q-lift-defect-plus-13
  | nima-q-lift-defect-plus-15
  | nima-q-lift-defect-plus-35
  | nima-q-lift-defect-minus-02
  | nima-q-lift-defect-minus-04
  | nima-q-lift-defect-minus-24

#define NimaQLiftDefectPacket : U := NimaZSum NimaQLiftRelationDefect

#define nima-q-lift-defect-cycle (d : NimaQLiftRelationDefect)
  : NimaQLiftDefectPacket
  := nima-sum-atom NimaQLiftRelationDefect d

#define nima-q-lift-defect-augmentation
  : NimaQLiftRelationDefect -> MariciInt
  := \ d -> marici-int-one

#define nima-q-lift-defect-primitive-value (d : NimaQLiftRelationDefect)
  : nima-sum-eval NimaQLiftRelationDefect nima-q-lift-defect-augmentation
      (nima-q-lift-defect-cycle d) = marici-int-one
  := refl

#define nima-q-lift-top-boundary : NimaQLiftDefectPacket -> NimaQLiftDefectPacket
  := \ p -> nima-sum-zero NimaQLiftRelationDefect

#define nima-q-lift-top-boundary-augmentation-zero (p : NimaQLiftDefectPacket)
  : nima-sum-eval NimaQLiftRelationDefect nima-q-lift-defect-augmentation
      (nima-q-lift-top-boundary p) = marici-int-zero
  := refl

#define nima-q-lift-defect-not-top-boundary
  (d : NimaQLiftRelationDefect) (p : NimaQLiftDefectPacket)
  (boundary : nima-sum-equal NimaQLiftRelationDefect
    (nima-q-lift-top-boundary p) (nima-q-lift-defect-cycle d))
  : marici-int-zero = marici-int-one
  := nima-frame-concat MariciInt marici-int-zero
       (nima-sum-eval NimaQLiftRelationDefect nima-q-lift-defect-augmentation
         (nima-q-lift-top-boundary p)) marici-int-one
       (nima-frame-rev MariciInt
         (nima-sum-eval NimaQLiftRelationDefect nima-q-lift-defect-augmentation
           (nima-q-lift-top-boundary p)) marici-int-zero
         (nima-q-lift-top-boundary-augmentation-zero p))
       (boundary nima-q-lift-defect-augmentation)
```
