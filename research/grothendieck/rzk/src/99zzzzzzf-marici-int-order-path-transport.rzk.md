# Integer-order endpoint transport

Order witnesses transport along equality of either endpoint. These dependent
transport lemmas are needed to align denominator-factor normal forms in the
rational transitivity proof.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-at-most-transport-left
  ( x x-prime y : MariciInt)
  ( path : x =_{MariciInt} x-prime)
  ( witness : MariciIntAtMost x y)
  : MariciIntAtMost x-prime y
  := idJ
      ( MariciInt , x
      , \ u p → MariciIntAtMost u y
      , witness , x-prime , path)

#define marici-int-at-most-transport-right
  ( x y y-prime : MariciInt)
  ( path : y =_{MariciInt} y-prime)
  ( witness : MariciIntAtMost x y)
  : MariciIntAtMost x y-prime
  := idJ
      ( MariciInt , y
      , \ u p → MariciIntAtMost x u
      , witness , y-prime , path)

#define marici-int-at-most-transport-both
  ( x x-prime y y-prime : MariciInt)
  ( left-path : x =_{MariciInt} x-prime)
  ( right-path : y =_{MariciInt} y-prime)
  ( witness : MariciIntAtMost x y)
  : MariciIntAtMost x-prime y-prime
  := marici-int-at-most-transport-right x-prime y y-prime right-path
      (marici-int-at-most-transport-left x x-prime y left-path witness)
```

## Boundary

These are path transports only; they do not prove new inequalities. Their role
is to preserve established order while reassociating commutative denominator
products.
