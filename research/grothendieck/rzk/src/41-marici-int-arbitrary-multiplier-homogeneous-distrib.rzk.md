# Homogeneous-addend distributivity for arbitrary multipliers

The four sign-specific left-distributive families are consolidated by
constructor analysis on the multiplier. The addends remain sign-homogeneous,
but the multiplier is now an arbitrary normalized integer.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-mul-add-left-distrib-arbitrary-by-embedded
  ( x : MariciInt)
  ( b c : MariciNat)
  : marici-int-mul x
      (marici-int-add
        (marici-int-embed-nat b) (marici-int-embed-nat c))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul x (marici-int-embed-nat b))
      (marici-int-mul x (marici-int-embed-nat c))
  := match x
      ( marici-int-zero ⇒
          marici-int-mul-add-left-distrib-embedded-nat
            marici-zero b c
      | marici-int-pos a ⇒
          marici-int-mul-add-left-distrib-embedded-nat
            (marici-succ a) b c
      | marici-int-neg a ⇒
          marici-int-mul-add-left-distrib-negated-by-embedded
            (marici-succ a) b c)

#define marici-int-mul-add-left-distrib-arbitrary-by-negated
  ( x : MariciInt)
  ( b c : MariciNat)
  : marici-int-mul x
      (marici-int-add
        (marici-int-negate (marici-int-embed-nat b))
        (marici-int-negate (marici-int-embed-nat c)))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul x
        (marici-int-negate (marici-int-embed-nat b)))
      (marici-int-mul x
        (marici-int-negate (marici-int-embed-nat c)))
  := match x
      ( marici-int-zero ⇒
          marici-int-mul-add-left-distrib-embedded-by-negated
            marici-zero b c
      | marici-int-pos a ⇒
          marici-int-mul-add-left-distrib-embedded-by-negated
            (marici-succ a) b c
      | marici-int-neg a ⇒
          marici-int-mul-add-left-distrib-negated-by-negated
            (marici-succ a) b c)
```

```rzk
#define marici-int-mul-add-right-distrib-embedded-by-arbitrary
  ( x : MariciInt)
  ( b c : MariciNat)
  : marici-int-mul
      (marici-int-add
        (marici-int-embed-nat b) (marici-int-embed-nat c)) x
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-embed-nat b) x)
      (marici-int-mul (marici-int-embed-nat c) x)
  := marici-int-right-distrib-from-left x
      (marici-int-embed-nat b) (marici-int-embed-nat c)
      (marici-int-mul-add-left-distrib-arbitrary-by-embedded x b c)

#define marici-int-mul-add-right-distrib-negated-by-arbitrary
  ( x : MariciInt)
  ( b c : MariciNat)
  : marici-int-mul
      (marici-int-add
        (marici-int-negate (marici-int-embed-nat b))
        (marici-int-negate (marici-int-embed-nat c))) x
    =_{MariciInt}
    marici-int-add
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat b)) x)
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat c)) x)
  := marici-int-right-distrib-from-left x
      (marici-int-negate (marici-int-embed-nat b))
      (marici-int-negate (marici-int-embed-nat c))
      (marici-int-mul-add-left-distrib-arbitrary-by-negated x b c)
```

## Boundary

Both distributive orientations now hold for arbitrary normalized multipliers
and either homogeneous addend image. Only unequal opposite-sign addend pairs
remain outside these families.
