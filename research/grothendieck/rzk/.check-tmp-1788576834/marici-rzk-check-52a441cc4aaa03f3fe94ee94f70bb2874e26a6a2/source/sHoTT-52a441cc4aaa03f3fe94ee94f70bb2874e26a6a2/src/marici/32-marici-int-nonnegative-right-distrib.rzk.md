# Integer right distributivity on the nonnegative image

Right distributivity on embedded naturals follows from the checked left law and
global integer multiplication commutativity. This closes both distributive
orientations on the full nonnegative image.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-mul-add-right-distrib-embedded-nat
  ( a b c : MariciNat)
  : marici-int-mul
      (marici-int-add
        (marici-int-embed-nat a) (marici-int-embed-nat b))
      (marici-int-embed-nat c)
    =_{MariciInt}
    marici-int-add
      (marici-int-mul
        (marici-int-embed-nat a) (marici-int-embed-nat c))
      (marici-int-mul
        (marici-int-embed-nat b) (marici-int-embed-nat c))
  := concat MariciInt
      (marici-int-mul
        (marici-int-add
          (marici-int-embed-nat a) (marici-int-embed-nat b))
        (marici-int-embed-nat c))
      (marici-int-mul (marici-int-embed-nat c)
        (marici-int-add
          (marici-int-embed-nat a) (marici-int-embed-nat b)))
      (marici-int-add
        (marici-int-mul
          (marici-int-embed-nat a) (marici-int-embed-nat c))
        (marici-int-mul
          (marici-int-embed-nat b) (marici-int-embed-nat c)))
      (marici-int-mul-comm
        (marici-int-add
          (marici-int-embed-nat a) (marici-int-embed-nat b))
        (marici-int-embed-nat c))
      (concat MariciInt
        (marici-int-mul (marici-int-embed-nat c)
          (marici-int-add
            (marici-int-embed-nat a) (marici-int-embed-nat b)))
        (marici-int-add
          (marici-int-mul
            (marici-int-embed-nat c) (marici-int-embed-nat a))
          (marici-int-mul
            (marici-int-embed-nat c) (marici-int-embed-nat b)))
        (marici-int-add
          (marici-int-mul
            (marici-int-embed-nat a) (marici-int-embed-nat c))
          (marici-int-mul
            (marici-int-embed-nat b) (marici-int-embed-nat c)))
        (marici-int-mul-add-left-distrib-embedded-nat c a b)
        (concat MariciInt
          (marici-int-add
            (marici-int-mul
              (marici-int-embed-nat c) (marici-int-embed-nat a))
            (marici-int-mul
              (marici-int-embed-nat c) (marici-int-embed-nat b)))
          (marici-int-add
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat c))
            (marici-int-mul
              (marici-int-embed-nat c) (marici-int-embed-nat b)))
          (marici-int-add
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat c))
            (marici-int-mul
              (marici-int-embed-nat b) (marici-int-embed-nat c)))
          (ap MariciInt MariciInt
            (marici-int-mul
              (marici-int-embed-nat c) (marici-int-embed-nat a))
            (marici-int-mul
              (marici-int-embed-nat a) (marici-int-embed-nat c))
            (\ z → marici-int-add z
              (marici-int-mul
                (marici-int-embed-nat c) (marici-int-embed-nat b)))
            (marici-int-mul-comm
              (marici-int-embed-nat c) (marici-int-embed-nat a)))
          (ap MariciInt MariciInt
            (marici-int-mul
              (marici-int-embed-nat c) (marici-int-embed-nat b))
            (marici-int-mul
              (marici-int-embed-nat b) (marici-int-embed-nat c))
            (\ z → marici-int-add
              (marici-int-mul
                (marici-int-embed-nat a) (marici-int-embed-nat c)) z)
            (marici-int-mul-comm
              (marici-int-embed-nat c) (marici-int-embed-nat b)))))
```

## Boundary

Both distributive orientations now hold for all embedded naturals. This does
not extend them to mixed-sign or negative inputs; those constructor branches
remain required for the integer commutative-ring package.
