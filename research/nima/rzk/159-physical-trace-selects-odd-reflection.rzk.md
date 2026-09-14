# Physical trace selects odd reflection

```rzk
#lang rzk-1
#define nima-reflection-path-concat
  (A : U) (x y z : A) (p : x = y) (q : y = z) : x = z
  := idJ (A, x, (\ y' p' -> (z' : A) -> (q' : y' = z') -> x = z'),
       (\ z' q' -> q'), y, p) z q
#define nima-reflection-path-ap
  (A B : U) (f : A -> B) (x y : A) (p : x = y) : f x = f y
  := idJ (A, x, (\ y' p' -> f x = f y'), refl, y, p)
#define nima-physical-trace-odd-reflection
  (Group Scalars : U)
  (addG : Group -> Group -> Group) (negG : Group -> Group)
  (addS : Scalars -> Scalars -> Scalars) (negS : Scalars -> Scalars)
  (zeroS : Scalars)
  (readout : Group -> Scalars)
  (W sW commutator : Group)
  (reflectionLaw : sW = addG (negG W) commutator)
  (readoutAdd : (x y : Group) ->
    readout (addG x y) = addS (readout x) (readout y))
  (readoutNeg : (x : Group) -> readout (negG x) = negS (readout x))
  (commutatorKilled : readout commutator = zeroS)
  (rightZero : (x : Scalars) -> addS x zeroS = x)
  : readout sW = negS (readout W)
  := nima-reflection-path-concat Scalars
       (readout sW)
       (readout (addG (negG W) commutator))
       (negS (readout W))
       (nima-reflection-path-ap Group Scalars readout sW
         (addG (negG W) commutator) reflectionLaw)
       (nima-reflection-path-concat Scalars
         (readout (addG (negG W) commutator))
         (addS (readout (negG W)) (readout commutator))
         (negS (readout W))
         (readoutAdd (negG W) commutator)
         (nima-reflection-path-concat Scalars
           (addS (readout (negG W)) (readout commutator))
           (addS (negS (readout W)) (readout commutator))
           (negS (readout W))
           (nima-reflection-path-ap Scalars Scalars
             (\ x -> addS x (readout commutator))
             (readout (negG W)) (negS (readout W)) (readoutNeg W))
           (nima-reflection-path-concat Scalars
             (addS (negS (readout W)) (readout commutator))
             (addS (negS (readout W)) zeroS)
             (negS (readout W))
             (nima-reflection-path-ap Scalars Scalars
               (\ x -> addS (negS (readout W)) x)
               (readout commutator) zeroS commutatorKilled)
             (rightZero (negS (readout W))))))
#data NimaPhysicalTraceParityScope
  := nima-odd-parity-is-theorem-from-additive-commutator-killing-trace
  | nima-commutator-killing-physical-trace-still-required
#define nima-physical-trace-parity-scope : NimaPhysicalTraceParityScope
  := nima-odd-parity-is-theorem-from-additive-commutator-killing-trace
```
