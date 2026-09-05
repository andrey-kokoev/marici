# Distributivity for a nonnegative multiplier and nonpositive addends

The complementary sign-homogeneous distributive family is obtained from the
negated embedding laws and natural right distributivity.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-mul-add-left-distrib-embedded-by-negated
  ( a b c : MariciNat)
  : marici-int-mul (marici-int-embed-nat a)
      (marici-int-add
        (marici-int-negate (marici-int-embed-nat b))
        (marici-int-negate (marici-int-embed-nat c)))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul
        (marici-int-embed-nat a)
        (marici-int-negate (marici-int-embed-nat b)))
      (marici-int-mul
        (marici-int-embed-nat a)
        (marici-int-negate (marici-int-embed-nat c)))
  := concat MariciInt
      (marici-int-mul (marici-int-embed-nat a)
        (marici-int-add
          (marici-int-negate (marici-int-embed-nat b))
          (marici-int-negate (marici-int-embed-nat c))))
      (marici-int-negate
        (marici-int-embed-nat
          (marici-mul a (marici-add b c))))
      (marici-int-add
        (marici-int-mul
          (marici-int-embed-nat a)
          (marici-int-negate (marici-int-embed-nat b)))
        (marici-int-mul
          (marici-int-embed-nat a)
          (marici-int-negate (marici-int-embed-nat c))))
      (concat MariciInt
        (marici-int-mul (marici-int-embed-nat a)
          (marici-int-add
            (marici-int-negate (marici-int-embed-nat b))
            (marici-int-negate (marici-int-embed-nat c))))
        (marici-int-mul (marici-int-embed-nat a)
          (marici-int-negate
            (marici-int-embed-nat (marici-add b c))))
        (marici-int-negate
          (marici-int-embed-nat
            (marici-mul a (marici-add b c))))
        (ap MariciInt MariciInt
          (marici-int-add
            (marici-int-negate (marici-int-embed-nat b))
            (marici-int-negate (marici-int-embed-nat c)))
          (marici-int-negate
            (marici-int-embed-nat (marici-add b c)))
          (\ z → marici-int-mul (marici-int-embed-nat a) z)
          (rev MariciInt
            (marici-int-negate
              (marici-int-embed-nat (marici-add b c)))
            (marici-int-add
              (marici-int-negate (marici-int-embed-nat b))
              (marici-int-negate (marici-int-embed-nat c)))
            (marici-int-negated-embed-add b c)))
        (rev MariciInt
          (marici-int-negate
            (marici-int-embed-nat
              (marici-mul a (marici-add b c))))
          (marici-int-mul (marici-int-embed-nat a)
            (marici-int-negate
              (marici-int-embed-nat (marici-add b c))))
          (marici-int-negated-embed-mul-right a (marici-add b c))))
      (concat MariciInt
        (marici-int-negate
          (marici-int-embed-nat
            (marici-mul a (marici-add b c))))
        (marici-int-add
          (marici-int-negate
            (marici-int-embed-nat (marici-mul a b)))
          (marici-int-negate
            (marici-int-embed-nat (marici-mul a c))))
        (marici-int-add
          (marici-int-mul
            (marici-int-embed-nat a)
            (marici-int-negate (marici-int-embed-nat b)))
          (marici-int-mul
            (marici-int-embed-nat a)
            (marici-int-negate (marici-int-embed-nat c))))
        (concat MariciInt
          (marici-int-negate
            (marici-int-embed-nat
              (marici-mul a (marici-add b c))))
          (marici-int-negate
            (marici-int-embed-nat
              (marici-add (marici-mul a b) (marici-mul a c))))
          (marici-int-add
            (marici-int-negate
              (marici-int-embed-nat (marici-mul a b)))
            (marici-int-negate
              (marici-int-embed-nat (marici-mul a c))))
          (ap MariciNat MariciInt
            (marici-mul a (marici-add b c))
            (marici-add (marici-mul a b) (marici-mul a c))
            (\ n → marici-int-negate (marici-int-embed-nat n))
            (marici-mul-add-right-distrib a b c))
          (marici-int-negated-embed-add
            (marici-mul a b) (marici-mul a c)))
        (concat MariciInt
          (marici-int-add
            (marici-int-negate
              (marici-int-embed-nat (marici-mul a b)))
            (marici-int-negate
              (marici-int-embed-nat (marici-mul a c))))
          (marici-int-add
            (marici-int-mul
              (marici-int-embed-nat a)
              (marici-int-negate (marici-int-embed-nat b)))
            (marici-int-negate
              (marici-int-embed-nat (marici-mul a c))))
          (marici-int-add
            (marici-int-mul
              (marici-int-embed-nat a)
              (marici-int-negate (marici-int-embed-nat b)))
            (marici-int-mul
              (marici-int-embed-nat a)
              (marici-int-negate (marici-int-embed-nat c))))
          (ap MariciInt MariciInt
            (marici-int-negate
              (marici-int-embed-nat (marici-mul a b)))
            (marici-int-mul
              (marici-int-embed-nat a)
              (marici-int-negate (marici-int-embed-nat b)))
            (\ z → marici-int-add z
              (marici-int-negate
                (marici-int-embed-nat (marici-mul a c))))
            (marici-int-negated-embed-mul-right a b))
          (ap MariciInt MariciInt
            (marici-int-negate
              (marici-int-embed-nat (marici-mul a c)))
            (marici-int-mul
              (marici-int-embed-nat a)
              (marici-int-negate (marici-int-embed-nat c)))
            (\ z → marici-int-add
              (marici-int-mul
                (marici-int-embed-nat a)
                (marici-int-negate (marici-int-embed-nat b))) z)
            (marici-int-negated-embed-mul-right a c))))
```

## Boundary

Left distributivity now holds for a nonnegative multiplier over a pair of
nonpositive addends. Sums with opposite-sign addends remain the unresolved
comparison/subtraction cases.
