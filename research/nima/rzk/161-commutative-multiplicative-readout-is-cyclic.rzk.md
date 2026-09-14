# A commutative multiplicative readout is cyclic

```rzk
#lang rzk-1
#define nima-cyclic-path-concat
  (A : U) (x y z : A) (p : x = y) (q : y = z) : x = z
  := idJ (A, x, (\ y' p' -> (z' : A) -> (q' : y' = z') -> x = z'),
       (\ z' q' -> q'), y, p) z q
#define nima-cyclic-path-inverse
  (A : U) (x y : A) (p : x = y) : y = x
  := idJ (A, x, (\ y' p' -> y' = x), refl, y, p)
#define nima-commutative-multiplicative-readout-is-cyclic
  (Group Scalars : U)
  (mulG : Group -> Group -> Group)
  (mulS : Scalars -> Scalars -> Scalars)
  (readout : Group -> Scalars)
  (multiplicative : (x y : Group) ->
    readout (mulG x y) = mulS (readout x) (readout y))
  (commutative : (a b : Scalars) -> mulS a b = mulS b a)
  (x y : Group)
  : readout (mulG x y) = readout (mulG y x)
  := nima-cyclic-path-concat Scalars
       (readout (mulG x y))
       (mulS (readout x) (readout y))
       (readout (mulG y x))
       (multiplicative x y)
       (nima-cyclic-path-concat Scalars
         (mulS (readout x) (readout y))
         (mulS (readout y) (readout x))
         (readout (mulG y x))
         (commutative (readout x) (readout y))
         (nima-cyclic-path-inverse Scalars
           (readout (mulG y x))
           (mulS (readout y) (readout x))
           (multiplicative y x)))
#data NimaConcreteReadoutCyclicityRoute
  := nima-direct-supported-trace-cyclicity
  | nima-multiplicative-readout-to-commutative-scalars
  | nima-either-route-kills-reflection-commutator
#define nima-concrete-readout-cyclicity-route : NimaConcreteReadoutCyclicityRoute
  := nima-either-route-kills-reflection-commutator
```
