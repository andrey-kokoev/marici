# Distributivity for a nonpositive multiplier and nonnegative addends

The first mixed-sign distributive family follows by transporting natural
right distributivity through embedding and negation.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-negated-embed-mul-left
  ( a b : MariciNat)
  : marici-int-negate
      (marici-int-embed-nat (marici-mul a b))
    =_{MariciInt}
    marici-int-mul
      (marici-int-negate (marici-int-embed-nat a))
      (marici-int-embed-nat b)
  := concat MariciInt
      (marici-int-negate
        (marici-int-embed-nat (marici-mul a b)))
      (marici-int-negate
        (marici-int-mul
          (marici-int-embed-nat a) (marici-int-embed-nat b)))
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat a))
        (marici-int-embed-nat b))
      (ap MariciInt MariciInt
        (marici-int-embed-nat (marici-mul a b))
        (marici-int-mul
          (marici-int-embed-nat a) (marici-int-embed-nat b))
        marici-int-negate
        (marici-int-embed-mul a b))
      (rev MariciInt
        (marici-int-mul
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-embed-nat b))
        (marici-int-negate
          (marici-int-mul
            (marici-int-embed-nat a) (marici-int-embed-nat b)))
        (marici-int-mul-negate-left
          (marici-int-embed-nat a) (marici-int-embed-nat b)))
```

```rzk
#define marici-int-mul-add-left-distrib-negated-by-embedded
  ( a b c : MariciNat)
  : marici-int-mul
      (marici-int-negate (marici-int-embed-nat a))
      (marici-int-add
        (marici-int-embed-nat b) (marici-int-embed-nat c))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat a))
        (marici-int-embed-nat b))
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat a))
        (marici-int-embed-nat c))
  := concat MariciInt
      (marici-int-mul
        (marici-int-negate (marici-int-embed-nat a))
        (marici-int-add
          (marici-int-embed-nat b) (marici-int-embed-nat c)))
      (marici-int-negate
        (marici-int-embed-nat
          (marici-mul a (marici-add b c))))
      (marici-int-add
        (marici-int-mul
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-embed-nat b))
        (marici-int-mul
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-embed-nat c)))
      (concat MariciInt
        (marici-int-mul
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-add
            (marici-int-embed-nat b) (marici-int-embed-nat c)))
        (marici-int-mul
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-embed-nat (marici-add b c)))
        (marici-int-negate
          (marici-int-embed-nat
            (marici-mul a (marici-add b c))))
        (ap MariciInt MariciInt
          (marici-int-add
            (marici-int-embed-nat b) (marici-int-embed-nat c))
          (marici-int-embed-nat (marici-add b c))
          (\ z → marici-int-mul
            (marici-int-negate (marici-int-embed-nat a)) z)
          (rev MariciInt
            (marici-int-embed-nat (marici-add b c))
            (marici-int-add
              (marici-int-embed-nat b) (marici-int-embed-nat c))
            (marici-int-embed-add b c)))
        (concat MariciInt
          (marici-int-mul
            (marici-int-negate (marici-int-embed-nat a))
            (marici-int-embed-nat (marici-add b c)))
          (marici-int-negate
            (marici-int-mul
              (marici-int-embed-nat a)
              (marici-int-embed-nat (marici-add b c))))
          (marici-int-negate
            (marici-int-embed-nat
              (marici-mul a (marici-add b c))))
          (marici-int-mul-negate-left
            (marici-int-embed-nat a)
            (marici-int-embed-nat (marici-add b c)))
          (ap MariciInt MariciInt
            (marici-int-mul
              (marici-int-embed-nat a)
              (marici-int-embed-nat (marici-add b c)))
            (marici-int-embed-nat
              (marici-mul a (marici-add b c)))
            marici-int-negate
            (rev MariciInt
              (marici-int-embed-nat
                (marici-mul a (marici-add b c)))
              (marici-int-mul
                (marici-int-embed-nat a)
                (marici-int-embed-nat (marici-add b c)))
              (marici-int-embed-mul a (marici-add b c))))))
      (concat MariciInt
        (marici-int-negate
          (marici-int-embed-nat
            (marici-mul a (marici-add b c))))
        (marici-int-negate
          (marici-int-embed-nat
            (marici-add (marici-mul a b) (marici-mul a c))))
        (marici-int-add
          (marici-int-mul
            (marici-int-negate (marici-int-embed-nat a))
            (marici-int-embed-nat b))
          (marici-int-mul
            (marici-int-negate (marici-int-embed-nat a))
            (marici-int-embed-nat c)))
        (ap MariciNat MariciInt
          (marici-mul a (marici-add b c))
          (marici-add (marici-mul a b) (marici-mul a c))
          (\ n → marici-int-negate (marici-int-embed-nat n))
          (marici-mul-add-right-distrib a b c))
        (concat MariciInt
          (marici-int-negate
            (marici-int-embed-nat
              (marici-add (marici-mul a b) (marici-mul a c))))
          (marici-int-add
            (marici-int-negate
              (marici-int-embed-nat (marici-mul a b)))
            (marici-int-negate
              (marici-int-embed-nat (marici-mul a c))))
          (marici-int-add
            (marici-int-mul
              (marici-int-negate (marici-int-embed-nat a))
              (marici-int-embed-nat b))
            (marici-int-mul
              (marici-int-negate (marici-int-embed-nat a))
              (marici-int-embed-nat c)))
          (marici-int-negated-embed-add
            (marici-mul a b) (marici-mul a c))
          (concat MariciInt
            (marici-int-add
              (marici-int-negate
                (marici-int-embed-nat (marici-mul a b)))
              (marici-int-negate
                (marici-int-embed-nat (marici-mul a c))))
            (marici-int-add
              (marici-int-mul
                (marici-int-negate (marici-int-embed-nat a))
                (marici-int-embed-nat b))
              (marici-int-negate
                (marici-int-embed-nat (marici-mul a c))))
            (marici-int-add
              (marici-int-mul
                (marici-int-negate (marici-int-embed-nat a))
                (marici-int-embed-nat b))
              (marici-int-mul
                (marici-int-negate (marici-int-embed-nat a))
                (marici-int-embed-nat c)))
            (ap MariciInt MariciInt
              (marici-int-negate
                (marici-int-embed-nat (marici-mul a b)))
              (marici-int-mul
                (marici-int-negate (marici-int-embed-nat a))
                (marici-int-embed-nat b))
              (\ z → marici-int-add z
                (marici-int-negate
                  (marici-int-embed-nat (marici-mul a c))))
              (marici-int-negated-embed-mul-left a b))
            (ap MariciInt MariciInt
              (marici-int-negate
                (marici-int-embed-nat (marici-mul a c)))
              (marici-int-mul
                (marici-int-negate (marici-int-embed-nat a))
                (marici-int-embed-nat c))
              (\ z → marici-int-add
                (marici-int-mul
                  (marici-int-negate (marici-int-embed-nat a))
                  (marici-int-embed-nat b)) z)
              (marici-int-negated-embed-mul-left a c)))))
```

## Boundary

Left distributivity now holds for every nonpositive multiplier and nonnegative
pair of addends. Other mixed-sign placements remain open.
