# Integer addition associativity on the nonpositive image

Negation of the natural embedding preserves addition into the nonpositive
integer image. Transporting natural associativity through that law proves
integer addition associativity for every triple in this image.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-negated-embed-add
  ( a b : MariciNat)
  : marici-int-negate (marici-int-embed-nat (marici-add a b))
    =_{MariciInt}
    marici-int-add
      (marici-int-negate (marici-int-embed-nat a))
      (marici-int-negate (marici-int-embed-nat b))
  := match a
      ( marici-zero ⇒ refl
      | marici-succ x ih ⇒ match b
          ( marici-zero ⇒
              ap MariciNat MariciInt
                (marici-add x marici-zero) x
                marici-int-neg
                (marici-add-zero-right x)
          | marici-succ y jh ⇒
              ap MariciNat MariciInt
                (marici-add x (marici-succ y))
                (marici-succ (marici-add x y))
                marici-int-neg
                (marici-add-succ-right x y)))
```

```rzk
#define marici-int-add-assoc-negated-embedded-nat
  ( a b c : MariciNat)
  : marici-int-add
      (marici-int-add
        (marici-int-negate (marici-int-embed-nat a))
        (marici-int-negate (marici-int-embed-nat b)))
      (marici-int-negate (marici-int-embed-nat c))
    =_{MariciInt}
    marici-int-add
      (marici-int-negate (marici-int-embed-nat a))
      (marici-int-add
        (marici-int-negate (marici-int-embed-nat b))
        (marici-int-negate (marici-int-embed-nat c)))
  := concat MariciInt
      (marici-int-add
        (marici-int-add
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-negate (marici-int-embed-nat b)))
        (marici-int-negate (marici-int-embed-nat c)))
      (marici-int-negate
        (marici-int-embed-nat
          (marici-add (marici-add a b) c)))
      (marici-int-add
        (marici-int-negate (marici-int-embed-nat a))
        (marici-int-add
          (marici-int-negate (marici-int-embed-nat b))
          (marici-int-negate (marici-int-embed-nat c))))
      (concat MariciInt
        (marici-int-add
          (marici-int-add
            (marici-int-negate (marici-int-embed-nat a))
            (marici-int-negate (marici-int-embed-nat b)))
          (marici-int-negate (marici-int-embed-nat c)))
        (marici-int-add
          (marici-int-negate
            (marici-int-embed-nat (marici-add a b)))
          (marici-int-negate (marici-int-embed-nat c)))
        (marici-int-negate
          (marici-int-embed-nat
            (marici-add (marici-add a b) c)))
        (ap MariciInt MariciInt
          (marici-int-add
            (marici-int-negate (marici-int-embed-nat a))
            (marici-int-negate (marici-int-embed-nat b)))
          (marici-int-negate
            (marici-int-embed-nat (marici-add a b)))
          (\ z → marici-int-add z
            (marici-int-negate (marici-int-embed-nat c)))
          (rev MariciInt
            (marici-int-negate
              (marici-int-embed-nat (marici-add a b)))
            (marici-int-add
              (marici-int-negate (marici-int-embed-nat a))
              (marici-int-negate (marici-int-embed-nat b)))
            (marici-int-negated-embed-add a b)))
        (rev MariciInt
          (marici-int-negate
            (marici-int-embed-nat
              (marici-add (marici-add a b) c)))
          (marici-int-add
            (marici-int-negate
              (marici-int-embed-nat (marici-add a b)))
            (marici-int-negate (marici-int-embed-nat c)))
          (marici-int-negated-embed-add (marici-add a b) c)))
      (concat MariciInt
        (marici-int-negate
          (marici-int-embed-nat
            (marici-add (marici-add a b) c)))
        (marici-int-negate
          (marici-int-embed-nat
            (marici-add a (marici-add b c))))
        (marici-int-add
          (marici-int-negate (marici-int-embed-nat a))
          (marici-int-add
            (marici-int-negate (marici-int-embed-nat b))
            (marici-int-negate (marici-int-embed-nat c))))
        (ap MariciNat MariciInt
          (marici-add (marici-add a b) c)
          (marici-add a (marici-add b c))
          (\ n → marici-int-negate (marici-int-embed-nat n))
          (marici-add-assoc a b c))
        (concat MariciInt
          (marici-int-negate
            (marici-int-embed-nat
              (marici-add a (marici-add b c))))
          (marici-int-add
            (marici-int-negate (marici-int-embed-nat a))
            (marici-int-negate
              (marici-int-embed-nat (marici-add b c))))
          (marici-int-add
            (marici-int-negate (marici-int-embed-nat a))
            (marici-int-add
              (marici-int-negate (marici-int-embed-nat b))
              (marici-int-negate (marici-int-embed-nat c))))
          (marici-int-negated-embed-add a (marici-add b c))
          (ap MariciInt MariciInt
            (marici-int-negate
              (marici-int-embed-nat (marici-add b c)))
            (marici-int-add
              (marici-int-negate (marici-int-embed-nat b))
              (marici-int-negate (marici-int-embed-nat c)))
            (\ z → marici-int-add
              (marici-int-negate (marici-int-embed-nat a)) z)
            (marici-int-negated-embed-add b c))))
```

## Boundary

Integer addition associativity now holds on both the full nonnegative and full
nonpositive images. Mixed-sign triples still require comparison/subtraction
coherence and are not inferred from these two image theorems.
