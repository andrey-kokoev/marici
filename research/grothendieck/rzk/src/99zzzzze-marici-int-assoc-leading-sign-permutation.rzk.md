# Transporting associativity to the leading-sign permutation

Commuting the inner pair moves the exceptional leading sign to the middle.
After applying middle-sign associativity, commuting the new inner pair and
reversing the checked trailing-sign associativity path moves it back to the
leading position.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-assoc-leading-permutation
  ( x y z : MariciInt)
  ( associates-yxz : MariciIntAddAssociates y x z)
  ( associates-yzx : MariciIntAddAssociates y z x)
  : MariciIntAddAssociates x y z
  := concat MariciInt
      (marici-int-add (marici-int-add x y) z)
      (marici-int-add (marici-int-add y x) z)
      (marici-int-add x (marici-int-add y z))
      (ap MariciInt MariciInt
        (marici-int-add x y) (marici-int-add y x)
        (\ value → marici-int-add value z)
        (marici-int-add-comm x y))
      (concat MariciInt
        (marici-int-add (marici-int-add y x) z)
        (marici-int-add y (marici-int-add x z))
        (marici-int-add x (marici-int-add y z))
        associates-yxz
        (concat MariciInt
          (marici-int-add y (marici-int-add x z))
          (marici-int-add y (marici-int-add z x))
          (marici-int-add x (marici-int-add y z))
          (ap MariciInt MariciInt
            (marici-int-add x z) (marici-int-add z x)
            (\ value → marici-int-add y value)
            (marici-int-add-comm x z))
          (concat MariciInt
            (marici-int-add y (marici-int-add z x))
            (marici-int-add (marici-int-add y z) x)
            (marici-int-add x (marici-int-add y z))
            (rev MariciInt
              (marici-int-add (marici-int-add y z) x)
              (marici-int-add y (marici-int-add z x))
              associates-yzx)
            (marici-int-add-comm (marici-int-add y z) x))))

#define marici-int-add-assoc-negative-positive-positive
  ( a b c : MariciNat)
  : MariciIntAddAssociates
      (marici-int-neg a) (marici-int-pos b) (marici-int-pos c)
  := marici-int-add-assoc-leading-permutation
      (marici-int-neg a) (marici-int-pos b) (marici-int-pos c)
      (marici-int-add-assoc-positive-negative-positive b a c)
      (marici-int-add-assoc-positive-positive-negative b c a)

#define marici-int-add-assoc-positive-negative-negative
  ( a b c : MariciNat)
  : MariciIntAddAssociates
      (marici-int-pos a) (marici-int-neg b) (marici-int-neg c)
  := marici-int-add-assoc-sign-reversal
      (marici-int-neg a) (marici-int-pos b) (marici-int-pos c)
      (marici-int-add-assoc-negative-positive-positive a b c)
```

## Boundary

All six nonzero mixed-sign constructor faces are now checked for arbitrary
magnitudes. Together with the same-sign and zero-face theorems, every
constructor branch of global integer addition associativity is available; the
next module only has to assemble the outer three-way match.
