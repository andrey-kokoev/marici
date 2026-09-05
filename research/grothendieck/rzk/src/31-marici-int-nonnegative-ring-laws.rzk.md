# Integer ring laws on the nonnegative image

This module resumes the integer interface directly. Addition associativity and
left distributivity are proved for all integers in the image of the natural
embedding by transporting the checked natural semiring laws.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-assoc-embedded-nat
  ( a b c : MariciNat)
  : marici-int-add
      (marici-int-add
        (marici-int-embed-nat a) (marici-int-embed-nat b))
      (marici-int-embed-nat c)
    =_{MariciInt}
    marici-int-add (marici-int-embed-nat a)
      (marici-int-add
        (marici-int-embed-nat b) (marici-int-embed-nat c))
  := concat MariciInt
      (marici-int-add
        (marici-int-add
          (marici-int-embed-nat a) (marici-int-embed-nat b))
        (marici-int-embed-nat c))
      (marici-int-embed-nat
        (marici-add (marici-add a b) c))
      (marici-int-add (marici-int-embed-nat a)
        (marici-int-add
          (marici-int-embed-nat b) (marici-int-embed-nat c)))
      (concat MariciInt
        (marici-int-add
          (marici-int-add
            (marici-int-embed-nat a) (marici-int-embed-nat b))
          (marici-int-embed-nat c))
        (marici-int-add
          (marici-int-embed-nat (marici-add a b))
          (marici-int-embed-nat c))
        (marici-int-embed-nat
          (marici-add (marici-add a b) c))
        (ap MariciInt MariciInt
          (marici-int-add
            (marici-int-embed-nat a) (marici-int-embed-nat b))
          (marici-int-embed-nat (marici-add a b))
          (\ z → marici-int-add z (marici-int-embed-nat c))
          (rev MariciInt
            (marici-int-embed-nat (marici-add a b))
            (marici-int-add
              (marici-int-embed-nat a) (marici-int-embed-nat b))
            (marici-int-embed-add a b)))
        (rev MariciInt
          (marici-int-embed-nat
            (marici-add (marici-add a b) c))
          (marici-int-add
            (marici-int-embed-nat (marici-add a b))
            (marici-int-embed-nat c))
          (marici-int-embed-add (marici-add a b) c)))
      (concat MariciInt
        (marici-int-embed-nat
          (marici-add (marici-add a b) c))
        (marici-int-embed-nat
          (marici-add a (marici-add b c)))
        (marici-int-add (marici-int-embed-nat a)
          (marici-int-add
            (marici-int-embed-nat b) (marici-int-embed-nat c)))
        (ap MariciNat MariciInt
          (marici-add (marici-add a b) c)
          (marici-add a (marici-add b c))
          (\ n → marici-int-embed-nat n)
          (marici-add-assoc a b c))
        (concat MariciInt
          (marici-int-embed-nat
            (marici-add a (marici-add b c)))
          (marici-int-add (marici-int-embed-nat a)
            (marici-int-embed-nat (marici-add b c)))
          (marici-int-add (marici-int-embed-nat a)
            (marici-int-add
              (marici-int-embed-nat b) (marici-int-embed-nat c)))
          (marici-int-embed-add a (marici-add b c))
          (ap MariciInt MariciInt
            (marici-int-embed-nat (marici-add b c))
            (marici-int-add
              (marici-int-embed-nat b) (marici-int-embed-nat c))
            (\ z → marici-int-add (marici-int-embed-nat a) z)
            (marici-int-embed-add b c))))
```

```rzk
#define marici-int-mul-add-left-distrib-embedded-nat
  ( a b c : MariciNat)
  : marici-int-mul (marici-int-embed-nat a)
      (marici-int-add
        (marici-int-embed-nat b) (marici-int-embed-nat c))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul
        (marici-int-embed-nat a) (marici-int-embed-nat b))
      (marici-int-mul
        (marici-int-embed-nat a) (marici-int-embed-nat c))
  := concat MariciInt
      (marici-int-mul (marici-int-embed-nat a)
        (marici-int-add
          (marici-int-embed-nat b) (marici-int-embed-nat c)))
      (marici-int-embed-nat
        (marici-mul a (marici-add b c)))
      (marici-int-add
        (marici-int-mul
          (marici-int-embed-nat a) (marici-int-embed-nat b))
        (marici-int-mul
          (marici-int-embed-nat a) (marici-int-embed-nat c)))
      (concat MariciInt
        (marici-int-mul (marici-int-embed-nat a)
          (marici-int-add
            (marici-int-embed-nat b) (marici-int-embed-nat c)))
        (marici-int-mul (marici-int-embed-nat a)
          (marici-int-embed-nat (marici-add b c)))
        (marici-int-embed-nat
          (marici-mul a (marici-add b c)))
        (ap MariciInt MariciInt
          (marici-int-add
            (marici-int-embed-nat b) (marici-int-embed-nat c))
          (marici-int-embed-nat (marici-add b c))
          (\ z → marici-int-mul (marici-int-embed-nat a) z)
          (rev MariciInt
            (marici-int-embed-nat (marici-add b c))
            (marici-int-add
              (marici-int-embed-nat b) (marici-int-embed-nat c))
            (marici-int-embed-add b c)))
        (rev MariciInt
          (marici-int-embed-nat (marici-mul a (marici-add b c)))
          (marici-int-mul (marici-int-embed-nat a)
            (marici-int-embed-nat (marici-add b c)))
          (marici-int-embed-mul a (marici-add b c))))
      (concat MariciInt
        (marici-int-embed-nat
          (marici-mul a (marici-add b c)))
        (marici-int-embed-nat
          (marici-add (marici-mul a b) (marici-mul a c)))
        (marici-int-add
          (marici-int-mul
            (marici-int-embed-nat a) (marici-int-embed-nat b))
          (marici-int-mul
            (marici-int-embed-nat a) (marici-int-embed-nat c)))
        (ap MariciNat MariciInt
          (marici-mul a (marici-add b c))
          (marici-add (marici-mul a b) (marici-mul a c))
          (\ n → marici-int-embed-nat n)
          (marici-mul-add-right-distrib a b c))
        (concat MariciInt
          (marici-int-embed-nat
            (marici-add (marici-mul a b) (marici-mul a c)))
          (marici-int-add
            (marici-int-embed-nat (marici-mul a b))
            (marici-int-embed-nat (marici-mul a c)))
          (marici-int-add
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat b))
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat c)))
          (marici-int-embed-add (marici-mul a b) (marici-mul a c))
          (concat MariciInt
            (marici-int-add
              (marici-int-embed-nat (marici-mul a b))
              (marici-int-embed-nat (marici-mul a c)))
            (marici-int-add
              (marici-int-mul
                (marici-int-embed-nat a) (marici-int-embed-nat b))
              (marici-int-embed-nat (marici-mul a c)))
            (marici-int-add
              (marici-int-mul
                (marici-int-embed-nat a) (marici-int-embed-nat b))
              (marici-int-mul
                (marici-int-embed-nat a) (marici-int-embed-nat c)))
            (ap MariciInt MariciInt
              (marici-int-embed-nat (marici-mul a b))
              (marici-int-mul
                (marici-int-embed-nat a) (marici-int-embed-nat b))
              (\ z → marici-int-add z
                (marici-int-embed-nat (marici-mul a c)))
              (marici-int-embed-mul a b))
            (ap MariciInt MariciInt
              (marici-int-embed-nat (marici-mul a c))
              (marici-int-mul
                (marici-int-embed-nat a) (marici-int-embed-nat c))
              (\ z → marici-int-add
                (marici-int-mul
                  (marici-int-embed-nat a) (marici-int-embed-nat b)) z)
              (marici-int-embed-mul a c)))))
```

## Boundary

These are unbounded theorems for the full nonnegative image, not finite tests.
They do not cover mixed-sign or all-negative integer cases. Global integer
addition associativity and distributivity remain open until those constructor
branches are proved.
