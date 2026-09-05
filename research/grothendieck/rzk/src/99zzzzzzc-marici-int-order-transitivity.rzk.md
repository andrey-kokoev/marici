# Integer-order transitivity

The middle integer cancels when two additive differences are summed. Closure of
nonnegativity under addition then proves transitivity of integer order.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-middle-cancel
  ( y z : MariciInt)
  : marici-int-add y
      (marici-int-add (marici-int-negate y) z)
    =_{MariciInt} z
  := concat MariciInt
      (marici-int-add y (marici-int-add (marici-int-negate y) z))
      (marici-int-add
        (marici-int-add y (marici-int-negate y)) z)
      z
      (rev MariciInt
        (marici-int-add (marici-int-add y (marici-int-negate y)) z)
        (marici-int-add y (marici-int-add (marici-int-negate y) z))
        (marici-int-add-assoc y (marici-int-negate y) z))
      (concat MariciInt
        (marici-int-add (marici-int-add y (marici-int-negate y)) z)
        (marici-int-add marici-int-zero z)
        z
        (ap MariciInt MariciInt
          (marici-int-add y (marici-int-negate y)) marici-int-zero
          (\ u → marici-int-add u z)
          (marici-int-add-inverse-right y))
        (marici-int-add-zero-left z))

#define marici-int-add-differences
  ( x y z : MariciInt)
  : marici-int-add
      (marici-int-add (marici-int-negate x) y)
      (marici-int-add (marici-int-negate y) z)
    =_{MariciInt}
    marici-int-add (marici-int-negate x) z
  := concat MariciInt
      (marici-int-add
        (marici-int-add (marici-int-negate x) y)
        (marici-int-add (marici-int-negate y) z))
      (marici-int-add (marici-int-negate x)
        (marici-int-add y (marici-int-add (marici-int-negate y) z)))
      (marici-int-add (marici-int-negate x) z)
      (marici-int-add-assoc
        (marici-int-negate x) y
        (marici-int-add (marici-int-negate y) z))
      (ap MariciInt MariciInt
        (marici-int-add y (marici-int-add (marici-int-negate y) z)) z
        (\ u → marici-int-add (marici-int-negate x) u)
        (marici-int-middle-cancel y z))

#define marici-int-nonnegative-transport
  ( x y : MariciInt)
  ( path : x =_{MariciInt} y)
  ( witness : MariciIntIsNonnegative x)
  : MariciIntIsNonnegative y
  := idJ
      ( MariciInt , x
      , \ q p → MariciIntIsNonnegative q
      , witness , y , path)

#define marici-int-at-most-transitive
  ( x y z : MariciInt)
  ( xy : MariciIntAtMost x y)
  ( yz : MariciIntAtMost y z)
  : MariciIntAtMost x z
  := marici-int-nonnegative-transport
      (marici-int-add
        (marici-int-add (marici-int-negate x) y)
        (marici-int-add (marici-int-negate y) z))
      (marici-int-add (marici-int-negate x) z)
      (marici-int-add-differences x y z)
      (marici-int-nonnegative-add
        (marici-int-add (marici-int-negate x) y)
        (marici-int-add (marici-int-negate y) z)
        xy yz)
```

## Boundary

Integer order is now reflexive and transitive. Rational transitivity additionally
requires transport through positive cross-multiplication and denominator
reassociation.
