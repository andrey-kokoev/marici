# Sign coherence for multiplication of embedded naturals

The right-negated embedding law complements the left law from module 34. Both
placements of one minus sign compute to the negation of the embedded natural
product and therefore agree.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-negated-embed-mul-right
  ( a b : MariciNat)
  : marici-int-negate
      (marici-int-embed-nat (marici-mul a b))
    =_{MariciInt}
    marici-int-mul
      (marici-int-embed-nat a)
      (marici-int-negate (marici-int-embed-nat b))
  := concat MariciInt
      (marici-int-negate
        (marici-int-embed-nat (marici-mul a b)))
      (marici-int-negate
        (marici-int-mul
          (marici-int-embed-nat a) (marici-int-embed-nat b)))
      (marici-int-mul
        (marici-int-embed-nat a)
        (marici-int-negate (marici-int-embed-nat b)))
      (ap MariciInt MariciInt
        (marici-int-embed-nat (marici-mul a b))
        (marici-int-mul
          (marici-int-embed-nat a) (marici-int-embed-nat b))
        marici-int-negate
        (marici-int-embed-mul a b))
      (rev MariciInt
        (marici-int-mul
          (marici-int-embed-nat a)
          (marici-int-negate (marici-int-embed-nat b)))
        (marici-int-negate
          (marici-int-mul
            (marici-int-embed-nat a) (marici-int-embed-nat b)))
        (marici-int-mul-negate-right
          (marici-int-embed-nat a) (marici-int-embed-nat b)))

#define marici-int-embedded-single-sign-placement
  ( a b : MariciNat)
  : marici-int-mul
      (marici-int-negate (marici-int-embed-nat a))
      (marici-int-embed-nat b)
    =_{MariciInt}
    marici-int-mul
      (marici-int-embed-nat a)
      (marici-int-negate (marici-int-embed-nat b))
  := concat MariciInt
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat a))
        (marici-int-embed-nat b))
      (marici-int-negate
        (marici-int-embed-nat (marici-mul a b)))
      (marici-int-mul
        (marici-int-embed-nat a)
        (marici-int-negate (marici-int-embed-nat b)))
      (rev MariciInt
        (marici-int-negate
          (marici-int-embed-nat (marici-mul a b)))
        (marici-int-mul
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-embed-nat b))
        (marici-int-negated-embed-mul-left a b))
      (marici-int-negated-embed-mul-right a b)
```

## Boundary

This closes sign-placement coherence for products of embedded naturals. It does
not itself establish the remaining mixed-sign distributive families.
