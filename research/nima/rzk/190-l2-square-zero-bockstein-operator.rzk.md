# L2 square-zero deformation and Bockstein operator

```rzk
#lang rzk-1
#define nima-L2-relation
  (Source Target : U)
  (zeroTarget : Target)
  (A : Source -> Target)
  : U
  := Sigma (source : Source), A source = zeroTarget
#define nima-L2-relation-source
  (Source Target : U)
  (zeroTarget : Target)
  (A : Source -> Target)
  (relation : nima-L2-relation Source Target zeroTarget A)
  : Source
  := first relation
#define nima-L2-square-zero-Bockstein-representative
  (Source Target : U)
  (zeroTarget : Target)
  (A B : Source -> Target)
  (relation : nima-L2-relation Source Target zeroTarget A)
  : Target
  := B (first relation)
#define nima-L2-deformed-labelled-operator
  (Source Target DeformedTarget : U)
  (A B : Source -> Target)
  (deform : Target -> Target -> DeformedTarget)
  : Source -> DeformedTarget
  := \ source -> deform (A source) (B source)
#data NimaL2BocksteinInterpretation
  := nima-A-is-u0-labelled-map
  | nima-B-is-u-over-two-coefficient-map
  | nima-B-of-integral-A-relation-represents-Bockstein-class
#define nima-L2-Bockstein-interpretation : NimaL2BocksteinInterpretation
  := nima-B-of-integral-A-relation-represents-Bockstein-class
#data NimaL2GlobalObjectCorrection
  := nima-global-locally-finite-object-is-square-zero-deformed-operator
  | nima-relation-to-cokernel-Bockstein-map-not-yet-road-chain-map
  | nima-ambient-road-differentials-still-unmodeled
#define nima-L2-global-object-correction : NimaL2GlobalObjectCorrection
  := nima-relation-to-cokernel-Bockstein-map-not-yet-road-chain-map
```
