# Concrete target-typed boundary model

```rzk
#lang rzk-1
#define nima-target-typed-packet (Scalars : U) : U
  := Sigma (_ : Scalars), Sigma (_ : Scalars), Scalars

#define nima-target-typed-primary (Scalars : U)
  : nima-target-typed-packet Scalars -> Scalars
  := \ packet -> first packet

#define nima-target-typed-reciprocal (Scalars : U)
  : nima-target-typed-packet Scalars -> Scalars
  := \ packet -> first (second packet)

#define nima-target-typed-relation (Scalars : U)
  : nima-target-typed-packet Scalars -> Scalars
  := \ packet -> second (second packet)

#define nima-target-typed-boundary-to-supported (Scalars : U)
  : nima-target-typed-packet Scalars -> nima-target-typed-packet Scalars
  := \ packet -> packet

#define nima-target-typed-packet-residue
  (Scalars : U)
  (add multiply : Scalars -> Scalars -> Scalars)
  (negate : Scalars -> Scalars)
  (beta : Scalars)
  : nima-target-typed-packet Scalars -> Scalars
  := \ packet -> negate
       (multiply beta
         (add (first packet)
           (add (first (second packet)) (second (second packet)))))

#define nima-concrete-target-typed-boundary-witness
  (Scalars : U)
  (add multiply : Scalars -> Scalars -> Scalars)
  (negate : Scalars -> Scalars)
  (beta a b c : Scalars)
  : Sigma (preparation : nima-target-typed-packet Scalars),
       Sigma (_ : nima-target-typed-primary Scalars
         (nima-target-typed-boundary-to-supported Scalars preparation) = a),
       Sigma (_ : nima-target-typed-reciprocal Scalars
         (nima-target-typed-boundary-to-supported Scalars preparation) = b),
       Sigma (_ : nima-target-typed-relation Scalars
         (nima-target-typed-boundary-to-supported Scalars preparation) = c),
       nima-target-typed-packet-residue Scalars add multiply negate beta
         (nima-target-typed-boundary-to-supported Scalars preparation)
       = negate (multiply beta (add a (add b c)))
  := ((a, (b, c)), (refl, (refl, (refl, refl))))

#data NimaConcreteTargetTypedBoundaryScope
  := nima-independent-primary-reciprocal-relation-coordinates-inhabited
  | nima-symbolic-minus-beta-a-plus-b-plus-c-inhabited
  | nima-coefficient-boundary-model-not-yet-geometric-physical-source
#define nima-concrete-target-typed-boundary-scope
  : NimaConcreteTargetTypedBoundaryScope
  := nima-coefficient-boundary-model-not-yet-geometric-physical-source
```
