# Residual-dominant branch of the third-dominant handler

When the residual left after cancelling the middle term still dominates the
leading positive predecessor, transport of the two explicit equations places
the triple in the checked general negative-dominant region.

```rzk
#lang rzk-1
```

```rzk
#define marici-third-handler-residual-dominant-branch
  ( a b c residual remainder : MariciNat)
  ( third-equation : c =_{MariciNat}
      marici-add (marici-succ b) residual)
  ( residual-equation : residual =_{MariciNat}
      marici-add (marici-succ a) remainder)
  : MariciIntAddAssociates
      (marici-int-pos a) (marici-int-pos b) (marici-int-neg c)
  := transport MariciNat
      (\ third → MariciIntAddAssociates
        (marici-int-pos a) (marici-int-pos b) (marici-int-neg third))
      (marici-add (marici-succ b) residual) c
      (rev MariciNat c (marici-add (marici-succ b) residual)
        third-equation)
      (transport MariciNat
        (\ residual-prime → MariciIntAddAssociates
          (marici-int-pos a) (marici-int-pos b)
          (marici-int-neg (marici-add (marici-succ b) residual-prime)))
        (marici-add (marici-succ a) remainder) residual
        (rev MariciNat residual
          (marici-add (marici-succ a) remainder)
          residual-equation)
        (marici-int-add-assoc-general-negative-dominant
          a b remainder))
```

## Boundary

All three branches needed by `MariciThirdDominantAssocHandler` now have
transported implementations. The next module can match the nested residual
classification, assemble that handler, and feed it to the outer factorization
to close the arbitrary `(+,+,-)` face.
