# Residual mixed-sign normalization

After common-prefix removal, one predecessor magnitude is zero. The mixed sum
then normalizes to the natural embedding of the residual magnitude, with the
sign determined by the nonzero side.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-pos-neg-residual-positive
  ( a : MariciNat)
  : marici-int-add (marici-int-pos a) (marici-int-neg marici-zero)
    =_{MariciInt} marici-int-embed-nat a
  := match a
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒
          ap MariciNat MariciInt
            (marici-sub k marici-zero) k
            marici-int-pos
            (marici-sub-zero-right k))

#define marici-int-add-pos-neg-residual-negative
  ( b : MariciNat)
  : marici-int-add (marici-int-pos marici-zero) (marici-int-neg b)
    =_{MariciInt}
    marici-int-negate (marici-int-embed-nat b)
  := match b
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒
          ap MariciNat MariciInt
            (marici-sub k marici-zero) k
            marici-int-neg
            (marici-sub-zero-right k))
```

```rzk
#define marici-int-add-neg-pos-residual-negative
  ( a : MariciNat)
  : marici-int-add (marici-int-neg a) (marici-int-pos marici-zero)
    =_{MariciInt}
    marici-int-negate (marici-int-embed-nat a)
  := marici-int-add-pos-neg-residual-negative a

#define marici-int-add-neg-pos-residual-positive
  ( b : MariciNat)
  : marici-int-add (marici-int-neg marici-zero) (marici-int-pos b)
    =_{MariciInt} marici-int-embed-nat b
  := marici-int-add-pos-neg-residual-positive b
```

## Boundary

Both residual orders and signs are normalized for arbitrary magnitudes. To
finish the mixed distributive family, multiplication must be shown compatible
with common-prefix removal and these residual embedded forms; no such theorem
is inferred here.
