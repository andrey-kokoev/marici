# First-dominant branch of the third-dominant handler

When the third negative predecessor exceeds the positive middle predecessor by
`r`, and the positive leading predecessor exceeds `r` by `s`, the explicit
region theorem applies after transporting those two supplied gap equations.

```rzk
#lang rzk-1
```

```rzk
#define marici-third-handler-first-dominant-branch
  ( a b c residual remainder : MariciNat)
  ( third-equation : c =_{MariciNat}
      marici-add (marici-succ b) residual)
  ( leading-equation : a =_{MariciNat}
      marici-add (marici-succ residual) remainder)
  : MariciIntAddAssociates
      (marici-int-pos a) (marici-int-pos b) (marici-int-neg c)
  := transport MariciNat
      (\ third → MariciIntAddAssociates
        (marici-int-pos a) (marici-int-pos b) (marici-int-neg third))
      (marici-add (marici-succ b) residual) c
      (rev MariciNat c (marici-add (marici-succ b) residual)
        third-equation)
      (transport MariciNat
        (\ leading → MariciIntAddAssociates
          (marici-int-pos leading) (marici-int-pos b)
          (marici-int-neg (marici-add (marici-succ b) residual)))
        (marici-add (marici-succ residual) remainder) a
        (rev MariciNat a
          (marici-add (marici-succ residual) remainder)
          leading-equation)
        (marici-int-add-assoc-intermediate-positive-residual
          b residual remainder))
```

## Boundary

One of the three residual branches of `MariciThirdDominantAssocHandler` is now
implemented with arbitrary transported inputs. Equal leading/residual and
residual-dominant branches remain to be transported from total cancellation and
general negative dominance respectively.
