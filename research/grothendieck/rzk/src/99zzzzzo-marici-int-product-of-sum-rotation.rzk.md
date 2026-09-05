# Product-of-sum four-factor rotation

This is the exact distributive normal form used on each side of raw-fraction
addition congruence.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-product-of-sum-rotate
  ( a b c d e f : MariciInt)
  : marici-int-mul
      (marici-int-add (marici-int-mul a b) (marici-int-mul c d))
      (marici-int-mul e f)
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-mul a e) (marici-int-mul b f))
      (marici-int-mul (marici-int-mul c e) (marici-int-mul d f))
  := concat MariciInt
      (marici-int-mul
        (marici-int-add (marici-int-mul a b) (marici-int-mul c d))
        (marici-int-mul e f))
      (marici-int-add
        (marici-int-mul (marici-int-mul a b) (marici-int-mul e f))
        (marici-int-mul (marici-int-mul c d) (marici-int-mul e f)))
      (marici-int-add
        (marici-int-mul (marici-int-mul a e) (marici-int-mul b f))
        (marici-int-mul (marici-int-mul c e) (marici-int-mul d f)))
      (marici-int-mul-add-right-distrib
        (marici-int-mul a b) (marici-int-mul c d)
        (marici-int-mul e f))
      (marici-int-add-congruent
        (marici-int-mul (marici-int-mul a b) (marici-int-mul e f))
        (marici-int-mul (marici-int-mul a e) (marici-int-mul b f))
        (marici-int-mul (marici-int-mul c d) (marici-int-mul e f))
        (marici-int-mul (marici-int-mul c e) (marici-int-mul d f))
        (marici-int-four-factor-rotate a b e f)
        (marici-int-four-factor-rotate c d e f))
```

## Boundary

This theorem distributes and rotates but does not substitute fraction
cross-product equalities. The raw congruence theorem supplies those two paths.
