# Positive-factor distributivity for strict mixed gaps

The reversed source gap is normalized, then both strict residual branches are
assembled into positive-factor mixed distributive paths.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-pos-neg-negative-gap
  ( b r : MariciNat)
  : marici-int-add
      (marici-int-pos b)
      (marici-int-neg (marici-add (marici-succ b) r))
    =_{MariciInt} marici-int-neg r
  := concat MariciInt
      (marici-int-add
        (marici-int-pos b)
        (marici-int-neg (marici-add (marici-succ b) r)))
      (marici-int-neg
        (marici-sub (marici-add (marici-succ b) r) (marici-succ b)))
      (marici-int-neg r)
      (ap MariciOrdering MariciInt
        (marici-compare b (marici-add (marici-succ b) r))
        marici-less
        (\ ordering → match ordering into (\ _ → MariciInt)
          ( marici-less ⇒ marici-int-neg
              (marici-sub (marici-add (marici-succ b) r)
                (marici-succ b))
          | marici-equal ⇒ marici-int-zero
          | marici-greater ⇒ marici-int-pos
              (marici-sub b
                (marici-succ (marici-add (marici-succ b) r)))))
        (marici-compare-explicit-gap-less b r))
      (ap MariciNat MariciInt
        (marici-sub (marici-add (marici-succ b) r) (marici-succ b))
        r marici-int-neg
        (marici-sub-add-prefix (marici-succ b) r))

#define marici-positive-factor-positive-gap-left-distrib
  ( p b r : MariciNat)
  : marici-int-mul (marici-int-pos p)
      (marici-int-add
        (marici-int-pos (marici-add (marici-succ b) r))
        (marici-int-neg b))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-pos p)
        (marici-int-pos (marici-add (marici-succ b) r)))
      (marici-int-mul (marici-int-pos p) (marici-int-neg b))
  := concat MariciInt
      (marici-int-mul (marici-int-pos p)
        (marici-int-add
          (marici-int-pos (marici-add (marici-succ b) r))
          (marici-int-neg b)))
      (marici-int-pos (marici-positive-product-predecessor p r))
      (marici-int-add
        (marici-int-mul (marici-int-pos p)
          (marici-int-pos (marici-add (marici-succ b) r)))
        (marici-int-mul (marici-int-pos p) (marici-int-neg b)))
      (ap MariciInt MariciInt
        (marici-int-add
          (marici-int-pos (marici-add (marici-succ b) r))
          (marici-int-neg b))
        (marici-int-pos r)
        (\ z → marici-int-mul (marici-int-pos p) z)
        (marici-int-add-pos-neg-gap b r))
      (rev MariciInt
        (marici-int-add
          (marici-int-pos
            (marici-positive-product-predecessor p
              (marici-add (marici-succ b) r)))
          (marici-int-neg (marici-positive-product-predecessor p b)))
        (marici-int-pos (marici-positive-product-predecessor p r))
        (marici-int-add-scaled-pos-neg-gap p b r))

#define marici-positive-factor-negative-gap-left-distrib
  ( p b r : MariciNat)
  : marici-int-mul (marici-int-pos p)
      (marici-int-add
        (marici-int-pos b)
        (marici-int-neg (marici-add (marici-succ b) r)))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-pos p) (marici-int-pos b))
      (marici-int-mul (marici-int-pos p)
        (marici-int-neg (marici-add (marici-succ b) r)))
  := concat MariciInt
      (marici-int-mul (marici-int-pos p)
        (marici-int-add
          (marici-int-pos b)
          (marici-int-neg (marici-add (marici-succ b) r))))
      (marici-int-neg (marici-positive-product-predecessor p r))
      (marici-int-add
        (marici-int-mul (marici-int-pos p) (marici-int-pos b))
        (marici-int-mul (marici-int-pos p)
          (marici-int-neg (marici-add (marici-succ b) r))))
      (ap MariciInt MariciInt
        (marici-int-add
          (marici-int-pos b)
          (marici-int-neg (marici-add (marici-succ b) r)))
        (marici-int-neg r)
        (\ z → marici-int-mul (marici-int-pos p) z)
        (marici-int-add-pos-neg-negative-gap b r))
      (rev MariciInt
        (marici-int-add
          (marici-int-pos (marici-positive-product-predecessor p b))
          (marici-int-neg
            (marici-positive-product-predecessor p
              (marici-add (marici-succ b) r))))
        (marici-int-neg (marici-positive-product-predecessor p r))
        (marici-int-add-scaled-pos-neg-negative-gap p b r))
```

## Boundary

Positive-factor distributivity now holds for equal magnitudes and for both
strict branches presented by explicit residual decompositions. A structural
case split converting arbitrary predecessor pairs into these presentations
remains before the unrestricted positive-factor mixed family.
