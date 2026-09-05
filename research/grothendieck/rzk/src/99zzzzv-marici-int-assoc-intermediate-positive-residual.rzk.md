# Mixed associativity in the intermediate positive-residual region

The negative term first exceeds the positive middle term by `r`, while the
positive first term exceeds that residual by `s`. Inner-first normalization
therefore produces `-r` and then `+s`; outer-first normalization uses the
checked reassociation path and produces the same `+s` directly.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-assoc-intermediate-positive-residual
  ( b r s : MariciNat)
  : MariciIntAddAssociates
      (marici-int-pos (marici-add (marici-succ r) s))
      (marici-int-pos b)
      (marici-int-neg (marici-add (marici-succ b) r))
  := concat MariciInt
      (marici-int-add
        (marici-int-add
          (marici-int-pos (marici-add (marici-succ r) s))
          (marici-int-pos b))
        (marici-int-neg (marici-add (marici-succ b) r)))
      (marici-int-pos s)
      (marici-int-add
        (marici-int-pos (marici-add (marici-succ r) s))
        (marici-int-add (marici-int-pos b)
          (marici-int-neg (marici-add (marici-succ b) r))))
      (concat MariciInt
        (marici-int-add
          (marici-int-pos
            (marici-succ
              (marici-add (marici-add (marici-succ r) s) b)))
          (marici-int-neg (marici-add (marici-succ b) r)))
        (marici-int-add
          (marici-int-pos
            (marici-add
              (marici-succ (marici-add (marici-succ b) r)) s))
          (marici-int-neg (marici-add (marici-succ b) r)))
        (marici-int-pos s)
        (ap MariciNat MariciInt
          (marici-succ
            (marici-add (marici-add (marici-succ r) s) b))
          (marici-add
            (marici-succ (marici-add (marici-succ b) r)) s)
          (\ predecessor →
            marici-int-add (marici-int-pos predecessor)
              (marici-int-neg (marici-add (marici-succ b) r)))
          (marici-intermediate-positive-outer-gap-path b r s))
        (marici-int-add-pos-neg-gap
          (marici-add (marici-succ b) r) s))
      (rev MariciInt
        (marici-int-add
          (marici-int-pos (marici-add (marici-succ r) s))
          (marici-int-add (marici-int-pos b)
            (marici-int-neg (marici-add (marici-succ b) r))))
        (marici-int-pos s)
        (concat MariciInt
          (marici-int-add
            (marici-int-pos (marici-add (marici-succ r) s))
            (marici-int-add (marici-int-pos b)
              (marici-int-neg (marici-add (marici-succ b) r))))
          (marici-int-add
            (marici-int-pos (marici-add (marici-succ r) s))
            (marici-int-neg r))
          (marici-int-pos s)
          (ap MariciInt MariciInt
            (marici-int-add (marici-int-pos b)
              (marici-int-neg (marici-add (marici-succ b) r)))
            (marici-int-neg r)
            (\ value → marici-int-add
              (marici-int-pos (marici-add (marici-succ r) s)) value)
            (marici-int-add-pos-neg-negative-gap b r))
          (marici-int-add-pos-neg-gap r s)))

#define marici-int-add-assoc-intermediate-negative-residual
  ( b r s : MariciNat)
  : MariciIntAddAssociates
      (marici-int-neg (marici-add (marici-succ r) s))
      (marici-int-neg b)
      (marici-int-pos (marici-add (marici-succ b) r))
  := marici-int-add-assoc-sign-reversal
      (marici-int-pos (marici-add (marici-succ r) s))
      (marici-int-pos b)
      (marici-int-neg (marici-add (marici-succ b) r))
      (marici-int-add-assoc-intermediate-positive-residual b r s)
```

## Boundary

The strict intermediate region with positive final residual is checked, with
its sign reversal. The equality subregion where the first magnitude exactly
matches the inner negative residual, and the subregion where that residual
still dominates the first term, remain separate.
