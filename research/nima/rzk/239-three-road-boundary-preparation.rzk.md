# Three-road boundary preparation before physical descent

```rzk
#lang rzk-1
#define nima-three-road-boundary-preparation
  (Cycle Scalars : U)
  (gamma-D03 gamma-D25 gamma-D14 : Cycle -> Scalars)
  (a b c : Scalars)
  : U
  := Sigma (lift : Cycle),
       Sigma (_ : gamma-D03 lift = a),
       Sigma (_ : gamma-D25 lift = b), gamma-D14 lift = c

#define nima-three-road-boundary-preparation-intro
  (Cycle Scalars : U)
  (gamma-D03 gamma-D25 gamma-D14 : Cycle -> Scalars)
  (a b c : Scalars)
  (lift : Cycle)
  (D03-law : gamma-D03 lift = a)
  (D25-law : gamma-D25 lift = b)
  (D14-law : gamma-D14 lift = c)
  : nima-three-road-boundary-preparation
      Cycle Scalars gamma-D03 gamma-D25 gamma-D14 a b c
  := (lift, (D03-law, (D25-law, D14-law)))

#define nima-three-road-selected-residue
  (Cycle Scalars : U)
  (gamma-D03 gamma-D25 gamma-D14 : Cycle -> Scalars)
  (add multiply : Scalars -> Scalars -> Scalars)
  (negate : Scalars -> Scalars)
  (beta a b c : Scalars)
  (preparation : nima-three-road-boundary-preparation
    Cycle Scalars gamma-D03 gamma-D25 gamma-D14 a b c)
  : Scalars
  := negate (multiply beta (add a (add b c)))

#define nima-three-road-selected-residue-law
  (Cycle Scalars : U)
  (gamma-D03 gamma-D25 gamma-D14 : Cycle -> Scalars)
  (add multiply : Scalars -> Scalars -> Scalars)
  (negate : Scalars -> Scalars)
  (beta a b c : Scalars)
  (preparation : nima-three-road-boundary-preparation
    Cycle Scalars gamma-D03 gamma-D25 gamma-D14 a b c)
  : nima-three-road-selected-residue
      Cycle Scalars gamma-D03 gamma-D25 gamma-D14
      add multiply negate beta a b c preparation
    = negate (multiply beta (add a (add b c)))
  := refl

#data NimaThreeRoadPreparationStatus
  := nima-joint-road-trace-has-rank-three-on-cycles
  | nima-conductor-boundary-is-in-joint-trace-kernel
  | nima-road-gluing-kills-rank-two-augmentation-ideal
  | nima-independent-a-b-c-live-before-physical-descent
#define nima-three-road-preparation-status : NimaThreeRoadPreparationStatus
  := nima-independent-a-b-c-live-before-physical-descent
```
