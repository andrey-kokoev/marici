# Transporting associativity to the middle-sign permutation

In a commutative operation, two associativity instances with the same three
inputs in adjacent positive orders transport associativity to the permutation
with the exceptional sign in the middle. The path is explicit and introduces
no new magnitude case split.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-assoc-middle-permutation
  ( x y z : MariciInt)
  ( associates-zxy : MariciIntAddAssociates z x y)
  ( associates-xzy : MariciIntAddAssociates x z y)
  : MariciIntAddAssociates x y z
  := concat MariciInt
      (marici-int-add (marici-int-add x y) z)
      (marici-int-add z (marici-int-add x y))
      (marici-int-add x (marici-int-add y z))
      (marici-int-add-comm (marici-int-add x y) z)
      (concat MariciInt
        (marici-int-add z (marici-int-add x y))
        (marici-int-add (marici-int-add z x) y)
        (marici-int-add x (marici-int-add y z))
        (rev MariciInt
          (marici-int-add (marici-int-add z x) y)
          (marici-int-add z (marici-int-add x y))
          associates-zxy)
        (concat MariciInt
          (marici-int-add (marici-int-add z x) y)
          (marici-int-add (marici-int-add x z) y)
          (marici-int-add x (marici-int-add y z))
          (ap MariciInt MariciInt
            (marici-int-add z x) (marici-int-add x z)
            (\ value → marici-int-add value y)
            (marici-int-add-comm z x))
          (concat MariciInt
            (marici-int-add (marici-int-add x z) y)
            (marici-int-add x (marici-int-add z y))
            (marici-int-add x (marici-int-add y z))
            associates-xzy
            (ap MariciInt MariciInt
              (marici-int-add z y) (marici-int-add y z)
              (\ value → marici-int-add x value)
              (marici-int-add-comm z y)))))

#define marici-int-add-assoc-positive-negative-positive
  ( a b c : MariciNat)
  : MariciIntAddAssociates
      (marici-int-pos a) (marici-int-neg b) (marici-int-pos c)
  := marici-int-add-assoc-middle-permutation
      (marici-int-pos a) (marici-int-neg b) (marici-int-pos c)
      (marici-int-add-assoc-positive-positive-negative c a b)
      (marici-int-add-assoc-positive-positive-negative a c b)

#define marici-int-add-assoc-negative-positive-negative
  ( a b c : MariciNat)
  : MariciIntAddAssociates
      (marici-int-neg a) (marici-int-pos b) (marici-int-neg c)
  := marici-int-add-assoc-sign-reversal
      (marici-int-pos a) (marici-int-neg b) (marici-int-pos c)
      (marici-int-add-assoc-positive-negative-positive a b c)
```

## Boundary

The `(+,-,+)` and `(-,+,-)` faces are closed for arbitrary magnitudes. Only the
faces with the exceptional sign in the leading position remain; they can be
transported using commutativity and the now-checked middle-sign face.
