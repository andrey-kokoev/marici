# Central Rees return versus shifted Gysin channel

```rzk
#lang rzk-1

#data NimaCentralReesOutcome
  := nima-central-ordinary-return-zero
  | nima-central-shifted-gysin-unit
  | nima-central-shifted-gysin-excess-unit

#define nima-central-rees-outcome-value
  : NimaCentralReesOutcome -> MariciInt
  := \ outcome -> match outcome
       (nima-central-ordinary-return-zero => marici-int-zero
       | nima-central-shifted-gysin-unit => marici-int-one
       | nima-central-shifted-gysin-excess-unit => marici-int-one)

#define nima-central-ordinary-return-vanishes
  : nima-central-rees-outcome-value nima-central-ordinary-return-zero
      = marici-int-zero
  := refl
#define nima-central-gysin-is-primitive
  : nima-central-rees-outcome-value nima-central-shifted-gysin-unit
      = marici-int-one
  := refl
#define nima-central-gysin-retains-excess
  : nima-central-rees-outcome-value nima-central-shifted-gysin-excess-unit
      = marici-int-one
  := refl

#data NimaCentralGysinFrame
  := nima-central-gysin-degree-three-dual-determinant

#define nima-central-gysin-reverse-pairing
  : NimaCentralGysinFrame -> NimaDualTransgressionClass -> MariciInt
  := \ frame dual -> match dual
       (nima-dual-short-functional => marici-int-one
       | nima-dual-generic-functional => marici-int-one)

#define nima-central-gysin-short-pairing-unit
  : nima-central-gysin-reverse-pairing
      nima-central-gysin-degree-three-dual-determinant
      nima-dual-short-functional = marici-int-one
  := refl
#define nima-central-gysin-generic-pairing-unit
  : nima-central-gysin-reverse-pairing
      nima-central-gysin-degree-three-dual-determinant
      nima-dual-generic-functional = marici-int-one
  := refl
```
