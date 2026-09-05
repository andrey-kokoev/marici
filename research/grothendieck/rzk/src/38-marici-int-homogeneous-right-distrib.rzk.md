# Right distributivity from left distributivity

Integer multiplication commutativity transports any left-distributive instance
to its right-distributive orientation. The generic transport is then applied
to the three sign families not already covered by module 32.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-right-distrib-from-left
  ( x y z : MariciInt)
  ( left-law
    : marici-int-mul x (marici-int-add y z)
      =_{MariciInt}
      marici-int-add (marici-int-mul x y) (marici-int-mul x z))
  : marici-int-mul (marici-int-add y z) x
    =_{MariciInt}
    marici-int-add (marici-int-mul y x) (marici-int-mul z x)
  := concat MariciInt
      (marici-int-mul (marici-int-add y z) x)
      (marici-int-add (marici-int-mul x y) (marici-int-mul x z))
      (marici-int-add (marici-int-mul y x) (marici-int-mul z x))
      (concat MariciInt
        (marici-int-mul (marici-int-add y z) x)
        (marici-int-mul x (marici-int-add y z))
        (marici-int-add (marici-int-mul x y) (marici-int-mul x z))
        (marici-int-mul-comm (marici-int-add y z) x)
        left-law)
      (concat MariciInt
        (marici-int-add (marici-int-mul x y) (marici-int-mul x z))
        (marici-int-add (marici-int-mul y x) (marici-int-mul x z))
        (marici-int-add (marici-int-mul y x) (marici-int-mul z x))
        (ap MariciInt MariciInt
          (marici-int-mul x y) (marici-int-mul y x)
          (\ w → marici-int-add w (marici-int-mul x z))
          (marici-int-mul-comm x y))
        (ap MariciInt MariciInt
          (marici-int-mul x z) (marici-int-mul z x)
          (\ w → marici-int-add (marici-int-mul y x) w)
          (marici-int-mul-comm x z)))
```

```rzk
#define marici-int-mul-add-right-distrib-negated-by-embedded
  ( a b c : MariciNat)
  : marici-int-mul
      (marici-int-add
        (marici-int-embed-nat b) (marici-int-embed-nat c))
      (marici-int-negate (marici-int-embed-nat a))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul
        (marici-int-embed-nat b)
        (marici-int-negate (marici-int-embed-nat a)))
      (marici-int-mul
        (marici-int-embed-nat c)
        (marici-int-negate (marici-int-embed-nat a)))
  := marici-int-right-distrib-from-left
      (marici-int-negate (marici-int-embed-nat a))
      (marici-int-embed-nat b) (marici-int-embed-nat c)
      (marici-int-mul-add-left-distrib-negated-by-embedded a b c)

#define marici-int-mul-add-right-distrib-embedded-by-negated
  ( a b c : MariciNat)
  : marici-int-mul
      (marici-int-add
        (marici-int-negate (marici-int-embed-nat b))
        (marici-int-negate (marici-int-embed-nat c)))
      (marici-int-embed-nat a)
    =_{MariciInt}
    marici-int-add
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat b))
        (marici-int-embed-nat a))
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat c))
        (marici-int-embed-nat a))
  := marici-int-right-distrib-from-left
      (marici-int-embed-nat a)
      (marici-int-negate (marici-int-embed-nat b))
      (marici-int-negate (marici-int-embed-nat c))
      (marici-int-mul-add-left-distrib-embedded-by-negated a b c)

#define marici-int-mul-add-right-distrib-negated-by-negated
  ( a b c : MariciNat)
  : marici-int-mul
      (marici-int-add
        (marici-int-negate (marici-int-embed-nat b))
        (marici-int-negate (marici-int-embed-nat c)))
      (marici-int-negate (marici-int-embed-nat a))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat b))
        (marici-int-negate (marici-int-embed-nat a)))
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat c))
        (marici-int-negate (marici-int-embed-nat a)))
  := marici-int-right-distrib-from-left
      (marici-int-negate (marici-int-embed-nat a))
      (marici-int-negate (marici-int-embed-nat b))
      (marici-int-negate (marici-int-embed-nat c))
      (marici-int-mul-add-left-distrib-negated-by-negated a b c)
```

## Boundary

Both distributive orientations now hold for every multiplier sign when the two
addends share a sign. Opposite-sign addends still require the normalized
comparison/subtraction laws.
