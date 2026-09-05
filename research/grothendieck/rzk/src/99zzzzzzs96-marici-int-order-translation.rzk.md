# Integer order is invariant under right translation

The defining difference for `x + z ≤ y + z` cancels the shared translate and
reduces to the defining difference for `x ≤ y`.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-translated-difference
  ( x y z : MariciInt)
  : marici-int-add
      (marici-int-negate (marici-int-add x z))
      (marici-int-add y z)
    =_{MariciInt}
    marici-int-add (marici-int-negate x) y
  := concat MariciInt
      (marici-int-add
        (marici-int-negate (marici-int-add x z))
        (marici-int-add y z))
      (marici-int-add
        (marici-int-add (marici-int-negate x) (marici-int-negate z))
        (marici-int-add y z))
      (marici-int-add (marici-int-negate x) y)
      (ap MariciInt MariciInt
        (marici-int-negate (marici-int-add x z))
        (marici-int-add (marici-int-negate x) (marici-int-negate z))
        (\ left → marici-int-add left (marici-int-add y z))
        (marici-int-negate-add x z))
      (concat MariciInt
        (marici-int-add
          (marici-int-add (marici-int-negate x) (marici-int-negate z))
          (marici-int-add y z))
        (marici-int-add (marici-int-negate x)
          (marici-int-add (marici-int-negate z) (marici-int-add y z)))
        (marici-int-add (marici-int-negate x) y)
        (marici-int-add-assoc (marici-int-negate x)
          (marici-int-negate z) (marici-int-add y z))
        (ap MariciInt MariciInt
          (marici-int-add (marici-int-negate z) (marici-int-add y z))
          y
          (\ middle → marici-int-add (marici-int-negate x) middle)
          (concat MariciInt
            (marici-int-add (marici-int-negate z) (marici-int-add y z))
            (marici-int-add
              (marici-int-add (marici-int-negate z) y) z)
            y
            (rev MariciInt
              (marici-int-add
                (marici-int-add (marici-int-negate z) y) z)
              (marici-int-add (marici-int-negate z) (marici-int-add y z))
              (marici-int-add-assoc (marici-int-negate z) y z))
            (concat MariciInt
              (marici-int-add
                (marici-int-add (marici-int-negate z) y) z)
              (marici-int-add y
                (marici-int-add (marici-int-negate z) z))
              y
              (concat MariciInt
                (marici-int-add
                  (marici-int-add (marici-int-negate z) y) z)
                (marici-int-add
                  (marici-int-add y (marici-int-negate z)) z)
                (marici-int-add y
                  (marici-int-add (marici-int-negate z) z))
                (ap MariciInt MariciInt
                  (marici-int-add (marici-int-negate z) y)
                  (marici-int-add y (marici-int-negate z))
                  (\ left → marici-int-add left z)
                  (marici-int-add-comm (marici-int-negate z) y))
                (marici-int-add-assoc y (marici-int-negate z) z))
              (concat MariciInt
                (marici-int-add y
                  (marici-int-add (marici-int-negate z) z))
                (marici-int-add y marici-int-zero)
                y
                (ap MariciInt MariciInt
                  (marici-int-add (marici-int-negate z) z)
                  marici-int-zero
                  (\ right → marici-int-add y right)
                  (marici-int-add-inverse-left z))
                (marici-int-add-zero-right y))))))

#define marici-int-at-most-add-right
  ( x y z : MariciInt)
  ( witness : MariciIntAtMost x y)
  : MariciIntAtMost
      (marici-int-add x z) (marici-int-add y z)
  := marici-int-nonnegative-transport
      (marici-int-add (marici-int-negate x) y)
      (marici-int-add
        (marici-int-negate (marici-int-add x z))
        (marici-int-add y z))
      (rev MariciInt
        (marici-int-add
          (marici-int-negate (marici-int-add x z))
          (marici-int-add y z))
        (marici-int-add (marici-int-negate x) y)
        (marici-int-translated-difference x y z))
      witness
```

## Boundary

Right translation preserves integer order. Left translation follows from
commutativity; two-sided addition monotonicity can now be derived by composing
translations.
