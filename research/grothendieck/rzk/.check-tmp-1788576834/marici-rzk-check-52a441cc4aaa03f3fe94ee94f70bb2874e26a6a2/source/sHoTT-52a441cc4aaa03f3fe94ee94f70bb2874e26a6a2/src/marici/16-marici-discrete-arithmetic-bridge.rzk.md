# Conditional discrete arithmetic bridge

In simplicial type theory, sethood does not by itself assert that every
directed interval map is constant. The exact bridge required by sHoTT is
`is-discrete`. This file makes that dependency explicit and derives the
Segal/Rezk structures only from supplied discreteness witnesses.

```rzk
#lang rzk-1

#assume extext-discrete-bridge : ExtExt
```

```rzk
#define marici-nat-segal-if-discrete uses (extext-discrete-bridge)
  ( discrete-Nat : is-discrete MariciNat)
  : is-segal MariciNat
  := is-segal-is-discrete
      extext-discrete-bridge MariciNat discrete-Nat

#define marici-nat-rezk-if-discrete uses (extext-discrete-bridge)
  ( discrete-Nat : is-discrete MariciNat)
  : is-rezk MariciNat
  := is-rezk-is-discrete
      extext-discrete-bridge MariciNat discrete-Nat

#define marici-int-segal-if-discrete uses (extext-discrete-bridge)
  ( discrete-Int : is-discrete MariciInt)
  : is-segal MariciInt
  := is-segal-is-discrete
      extext-discrete-bridge MariciInt discrete-Int

#define marici-int-rezk-if-discrete uses (extext-discrete-bridge)
  ( discrete-Int : is-discrete MariciInt)
  : is-rezk MariciInt
  := is-rezk-is-discrete
      extext-discrete-bridge MariciInt discrete-Int
```

Given the two missing discreteness witnesses, the already checked natural-to-
integer arithmetic map acts on directed arrows and preserves canonical Segal
composition.

```rzk
#define marici-nat-int-map-arrow-if-discrete
  ( discrete-Nat : is-discrete MariciNat)
  ( discrete-Int : is-discrete MariciInt)
  ( x y : MariciNat)
  ( f : hom MariciNat x y)
  : hom MariciInt
      (marici-int-embed-nat x) (marici-int-embed-nat y)
  := marici-map-arrow
      MariciNat MariciInt marici-int-embed-nat x y f

#define marici-nat-int-preserves-composite-if-discrete uses (extext-discrete-bridge)
  ( discrete-Nat : is-discrete MariciNat)
  ( discrete-Int : is-discrete MariciInt)
  ( x y z : MariciNat)
  ( f : hom MariciNat x y)
  ( g : hom MariciNat y z)
  : ( comp-is-segal MariciInt
        (marici-int-segal-if-discrete discrete-Int)
        (marici-int-embed-nat x)
        (marici-int-embed-nat y)
        (marici-int-embed-nat z)
        (marici-nat-int-map-arrow-if-discrete
          discrete-Nat discrete-Int x y f)
        (marici-nat-int-map-arrow-if-discrete
          discrete-Nat discrete-Int y z g))
  = ( marici-nat-int-map-arrow-if-discrete
        discrete-Nat discrete-Int x z
        (comp-is-segal MariciNat
          (marici-nat-segal-if-discrete discrete-Nat)
          x y z f g))
  := marici-map-preserves-composite
      MariciNat MariciInt
      (marici-nat-segal-if-discrete discrete-Nat)
      (marici-int-segal-if-discrete discrete-Int)
      marici-int-embed-nat x y z f g
```

## Boundary

This is a conditional bridge theorem, not a discreteness proof. Its first
missing typed objects are inhabitants of `is-discrete MariciNat` and
`is-discrete MariciInt`. Proving only `is-set` for those carriers would not fill
this interface: sethood controls identity proofs, while discreteness compares
identity paths with directed homs.
