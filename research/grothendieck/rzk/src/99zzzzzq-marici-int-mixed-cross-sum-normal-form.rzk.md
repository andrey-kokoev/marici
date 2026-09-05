# Mixed cross-sum normal form

The two summands of a fraction sum must expose different input equivalences.
This normal form rotates the first through one outer denominator and the second
through the other.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-four-factor-rotate-second-swap
  ( a b c d : MariciInt)
  : marici-int-mul (marici-int-mul a b) (marici-int-mul c d)
    =_{MariciInt}
    marici-int-mul (marici-int-mul a d) (marici-int-mul b c)
  := concat MariciInt
      (marici-int-mul (marici-int-mul a b) (marici-int-mul c d))
      (marici-int-mul (marici-int-mul a b) (marici-int-mul d c))
      (marici-int-mul (marici-int-mul a d) (marici-int-mul b c))
      (ap MariciInt MariciInt
        (marici-int-mul c d) (marici-int-mul d c)
        (\ z → marici-int-mul (marici-int-mul a b) z)
        (marici-int-mul-comm c d))
      (marici-int-four-factor-rotate a b d c)

#define marici-int-mixed-cross-sum-normal-form
  ( a b c d e f : MariciInt)
  : marici-int-mul
      (marici-int-add (marici-int-mul a b) (marici-int-mul c d))
      (marici-int-mul e f)
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-mul a e) (marici-int-mul b f))
      (marici-int-mul (marici-int-mul c f) (marici-int-mul d e))
  := concat MariciInt
      (marici-int-mul
        (marici-int-add (marici-int-mul a b) (marici-int-mul c d))
        (marici-int-mul e f))
      (marici-int-add
        (marici-int-mul (marici-int-mul a b) (marici-int-mul e f))
        (marici-int-mul (marici-int-mul c d) (marici-int-mul e f)))
      (marici-int-add
        (marici-int-mul (marici-int-mul a e) (marici-int-mul b f))
        (marici-int-mul (marici-int-mul c f) (marici-int-mul d e)))
      (marici-int-mul-add-right-distrib
        (marici-int-mul a b) (marici-int-mul c d)
        (marici-int-mul e f))
      (marici-int-add-congruent
        (marici-int-mul (marici-int-mul a b) (marici-int-mul e f))
        (marici-int-mul (marici-int-mul a e) (marici-int-mul b f))
        (marici-int-mul (marici-int-mul c d) (marici-int-mul e f))
        (marici-int-mul (marici-int-mul c f) (marici-int-mul d e))
        (marici-int-four-factor-rotate a b e f)
        (marici-int-four-factor-rotate-second-swap c d e f))
```

## Boundary

This establishes the shared algebraic normal form. The fraction theorem still
specializes the six factors to numerators and embedded denominators, transports
the two equivalence witnesses, and reverses the target normalization path.
