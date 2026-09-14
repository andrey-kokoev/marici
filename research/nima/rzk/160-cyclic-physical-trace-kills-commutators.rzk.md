# Cyclic physical trace kills commutators

```rzk
#lang rzk-1
#define nima-trace-path-concat
  (A : U) (x y z : A) (p : x = y) (q : y = z) : x = z
  := idJ (A, x, (\ y' p' -> (z' : A) -> (q' : y' = z') -> x = z'),
       (\ z' q' -> q'), y, p) z q
#define nima-trace-path-ap
  (A B : U) (f : A -> B) (x y : A) (p : x = y) : f x = f y
  := idJ (A, x, (\ y' p' -> f x = f y'), refl, y, p)
#define nima-cyclic-physical-trace-kills-commutator
  (Group Scalars : U)
  (mul : Group -> Group -> Group)
  (addG : Group -> Group -> Group) (negG : Group -> Group)
  (addS : Scalars -> Scalars -> Scalars) (negS : Scalars -> Scalars)
  (zeroS : Scalars) (readout : Group -> Scalars)
  (x y commutator : Group)
  (commutatorLaw : commutator = addG (mul x y) (negG (mul y x)))
  (readoutAdd : (u v : Group) ->
    readout (addG u v) = addS (readout u) (readout v))
  (readoutNeg : (u : Group) -> readout (negG u) = negS (readout u))
  (cyclicity : readout (mul y x) = readout (mul x y))
  (addInverse : (s : Scalars) -> addS s (negS s) = zeroS)
  : readout commutator = zeroS
  := nima-trace-path-concat Scalars
       (readout commutator)
       (readout (addG (mul x y) (negG (mul y x)))) zeroS
       (nima-trace-path-ap Group Scalars readout commutator
         (addG (mul x y) (negG (mul y x))) commutatorLaw)
       (nima-trace-path-concat Scalars
         (readout (addG (mul x y) (negG (mul y x))))
         (addS (readout (mul x y)) (readout (negG (mul y x)))) zeroS
         (readoutAdd (mul x y) (negG (mul y x)))
         (nima-trace-path-concat Scalars
           (addS (readout (mul x y)) (readout (negG (mul y x))))
           (addS (readout (mul x y)) (negS (readout (mul y x)))) zeroS
           (nima-trace-path-ap Scalars Scalars
             (\ s -> addS (readout (mul x y)) s)
             (readout (negG (mul y x))) (negS (readout (mul y x)))
             (readoutNeg (mul y x)))
           (nima-trace-path-concat Scalars
             (addS (readout (mul x y)) (negS (readout (mul y x))))
             (addS (readout (mul x y)) (negS (readout (mul x y)))) zeroS
             (nima-trace-path-ap Scalars Scalars
               (\ s -> addS (readout (mul x y)) (negS s))
               (readout (mul y x)) (readout (mul x y)) cyclicity)
             (addInverse (readout (mul x y))))))
#data NimaPhysicalTraceCommutatorGate
  := nima-additive-cyclic-trace-suffices
  | nima-prove-concrete-supported-readout-cyclic
#define nima-physical-trace-commutator-gate : NimaPhysicalTraceCommutatorGate
  := nima-prove-concrete-supported-readout-cyclic
```
