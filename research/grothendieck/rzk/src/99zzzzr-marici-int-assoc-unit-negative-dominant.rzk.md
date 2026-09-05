# Mixed associativity in a negative-dominant unit slice

Take positive one, an arbitrary positive middle term, and a negative term whose
predecessor exceeds the middle predecessor by `r+1`. Both parenthesizations
normalize through explicit negative gaps to `-r`. A short successor-shift path
aligns the outer gap presentation.

```rzk
#lang rzk-1
```

```rzk
#define marici-add-successor-shift
  ( b r : MariciNat)
  : marici-add (marici-succ b) (marici-succ r)
    =_{MariciNat}
    marici-add (marici-succ (marici-succ b)) r
  := match b
      ( marici-zero ⇒ refl
      | marici-succ k induction ⇒
          ap MariciNat MariciNat
            (marici-add (marici-succ k) (marici-succ r))
            (marici-add (marici-succ (marici-succ k)) r)
            marici-succ induction)

#define marici-int-add-assoc-one-negative-dominates
  ( b r : MariciNat)
  : MariciIntAddAssociates
      marici-int-one
      (marici-int-pos b)
      (marici-int-neg (marici-add (marici-succ b) (marici-succ r)))
  := concat MariciInt
      (marici-int-add
        (marici-int-add marici-int-one (marici-int-pos b))
        (marici-int-neg
          (marici-add (marici-succ b) (marici-succ r))))
      (marici-int-neg r)
      (marici-int-add marici-int-one
        (marici-int-add (marici-int-pos b)
          (marici-int-neg
            (marici-add (marici-succ b) (marici-succ r)))))
      (concat MariciInt
        (marici-int-add (marici-int-pos (marici-succ b))
          (marici-int-neg
            (marici-add (marici-succ b) (marici-succ r))))
        (marici-int-add (marici-int-pos (marici-succ b))
          (marici-int-neg
            (marici-add (marici-succ (marici-succ b)) r)))
        (marici-int-neg r)
        (ap MariciNat MariciInt
          (marici-add (marici-succ b) (marici-succ r))
          (marici-add (marici-succ (marici-succ b)) r)
          (\ predecessor →
            marici-int-add (marici-int-pos (marici-succ b))
              (marici-int-neg predecessor))
          (marici-add-successor-shift b r))
        (marici-int-add-pos-neg-negative-gap (marici-succ b) r))
      (rev MariciInt
        (marici-int-add marici-int-one
          (marici-int-add (marici-int-pos b)
            (marici-int-neg
              (marici-add (marici-succ b) (marici-succ r)))))
        (marici-int-neg r)
        (concat MariciInt
          (marici-int-add marici-int-one
            (marici-int-add (marici-int-pos b)
              (marici-int-neg
                (marici-add (marici-succ b) (marici-succ r)))))
          (marici-int-add marici-int-one (marici-int-neg (marici-succ r)))
          (marici-int-neg r)
          (ap MariciInt MariciInt
            (marici-int-add (marici-int-pos b)
              (marici-int-neg
                (marici-add (marici-succ b) (marici-succ r))))
            (marici-int-neg (marici-succ r))
            (\ value → marici-int-add marici-int-one value)
            (marici-int-add-pos-neg-negative-gap b (marici-succ r)))
          (marici-int-add-pos-neg-negative-gap marici-zero r)))

#define marici-int-add-assoc-minus-one-positive-dominates
  ( b r : MariciNat)
  : MariciIntAddAssociates
      marici-int-minus-one
      (marici-int-neg b)
      (marici-int-pos (marici-add (marici-succ b) (marici-succ r)))
  := marici-int-add-assoc-sign-reversal
      marici-int-one
      (marici-int-pos b)
      (marici-int-neg (marici-add (marici-succ b) (marici-succ r)))
      (marici-int-add-assoc-one-negative-dominates b r)
```

## Boundary

A strict negative-dominant region is checked for unit first magnitude, together
with its sign reversal. Extending the first magnitude from one to arbitrary
positive value requires the corresponding general successor-shift/reassociation
path, not another comparison principle.
