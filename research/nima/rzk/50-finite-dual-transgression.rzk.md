# Finite graded reverse transgression

This packet records the variance reversal seen after dualizing the finite
homogeneous mapping complex. It is not identified with spatial Verdier duality.

```rzk
#lang rzk-1

#data NimaPrimalTransgressionClass
  := nima-primal-generic-class
  | nima-primal-short-obstruction
#data NimaDualTransgressionClass
  := nima-dual-short-functional
  | nima-dual-generic-functional

#define nima-primal-connecting
  : NimaPrimalTransgressionClass -> NimaPrimalTransgressionClass
  := \ c -> match c
       (nima-primal-generic-class => nima-primal-short-obstruction
       | nima-primal-short-obstruction => nima-primal-short-obstruction)

#define nima-dual-reverse-connecting
  : NimaDualTransgressionClass -> NimaDualTransgressionClass
  := \ c -> match c
       (nima-dual-short-functional => nima-dual-generic-functional
       | nima-dual-generic-functional => nima-dual-generic-functional)

#define nima-transgression-pairing
  : NimaDualTransgressionClass -> NimaPrimalTransgressionClass -> MariciInt
  := \ dual primal -> match dual
       (nima-dual-short-functional => match primal
          (nima-primal-generic-class => marici-int-zero
          | nima-primal-short-obstruction => marici-int-one)
       | nima-dual-generic-functional => match primal
          (nima-primal-generic-class => marici-int-one
          | nima-primal-short-obstruction => marici-int-zero))

#define nima-short-obstruction-pairing-primitive
  : nima-transgression-pairing nima-dual-short-functional
      nima-primal-short-obstruction = marici-int-one
  := refl
#define nima-generic-pairing-primitive
  : nima-transgression-pairing nima-dual-generic-functional
      nima-primal-generic-class = marici-int-one
  := refl
#define nima-dual-connecting-reverses-support
  : nima-dual-reverse-connecting nima-dual-short-functional
      = nima-dual-generic-functional
  := refl
```
