# Soft D1 realization extends by zero to the principal road

```rzk
#lang rzk-1
#define nima-road-path-ap
  (A B : U) (f : A -> B) (x y : A) (p : x = y) : f x = f y
  := idJ (A, x, (\ y' p' -> f x = f y'), refl, y, p)
#define nima-principal-road-Cech
  (SoftD1 OtherRoads : U) : U
  := Sigma (_ : SoftD1), OtherRoads
#define nima-extend-soft-D1-by-zero
  (SoftD1 OtherRoads : U)
  (zeroOther : OtherRoads)
  : SoftD1 -> nima-principal-road-Cech SoftD1 OtherRoads
  := \ d1 -> (d1, zeroOther)
#define nima-soft-D1-comparison-extends-by-zero
  (SoftD1 OtherRoads : U)
  (zeroOther : OtherRoads)
  (x y : SoftD1)
  (softComparison : x = y)
  : nima-extend-soft-D1-by-zero SoftD1 OtherRoads zeroOther x
    = nima-extend-soft-D1-by-zero SoftD1 OtherRoads zeroOther y
  := nima-road-path-ap SoftD1 (nima-principal-road-Cech SoftD1 OtherRoads)
       (nima-extend-soft-D1-by-zero SoftD1 OtherRoads zeroOther)
       x y softComparison
#define nima-soft-relation-cell-full-road-boundary
  (Relation RoadCell SoftD1 OtherRoads : U)
  (zeroOther : OtherRoads)
  (realize : Relation -> RoadCell)
  (softBoundary : RoadCell -> SoftD1)
  (softCoefficient : Relation -> SoftD1)
  (softComparison : (r : Relation) ->
    softBoundary (realize r) = softCoefficient r)
  (r : Relation)
  : nima-extend-soft-D1-by-zero SoftD1 OtherRoads zeroOther
      (softBoundary (realize r))
    = nima-extend-soft-D1-by-zero SoftD1 OtherRoads zeroOther
      (softCoefficient r)
  := nima-soft-D1-comparison-extends-by-zero SoftD1 OtherRoads zeroOther
       (softBoundary (realize r)) (softCoefficient r) (softComparison r)
#data NimaPrincipalRoadRealizationReduction
  := nima-D2-D3-incidence-and-corners-extend-by-zero
  | nima-only-soft-D1-relation-cell-map-required
  | nima-soft-comparison-induces-full-principal-road-comparison
#define nima-principal-road-realization-reduction
  : NimaPrincipalRoadRealizationReduction
  := nima-soft-comparison-induces-full-principal-road-comparison
```
