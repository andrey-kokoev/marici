# Natural reassociation for the intermediate mixed region

When the negative term dominates the positive middle term by residual `r`,
but the positive first term dominates that residual by `s`, the predecessor of
the positive pair admits exactly the outer-gap presentation needed for mixed
associativity.

```rzk
#lang rzk-1
```

```rzk
#define marici-intermediate-positive-outer-gap-path
  ( b r s : MariciNat)
  : marici-succ
      (marici-add (marici-add (marici-succ r) s) b)
    =_{MariciNat}
    marici-add
      (marici-succ (marici-add (marici-succ b) r)) s
  := concat MariciNat
      (marici-succ
        (marici-add (marici-add (marici-succ r) s) b))
      (marici-add (marici-succ b)
        (marici-add (marici-succ r) s))
      (marici-add
        (marici-succ (marici-add (marici-succ b) r)) s)
      (ap MariciNat MariciNat
        (marici-add (marici-add (marici-succ r) s) b)
        (marici-add b (marici-add (marici-succ r) s))
        marici-succ
        (marici-add-comm (marici-add (marici-succ r) s) b))
      (concat MariciNat
        (marici-add (marici-succ b)
          (marici-add (marici-succ r) s))
        (marici-add (marici-succ (marici-succ (marici-add r b))) s)
        (marici-add
          (marici-succ (marici-add (marici-succ b) r)) s)
        (marici-two-positive-gap-reassociate r b s)
        (ap MariciNat MariciNat
          (marici-succ (marici-succ (marici-add r b)))
          (marici-succ (marici-add (marici-succ b) r))
          (\ value → marici-add value s)
          (ap MariciNat MariciNat
            (marici-succ (marici-add r b))
            (marici-add (marici-succ b) r)
            marici-succ
            (ap MariciNat MariciNat
              (marici-add r b) (marici-add b r)
              marici-succ (marici-add-comm r b)))))
```

## Boundary

The natural-number coherence path for the strict intermediate region is now
checked. The next module can use it with two negative-gap normalizations to
prove the corresponding mixed integer associativity family.
