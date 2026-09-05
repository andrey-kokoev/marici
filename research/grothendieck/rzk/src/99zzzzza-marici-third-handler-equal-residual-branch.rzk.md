# Equal-residual branch of the third-dominant handler

When the leading predecessor equals the residual left after the negative third
term cancels the positive middle term, the total positive magnitude equals the
negative magnitude. Transporting the supplied equations therefore reduces this
branch to total-magnitude cancellation.

```rzk
#lang rzk-1
```

```rzk
#define marici-third-handler-equal-residual-branch
  ( a b c residual : MariciNat)
  ( third-equation : c =_{MariciNat}
      marici-add (marici-succ b) residual)
  ( leading-equation : a =_{MariciNat} residual)
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
        residual a
        (rev MariciNat a residual leading-equation)
        (transport MariciNat
          (\ third → MariciIntAddAssociates
            (marici-int-pos residual) (marici-int-pos b)
            (marici-int-neg third))
          (marici-succ (marici-add residual b))
          (marici-add (marici-succ b) residual)
          (marici-successor-add-swap residual b)
          (marici-int-add-assoc-total-positive-magnitude-cancellation
            residual b)))
```

## Boundary

The equal leading/residual branch of `MariciThirdDominantAssocHandler` is now
implemented for arbitrary transported inputs. Only the residual-dominant branch
remains before assembling the handler.
