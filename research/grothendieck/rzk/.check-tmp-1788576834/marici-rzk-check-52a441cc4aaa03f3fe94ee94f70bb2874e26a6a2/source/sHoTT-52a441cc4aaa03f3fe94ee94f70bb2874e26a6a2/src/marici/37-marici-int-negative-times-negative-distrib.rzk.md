# Distributivity for a nonpositive multiplier and nonpositive addends

This closes the remaining homogeneous-sign addend family. Two minus signs in
each product reduce to the corresponding nonnegative product.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-mul-add-left-distrib-negated-by-negated
  ( a b c : MariciNat)
  : marici-int-mul
      (marici-int-negate (marici-int-embed-nat a))
      (marici-int-add
        (marici-int-negate (marici-int-embed-nat b))
        (marici-int-negate (marici-int-embed-nat c)))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat a))
        (marici-int-negate (marici-int-embed-nat b)))
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat a))
        (marici-int-negate (marici-int-embed-nat c)))
  := concat MariciInt
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat a))
        (marici-int-add
          (marici-int-negate (marici-int-embed-nat b))
          (marici-int-negate (marici-int-embed-nat c))))
      (marici-int-mul
        (marici-int-embed-nat a)
        (marici-int-embed-nat (marici-add b c)))
      (marici-int-add
        (marici-int-mul
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-negate (marici-int-embed-nat b)))
        (marici-int-mul
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-negate (marici-int-embed-nat c))))
      (concat MariciInt
        (marici-int-mul
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-add
            (marici-int-negate (marici-int-embed-nat b))
            (marici-int-negate (marici-int-embed-nat c))))
        (marici-int-mul
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-negate
            (marici-int-embed-nat (marici-add b c))))
        (marici-int-mul
          (marici-int-embed-nat a)
          (marici-int-embed-nat (marici-add b c)))
        (ap MariciInt MariciInt
          (marici-int-add
            (marici-int-negate (marici-int-embed-nat b))
            (marici-int-negate (marici-int-embed-nat c)))
          (marici-int-negate
            (marici-int-embed-nat (marici-add b c)))
          (\ z → marici-int-mul
            (marici-int-negate (marici-int-embed-nat a)) z)
          (rev MariciInt
            (marici-int-negate
              (marici-int-embed-nat (marici-add b c)))
            (marici-int-add
              (marici-int-negate (marici-int-embed-nat b))
              (marici-int-negate (marici-int-embed-nat c)))
            (marici-int-negated-embed-add b c)))
        (marici-int-mul-negate-both
          (marici-int-embed-nat a)
          (marici-int-embed-nat (marici-add b c))))
      (concat MariciInt
        (marici-int-mul
          (marici-int-embed-nat a)
          (marici-int-embed-nat (marici-add b c)))
        (marici-int-add
          (marici-int-mul
            (marici-int-embed-nat a) (marici-int-embed-nat b))
          (marici-int-mul
            (marici-int-embed-nat a) (marici-int-embed-nat c)))
        (marici-int-add
          (marici-int-mul
            (marici-int-negate (marici-int-embed-nat a))
            (marici-int-negate (marici-int-embed-nat b)))
          (marici-int-mul
            (marici-int-negate (marici-int-embed-nat a))
            (marici-int-negate (marici-int-embed-nat c))))
        (concat MariciInt
          (marici-int-mul
            (marici-int-embed-nat a)
            (marici-int-embed-nat (marici-add b c)))
          (marici-int-mul
            (marici-int-embed-nat a)
            (marici-int-add
              (marici-int-embed-nat b) (marici-int-embed-nat c)))
          (marici-int-add
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat b))
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat c)))
          (ap MariciInt MariciInt
            (marici-int-embed-nat (marici-add b c))
            (marici-int-add
              (marici-int-embed-nat b) (marici-int-embed-nat c))
            (\ z → marici-int-mul (marici-int-embed-nat a) z)
            (marici-int-embed-add b c))
          (marici-int-mul-add-left-distrib-embedded-nat a b c))
        (concat MariciInt
          (marici-int-add
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat b))
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat c)))
          (marici-int-add
            (marici-int-mul
              (marici-int-negate (marici-int-embed-nat a))
              (marici-int-negate (marici-int-embed-nat b)))
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat c)))
          (marici-int-add
            (marici-int-mul
              (marici-int-negate (marici-int-embed-nat a))
              (marici-int-negate (marici-int-embed-nat b)))
            (marici-int-mul
              (marici-int-negate (marici-int-embed-nat a))
              (marici-int-negate (marici-int-embed-nat c))))
          (ap MariciInt MariciInt
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat b))
            (marici-int-mul
              (marici-int-negate (marici-int-embed-nat a))
              (marici-int-negate (marici-int-embed-nat b)))
            (\ z → marici-int-add z
              (marici-int-mul
                (marici-int-embed-nat a) (marici-int-embed-nat c)))
            (rev MariciInt
              (marici-int-mul
                (marici-int-negate (marici-int-embed-nat a))
                (marici-int-negate (marici-int-embed-nat b)))
              (marici-int-mul
                (marici-int-embed-nat a) (marici-int-embed-nat b))
              (marici-int-mul-negate-both
                (marici-int-embed-nat a) (marici-int-embed-nat b))))
          (ap MariciInt MariciInt
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat c))
            (marici-int-mul
              (marici-int-negate (marici-int-embed-nat a))
              (marici-int-negate (marici-int-embed-nat c)))
            (\ z → marici-int-add
              (marici-int-mul
                (marici-int-negate (marici-int-embed-nat a))
                (marici-int-negate (marici-int-embed-nat b))) z)
            (rev MariciInt
              (marici-int-mul
                (marici-int-negate (marici-int-embed-nat a))
                (marici-int-negate (marici-int-embed-nat c)))
              (marici-int-mul
                (marici-int-embed-nat a) (marici-int-embed-nat c))
              (marici-int-mul-negate-both
                (marici-int-embed-nat a) (marici-int-embed-nat c))))))
```

## Boundary

Left distributivity is now checked for every multiplier sign when the two
addends have the same sign. Opposite-sign addend pairs remain open.
