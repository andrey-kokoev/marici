# Synthetic principal-road model for L2 relations

```rzk
#lang rzk-1
#define nima-L2-principal-relation-cell
  (Source Target : U)
  (zeroTarget : Target)
  (A : Source -> Target)
  : U
  := Sigma (source : Source), A source = zeroTarget
#define nima-L2-synthetic-principal-boundary
  (Source Target OtherRoads : U)
  (zeroTarget : Target) (zeroOther : OtherRoads)
  (A B : Source -> Target)
  : nima-L2-principal-relation-cell Source Target zeroTarget A ->
      Sigma (_ : Target), OtherRoads
  := \ relation -> (B (first relation), zeroOther)
#define nima-L2-synthetic-principal-coefficient
  (Source Target OtherRoads : U)
  (zeroTarget : Target) (zeroOther : OtherRoads)
  (A B : Source -> Target)
  : nima-L2-principal-relation-cell Source Target zeroTarget A ->
      Sigma (_ : Target), OtherRoads
  := \ relation -> (B (first relation), zeroOther)
#define nima-L2-synthetic-principal-comparison
  (Source Target OtherRoads : U)
  (zeroTarget : Target) (zeroOther : OtherRoads)
  (A B : Source -> Target)
  (relation : nima-L2-principal-relation-cell Source Target zeroTarget A)
  : nima-L2-synthetic-principal-boundary Source Target OtherRoads
      zeroTarget zeroOther A B relation
    = nima-L2-synthetic-principal-coefficient Source Target OtherRoads
      zeroTarget zeroOther A B relation
  := refl
#data NimaL2SyntheticPrincipalRoadStatus
  := nima-full-principal-coefficient-road-model-inhabited
  | nima-soft-D1-boundary-is-Bx
  | nima-all-other-road-components-zero
  | nima-comparison-definitional
#define nima-L2-synthetic-principal-road-status : NimaL2SyntheticPrincipalRoadStatus
  := nima-full-principal-coefficient-road-model-inhabited
#data NimaL2PhysicalRoadComparisonGate
  := nima-map-synthetic-soft-D1-cell-to-physical-nearby-cycle-cell
  | nima-preserve-Bx-boundary
  | nima-no-other-principal-road-data-required
#define nima-L2-physical-road-comparison-gate : NimaL2PhysicalRoadComparisonGate
  := nima-map-synthetic-soft-D1-cell-to-physical-nearby-cycle-cell
```
